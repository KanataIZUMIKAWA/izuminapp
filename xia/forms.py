from distutils.log import info
from django import forms

class PlayerForm(forms.Form) :
    name = forms.CharField(label="プレイヤー名")
    info = forms.CharField(label="　　　　説明", required=False, widget=forms.Textarea())

class MinisterForm(forms.Form) :
    name = forms.CharField(label="プレイヤー名")
    title = forms.CharField(label="　　　　身分")