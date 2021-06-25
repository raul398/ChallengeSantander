from django.shortcuts import render
from meeting.models import Meeting
import requests
import json


# Create your views here.


def home(request):
    url = 'http://127.0.0.1:8000/apis/meeting-list/'
    response = requests.request("GET", url)
    meetings = json.loads(response.text)
    return render(request, 'home/home.html', {'meetings': meetings})
