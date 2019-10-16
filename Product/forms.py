from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):
    name = forms.CharField(
        max_length = 20,
        required = True,
        widget = forms.TextInput(
            attrs = {'class': 'summernote'}
        )
    )
    class Meta:
        model = Category
        fields = [ 'name']

        def __str__(self):
            return self.name


class ProductForm(forms.ModelForm):
    name = forms.CharField(
        label='Product name',
        max_length = 20,
        required = True,
        widget = forms.TextInput(
            attrs = {'class': 'summernote'}
        )
    )
    code = forms.CharField(
        label='Product code',
        max_length = 20,
        required = True,
        )
    quantity = forms.IntegerField()
  
    
    class Meta:
        model = Product
        fields = [ 'name','code','price','quantity','category']

        def __str__(self):
            return self.name