from rest_framework import serializers
from .models import Advocate, Company

class CompanySerializer(serializers.ModelSerializer):
  links = serializers.ReadOnlyField(source='set_links')
  url = serializers.HyperlinkedIdentityField(
    view_name='company_details',
    lookup_field='pk'
  )
  # advocates = serializers.PrimaryKeyRelatedField(source='advocate_of_a_company', many=True, read_only=True)
  class Meta:
    model = Company
    fields = ['id', 'name', 'logo', 'summary', 'url', 'links']
    depth = 1
      

class AdvocateSerializer(serializers.ModelSerializer):
  company = CompanySerializer()
  links = serializers.ReadOnlyField(source='set_links')
  url = serializers.HyperlinkedIdentityField(
    view_name='advocate_details',
    lookup_field='pk'
  )
  class Meta:
    model = Advocate
    fields = [ 'id', 'name', 'username', 'profile_pic', 'short_bio', 'long_bio', 'advocate_years_exp', 'url', 'links', 'company']
