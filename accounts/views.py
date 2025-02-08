from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login,logout

import requests
import json
User = get_user_model()


CODEFORCES_User_Info = "https://codeforces.com/api/user.info?handles={handle}"

CODEFORCCES_RATING_INFO = "https://codeforces.com/api/user.rating?handle={handle}"


def register(request):
    if (request.method == "POST"):
        username = request.POST.get('username')
        email = request.POST.get('email')
        codeforcesId = request.POST.get('CodeforcesID')
        leetcodeId = request.POST.get('LeetcodeID')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'accounts/register.html', {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/login.html', {"error": "Username already taken"})

        user = User.objects.create_user(username=username, password=password, CodeForcesID=codeforcesId, LeetCodeID=leetcodeId,email = email)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            return redirect('/')

        return redirect('/accounts/login')

    return render(request, 'accounts/register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            print("Invalid username or password")  # Debugging
            return render(request, 'accounts/login.html', {'error': 'Invalid username or password'})

    return render(request, 'accounts/login.html')



def Logout(request):
	logout(request)
	return redirect('/')






def profile(request):
	if(request.user == None):
		return redirect('accounts/register')

	handle = request.user.CodeForcesID
	url = CODEFORCES_User_Info.format(handle= handle)
	response = requests.get(url).json()
	user_info = response['result'][0]

	profile_url = user_info['titlePhoto']
	url = CODEFORCCES_RATING_INFO.format(handle=handle)
	response = requests.get(url).json()
	ratingHistory = {}
	for items in response['result']:
		key = f"{items['contestName']} Rank:-({items['rank']})"
		value = int(items['newRating'])
		ratingHistory[key] = value

	context = {"profile_url":profile_url,"Contest_rating":user_info['rating'],'RatingHistory':ratingHistory,'UserInfo':user_info}

	return render(request,'accounts/profile.html',context)




