from django import forms
from django.contrib import auth
from asker.models import *

from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# class Question(forms.Form):
#     title = forms.CharField(max_length=50, min_length=10)
#     text = forms.Textarea()
#     tags = forms.TypedMultipleChoiceField(

#     def clean_title(self):
#         good_title = self.cleaned_data['title']
#         return good_title

#     def save(self):
#         new_question = Question.objects.create(
#             title = self.cleaned_data['title'],
#             text = self.cleaned_data['text'],
#             tags = self.cleaned_data['tags']
#         )
#         return new_question


textValidator = RegexValidator(r"[а-яА-Яa-zA-Z]",
                               "Text should contain letters")
tagsValidator = RegexValidator(r"[а-яА-Яa-zA-Z]",
                               "Tags should contain letters")
passwordValidator = RegexValidator(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$",
                                   "Password should contain minimum 8 characters, at least 1 letter and 1 number")


class UserSignUpForm(forms.ModelForm):
    first_name = forms.CharField(validators=[textValidator],
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'minlength': 2,
                                                               'maxlength': 30,
                                                               'placeholder': 'First name'}))
    last_name = forms.CharField(validators=[textValidator],
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'minlength': 2,
                                                              'maxlength': 30,
                                                              'placeholder': 'Last name'}))
    username = forms.CharField(validators=[textValidator],
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'minlength': 5,
                                                             'maxlength': 30,
                                                             'placeholder': 'Username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-mail'}))
    password = forms.CharField(validators=[passwordValidator],
                               widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password'}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                              'placeholder': 'Password confirmation'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)


class UserSignInForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'maxlength': 30,
                                                             'placeholder': 'Username'}))

    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password',)


class UserSettingsForm(forms.ModelForm):
    first_name = forms.CharField(required=False,
                                 validators=[textValidator],
                                 widget=forms.TextInput(attrs={'class': 'form-control',
                                                               'minlength': 2,
                                                               'maxlength': 30,
                                                               'placeholder': 'First name'}))
    last_name = forms.CharField(required=False,
                                validators=[textValidator],
                                widget=forms.TextInput(attrs={'class': 'form-control',
                                                              'minlength': 2,
                                                              'maxlength': 30,
                                                              'placeholder': 'Last name'}))

    username = forms.CharField(validators=[textValidator],
                               required=False,
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'minlength': 5,
                                                             'maxlength': 30,
                                                             'placeholder': 'Username'}))

    email = forms.EmailField(required=False,
                             widget=forms.EmailInput(attrs={'class': 'form-control',
                                                            'placeholder': 'E-mail'}))

    upload = forms.ImageField(required=False,
                              widget=forms.FileInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email',)


class NewQuestionForm(forms.ModelForm):
    title = forms.CharField(validators=[textValidator],
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'maxlength': 100,
                                                          'minlength': 10,
                                                          'placeholder': 'Write here your title'}))

    text = forms.CharField(validators=[textValidator],
                           widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'minlength': 30,
                                                        'placeholder': 'And here tell about your question in more detail'}))

    tags = forms.CharField(validators=[tagsValidator],
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'List here tags by separating them with a '
                                                                        'space (the first 10 will be saved)'}))

    class Meta:
        model = Question
        fields = ('title', 'text', 'tags',)


class WriteAnswerForm(forms.ModelForm):
    text = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                        'minlength': 20,
                                                        'placeholder': 'Enter your reply text'}))

    class Meta:
        model = Answer
        fields = ('text',)


# class LoginForm(forms.Form):
    # username = forms.CharField(help_text="hello")
    # username = forms.CharField(min_length=3)
    # password = forms.CharField(widget=forms.PasswordInput)
    # password1 = forms.CharField(widget=forms.PasswordInput)
    # password2 = forms.CharField(widget=forms.PasswordInput)

    # def clean(self):
    #     cleaned_data = super().clean()
    #     pass_one = cdata.get('password1')
    #     pass_two = cdata.get('password2')
    #     if pass_one != pass_two:
    #         raise forms.ValidationError()

    # def clean_username(self):
    #         username = self.cleaned_data.get('username')
    #         if username == 'bob':
    #             raise forms.ValidationError('no bobs hear!')

    # def clean(self):
    #     cdata = super().clean()
    #     user = auth.authenticate(**cdata)
    #     if user is None:
    #         raise forms.ValidationError("no such user")

# class AskForm(forms.ModelForm):

#     class Meta:
#         model = Question
#         fields = ['title', 'text']

#     def __init__(self, Profile, *args, **kwargs):
#         self.profile = Profile
#         super().__init__(*args, **kwargs)

#     def save(self, commit=True):
#         if self.cleaned_data:
#             cdata = self.cleaned_data
#             question = Question(**cdata)
#             question.author = self.profile
#             if commit:
#                 Question.save()
