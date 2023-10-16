
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
from main.models import User, Registry
from .send_to_ino import send_to_ino


@bp.route("/get_latest_registry/<id>")
def get_latest_registry(id):
	registry_data = [registry.to_json() for registry in
		Registry.query
			.filter(Registry.deleted < 1)\
			.filter(Registry.status == "")\
			.filter(Registry.doctor_id == int(id))\
			.order_by(Registry.id.desc())\
			.order_by(Registry.doctor_id.desc()).all()]
	return {
		"data": registry_data,
		"doctor_id": id,
		"status": 1
	}


@bp.route("/registry_home/")
def get_registry_home():
	dentists = User.query.filter_by(position="dentist").all()
	registry_data = [registry.to_json() for registry in
		Registry.query
			.filter(Registry.deleted < 1)\
			.order_by(Registry.id.desc())\
			.order_by(Registry.doctor_id.desc()).all()]
	return render_template("registry_home.html", dentists=dentists, registry_data=registry_data)


@bp.route("/manage_registry/", methods=["post"])
def manage_registry():
	# delete = request.args.get("delete",0,type=int)
	status, message = 0, ""
	req = request.get_json()
	payload = {
		"hex": req.get("hex") if "hex" in req else None,
		"doctor_id": req.get("doctor_id") if "doctor_id" in req else None,
		"user_fullname": req.get("user_fullname") if "user_fullname" in req else None,
		"title": req.get("title") if "title" in req else None,
		"description": req.get("description") if "description" in req else None,	
		"time_str": req.get("time_str") if "time_str" in req else None,
		"status": req.get("status") if "status" in req else "",
		"registry_date": datetime.strptime(req.get("registry_date"), "%d.%m.%Y") if "date_str" in req else None,	
	}

	if "deleted" in req:
		payload["deleted"] = req.get("deleted")

	this_model = None
	if payload['hex']:
		this_model = Registry.query.filter_by(hex = payload["hex"]).filter(Registry.deleted < 1).first()
	
	if not this_model:
		payload["hex"] = secrets.token_hex((randint(9,15)))
		this_model = Registry(**payload)
		db.session.add(this_model)
		# if payload["doctor_id"] == 3:
		try:
			send_to_ino(payload["user_fullname"],payload["title"])
		except Exception as e:
			print(e)
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


@bp.route("/update_latest/")
def update_latest():
	doctor_id = request.args.get("doctor_id", 0, type=int)
	# accepted
	# declined
	status = request.args.get("status","",type=str)
	reg = Registry.query.filter_by(doctor_id=doctor_id)\
		.filter(Registry.status == "")\
		.order_by(Registry.created_date.desc()).first()
	print("changing..")
	print(reg.to_json())
	reg.status = status
	db.session.commit()
	print("++++++++++++++++")
	print(reg.to_json())
	return "ok"


@bp.route("/registry_doctor/<id>")
def get_registry_doctor(id=1):
	dentist = User.query.get(id)
	registry_data = [registry.to_json() for registry in
		Registry.query
			.filter_by(doctor_id = id).filter(Registry.deleted < 1)\
			.order_by(Registry.id.desc())\
			.order_by(Registry.doctor_id.desc()).all()]
	return render_template("registry_doctor.html", dentist=dentist, registry_data=registry_data)
