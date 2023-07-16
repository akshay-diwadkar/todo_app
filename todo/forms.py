# from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from django import forms
from .models import Task

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ('title', 'description', 'start_date', 'end_date')
        widgets = {
            "start_date": DateTimeInput(),
            "end_date": DateTimeInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")
        if end_date < start_date:
            raise forms.ValidationError("End date should be greater than start date.")