from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.utils import IntegrityError

from users.models import Profile
from users.forms import ProfileForm

# Create your views here.
@login_required
def update_profile(request):
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        # Performs validations
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
    else:
        print('get request')
        form = ProfileForm()

    return render(
        request=request, 
        template_name='users/update_profile.html', 
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )

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

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password does not match'})

        # Registering the new user into DB
        try:
            user = User.objects.create_user(username=username, password=password)    
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'The username already exists'})

        # Adding extra data to db new user registered
        user.first_name = request.POST['firstname']
        user.last_name = request.POST['lastname']
        user.email = request.POST['email']
        user.save() # Saves changes in DB

        # Registering its profile
        profile = Profile(user=user)
        profile.save() 
        
        return redirect('login')

    return render(request, 'users/signup.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')