from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login,logout

User = get_user_model()

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
	if(request.user != None):
		return reidrect('/')
	if(request.method == 'POST'):
		username = request.POST.get('username')
		password = request.POST.get('password')
		users = User.objects.filter(username= username,password = password)
		user = authenticate(users)
		
		if(user != None):
			login(request,user)
			return redirect('/')

		return render(request,'accounts/login.html')
		
	return render(request,'accounts/login.html')





def Logout(request):
	logout(request)
	return redirect('/')