from django.http import HttpResponse


from django.shortcuts import render

import requests

CODEFORCES_User_Info = "https://codeforces.com/api/user.info?handles={handle}"

def Home(request):
	context = {'user':request.user}
	profile_url = 'something.jpg'
	
	if request.user.is_authenticated:
		url = CODEFORCES_User_Info.format(handle=request.user.CodeForcesID)
		response = requests.get(url).json()
		response = response['result'][0]
		profile_url = response['titlePhoto']

	context['profile_url'] = profile_url
	return render(request,'CodePulse/index.html',context)


