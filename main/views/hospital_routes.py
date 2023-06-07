

from flask import (
	render_template,
	redirect,
	url_for,
	request,
	make_response
)
import secrets
from random import randint
from main import db
from . import bp
from main.views.data_utils import (
	get_hospital_records_list,
	get_hospital_info,
)
from main.models import Curing_record

@bp.get("/hospital_records/")
def get_hospital_records():
	id = request.args.get("id")
	data = get_hospital_records_list(id)
	hospital_data = get_hospital_info(id)
	return render_template("hospital_records_table.html", hospital_data=hospital_data, data = data)


@bp.post("/manage_hospital_records/")
def manage_hospital_records():
	delete = request.args.get("delete",0,type=int)
	status, message = 0, ""
	req = request.get_json()
	payload = {
		"hex": req.get("hex") if "hex" in req else None,
		"name": req.get("name") if "name" in req else None,
		"note": req.get("note") if "note" in req else None,
		"unit": req.get("unit") if "unit" in req else None,
		"qty": req.get("qty") if "qty" in req else None,
	}

	if delete:
		payload = {
			"hex": req.get("hex"),
			"deleted": 1
		}

	this_model = None
	if payload['hex']:
		this_model = Curing_record.query.filter_by(hex = payload["hex"]).first()
	
	if not this_model:
		payload["hex"] = secrets.token_hex((randint(9,15)))
		this_model = Curing_record(**payload)
		db.session.add(this_model)
		status, message = 1, "created"
	else:
		this_model.update(**payload)
		status, message = 2, "updated"

	db.session.commit()
	return {
		"status": status,
		"message": message,
		"data": this_model.to_json()
	}