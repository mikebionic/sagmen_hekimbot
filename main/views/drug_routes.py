
from flask import (
	render_template,
	redirect,
	url_for,
	request,
	make_response
)
from main import db
from . import bp
from main.views.data_utils import (
	get_drugs_list
)
from main.models import Drug

@bp.get("/drugs/")
def get_drugs():
	data = get_drugs_list()
	return render_template("drugs_table.html", data = data)



@bp.post("/manage_drugs/")
def manage_drugs():
	#data = get_drugs_list()
	req = request.get_json()
	payload = {
		"hex": req.get("hex") if "hex" in req else None,
		"name": req.get("name") if "name" in req else None,
		"name": req.get("name") if "name" in req else None,
		"name": req.get("name") if "name" in req else None,
	}
	return req