from main.models import (
	Curing_record,
	Person,
	Physical,
	Physical_review,
	Medical_checkup,
	Review,
	Stomatology,
	Flurography,
	Vaccine,
	Growth_result,
	Hospitalizing,
	Radiometry,
	Note,
	Analysis,
	Drug,
)
from main import db
from datetime import datetime
from sqlalchemy import or_

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

def get_hospital_list():
	h = Curing_record.query.filter(or_(
		Curing_record.exit_date <= datetime.now().date(),
		Curing_record.exit_date == None)
	).all()
	return h

def get_drugs_list():
	drugs_data = Drug.query\
		.filter_by(deleted = 0)\
		.order_by(Drug.updated_date.desc())\
		.all()
	
	return [data.to_json() for data in drugs_data]