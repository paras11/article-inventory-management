from django import forms
from django.contrib.auth import(
authenticate,
get_user_model,
)
from .models import ProductPost
class PostForm(forms.ModelForm):
    class Meta:
        model = ProductPost
        fields = ('product_id','product_image','product_name','product_type','product_price','product_quanty',)



