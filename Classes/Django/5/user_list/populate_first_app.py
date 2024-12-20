import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_list.settings")

import django

django.setup()

# Fake pop script

import random
from first_app.models import User
from faker import Faker

fakegen = Faker()


def populate(N=5):
    for entry in range(N):

        fake_first_name = fakegen.first_name()
        fake_last_name = fakegen.last_name()
        fake_email = fakegen.email()

        newUser = User.objects.get_or_create(
            firstName=fake_first_name, lastName=fake_last_name, email=fake_email
        )[0]


if __name__ == "__main__":
    print("populating script!")
    populate(20)
    print("populating complete")
