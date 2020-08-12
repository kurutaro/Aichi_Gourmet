from django import forms
from .models import Genre, Location, User, Store, Picture

class PostForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ('store_name','genre', 'location', 'link', 'comment', 'user')
        labels = {
            'store_name': '店名',
            'genre': 'ジャンル',
            'location': 'エリア',
            'link': 'URL',
            # 'picture': '写真',
            'comment': 'コメント',
            'user': '登録者',
        }

        help_texts = {
            'store_name': '店名を入れてください',
            'genre': 'ジャンルを選択してください',
            'location': 'エリアを選択してください',
            'link': 'Instagram → 食べログの優先順位で載せてください',
            # 'picture': '写真を登録してください',
            'comment': '300字以内でコメントを記入してください',
            'user': '登録者を選択してください',
        }

class PostPictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('store','picture')
        labels = {
            'store': '店名',
            'picture': '写真',
        }

        help_texts = {
            'store': '店名を選択してください',
            'picture': '写真を登録してください',
        }