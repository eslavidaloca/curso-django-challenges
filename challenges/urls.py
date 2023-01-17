from django.urls import path

from . import views

urlpatterns = [
    # path("january", views.january),
    # path("february", views.february),
    # path("march", views.march),
    path("", views.index, name="index"), # /challenges/ will trigger it
    path("<int:month>", views.monthly_challenge_by_number), #Dinamic path with an argument int type
    path("<str:month>", views.monthly_challenge, name="month-challenge"), #Dinamic path with an argument string type
]
