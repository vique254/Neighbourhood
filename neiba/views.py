from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def home(request):
      try: 
        current_user = request.user
        profile = Profile.objects.get(user=current_user)
    except ObjectDoesNotExist:
        return redirect('edit')
    return render (request,'home.html')




def profile(request):
    current_user =request.user
    profile=Profile.objects.get(user=current_user)
    
    return render(request,'profile.html',{'profile':profile})