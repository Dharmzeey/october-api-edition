from api_edition.models import Advocate, Company
from faker import Faker
import random

fake = Faker()

def run():
  for _ in range(5000):
    name = fake.name()
    short = fake.text()[:248]
    long = fake.text() + fake.sentence() + fake.sentence()
    exp = random.randint(1, 10)
    rand_comp = random.randint(10, 200)
    comp = Company.objects.get(id=rand_comp)
    advocate = Advocate.objects.create(name=name, short_bio=short, long_bio=long, advocate_years_exp=exp, company=comp)
    advocate.save()
