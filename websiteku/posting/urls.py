from django.urls import path
from posting.views import *

urlpatterns = [
    path('',views.index),
    ]