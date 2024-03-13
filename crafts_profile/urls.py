from django.urls import path
from crafts_profile import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view()),
]