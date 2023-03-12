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
from main.models import Person

from . import bp


@bp.route("/")
@bp.route("/main")
def main():
	return render_template("main.html")


@bp.route("/person_table/<id>")
def person_table(id):
	person = Person.query.get_or_404(id)
	return render_template("person_table.html", data=build_person_data(person))

@bp.route("/people")
def people():
	people = Person.query.all()
	return render_template(
		"people.html",
		data=[build_person_data(person) for person in people]
	)

def build_person_data(person):
	data = person.to_json()
	data["Physical"] = person.Physical[-1].to_json() if person.Physical else {}
	data["Physical_review"] = [this_data.to_json() for this_data in person.Physical_review] if person.Hospitalizing else {}
	data["Medical"] = person.Medical_checkup[-1].to_json() if person.Medical_checkup else {}
	data["Stomatology"] = person.Stomatology[-1].to_json() if person.Stomatology else {}
	data["Review"] = [this_data.to_json() for this_data in person.Review] if person.Review else {}
	data["Flurography"] = person.Flurography[-1].to_json() if person.Flurography else {}
	data["Vaccine"] = [this_data.to_json() for this_data in person.Vaccine] if person.Vaccine else {}
	data["Growth_result"] = [this_data.to_json() for this_data in person.Growth_result] if person.Growth_result else {}
	data["Hospitalizing"] = [this_data.to_json() for this_data in person.Hospitalizing] if person.Hospitalizing else {}
	data["Radiometry"] = [this_data.to_json() for this_data in person.Radiometry] if person.Radiometry else {}
	data["Note"] = [this_data.to_json() for this_data in person.Note] if person.Note else {}
	data["Analysis"] = [this_data.to_json() for this_data in person.Analysis] if person.Analysis else {}
	return data

@bp.get("/manage_person/")
@bp.get("/manage_person/<id>")
def manage_person(id=None):
	if not id:
		return render_template("manage_person.html")

	person = Person.query.get_or_404(id)
	return render_template("manage_person.html", data=build_person_data(person))

@bp.post("/manage_person/")
def manage_person_post():
	req_data = dict(request.form).copy()
	this_model = manage_person_data(req_data)
	return redirect(url_for('views.manage_person',id=this_model.id))

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

