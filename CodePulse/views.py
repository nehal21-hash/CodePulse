from django.http import HttpResponse


from django.shortcuts import render

def Home(request):
	context = {'user':request.user}

	return render(request,'CodePulse/index.html',context)


