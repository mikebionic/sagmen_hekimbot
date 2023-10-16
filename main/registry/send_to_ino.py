

from flask import (
	render_template,
	redirect,
	url_for,
	request,
	make_response
)
from . import bp
from main.config import Config

# ino_ip = "192.168.43.223"

def send_to_ino(name, title):
	req_line = f"http://{Config['INO_IP']}/control/?name={name}&title={title}"
	r = requests.get(req_line)
	print(r.text)

