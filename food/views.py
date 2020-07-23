from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
from django.views.generic import ListView


#最初に飛ぶページ 
def index(request):
    return render(request, 'index.html')

# def about(request):
#     return render(request, 'about.html') 

def products(request):
    return render(request, 'products.html')

def store(request):
    return render(request, 'store.html') 


class ReviewListView(ListView):
    model = Review
    context_object_name = "Reviews"