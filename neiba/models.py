from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Neighbourhood(models.Model):
    name = models.CharField(max_length =255)
    location = models.CharField(max_length=255)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def save_neighbour(self):
        self.save()
        
    @classmethod
    def delete_neighbour(cls,neiba):
        cls.objects.filter(name=neiba).delete()
        
    @classmethod
    def update_neighbour(cls,neiba,new_neiba):
        cls.objects.filte(name=neiba).update(name=new_neiba)
        
    @classmethod
    def update_occupants(cls,neiba,new_occ):
        cls.objects.filter(name=neiba).update(occupants=new_occ)
        
    @classmethod 
    def find_neiba(cls,name):
        result = cls.objects.filter(name__icontains=name)
        return result

class Profile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic = models.ImageField(upload_to='profiles/')
    bio = models.CharField(max_length=255)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    profile_email = models.CharField(max_length=255)
    
    def __str__(self):
        return self.bio
    
    def save_profile(self):
        self.save()
        
    @classmethod
    def delete_profile(cls,username):
        cls.objects.filter(user=username).delete()
        
class Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    neibourhood = models.ForeignKey(Neighbourhood,on_delete=models.CASCADE)
    bizpic = models.ImageField(upload_to='bizpic/',default='img.jpg')
    biz_email = models.EmailField()
    
    def __str__(self):
        return self.name
    
    def save_biz(self):
        self.save()
    
    @classmethod
    def delete_biz(cls,name):
        cls.objects.filter(name=name).delete()
        
    @classmethod
    def update_biz(cls,biz,email):
        cls.objects.filter(name=biz).update(biz_email=email)
        
    @classmethod
    def find_biz(cls,term):
        result = cls.objects.filter(name__icontains=term)
        return result
    
    def search_by_name(cls,search_term):
        neiba = cls.objects.filter(name__icontains=search_term)
        return neiba
