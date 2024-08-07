import subprocess

vlc_path = r"C:\Program Files\VideoLAN\VLC\vlc.exe"

try:
  url = input('URL: ')
  subprocess.call(f'yt-dlp -F {url}')
  f = input('(Optional) Choose format: ') or 'best'
  res = subprocess.check_output(f'yt-dlp --get-url --format {f} {url}')
  res = res.decode('utf-8').split('\n')[0]
  subprocess.Popen([vlc_path, "--meta-title=youtube-dl", res])
except Exception as e:
  print(e)
  input('Press Enter to exit')
