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
	Hospital,
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
	people_qty = Person.query.count()
	hospitals = Hospital.query.all()
	h_list = []
	all_in_hospitals = 0
	for h in hospitals:
		h_data = h.to_json()
		h_data['qty'] = h = Curing_record.query\
			.filter(Curing_record.hospital_id == h.id)\
			.filter(
				Curing_record.enter_date <= datetime.now().date(),
				Curing_record.completed == 0)\
			.count()
			# .filter(or_(
			# 	Curing_record.exit_date <= datetime.now().date(),
			# 	Curing_record.exit_date == None))\
		all_in_hospitals += h_data['qty']
		h_list.append(h_data)

	return {
		"data": [
			{
				"name": "Işjeň",
				"qty": people_qty - all_in_hospitals,
				"maxval": people_qty,
				"hex": "rest",
				"id": "rest",
				"color_code": "#2BB930",
			},
			*h_list,
		]
	}

def get_loc_clinic_list():
	local_list = Curing_record.query\
		.filter_by(hospital_id = 1)\
		.filter(
			Curing_record.enter_date <= datetime.now().date(),
			or_(Curing_record.completed == 0, Curing_record.completed == None))\
		.all()
	return {
		"data": [
			item.person.to_json() for item in local_list
		]
	}

def get_drugs_list():
	drugs_data = Drug.query\
		.filter_by(deleted = 0)\
		.order_by(Drug.updated_date.desc())\
		.all()
	
	return [data.to_json() for data in drugs_data]