import	requests

from . import bp
from main.config import Config

# ino_ip = "192.168.43.223"

def send_to_ino(name, title):
	try:
		req_line = f"http://{Config.INO_IP}/control/?name={name}&title={title}"
		print(req_line)
		r = requests.get(req_line)
		print(r.text)
	except Exception as e:
		print(e)

