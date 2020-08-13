from django import forms
from .models import Genre, Location, User, Store, Picture

class StoreForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Store
        fields = ('store_name','genre', 'location', 'link', 'comment', 'user')
        
        labels = {
            'store_name': '店名',
            'genre': 'ジャンル',
            'location': 'エリア',
            'link': 'URL',
            'comment': 'コメント',
            'user': '登録者',
        }

        help_texts = {
            'store_name': '店名を入れてください',
            'genre': 'ジャンルを選択してください',
            'location': 'エリアを選択してください',
            'link': 'Instagram → 食べログの優先順位で載せてください',
            'comment': '300字以内でコメントを記入してください',
            'user': '登録者を選択してください',
        }



FileFormset = forms.inlineformset_factory(
    Store, Picture, fields='__all__',
    extra=10, max_num=10, can_delete=False
)
