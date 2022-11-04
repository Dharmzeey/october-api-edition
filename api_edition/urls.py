from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home"),
  path("advocates/", views.list_advocates, name="advocates"),
  path("advocates/<int:pk>/", views.advocate_details, name="advocate_details"),
  path("advocates/<str:username>/", views.fetch_advocate, name="fetch_advocate"),
  
  path("companies/", views.list_companies, name="companies"),
  path("companies/<int:pk>/", views.company_details, name="company_details"),
  
  path("add-advocate/", views.add_advocate, name="add_advocate"),
  path("add-company/", views.add_company, name="add_company"),
  
  
  # path("search-advocate/", views.search_advocate, name="search_advocate"),
  # path("search-company/", views.search_company, name="search_company"),
  
]