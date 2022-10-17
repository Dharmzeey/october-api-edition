from django.contrib import admin
from django.urls import reverse

from django.contrib import messages
from .models import Advocate, Company

# THE CLASSES BELOW WORKS ON THE URL BY REMOVING IT FROM THE INPUT FIELD AND ALSO POPULATING IT WHEN SAVE IS CALLED
class EditAdvocate(admin.ModelAdmin):
  exclude = ("url", )  
  def save_model(self, request, obj, form, change):
    obj.save()
    obj.url = request.build_absolute_uri(reverse('advocate_details', args=(obj.id, )))
    messages.info(request, "Advocate Added Successfully")
    return super().save_model(request, obj, form, change)

class EditCompany(admin.ModelAdmin):
  exclude = ("url", )  
  def save_model(self, request, obj, form, change):
    obj.save()
    obj.url = request.build_absolute_uri(reverse('company_details', args=(obj.id, )))
    messages.info(request, "Advocate Added Successfully")
    return super().save_model(request, obj, form, change)
  
admin.site.register(Advocate, EditAdvocate)
admin.site.register(Company, EditCompany)