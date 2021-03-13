from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.urls import reverse

class ProfileCompletionMiddleware:
    """ Profile completion middleware
        Ensures that every user has a biography and
        profile picture, redirecting to profile udpate
        template in order to add that information.
     """

    def __init__(self, get_response):
        """ Middleware initialization """
        self.get_response = get_response
    
    def __call__(self, request):
        """ Logic of middleware """
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('update_profile'),reverse('logout')]:
                        return redirect('update_profile')
        response = self.get_response(request)
        return response