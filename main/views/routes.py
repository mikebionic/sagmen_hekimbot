from flask import (
	render_template,
	redirect,
	url_for,
	request
)
from main.views.req_utils import (
	manage_person_data,
	manage_physical_data,
	manage_medical_data
)
from main.views.data_utils import (
	build_person_data,
	get_hospital_list
)
from main.models import Person
from main import db
from . import bp


@bp.route("/")
@bp.route("/main")
def main():
	return render_template("main.html")


@bp.route("/person_table/<id>")
def person_table(id):
	person = Person.query.filter_by(deleted = 0, id = id).first()
	return render_template("person_table.html", data=build_person_data(person))

@bp.route("/people")
def people():
	people = Person.query.filter_by(deleted = 0).all()
	return render_template(
		"people.html",
		data=[build_person_data(person) for person in people]
	)


@bp.get("/manage_person/")
@bp.get("/manage_person/<id>")
def manage_person(id=None):
	if not id:
		return render_template("manage_person.html")

	person = Person.query.filter_by(deleted = 0, id = id).first()
	return render_template("manage_person.html", data=build_person_data(person))

@bp.post("/manage_person/")
def manage_person_post():
	req_data = dict(request.form).copy()
	this_model = manage_person_data(req_data)
	return redirect(url_for('views.manage_person',id=this_model.id))

@bp.get("/manage_person/delete/<hex>/")
def manage_person_delete(hex):
	if not hex:
		return redirect(url_for('views.people'))
	person = Person.query.filter_by(hex = hex).first()
	if person:
		person.deleted = 1
		db.session.commit()
	return redirect(url_for('views.people'))


@bp.post("/manage_person/physical/")
def manage_physical():
	req_data = dict(request.form).copy()
	this_model = manage_physical_data(req_data)
	return redirect(url_for('views.manage_person',id=this_model.person_id))

@bp.post("/manage_person/medical/")
def manage_medical():
	req_data = dict(request.form).copy()
	this_model = manage_medical_data(req_data)
	return redirect(url_for('views.manage_person',id=this_model.person_id))


@bp.get("/curing_records/")
def get_curing_records():
	data = get_hospital_list()
	print(data)
	print([item.to_json() for item in data])
	return "ok"