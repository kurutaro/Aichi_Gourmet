from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Genre, Location, User, Store, Picture
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .forms import StoreForm, FileFormset



#最初に飛ぶページ 
def index(request):
    return render(request, 'index.html')

def post(request):
    return render(request, 'post.html')

def fin(request):
    return render(request, 'post_fin.html')

def delete(request):
    return render(request, 'post_delete.html')

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



#店の新規登録
@login_required
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



#店のアップデート
@login_required
def update_post(request, pk):
    post = get_object_or_404(Store, pk=pk)
    form = StoreForm(request.POST or None, instance=post)
    formset = FileFormset(request.POST or None, files=request.FILES or None, instance=post)
    if request.method == 'POST' and form.is_valid() and formset.is_valid():
        form.save()
        formset.save()
        # 編集ページを再度表示
        return redirect('stores:post_fin')

    context = {
        'form': form,
        'formset': formset
    }

    return render(request, 'post.html', context)


#店の削除
@login_required
def delete_post(request, pk):
    post = get_object_or_404(Store, pk=pk)
    post.delete()
    return redirect('stores:post_delete')