from django import forms
from product.models import Brand

class UnknownForm(forms.Form):
    brands = forms.ModelMultipleChoiceField(
        queryset = Brand.objects.all(),
        widget  = forms.CheckboxSelectMultiple,
    )