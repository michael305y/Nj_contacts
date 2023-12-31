from django.forms import ModelForm, widgets
from . models import Contact, KCPE_collection_point, Kepsea_collection_point, Kcse_collection_point

from django import forms
from django.core import validators

# CONTACTS FORM 
# ==== method1 : creating native forms ========
class Contacts_Form(forms.ModelForm):
    # giving fields attributes
    # school_code = forms.CharField(widget=forms.NumberInput(attrs={
    #     'class': "",
    #     'type': "number",
    #     'placeholder': "Enter School Code",
    # }), label='')

    # school_name = forms.CharField(widget=forms.TextInput(attrs={
    #     'class': "",
    #     'type': "",
    #     'placeholder': "Enter School Name",
    # }), label=''
    # )

    # ============ data validation ========== #
    # def clean_school_code(self):
    #     school_code = self.cleaned_data['school_code']
    #     if not school_code.isdigit():
    #         raise forms.ValidationError("Only numeric values are allowed.")
    #     return school_code
        
    class Meta:
        model = Contact
        fields = "__all__" 
        


# # / ==== method2 : creating customizable form ======== /
# class Contacts_Form(ModelForm):
#     # def __init__(self, *args, **kwargs):
#     #     super().__init__(*args, **kwargs)
#     #     self.fields['school_name'].initial = ''
#     #     self.fields['school_code'].initial = '20409'

#     #     self.fields['school_name'].widget.attrs['placeholder'] = 'Enter name of the school'

#     class Meta:
#         model = Contact
#         fields = "__all__" 

# KCPE collection points FORM
class KCPE_collection_points_form(forms.ModelForm):
    class Meta:
        model = KCPE_collection_point
        fields = "__all__"

# KEPSEA collection points FORM
class KEPSEA_collection_points_form(forms.ModelForm):
    class Meta:
        model = Kepsea_collection_point
        fields = "__all__"

# KCSE collection points FORM
class KCSE_collection_points_form(forms.ModelForm):
    class Meta:
        model = Kcse_collection_point
        fields = "__all__"


