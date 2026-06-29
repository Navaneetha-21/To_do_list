from django import forms
from .models import To_do_model

class To_do_form(forms.ModelForm):
    class Meta:
        model = To_do_model
        fields ="__all__"
        widgets ={
            'Task':forms.TextInput(attrs={
                'placeholder':"Enter your Task Here..",
                "style":"width :300px; padding:10px "
            }),
        }


