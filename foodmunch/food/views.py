from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from food.models import Food
from .forms import FoodForm

# Create your views here.
def home(request):
    items=Food.objects.all()
    return render(request,'home.html',{'items':items})


def detail(request,id):
    item=Food.objects.get(id=id)
    return render(request,'detail.html',{'item':item})



def additem(request):
    form=FoodForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request,'additem.html',{'form':form})