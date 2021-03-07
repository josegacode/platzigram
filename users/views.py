from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # built-in method from django auth models
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            # The context (error key) will be passed to the template in order to show the message
            return render(request, "users/login.html", {'error': "Invalid username or password"})
    return render(request, "users/login.html")
