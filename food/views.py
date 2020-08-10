from django.shortcuts import render
from django.http import HttpResponse
from .models import Genre, Location, User, Store, Comment, Picture
from django.views.generic import ListView
from django.db.models import Q


#最初に飛ぶページ 
def index(request):
    return render(request, 'index.html')


def post(request):
    return render(request, 'post.html')

def other(request):
    return render(request, 'other.html') 

# def research(request):
#     return render(request, 'research.html')


#テーブルの検索
class StoreListView(ListView):
 
    def get_queryset(self):
        q_word1 = self.request.GET.get('area')
        q_word2 = self.request.GET.get('genre')

        if q_word1 and q_word2:
            print("けけけけけ")
            print(Store.store_name)
            print("こここここ")
            object_list = Store.objects.filter(Q(location__locate__exact=q_word1), Q(genre__genre__exact=q_word2))
            print("あああああ")
        else:
            object_list = Store.objects.all()
        return object_list