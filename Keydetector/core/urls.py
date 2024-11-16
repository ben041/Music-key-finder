from django.urls import path
from .views import *

app_name = 'audio_analyzer'

urlpatterns = [
    path('', AudioUploadView.as_view(), name='upload'),
    path('result/', ResultView.as_view(), name='result'),
    path('About/', about, name='about'),
]