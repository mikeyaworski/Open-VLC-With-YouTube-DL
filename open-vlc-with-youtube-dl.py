import subprocess

vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"

while True:
  try:
    url = input('URL: ')
    subprocess.call(f'yt-dlp -F {url}')

    video_format = input('(Optional) Choose VIDEO format: ') or 'best'
    audio_format = input('(Optional) Choose AUDIO format: ')

    # Two separate commands since the format of --get-url sometimes returns multiple results for the video format,
    # which means doing --format={video_format}+{audio_format} is difficult to parse
    video_stream_url = subprocess.check_output(f'yt-dlp --get-url --format {video_format} {url}')
    video_stream_url = video_stream_url.decode('utf-8').split('\n')[0]

    args = [
      vlc_path,
      '--meta-title=youtube-dl',
      video_stream_url,
    ]

    if audio_format:
      audio_stream_url = subprocess.check_output(f'yt-dlp --get-url --format {audio_format} {url}')
      audio_stream_url = audio_stream_url.decode('utf-8').split('\n')[0]
      args.extend([
        "--input-slave",
        audio_stream_url
      ])

    subprocess.Popen(args)
    break
  except Exception as e:
    print(e)
