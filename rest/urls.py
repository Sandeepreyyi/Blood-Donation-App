from django.urls import path
from rest.views import *



urlpatterns = [
    path('user/', UserSerializerView.as_view(), name='userserilizer'),
]

# urlpatterns = [
#     path('user/', UserSerializerView.as_view, name='userserilizer'),
#     # Add other routes here
# ]
