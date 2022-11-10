from django.core import validators
from django import forms
from .models import customerrole

class vendor_group_registration(forms.ModelForm):
    class Meta:
        model=customerrole
        # fields='__all__'
        fields = ("Group_Name","Group_Level","Status","Image")
        widgets = {
            "Group_Name":forms.TextInput(attrs={'class':'form-control'}),
            "Group_Level":forms.NumberInput(attrs={'class':'form-control'}),
            "Status":forms.Select(choices=(("Active",'Active'), ("Deactive",'Deactive')),attrs={'class':'form-control'}),
            "Image": forms.FileInput(attrs={'class':'form-control'})
        }

class vendor_group_update(forms.ModelForm):
    class Meta:
        model=customerrole
        fields = ["Group_Name","Group_Level","Status","Image"]
        widgets = {
            "Group_Name":forms.TextInput(attrs={'class':'form-control'}),
            "Group_Level":forms.NumberInput(attrs={'class':'form-control'}),
            "Status":forms.Select(choices=(("Active",'Active'), ("Deactive",'Deactive')),attrs={'class':'form-control'})
        }