from django import forms
from .models import Application
from datetime import datetime

class LeaveApplyForm(forms.ModelForm):

    class Meta:
        model = Application
        fields = ('type', 'reason', 'time_period',
                  'date_from', 'date_to', 'station_leave')

    # custom form fields attributes
    def __init__(self, *args, **kwargs):
        super(LeaveApplyForm, self).__init__(*args, **kwargs)
        self.fields['reason'].widget = forms.Textarea(
            attrs={'placeholder': 'Reason (optional)'})
        self.fields['reason'].required = False
        self.fields['time_period'].required = False
        self.fields['date_from'].widget = forms.DateInput(
            attrs={"min": datetime.today().date(), "type": 'Date'})
        self.fields['date_to'].widget = forms.DateInput(
            attrs={"min": datetime.today().date(), "type": 'Date'})
