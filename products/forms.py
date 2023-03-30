from django import forms


class ProductCreateForm(forms.Form):
    image = forms.FileField(required=False)
    title = forms.CharField(max_length=255, min_length=6)
    description = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField(required=False)

class ReviewCreateForm(forms.Form):
    text = forms.CharField(max_length=255, min_length=3)
