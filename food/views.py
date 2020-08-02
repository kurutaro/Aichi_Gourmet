from django.shortcuts import render
from django.http import HttpResponse
from .models import Review
from django.views.generic import ListView


#最初に飛ぶページ 
def index(request):
    return render(request, 'index.html')


def post(request):
    return render(request, 'post.html')

def other(request):
    return render(request, 'other.html') 

def research(request):
    return render(request, 'research.html')

class ReviewListView(ListView):
    model = Review
    context_object_name = "Reviews"