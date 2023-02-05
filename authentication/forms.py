from django import forms
from django.contrib.auth.models import User


class ForgotPassForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={"placeholder": "Enter email"}))

    def clean(self):
        # data from the form is fetched using super function
        super(ForgotPassForm, self).clean()

        # extract the username and text field from the data
        username = self.cleaned_data.get('email')
        if not User.objects.filter(username=username).values().exists():
            self.add_error('email', forms.ValidationError(
                f'{username} is not registered'))
        # return any errors if found
        return self.cleaned_data
