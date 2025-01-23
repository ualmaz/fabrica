from django import forms
from .models import Client

class ContactForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['firstname', 'lastname', 'email', 'phone', 'message']
    
    # Define custom widgets for the form fields
    firstname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'First Name'}))
    lastname = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'Email Address'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Phone Number'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-textarea', 'placeholder': 'Your Message'}))

def clean_email(self):
        """ Allow multiple submissions with the same email. """
        return self.cleaned_data.get('email')