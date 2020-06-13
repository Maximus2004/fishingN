from django.urls import path, include
from . import views
from django.contrib.auth import views as v
from fish.views import *

urlpatterns = (
    path('', main_list, name='main_list'),
    path('auth/vk/', squads_reg, name='squads_reg'),
    path('success', success, name='success'),
)
