from django.urls import path
from crafts_contact import views

urlpatterns = [
    path('contact/', views.Contact.as_view()),
]