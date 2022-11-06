from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    # A versão mais simples de um ModelForm é constituída de uma classe Meta
    # aninhada que diz a Django em qual modelo o formulário deve se basear
    # e quais campos devem ser incluídos nesse formulário.
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}