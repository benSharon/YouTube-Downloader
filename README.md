
# YouTube CLI Downloader

A command-line tool for downloading single or multiple YouTube videos using `pytubefix`. 

## Features

- Download a single YouTube video.
- Download all videos from a YouTube channel.
- Automatically organizes downloaded videos by the author's name.

## Requirements

- Python 3.x
- `pytubefix` library

## Installation

1. Clone this repository or download the files.
2. Install dependencies:
    ```bash
    pip install pytubefix
    ```

## Usage

Run the script using the command line with the appropriate options.

### Commands

- **Download a Single Video**
    ```bash
    python youtube_cli.py --url https://www.youtube.com/watch?v=<video_id> --download
    ```

- **Download All Videos from a Channel**
    ```bash
    python youtube_cli.py --url https://www.youtube.com/@<channel_name> --all-channel-videos
    ```

### Example

1. Download a single video:
    ```bash
    python youtube_cli.py --url https://www.youtube.com/watch?v=example123 --download
    ```

2. Download all videos from a channel:
    ```bash
    python youtube_cli.py --url https://www.youtube.com/@exampleChannel --all-channel-videos
    ```

## File Structure

- `youtube_cli.py`: Main script to handle command-line arguments and invoke the downloader functions.
- `downloader.py`: Contains functions for downloading single videos and all videos from a channel.

## Error Handling

- **VideoUnavailable Error**: If a video is restricted or unavailable, it will display a specific error message.
- **General Errors**: Any other issues will be caught and logged for debugging.

## Output

- Videos are downloaded to:
    ```
    C:\Users\<YourUsername>\Downloads\<AuthorName>
    ```

## Contributing

Feel free to fork the repository and submit pull requests for new features or bug fixes.

## License

This project is licensed under the MIT License.
