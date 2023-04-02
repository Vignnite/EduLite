from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.starting_page, name="edusol-starting-page"),
    path('cutoff', views.form_cutoff, name="edusol-form-page"),
    path('Choices', views.choice_detail, name="choice-detail-page")
]