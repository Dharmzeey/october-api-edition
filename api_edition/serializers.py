from rest_framework import serializers
from .models import Advocate, Company


class CompanySerializer(serializers.ModelSerializer):
  links = serializers.ReadOnlyField(source='set_links')
  class Meta:
    model = Company
    fields = ['id', 'name', 'logo', 'summary', 'url', 'links']
    depth = 1
    
    
# class CompanyFilterSerializer(serializers.ModelSerializer):  
#   class Meta:
#     model = Company
#     fields = ['id', 'name', 'logo', 'url', 'summary']
   

class AdvocateSerializer(serializers.ModelSerializer):
  company = CompanySerializer()
  links = serializers.ReadOnlyField(source='set_links')
  
  class Meta:
    model = Advocate
    fields = [ 'id', 'name', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'url', 'links', 'company']