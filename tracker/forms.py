from django import forms
from models import Application

class ApplicationForm(forms.Form):
        company_name = forms.CharField(
                label="Company Name",
                max_length=200,
                widget=forms.TextInput(attrs={
                        'placeholder': 'e.g. Microsoft, Apple, BMW or local bakery',
                        'class': 'input-field',
                        'autofocus': 'autofocus'
                })
        )

        company_symbol = forms.CharField(
                label="Optional Ticker Symbol",
                required=False,
                help_text="Only needed if you want to fetch stock data (e.g. AAPL)",
                widget=forms.TextInput(attrs={
                        'placeholder': 'e.g. AAPL or MSFT',
                        'class': 'input-filed'
                })
        )

        class Meta:
                model = Application
                fields = ['role', 'status', 'job_link', 'notes']
                widgets = {
                        'role': forms.TextInput(attrs={
                                'placeholder': 'e.g. Software Engineer intern'
                        }),

                        'job_link': forms.URLInput(attrs={
                                'placeholder': 'https://...'
                        }),

                        'notes': forms.Textarea(attrs={
                                'rows': 5,
                                'placeholder': 'Notes: Salary, Interview feedback, etc.'
                        })
                }