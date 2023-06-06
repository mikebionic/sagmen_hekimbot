import sys, json
from os import path
from datetime import datetime, date, timedelta
import secrets
from random import randint

from main import db, create_app
from main.config import Config
from main.models import Curing_record, Drug, Hospital, User, Physical, Medical_checkup, Person



migration_data = None
try:
    with open('migration_data.json', 'r', encoding="utf-8") as f:
        migration_data = json.load(f)
except:
	pass

try:
	if not migration_data:
		raise Exception("Migration data error")


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
	db.session.commit()


	for user in migration_data["users_data"]:
		current_user = User(**user)
		db.session.add(current_user)
		db.session.commit()

	p_count = 0
	for person in migration_data["persons_data"]:
		person["date"] = datetime.strptime(person["date"], "%d.%m.%Y") if len(person["date"]) > 5 else None
		person["birth_date"] = datetime.strptime(person["birth_date"], "%d.%m.%Y") if len(person["birth_date"]) > 5 else None
		current_person = Person(
			**person,
		)
		db.session.add(current_person)
		db.session.commit()

		if p_count < len(migration_data["physicals_data"]):
			migration_data["physicals_data"][p_count]["person_id"] = current_person.id ##p_count ##
			migration_data["mcheckups_data"][p_count]["person_id"] = current_person.id ##p_count ##
		p_count += 1


	for physical in migration_data["physicals_data"]:
		physical["first_review_date"] = datetime.strptime(physical["first_review_date"], "%d.%m.%Y") if len(physical["first_review_date"]) > 5 else None
		current_physical = Physical(**physical)
		db.session.add(current_physical)
		db.session.commit()

	for mcheckup in migration_data["mcheckups_data"]:
		mcheckup["first_review_date"] = datetime.strptime(mcheckup["first_review_date"], "%d.%m.%Y") if len(mcheckup["first_review_date"]) > 5 else None
		current_mcheckup = Medical_checkup(**mcheckup)
		db.session.add(current_mcheckup)
		db.session.commit()


	for drug in migration_data["drugs_data"]:
		current_drug = Drug(
			**drug,
			hex = secrets.token_hex(randint(9,15))
		)
		db.session.add(current_drug)
		db.session.commit()


	############


	for hospital in migration_data["hospitals_data"]:
		current_hospital = Hospital(**hospital)
		db.session.add(current_hospital)
		db.session.commit()

	############################


	for curingr in migration_data["curingrs_data"]:
		curingr["enter_date"] = datetime.strptime(curingr["enter_date"], "%d.%m.%Y") if len(curingr["enter_date"]) > 5 else None
		curingr["exit_date"] = datetime.strptime(curingr["exit_date"], "%d.%m.%Y") if len(curingr["exit_date"]) > 5 else None
		current_curingr = Curing_record(**curingr)
		db.session.add(current_curingr)
		db.session.commit()


	db.session.commit()


except Exception as ex:
	print(ex)
