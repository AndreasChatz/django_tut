from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, worldS. You're at the polls index.")