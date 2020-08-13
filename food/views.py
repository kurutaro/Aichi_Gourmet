from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Genre, Location, User, Store, Picture
from django.views.generic import ListView, DetailView
from django.db.models import Q

from .forms import StoreForm, FileFormset
from extra_views import InlineFormSetFactory, CreateWithInlinesView, UpdateWithInlinesView



#最初に飛ぶページ 
def index(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

def fin(request):
    return render(request, 'post_fin.html')

def other(request):
    return render(request, 'other.html') 



#テーブルの検索
class StoreListView(ListView):
 
    def get_queryset(self):
        q_word1 = self.request.GET.get('area')
        q_word2 = self.request.GET.get('genre')

        if q_word1 and q_word2:
            object_list = Store.objects.filter(Q(location__locate__exact=q_word1), Q(genre__genre__exact=q_word2))
        else:
            object_list = Store.objects.all()
        return object_list


class StoreDetailView(DetailView):
    model = Store
    context_object_name = 'store'



def formfunc(request):
    form = StoreForm(request.POST or None)
    context = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        formset = FileFormset(request.POST, files=request.FILES, instance=post)  # 今回はファイルなのでrequest.FILESが必要
        if formset.is_valid():
            post.save()
            formset.save()
            return redirect('stores:post_fin')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            context['formset'] = formset

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        context['formset'] = FileFormset()

    return render(request, 'post.html', context)



# フォームからデータベースへの登録
# def formfunc(request):
#     if request.method == 'POST':
#         form = StoreForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.save()
#             return redirect('stores:post_fin')
#     else:
#         form = StoreForm()
#     return render(request, 'post.html', {'form': form})








# class PictureInline(InlineFormSetFactory):
#     model = Picture
#     fields = '__all__'


# class StoreCreateView(CreateWithInlinesView):
#     model = Store
#     fields = ['store_name','genre', 'location', 'link', 'comment', 'user']
#     context_object_name = 'store'
#     inlines = [PictureInline]
#     template_name = 'post.html'
#     success_url = reverse_lazy('stores:post_fin')


