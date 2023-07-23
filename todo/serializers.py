from django import forms

from rest_framework import serializers
from .models import Task

class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('title', 'description', 'start_date', 'end_date')