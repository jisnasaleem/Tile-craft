from django import forms
from django.forms import CharField
from tileapp.models import pmodel

# ----------------------------------------------user registration-------------------------------------------------------------------------------------------------------------------			 
class pform(forms.Form):
	iname = forms.CharField(max_length=20)
	p_image = forms.FileField()
	class Meta:
		model = pmodel
		fields = ['icode','iname','ccode','scode','bcode','desp','mrp','qty','p_image','size']
		
# ------------------------