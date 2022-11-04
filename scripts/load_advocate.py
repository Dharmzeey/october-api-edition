from api_edition.models import Advocate, Company
from faker import Faker
import random

fake = Faker()

def run():
  for _ in range(4999):
    name = fake.name()
    username = str(name.split(" ")[1])
    short = fake.text()[:245]
    long = fake.text() + fake.sentence() + fake.sentence()
    # THIS GENERATES A RANDON EXPERIENCE YEARS FROM 1 - 10
    rand_comp = random.randint(1, 500)
    # THIS GENERATES A RANDON DIGIT YEARS FROM 1 - 500 (WHICH IS THE TOTAL COMPANY WE HAVE)
    exp = random.randint(1, 10)
    # THIS PICKS THE RANDOM NO GENERATED ITEM IN THE RETURNED ITEM
    comp = Company.objects.order_by("?")[rand_comp - 1]
    advocate = Advocate.objects.create(username=username, name=name, short_bio=short, long_bio=long, advocate_years_exp=exp, company=comp)
    advocate.save()
    
    advocate_username = f"{advocate.username}{advocate.id}"
    advocate.username = advocate_username
    advocate.save()
