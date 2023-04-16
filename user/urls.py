from django.urls import path,include
from .views import *

urlpatterns = [

    path("signup/",my_functional_view,name="signup"),
    path('confirm/<int:id>/',confirm_needed,name="confirm_needed"),
    path('logout/',Logout,name="logout"),
    path('settings/',settings,name= "settings")
]