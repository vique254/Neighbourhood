from __future__ import unicode_literals
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from .forms import *
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login')
def home(request):
            form = BusinessForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['your_name']
                email = form.cleaned_data['email']

                recipient = NewsLetterRecipients(name = name,email =email)
                recipient.save()
                send_welcome_email(name,email)

            HttpResponseRedirect('/')
    
            
            return render (request,'home.html',{"letterForm":form})




def profile(request):
    current_user =request.user
    profile=Profile.objects.get(user_id =current_user.id)
    
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
    profile = Profile.objects.get(user_id = current_user.id)
    business = Business.objects.all()
    print(business)
    return render(request,'bs.html',{'business':business})
  
def new_biz(request):
    current_user = request.user
    if request.method == 'POST':
        form = BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            biz = form.save(commit = False)
            biz.user = current_user
            biz.save()
        return redirect('business')
    else:
        form = BusinessForm()
        
    return render(request,'new_bs.html',{'form':form}) 


def search_results(request):

    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_businesses = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"business": searched_businesses})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})