from django import forms
from utils.choices import FieldChoices
from django.contrib.auth.models import User


class RegisterForm(forms.Form):
    title = forms.ChoiceField(choices=FieldChoices.titleChoices, label="")
    name = forms.CharField(max_length=20, label="", required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    username = forms.EmailField(max_length=50, label="", required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(min_length=6, required=True, label="",
                               widget=forms.TextInput(attrs={'placeholder': 'Password'}))
    phone = forms.CharField(max_length=10, min_length=10, label="",
                            widget=forms.TextInput(attrs={'placeholder': 'Mobile no.'}))
    gender = forms.ChoiceField(
        choices=FieldChoices.genderChoices, label="", required=True)
    branch = forms.ChoiceField(
        choices=FieldChoices.branchChoices, label="", required=True)
    designation = forms.ChoiceField(
        choices=FieldChoices.designationChoices, label="", required=True)

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
