from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.EmailField(max_length=50, label="", required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(min_length=6, required=True, label="",
                               widget=forms.TextInput(attrs={'placeholder': 'Password'}))

    def clean(self):
        # data from the form is fetched using super function
        super(RegisterForm, self).clean()
        university_mail = '@mdu.ac.in'

        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        if university_mail not in username:
            self.add_error('username', forms.ValidationError(
                f'{username} must be university email {university_mail}.'))
        if User.objects.filter(username=username).values().exists():
            self.add_error('username', forms.ValidationError(
                f'{username} is already registered.'))
        # return any errors if found
        return self.cleaned_data
