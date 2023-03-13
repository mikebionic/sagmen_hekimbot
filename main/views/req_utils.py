from main.models import (
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
)
from main import db
from datetime import datetime

def manage_person_data(req_data, action=None):
	insertion_data = {}
	#if "person_hex" in req_data:
	#	insertion_data["hex"] = req_data["person_hex"]
	if "person_name" in req_data:
		insertion_data["name"] = req_data["person_name"]
	if "person_surname" in req_data:
		insertion_data["surname"] = req_data["person_surname"]
	if "person_patronomic" in req_data:
		insertion_data["patronomic"] = req_data["person_patronomic"]
	if "person_birth_date" in req_data:
		insertion_data["birth_date"] = datetime.strptime(req_data["person_birth_date"], "%d.%m.%Y")
	if "person_birth_place" in req_data:
		insertion_data["birth_place"] = req_data["person_birth_place"]
	if "person_home_address" in req_data:
		insertion_data["home_address"] = req_data["person_home_address"]
	if "person_ehw_name" in req_data:
		insertion_data["ehw_name"] = req_data["person_ehw_name"]
	if "person_knowledge_level" in req_data:
		insertion_data["knowledge_level"] = req_data["person_knowledge_level"]
	if "person_last_job" in req_data:
		insertion_data["last_job"] = req_data["person_last_job"]
	if "person_m_call_year" in req_data:
		insertion_data["m_call_year"] = req_data["person_m_call_year"]
	if "person_sport_level" in req_data:
		insertion_data["sport_level"] = req_data["person_sport_level"]
	if "person_m_level" in req_data:
		insertion_data["m_level"] = req_data["person_m_level"]
	if "person_m_job" in req_data:
		insertion_data["m_job"] = req_data["person_m_job"]
	if "person_m_place" in req_data:
		insertion_data["m_place"] = req_data["person_m_place"]
	
	if action == "delete":
		print("deleting.......")
		insertion_data["deleted"] = 1

	if "person_hex" in req_data:
		this_model = Person.query.filter_by(hex = req_data["person_hex"]).first()
	
	if this_model:
		this_model.update(**insertion_data)
		db.session.commit()
	if not this_model:
		this_model = Person(**insertion_data)
		db.session.add(this_model)
		db.session.commit()
	return this_model

def manage_physical_data(req_data):
	insertion_data = {}
	if "physical_hex" in req_data:
		insertion_data["hex"] = req_data["physical_hex"]
	if "physical_note" in req_data:
		insertion_data["note"] = req_data["physical_note"]
	if "physical_person_id" in req_data:
		insertion_data["person_id"] = req_data["physical_person_id"]
	#if "physical_created_date" in req_data:
	#	insertion_data["created_date"] = datetime.strptime(req_data["physical_created_date"], "%d.%m.%Y") if req_data["physical_created_date"] else None,
	if "physical_first_review_date" in req_data:
		insertion_data["first_review_date"] = datetime.strptime(req_data["physical_first_review_date"], "%d.%m.%Y") if req_data["physical_first_review_date"] else None,
	if "physical_height" in req_data:
		insertion_data["height"] = req_data["physical_height"]
	if "physical_weight" in req_data:
		insertion_data["weight"] = req_data["physical_weight"]
	if "physical_lungs_default" in req_data:
		insertion_data["lungs_default"] = req_data["physical_lungs_default"]
	if "physical_lungs_inhaled" in req_data:
		insertion_data["lungs_inhaled"] = req_data["physical_lungs_inhaled"]
	if "physical_lungs_exhaled" in req_data:
		insertion_data["lungs_exhaled"] = req_data["physical_lungs_exhaled"]
	if "physical_spirometry" in req_data:
		insertion_data["spirometry"] = req_data["physical_spirometry"]
	if "physical_dinamometry_right" in req_data:
		insertion_data["dinamometry_right"] = req_data["physical_dinamometry_right"]
	if "physical_dinamometry_left" in req_data:
		insertion_data["dinamometry_left"] = req_data["physical_dinamometry_left"]

	if "physical_hex" in req_data:
		this_model = Physical.query.filter_by(hex = req_data["physical_hex"]).first()
	
	if this_model:
		this_model.update(**insertion_data)
		db.session.commit()
	if not this_model:
		this_model = Physical(**insertion_data)
		db.session.add(this_model)
		db.session.commit()
	return this_model


def manage_medical_data(req_data):
	insertion_data = {}

	if "medical_hex" in req_data:
		insertion_data["hex"] = req_data["medical_hex"]
	if "medical_note" in req_data:
		insertion_data["note"] = req_data["medical_note"]
	if "medical_person_id" in req_data:
		insertion_data["person_id"] = req_data["medical_person_id"]
	#if "medical_created_date" in req_data:
	#	insertion_data["created_date"] = datetime.strptime(req_data["medical_created_date"], "%d.%m.%Y") if req_data["medical_created_date"] else None,
	if "medical_first_review_date" in req_data:
		insertion_data["first_review_date"] = datetime.strptime(req_data["medical_first_review_date"], "%d.%m.%Y") if req_data["medical_first_review_date"] else None,
	if "medical_allergy" in req_data:
		insertion_data["allergy"] = req_data["medical_allergy"]
	if "medical_has_allergy" in req_data:
		insertion_data["has_allergy"] = req_data["medical_has_allergy"]
	if "medical_body_construction" in req_data:
		insertion_data["body_construction"] = req_data["medical_body_construction"]
	if "medical_body_state" in req_data:
		insertion_data["body_state"] = req_data["medical_body_state"]
	if "medical_bone_muscle" in req_data:
		insertion_data["bone_muscle"] = req_data["medical_bone_muscle"]
	if "medical_breathing" in req_data:
		insertion_data["breathing"] = req_data["medical_breathing"]
	if "medical_blood_cycling" in req_data:
		insertion_data["blood_cycling"] = req_data["medical_blood_cycling"]
	if "medical_pulse" in req_data:
		insertion_data["pulse"] = req_data["medical_pulse"]
	if "medical_blood_pressure" in req_data:
		insertion_data["blood_pressure"] = req_data["medical_blood_pressure"]
	if "medical_blood_category" in req_data:
		insertion_data["blood_category"] = req_data["medical_blood_category"]
	if "medical_stomach" in req_data:
		insertion_data["stomach"] = req_data["medical_stomach"]
	if "medical_vision" in req_data:
		insertion_data["vision"] = req_data["medical_vision"]
	if "medical_withGlass" in req_data:
		insertion_data["withGlass"] = req_data["medical_withGlass"]
	if "medical_hearing" in req_data:
		insertion_data["hearing"] = req_data["medical_hearing"]
	if "medical_nerve" in req_data:
		insertion_data["nerve"] = req_data["medical_nerve"]
	if "medical_other" in req_data:
		insertion_data["other"] = req_data["medical_other"]
	if "medical_reviewed_medic" in req_data:
		insertion_data["reviewed_medic"] = req_data["medical_reviewed_medic"]

	if "medical_hex" in req_data:
		this_model = Medical_checkup.query.filter_by(hex = req_data["medical_hex"]).first()
	
	if this_model:
		this_model.update(**insertion_data)
		db.session.commit()
	if not this_model:
		this_model = Medical_checkup(**insertion_data)
		db.session.add(this_model)
		db.session.commit()
	return this_model