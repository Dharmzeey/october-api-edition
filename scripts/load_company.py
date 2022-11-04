from api_edition.models import Company
from faker import Faker

fake = Faker()

def run():
  for _ in range(499):
    name = str(fake.name().split(" ")[0])
    summary = fake.text()
    company = Company.objects.create(name=name, summary=summary)
    company.save()