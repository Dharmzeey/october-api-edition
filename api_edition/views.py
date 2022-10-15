from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from rest_framework.views import APIView
from django.views.generic import CreateView
from rest_framework import generics
from rest_framework.response import Response
from .models import Advocate, Company
from .serializers import AdvocateSerializer, CompanySerializer

class APIEndpoints(APIView):
  def get(self, request):
    companies = request.build_absolute_uri('companies')
    advocates = request.build_absolute_uri('advocates')
    return Response({"Companies": companies, "Advocates": advocates})
home = APIEndpoints.as_view()

class AddAdvocate(LoginRequiredMixin, CreateView):
  model = Advocate
  template_name = 'api_edition/add_advocate.html'
  fields = ["name", "profile_pic", "short_bio", "long_bio","advocate_years_exp", "company", "youtube", "twitter", "github", "linkedin", "website"]
  success_url = 'add-advocate'
  def form_valid(self, form):
    form.save()
    form.instance.url = self.request.build_absolute_uri(reverse('advocate_details', args=(form.instance.id, )))
    form.save()
    print(form.instance.url)
    return super().form_valid(form)
add_advocate = AddAdvocate.as_view()

class AddCompany(LoginRequiredMixin, CreateView):
  model = Company
  template_name = 'api_edition/add_advocate.html'
  fields = ["name", "logo", "summary", "advocates", "youtube", "twitter", "github", "linkedin", "website"]
  success_url = 'add-company'
  def form_valid(self, form):
    form.save()
    form.instance.url = self.request.build_absolute_uri(reverse('company_details', args=(form.instance.id, )))
    form.save()
    print(form.instance.url)
    return super().form_valid(form)
add_company = AddCompany.as_view()

class ListAdvocates(generics.ListAPIView):
  queryset = Advocate.objects.all()
  serializer_class = AdvocateSerializer
list_advocates = ListAdvocates.as_view()


class ListCompanies(generics.ListAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
list_companies = ListCompanies.as_view()


class DetailAdvocate(generics.RetrieveAPIView):
  queryset = Advocate.objects.all()
  serializer_class = AdvocateSerializer
  lookup_field = 'pk'
advocate_details = DetailAdvocate.as_view()


class DetailCompany(generics.RetrieveAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  lookup_field = 'pk'
company_details = DetailCompany.as_view()
