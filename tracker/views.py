from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CompanyForm
from .models import Company
from .services.company_api import save_company_to_db

# Create your views here.
def company_list(request):
        # Case 1: User clicked 'Add Company'
        if request.method == 'POST':
                form = CompanyForm(request.POST)

                if form.is_valid():
                        # Get the clean data from the form
                        symbol = form.cleaned_data['symbol']

                        # Call the service to fetch data from Yahoo and save to DB
                        new_company = save_company_to_db(symbol)

                        # Give feedback to the user
                        if new_company:
                                messages.success(request, f"{new_company.name} successfully added!")
                        else:
                                messages.error(request, f"Could not find data for {symbol}.")
                        
                        # Reloading the page to clear the form
                        return redirect('company_list')
        # Case 2: User just opened the page
        else:
                form = CompanyForm()
        
        # Always fetch all the companies to show them in the list
        companies = Company.objects.all().order_by('-id')

        context = {
                'form': form,
                'companies': companies
        }

        return render(request, 'tracker/company_list.html', context)