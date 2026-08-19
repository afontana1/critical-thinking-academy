import argparse
import re
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id(value: str) -> str:
    value = value.strip()

    # Handle Markdown links:
    # [https://youtube.com/...](https://youtube.com/...)
    markdown_match = re.fullmatch(r"\[.*?\]\((.*?)\)", value)
    if markdown_match:
        value = markdown_match.group(1)

    value = value.replace("\\_", "_")

    # Raw video ID
    if re.fullmatch(r"[A-Za-z0-9_-]{11}", value):
        return value

    parsed = urlparse(value)
    hostname = (parsed.hostname or "").lower()

    # youtu.be/VIDEO_ID
    if hostname in {"youtu.be", "www.youtu.be"}:
        video_id = parsed.path.strip("/").split("/")[0]

        if re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
            return video_id

    # youtube.com URLs
    if hostname in {
        "youtube.com",
        "www.youtube.com",
        "m.youtube.com",
        "music.youtube.com",
    }:
        # youtube.com/watch?v=VIDEO_ID
        if parsed.path == "/watch":
            query = parse_qs(parsed.query)

            if "v" in query:
                video_id = query["v"][0]

                if re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
                    return video_id

        # /shorts/VIDEO_ID
        # /live/VIDEO_ID
        # /embed/VIDEO_ID
        parts = parsed.path.strip("/").split("/")

        if len(parts) >= 2 and parts[0] in {"shorts", "live", "embed"}:
            video_id = parts[1]

            if re.fullmatch(r"[A-Za-z0-9_-]{11}", video_id):
                return video_id

    raise ValueError(f"Could not find a valid YouTube video ID in: {value}")


def clean_text(text: str) -> str:
    """
    Clean common caption formatting issues.
    """
    text = text.replace("\n", " ")

    # Collapse repeated whitespace
    text = re.sub(r"\s+", " ", text)

    # Remove spaces before punctuation
    text = re.sub(r"\s+([,.!?;:])", r"\1", text)

    return text.strip()


def format_timestamp(seconds: float) -> str:
    seconds = int(seconds)

    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    if hours:
        return f"{hours:02}:{minutes:02}:{secs:02}"

    return f"{minutes:02}:{secs:02}"


def build_paragraphs(
    transcript,
    max_chars=700,
    pause_threshold=2.5,
):
    """
    Combine transcript snippets into readable paragraphs.

    A new paragraph starts when:
      - there's a noticeable pause
      - the paragraph becomes fairly long
      - a sentence ends and the paragraph is already substantial
    """

    paragraphs = []

    current_text = []
    paragraph_start = None
    previous_end = None

    for snippet in transcript:
        text = clean_text(snippet.text)

        if not text:
            continue

        start = snippet.start
        end = snippet.start + snippet.duration

        if paragraph_start is None:
            paragraph_start = start

        current_length = sum(len(x) for x in current_text)

        pause = 0
        if previous_end is not None:
            pause = start - previous_end

        previous_text = current_text[-1] if current_text else ""

        sentence_finished = bool(
            re.search(r'[.!?]["\']?$', previous_text)
        )

        should_break = False

        # Strong pause between spoken segments
        if current_text and pause >= pause_threshold:
            should_break = True

        # Paragraph getting too large
        elif current_text and current_length >= max_chars:
            should_break = True

        # Natural sentence boundary after a decent-sized paragraph
        elif (
            current_text
            and sentence_finished
            and current_length >= 350
        ):
            should_break = True

        if should_break:
            paragraphs.append({
                "start": paragraph_start,
                "text": " ".join(current_text),
            })

            current_text = []
            paragraph_start = start

        current_text.append(text)
        previous_end = end

    # Final paragraph
    if current_text:
        paragraphs.append({
            "start": paragraph_start,
            "text": " ".join(current_text),
        })

    return paragraphs


def download_transcript(
    video_url: str,
    language: str,
    output: str | None,
    timestamps: bool,
):
    video_id = get_video_id(video_url)

    print(f"Video ID: {video_id}")
    print(f"Downloading transcript ({language})...")

    api = YouTubeTranscriptApi()

    transcript = api.fetch(
        video_id,
        languages=[language],
    )

    paragraphs = build_paragraphs(transcript)

    output_lines = []

    for paragraph in paragraphs:
        if timestamps:
            timestamp = format_timestamp(paragraph["start"])
            output_lines.append(f"[{timestamp}]")

        output_lines.append(paragraph["text"])
        output_lines.append("")

    full_text = "\n".join(output_lines).strip() + "\n"

    if output:
        output_path = Path(output)
    else:
        output_path = Path(f"{video_id}_transcript.txt")

    output_path.write_text(
        full_text,
        encoding="utf-8",
    )

    print()
    print(f"Created {len(paragraphs)} paragraphs.")
    print(f"Saved to: {output_path.resolve()}")


def main():
    parser = argparse.ArgumentParser(
        description="Download and format a YouTube transcript."
    )

    parser.add_argument(
        "video",
        help="YouTube URL or video ID",
    )

    parser.add_argument(
        "-l",
        "--language",
        default="en",
        help="Transcript language code (default: en)",
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Output filename",
    )

    parser.add_argument(
        "--timestamps",
        action="store_true",
        help="Add a timestamp before each paragraph",
    )

    args = parser.parse_args()

    try:
        download_transcript(
            args.video,
            args.language,
            args.output,
            args.timestamps,
        )

    except Exception as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()