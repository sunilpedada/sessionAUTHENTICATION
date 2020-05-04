from django import forms
class items(forms.Form):
    name=forms.CharField(max_length=100)
    quantity=forms.IntegerField()