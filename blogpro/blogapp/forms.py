from django import forms
from .models import Comment,Contactus


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('name','email','body')


class ContactusForm(forms.ModelForm):
    class Meta:
        model=Contactus
        fields=('Name','Email','Mobile','Feedback')

