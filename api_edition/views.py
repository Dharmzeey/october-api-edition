from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
from django.contrib import messages
from django.db.models import Q
from rest_framework.views import APIView
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

# THIS NEXT TWO CLASSES ARE FOR FRONTEND PURPOSE
class AddAdvocate(LoginRequiredMixin, CreateView):
  model = Advocate
  template_name = 'api_edition/add_advocate.html'
  fields = ["name", "profile_pic", "short_bio", "long_bio","advocate_years_exp", "company", "youtube", "twitter", "github", "linkedin", "website"]
  success_url = 'add-advocate'
add_advocate = AddAdvocate.as_view()

class AddCompany(LoginRequiredMixin, CreateView):
  model = Company
  template_name = 'api_edition/add_advocate.html'
  fields = ["name", "logo", "summary", "advocates", "youtube", "twitter", "github", "linkedin", "website"]
  success_url = 'add-company'
add_company = AddCompany.as_view()


class ListAdvocates(generics.ListAPIView):
  queryset = Advocate.objects.all()
  serializer_class = AdvocateSerializer

  def list(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    q = request.GET.get("q")
    if q is not None:
      queryset = Advocate.objects.filter(Q(name__icontains=q))
    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = self.get_serializer(page, many=True)
      return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)
list_advocates = ListAdvocates.as_view()


class ListCompanies(generics.ListAPIView):
  queryset = Company.objects.all()
  serializer_class = CompanySerializer
  
  def list(self, request, *args, **kwargs):
    queryset = self.filter_queryset(self.get_queryset())
    q = request.GET.get("q")
    print(q)
    if q is not None:
      queryset = Company.objects.filter(Q(name__icontains=q))
    page = self.paginate_queryset(queryset)
    if page is not None:
      serializer = self.get_serializer(page, many=True)
      return self.get_paginated_response(serializer.data)

    serializer = self.get_serializer(queryset, many=True)
    return Response(serializer.data)
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


# class SearchAdvocate(APIView):
#   def get(self, request):
#     q = request.GET.get("q")
#     if q is not None:
#       result = Advocate.objects.filter(Q(name__icontains = q))
#     else:
#       result = Advocate.objects.all()
#     serialized = AdvocateSerializer(result, many=True)
#     return Response({"Search Result": serialized.data})
# search_advocate = SearchAdvocate.as_view()
  
# class SearchCompany(APIView):
#   def get(self, request):
#     q = request.GET.get("q")
#     if q is not None:
#       result = Company.objects.filter(Q(name__icontains = q))
#       serialized = CompanySerializer(result, many=True)
#     return Response({"Search Result": serialized.data})
# search_company = SearchCompany.as_view()