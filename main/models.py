from flask_login import UserMixin
from datetime import datetime
import secrets
from random import randint

from main import db
from main import login_manager

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	username = db.Column(db.String(255))
	name = db.Column(db.String)
	surname = db.Column(db.String)
	patronomic = db.Column(db.String)
	position = db.Column(db.String)
	work_place = db.Column(db.String)
	work_time = db.Column(db.String)
	work_map_img = db.Column(db.String)
	phone_number = db.Column(db.String)
	password = db.Column(db.String(80))
	avatar = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"username": self.username,
			"name": self.name,
			"surname": self.surname,
			"patronomic": self.patronomic,
			"position": self.position,
			"work_place": self.work_place,
			"work_time": self.work_time,
			"work_map_img": self.work_map_img,
			"phone_number": self.phone_number,
			"password": self.password,
			"avatar": self.avatar,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)


# update(** code)
class Person(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex)
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	name = db.Column(db.String)
	surname = db.Column(db.String)
	patronomic = db.Column(db.String)
	home_address = db.Column(db.String)
	m_place = db.Column(db.String)
	m_job = db.Column(db.String)
	m_level = db.Column(db.String)
	birth_date = db.Column(db.DateTime)
	birth_place = db.Column(db.String)
	country = db.Column(db.String)
	state = db.Column(db.String)
	city = db.Column(db.String)
	address = db.Column(db.String)
	ehw_name = db.Column(db.String)
	knowledge_level = db.Column(db.String)
	major = db.Column(db.String)
	last_job = db.Column(db.String)
	m_call_year = db.Column(db.Integer)
	sport_level = db.Column(db.String)

	Physical = db.relationship("Physical",backref='person',lazy=True)
	Physical_review = db.relationship("Physical_review",backref='physical_state',lazy=True)
	Medical_checkup = db.relationship("Medical_checkup",backref='person',lazy=True)
	Stomatology = db.relationship("Stomatology",backref='person',lazy=True)
	Review = db.relationship("Review",backref='person',lazy=True)
	Flurography = db.relationship("Flurography",backref='person',lazy=True)
	Vaccine = db.relationship("Vaccine",backref='person',lazy=True)
	Growth_result = db.relationship("Growth_result",backref='person',lazy=True)
	Hospitalizing = db.relationship("Hospitalizing",backref='person',lazy=True)
	Radiometry = db.relationship("Radiometry",backref='person',lazy=True)
	Note = db.relationship("Note",backref='person',lazy=True)
	Analysis = db.relationship("Analysis",backref='person',lazy=True)
	Curing_record = db.relationship("Curing_record",backref='person',lazy=True)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note":self.note,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"name": self.name,
			"surname": self.surname,
			"patronomic": self.patronomic,
			"home_address": self.home_address,
			"m_place": self.m_place,
			"m_job": self.m_job,
			"m_level": self.m_level,
			"birth_date": self.birth_date.strftime("%d.%m.%Y") if self.birth_date else None,
			"birth_place": self.birth_place,
			"country": self.country,
			"state": self.state,
			"city": self.city,
			"address": self.address,
			"ehw_name": self.ehw_name,
			"knowledge_level": self.knowledge_level,
			"major": self.major,
			"last_job": self.last_job,
			"m_call_year": self.m_call_year,
			"sport_level": self.sport_level,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Physical(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	first_review_date = db.Column(db.DateTime,default=datetime.now())
	height = db.Column(db.Integer)
	weight = db.Column(db.Integer)
	lungs_default = db.Column(db.Integer)
	lungs_inhaled = db.Column(db.Integer)
	lungs_exhaled = db.Column(db.Integer)
	spirometry = db.Column(db.String)
	dinamometry_right = db.Column(db.String)
	dinamometry_left = db.Column(db.String)
	
	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"first_review_date": self.first_review_date.strftime("%d.%m.%Y") if self.first_review_date else None,
			"height": self.height,
			"weight": self.weight,
			"lungs_default": self.lungs_default,
			"lungs_inhaled": self.lungs_inhaled,
			"lungs_exhaled": self.lungs_exhaled,
			"spirometry": self.spirometry,
			"dinamometry_right": self.dinamometry_right,
			"dinamometry_left": self.dinamometry_left,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Physical_review(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	height = db.Column(db.Integer)
	weight = db.Column(db.Integer)
	lungs_default = db.Column(db.Integer)
	lungs_inhaled = db.Column(db.Integer)
	lungs_exhaled = db.Column(db.Integer)
	spirometry = db.Column(db.String)
	dinamometry_right = db.Column(db.String)
	dinamometry_left = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"height": self.height,
			"weight": self.weight,
			"lungs_default": self.lungs_default,
			"lungs_inhaled": self.lungs_inhaled,
			"lungs_exhaled": self.lungs_exhaled,
			"spirometry": self.spirometry,
			"dinamometry_right": self.dinamometry_right,
			"dinamometry_left": self.dinamometry_left,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Medical_checkup(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	first_review_date = db.Column(db.DateTime,default=datetime.now())
	allergy = db.Column(db.String)
	has_allergy = db.Column(db.Integer,nullable=False,default=0)
	body_construction = db.Column(db.String)
	body_state = db.Column(db.String)
	bone_muscle = db.Column(db.String)
	breathing = db.Column(db.String)
	blood_cycling = db.Column(db.String)
	pulse = db.Column(db.String)
	blood_pressure = db.Column(db.String)
	blood_category = db.Column(db.String)
	stomach = db.Column(db.String)
	vision = db.Column(db.String)
	withGlass = db.Column(db.Integer, nullable=False, default=0)
	hearing = db.Column(db.String)
	nerve = db.Column(db.String)
	other = db.Column(db.String)
	reviewed_medic = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"first_review_date": self.first_review_date.strftime("%d.%m.%Y") if self.first_review_date else None,
			"allergy": self.allergy,
			"has_allergy": self.has_allergy,
			"body_construction": self.body_construction,
			"body_state": self.body_state,
			"bone_muscle": self.bone_muscle,
			"breathing": self.breathing,
			"blood_cycling": self.blood_cycling,
			"pulse": self.pulse,
			"blood_pressure": self.blood_pressure,
			"blood_category": self.blood_category,
			"stomach": self.stomach,
			"vision": self.vision,
			"withGlass": self.withGlass,
			"hearing": self.hearing,
			"nerve": self.nerve,
			"other": self.other,
			"reviewed_medic": self.reviewed_medic,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Stomatology(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Review(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	result = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"date": self.date.strftime("%d.%m.%Y") if self.date else None,
			"result": self.result,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Flurography(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	result = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"date": self.date.strftime("%d.%m.%Y") if self.date else None,
			"result": self.result,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Vaccine(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	vaccine_name = db.Column(db.String)
	quantity = db.Column(db.String)
	reaction = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"date": self.date.strftime("%d.%m.%Y") if self.date else None,
			"vaccine_name": self.vaccine_name,
			"quantity": self.quantity,
			"reaction": self.reaction,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Growth_result(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	growth = db.Column(db.String)
	health_state = db.Column(db.String)
	reviewed_medic = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"date": self.date.strftime("%d.%m.%Y") if self.date else None,
			"growth": self.growth,
			"health_state": self.health_state,
			"reviewed_medic": self.reviewed_medic,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Hospitalizing(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	result = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"date": self.date.strftime("%d.%m.%Y") if self.date else None,
			"result": self.result,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Radiometry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	result = db.Column(db.String)
	review_range = db.Column(db.String)
	yearly = db.Column(db.String)
	work_start = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"date": self.date.strftime("%d.%m.%Y") if self.date else None,
			"result": self.result,
			"review_range": self.review_range,
			"yearly": self.yearly,
			"work_start": self.work_start,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Note(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Analysis(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	
	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)


class Hospital(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	name = db.Column(db.String)
	location = db.Column(db.String)
	address = db.Column(db.String)
	color_code = db.Column(db.String)
	maxval = db.Column(db.String)
	note = db.Column(db.String)
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	Curing_record = db.relationship("Curing_record",backref='hospital',lazy=True)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"name": self.name,
			"location": self.location,
			"address": self.address,
			"color_code": self.color_code,
			"maxval": self.maxval,
			"note": self.note,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Curing_record(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	person_id = db.Column(db.Integer,db.ForeignKey("person.id"))
	hospital_id = db.Column(db.Integer,db.ForeignKey("hospital.id"))
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	enter_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	exit_date = db.Column(db.DateTime)
	completed = db.Column(db.Integer,nullable=False,default=0)
	reason = db.Column(db.String)

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"person_id": self.person_id,
			"hospital_id": self.hospital_id,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"enter_date": self.enter_date.strftime("%d.%m.%Y") if self.enter_date else None, 
			"exit_date": self.exit_date.strftime("%d.%m.%Y") if self.exit_date else None, 
			"completed": self.completed,
			"reason": self.reason,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Drug(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,nullable=False,default=datetime.now().timestamp())
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	name = db.Column(db.String)
	description = db.Column(db.String)
	qty = db.Column(db.Integer)
	unit = db.Column(db.String)
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	updated_date = db.Column(db.DateTime,nullable=False,default=datetime.now(),onupdate=datetime.now())

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"name": self.name,
			"description": self.description,
			"qty": self.qty,
			"unit": self.unit,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"updated_date": self.updated_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Drug_inv(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	name = db.Column(db.String)
	unit = db.Column(db.String)
	qty_sent = db.Column(db.Integer)
	qty_received = db.Column(db.Integer)
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	updated_date = db.Column(db.DateTime,nullable=False,default=datetime.now(),onupdate=datetime.now())

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"updated_date": self.updated_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)

class Drug_inv_line(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,default=secrets.token_hex(randint(9,15)))
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	name = db.Column(db.String)
	unit = db.Column(db.String)
	qty_sent = db.Column(db.Integer)
	qty_received = db.Column(db.Integer)
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	updated_date = db.Column(db.DateTime,nullable=False,default=datetime.now(),onupdate=datetime.now())

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"name": self.name,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"updated_date": self.updated_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)
	


class Registry(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	hex = db.Column(db.String,nullable=False,default=datetime.now().timestamp())
	deleted = db.Column(db.Integer,nullable=False,default=0)
	note = db.Column(db.String)
	doctor_id = db.Column(db.Integer)
	user_fullname = db.Column(db.String)
	title = db.Column(db.Integer)
	description = db.Column(db.String)
	date_str = db.Column(db.String)
	time_str = db.Column(db.String)
	status = db.Column(db.String)
	registry_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	created_date = db.Column(db.DateTime,nullable=False,default=datetime.now())
	updated_date = db.Column(db.DateTime,nullable=False,default=datetime.now(),onupdate=datetime.now())

	def to_json(self):
		return {
			"id": self.id,
			"hex": self.hex,
			"deleted": self.deleted,
			"note": self.note,
			"doctor_id": self.doctor_id,			
			"user_fullname": self.user_fullname,
			"title": self.title,
			"description": self.description,
			"date_str": self.date_str,
			"time_str": self.time_str,
			"status": self.status,
			"color": "red" if self.status == "declined" else "green" if self.status == "accepted" else "grey",
			"registry_date": self.registry_date.strftime("%d.%m.%Y") if self.registry_date else None,
			"created_date": self.created_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
			"updated_date": self.updated_date.strftime("%d.%m.%Y %H:%M:S") if self.created_date else None,
		}

	def update(self, **kwargs):
		for key, value in kwargs.items():
			if value is not None:
				if hasattr(self, key):
					setattr(self, key, value)