
# YouTube Video Downloader CLI

This project provides a command-line interface (CLI) tool for downloading YouTube videos, either as a single video or all videos from a specific YouTube channel, using the `pytubefix` library.

## Features

- Download a single YouTube video.
- Download all videos from a specific YouTube channel.

## Requirements

- Python 3.6 or later
- `pytubefix` library

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Ensure `pytubefix` is installed. You can find it here: [pytubefix GitHub](https://github.com/JuanBindez/pytubefix).

## Usage

Run the CLI tool using the following syntax:

```bash
python youtube_cli.py [-h] [-u URL (--single-video | --all-channel-videos)]
```

### Arguments

- **`-u, --url`**:
  Provide the YouTube video or channel URL.  
  For a single video: `https://www.youtube.com/watch?v=<video_id>`  
  For a channel: `https://www.youtube.com/@<channel_name>`

- **`-s, --single-video`**:
  Download a single YouTube video.

- **`-a, --all-channel-videos`**:
  Download all videos from a YouTube channel.

### Examples

1. Download a single video:

   ```bash
   python youtube_cli.py --url https://www.youtube.com/watch?v=<video_id> --single-video
   ```

2. Download all videos from a channel:

   ```bash
   python youtube_cli.py --url https://www.youtube.com/@<channel_name> --all-channel-videos
   ```

### Notes

- Downloaded videos will be saved in the directory: `C:\Users\<user>\Downloads\<author_name>`
- If `pytubefix` fails to fetch a specific resolution, the highest resolution available will be downloaded.

## File Structure

```
.
├── youtube_cli.py          # Main CLI script
├── downloader.py           # Contains the logic for downloading videos
├── requirements.txt        # List of dependencies
└── README.md               # Documentation
```

## Error Handling

- If an invalid URL is provided or there is an issue with the download, an error message will be displayed in the console.
- The `--url` argument is required when using `--single-video` or `--all-channel-videos`.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is licensed under the MIT License.
