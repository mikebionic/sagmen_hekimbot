from flask import (
	render_template,
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
	data["Medical"] = person.Medical_checkup[-1].to_json() if person.Medical_checkup else {}
	data["Stomatology"] = person.Stomatology[-1].to_json() if person.Stomatology else {}
	data["Review"] = person.Review[-1].to_json() if person.Review else {}
	data["Flurography"] = person.Flurography[-1].to_json() if person.Flurography else {}
	data["Vaccine"] = person.Vaccine[-1].to_json() if person.Vaccine else {}
	data["Growth_result"] = person.Growth_result[-1].to_json() if person.Growth_result else {}
	data["Hospitalizing"] = person.Hospitalizing[-1].to_json() if person.Hospitalizing else {}
	data["Radiometry"] = person.Radiometry[-1].to_json() if person.Radiometry else {}
	data["Note"] = person.Note[-1].to_json() if person.Note else {}
	data["Analysis"] = person.Analysis[-1].to_json() if person.Analysis else {}
	return data

@bp.route("/manage_person/")
@bp.route("/manage_person/<id>")
def manage_person(id=None):
	if not id:
		return render_template("manage_person.html")
	
	person = Person.query.get_or_404(id)
	return render_template("manage_person.html", data=build_person_data(person))
	