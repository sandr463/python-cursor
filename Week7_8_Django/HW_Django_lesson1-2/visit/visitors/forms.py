from django import forms
from .models import Visitor
from ckeditor_uploader.fields import RichTextUploadingFormField


class NewVisitorForm(forms.ModelForm):
    some_info =RichTextUploadingFormField()
    class Meta:
        model = Visitor
        fields = ['age', 'some_info']
