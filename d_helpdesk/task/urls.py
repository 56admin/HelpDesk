from django.urls import path
from .models import Start_task

from .views import *


urlpatterns = {
    path('', index),
}
