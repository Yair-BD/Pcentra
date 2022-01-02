from django.urls import path
from .views import *

urlpatterns = [
    path('', create_short_url, name="create-page"),
    path('<str:url>', redirect_to_original_url, name="redirect")   
]
