from __future__ import unicode_literals
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
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


def edit_profile(request):
    current_user=request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')
    else:
        form = ProfileForm()
    return render(request,'edit_profile.html',{"form":form})
  
@login_required(login_url='/accounts/login/')
def business(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    business = Business.objects.filter(neibourhood=profile.neighbourhood)
    print(business)
    return render(request,'bs.html',{'business':business})
  
def new_biz(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            biz = form.save(commit = False)
            biz.user = current_user
            biz.neighbourhood = profile.neighbourhood
            biz.save()
        return redirect('business')
    else:
        form = BusinessForm()
        
    return render(request,'biz.html',{'form':form}) 


def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"business": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})