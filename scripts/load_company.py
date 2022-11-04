from api_edition.models import Company
from faker import Faker

fake = Faker()

def run():
  for _ in range(200):
    name = fake.name()
    summary = fake.text()
    
    company = Company.objects.create(name=name, summary=summary)
    company.save()