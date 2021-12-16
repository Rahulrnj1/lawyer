from django.urls import path
from django.urls.resolvers import URLPattern
from lawyerapp2 import views

URLPattern=[
    path('departments',views.lawyerapi2),
    path('department/([0-9]+$',views.lawyerapi2),
    
]