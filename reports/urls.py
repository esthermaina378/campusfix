from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report_issue, name='report'),
    path('reports/', views.view_reports, name='reports'),
]