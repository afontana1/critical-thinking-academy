#!/usr/bin/env python3
import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def download_video(
    url: str,
    output_dir: str,
    audio_only: bool = False,
    browser_cookies: str | None = None,
) -> None:
    out_path = Path(output_dir).expanduser().resolve()
    out_path.mkdir(parents=True, exist_ok=True)

    yt_dlp = shutil.which("yt-dlp")
    if yt_dlp is None:
        print("Error: yt-dlp is not installed or not on your PATH.")
        print("Install it with: python -m pip install -U yt-dlp")
        sys.exit(1)

    command = [
        yt_dlp,
        "--js-runtimes",
        "deno",
        "--rm-cache-dir",
        "-o",
        str(out_path / "%(title)s.%(ext)s"),
    ]

    if browser_cookies:
        command += ["--cookies-from-browser", browser_cookies]

    if audio_only:
        command += [
            "-x",
            "--audio-format",
            "mp3",
            "--audio-quality",
            "0",
        ]
    else:
        command += [
            "-f",
            "bv*+ba/b",
            "--merge-output-format",
            "mp4",
        ]

    command.append(url)

    try:
        subprocess.run(command, check=True)
        print(f"Done. Saved to: {out_path}")
    except subprocess.CalledProcessError as e:
        print(f"Download failed with exit code {e.returncode}")
        print()
        print("Things to try:")
        print("  1. Make sure Deno is installed: deno --version")
        print("  2. Try cookies: python download_video.py URL --browser-cookies chrome")
        print("  3. Try updating yt-dlp: yt-dlp -U")
        sys.exit(e.returncode)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download an allowed YouTube/video URL using yt-dlp."
    )
    parser.add_argument("url", help="Video URL")
    parser.add_argument(
        "-o",
        "--output-dir",
        default="downloads",
        help="Folder to save the file into. Default: downloads",
    )
    parser.add_argument(
        "--audio-only",
        action="store_true",
        help="Download audio only as MP3",
    )
    parser.add_argument(
        "--browser-cookies",
        choices=["chrome", "firefox", "edge", "brave", "safari"],
        help="Use cookies from your browser if the video needs your signed-in session.",
    )

    args = parser.parse_args()

    download_video(
        url=args.url,
        output_dir=args.output_dir,
        audio_only=args.audio_only,
        browser_cookies=args.browser_cookies,
    )

if __name__ == "__main__":
    """
    python3 download_video.py "http://www.youtube.com/watch?v=BLiEkiBwyzU"

    python3 download_video.py "http://www.youtube.com/watch?v=BLiEkiBwyzU" --audio-only
    """
    main()