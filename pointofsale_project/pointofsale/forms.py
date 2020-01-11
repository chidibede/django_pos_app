from django import forms
from pointofsale.models import Category, Product

class AddCategoryForm(forms.ModelForm):
      
    class Meta:
        model = Category
        fields = '__all__'

class AddProductForm(forms.ModelForm):
      
    class Meta:
        model = Product
        fields = ['name',  'category', 'description', 'selling_price', 'image_field']

    
    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select Category'
        self.fields['image_field'].label = 'Images (Must Upload image)'


class UpdateProductForm(forms.ModelForm):
      
    class Meta:
        model = Product
        fields = ['name', 'category', 'description', 'selling_price']

    
    def __init__(self, *args, **kwargs):
        super(UpdateProductForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = 'Select Category'