from django import forms
from django.contrib import auth
from asker.models import *


class LoginForm(forms.Form):
    # username = forms.CharField(help_text="hello")
    username = forms.CharField(min_length=3)
    password = forms.CharField(widget=forms.PasswordInput)
    # password1 = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     pass_one = cdata.get('password1')
    #     pass_two = cdata.get('password2')
    #     if pass_one != pass_two:
    #         raise forms.ValidationError()

    def clean_username(self):
            username = self.cleaned_data.get('username')
            if username == 'bob':
                raise forms.ValidationError('no bobs hear!')

    def clean(self):
        cdata = super().clean()
        user = auth.authenticate(**cdata)
        if user is None:
            raise forms.ValidationError("no such user")

class AskForm(forms.ModelForm):

    class Meta:
        model = Question
        fields = ['title', 'text']

    def __init__(self, Profile, *args, **kwargs):
        self.profile = Profile
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        if self.cleaned_data:
            cdata = self.cleaned_data
            question = Question(**cdata)
            question.author = self.profile
            if commit:
                Question.save()
