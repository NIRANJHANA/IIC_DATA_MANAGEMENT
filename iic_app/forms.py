from django import forms
from .models import Event, EventProof
from django.core.exceptions import ValidationError

# Validator for file size
def validate_file_size(value):
    filesize = value.size
    if filesize > 2 * 1024 * 1024:  # Limit size to 2MB
        raise ValidationError("The maximum file size that can be uploaded is 2MB.")
    return value

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'event_type', 'theme', 'quarter', 'category', 'mode', 'objective', 'outcome', 'start_date', 'end_date', 'students', 'faculty', 'external_participants', 'duration', 'expenditure']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'objective': forms.Textarea(attrs={'rows': 2}),
            'outcome': forms.Textarea(attrs={'rows': 2}),
        }

    def clean_objective(self):
        objective = self.cleaned_data.get('objective')
        if len(objective) > 150:
            raise ValidationError("Objective must be within 150 characters.")
        return objective

    def clean_outcome(self):
        outcome = self.cleaned_data.get('outcome')
        if len(outcome) > 100:
            raise ValidationError("Outcome must be within 100 characters.")
        return outcome

class EventProofForm(forms.ModelForm):
    class Meta:
        model = EventProof
        fields = ['document_type', 'file_reference', 'url_reference']
        widgets = {
            'file_reference': forms.ClearableFileInput(attrs={'accept': 'application/pdf,image/*'}),
            'url_reference': forms.URLInput(attrs={'placeholder': 'Enter URL if applicable'}),
        }
    
    def clean_file_reference(self):
        file = self.cleaned_data.get('file_reference')
        if file:
            validate_file_size(file)
        return file

    def clean_url_reference(self):
        url = self.cleaned_data.get('url_reference')
        document_type = self.cleaned_data.get('document_type')
        if document_type != 'Promotional URL' and not url:
            raise ValidationError(f"{document_type} is required.")
        return url
