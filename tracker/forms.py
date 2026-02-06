from django import forms


class CompanyForm(forms.Form):
        symbol = forms.CharField(
                label="Ticker Symbol",
                max_length=50,
                help_text="e. g. AAPL for Apple or MSFT for Microsoft",
                widget=forms.TextInput(attrs={
                        'placeholder': 'AAPL',
                        'class': 'input-field',
                        'autofocus': 'autofocus'
                })
        )