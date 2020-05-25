from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserSignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError('User does not exits!')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password!')
            if not user.is_active:
                raise forms.ValidationError('Current user is not active!')
        return super(UserSignInForm, self).clean(*args, **kwargs)

class UserSignUpForm(forms.Form):
    email = forms.EmailField(label = 'Email address')
    confirmedEmail = forms.EmailField(label = 'Confirm email')
    password = forms.CharField(widget = forms.PasswordInput)

    class Meta:
        module = User
        fields = [
            'username',
            'email,'
            'confirmedEmail',
            'password'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        confirmedEmail = self.cleaned_data.get('confirmedEmail')
        password = self.cleaned_data.get('password')
        if email != confirmedEmail:
            raise forms.ValidationError('Email must match!')
        email_qs = User.objects.filter(email = email)
        if email_qs.exists():
            raise forms.ValidationError('This email is already being used!')
        return email


