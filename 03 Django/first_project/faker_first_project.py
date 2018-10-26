import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

import django
django.setup()

## Fake Population Scripts
from faker import Faker
from second_app.models import User

fakegen = Faker()


def add_users(N=5):
	for entry in range(N):
		fname = fakegen.first_name()
		lname = fakegen.last_name()
		email = fakegen.safe_email()

		#create new user
		user = User.objects.get_or_create(first_name=fname,last_name=lname,email=email)[0]

if __name__ == '__main__':
    print("populating script!")
    add_users(10)
    print("populating complete")