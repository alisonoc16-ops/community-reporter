from django.urls import path
from . import views

urlpatterns = [
    # URL 1: The home screen (root URL /)
    path('', views.home_view, name='home'),
    
    # URL 2: The report submission form
    path('report/submit/', views.submit_report_view, name='submit_report'),
]