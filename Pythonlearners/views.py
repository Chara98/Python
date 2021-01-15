from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
import json


users = []
auth = 0

class User:
	def __init__(self,avatar,name):
		self.name = name or 'NaN'
		self.avatar = avatar or ''

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def join(request):
    return render(request,'join.html')

def peo(request):
    print(users)
    return render(request, 'peo.html', {'users':[User(*list(i.values())) for i in users]})

def api_upload_users(request):
	if request.method != 'POST':
		return JsonResponse({'status':405})

	if request.headers.get('Authorization') is None:
		return JsonResponse({'status':401})

	elif request.headers['Authorization'] != str(auth):
		return JsonResponse({'status':403})

	try:
		global users
		users = json.loads(request.body)['users']
	except Exception as e:
		return JsonResponse({'status':500,'message':str(e)})

	return JsonResponse({'status':200})