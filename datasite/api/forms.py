from django import forms

from .models import DatasetDirectory

class DatasetForm(forms.Form):
    dataSet = forms.ModelChoiceField(queryset=DatasetDirectory.objects.all().order_by('dataset_id'))
    