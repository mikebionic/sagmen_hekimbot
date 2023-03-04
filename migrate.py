from main import db, create_app
from main.config import Config
from main.models import User, Physical, Medical_checkup, Person

from datetime import datetime


app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

admin_user = User(
	username = Config.ADMIN_USERNAME,
	password = Config.ADMIN_PIN,
	position="admin"
)
db.session.add(admin_user)

users_data = [
	{
		"username": "plan",
		"password": "123",
		"name": "Plan",
		"surname": "Planyyew",
		"patronomic": "Planyyewic",
		"position": "medic",
	},
	{
		"username": "jemal",
		"password": "123",
		"name": "Jemal",
		"surname": "Planyyewa",
		"patronomic": "Planyyewna",
		"position": "medic",
	}
]


for user in users_data:
	current_user = User(**user)
	db.session.add(current_user)


persons_data = [
	{
		"note": "",
		"date": datetime(2020,11,23),
		"name": "Süleýman",
		"surname": "Ataýew",
		"patronomic": "Ahmedowiç",
		"home_address": "Balkan w. Türkmenbaşy ş. Andalyp",
		"m_place": "000 h/b Balkan wel",
		"m_job": "",
		"m_level": "Orta",
		"birth_date": datetime(2002,10,14),
		"birth_place": "",
		"country": "",
		"state": "",
		"city": "",
		"address": "",
		"ehw_name": "Türkmenbaşy ş. hw",
		"knowledge_level": "",
		"major": "",
		"last_job": "Öý işler",
		"m_call_year": 2020,
		"sport_level": "",
	},
]



physicals_data = [
	{
		"note": "",
		"person_id": None,
		"first_review_date": datetime(2020,11,22),
		"height": 181,
		"weight": 62,
		"lungs_default": 86,
		"lungs_inhaled": 88,
		"lungs_exhaled": 85,
		"spirometry": "",
		"dinamometry_right": "",
		"dinamometry_left": "",
	}
]

mcheckups_data = [
	{
		"note": "",
		"person_id": None,
		"first_review_date": datetime(2020,11,22),
		"allergy": "Dermana, iýmite allergiýasy ýok",
		"has_allergy": 0,
		"body_construction": "Normosteniki",
		"body_state": "Adaty",
		"bone_muscle": "Göze görünýän deformasiýa ýok",
		"breathing": "Öýkenlerde wezikulýar dem alyş eşdilýär. DAÝ:16'",
		"blood_cycling": "Ýürek toulary aýdyň, ritmiki",
		"pulse": "P8: 78'",
		"blood_pressure": "AGB: 170/80 mmss",
		"blood_category": "4B+",
		"stomach": "Dili çygly, arassa. Garny ýumşak, agry ýok. Bagry we dalagy ",
		"vision": "OU = 1.0",
		"withGlass": 0,
		"hearing": "Pyşdyly sesi 6m eşidýär",
		"nerve": "Durnukly",
		"other": "K/K: Sagdyn",
		"reviewed_medic": "",
	}
]


p_count = 0
for person in persons_data:
	current_person = Person(**person)
	db.session.add(current_person)
	db.session.commit()
	if p_count < len(physicals_data):
		physicals_data[p_count]["person_id"] = current_person.id ##p_count ##
		mcheckups_data[p_count]["person_id"] = current_person.id ##p_count ##
	p_count += 1


for physical in physicals_data:
	current_physical = Physical(**physical)
	db.session.add(current_physical)

for mcheckup in mcheckups_data:
	current_mcheckup = Medical_checkup(**mcheckup)
	db.session.add(current_mcheckup)

db.session.commit()