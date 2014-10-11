import json

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def index(request):
	return HttpResponse("Hello web!")
