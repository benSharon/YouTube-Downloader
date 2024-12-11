# reference: https://github.com/JuanBindez/pytubefix
import argparse

from downloader import (
    download_single_video,
    download_all_channel_videos,
    get_channel_urls,
)


def main():
    PROG = "python youtube_cli.py"
    USAGE = "python __main__.py [-h] [-u URL (--download | --all-channel-videos)]"
    DESCRIPTION = "Command-line tool for downloading single or multiple YouTube videos."
    EPILOG = """Example of usage:
    python youtube_cli.py --url https://www.youtube.com/watch?v=<video_id> --download
    python youtube_cli.py --url https://www.youtube.com/@<channel_name> --all-channel-videos
    """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        usage=USAGE,
        prog=PROG,
        description=DESCRIPTION,
        epilog=EPILOG,
    )

    download_group = parser.add_argument_group("Download options")

    download_group.add_argument(
        "-d",
        "--download",
        help="Download a single YouTube video",
        action="store_true",
    )

    download_group.add_argument(
        "-a",
        "--all-channel-videos",
        help="Download all videos of a YouTube channel",
        action="store_true",
    )

    download_group.add_argument(
        "-u",
        "--url",
        type=str,
        help="https://www.youtube.com/watch?v=<video_id> for --download and "
        "https://www.youtube.com/@<channel_name> for --all-channel-videos",
    )

    args = parser.parse_args()

    if (args.download or args.all_channel_videos) and not args.url:
        parser.error("--url is required with --single-videos or --all-channel-videos")

    if args.download:
        download_single_video(args.url)
    elif args.all_channel_videos:
        download_all_channel_videos(args.url)


if __name__ == "__main__":
    main()
