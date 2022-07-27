from django import forms
from .models import mymodel
 

class myform(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = "__all__"