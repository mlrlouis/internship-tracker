from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ApplicationForm
from .models import Company, Application
from .services.company_api import get_company_profile

# Create your views here.
def company_list(request):
        # Case 1: Adding new application
        if request.method == 'POST':
                form = ApplicationForm(request.POST)

                if form.is_valid():
                        # Get the clean data from the form
                        company_name = form.cleaned_data['company_name']
                        symbol = form.cleaned_data['company_symbol']

                        # Check if company already exists
                        company, created = Company.get_or_create(name=company_name)
                        
                        # If company is new and as a symbol exists -> get Yahoo data
                        if created and symbol:
                                api_data = get_company_profile(symbol)
                                if api_data:
                                        # Writing the Yahoo data into Company
                                        company.industry = api_data.get('industry')
                                        company.description = api_data.get('description')
                                        company.employee_count = api_data.get('employee_count')
                                        company.revenue = api_data.get('revenue')
                                        company.website = api_data.get('website')
                                        company.save()
                                        messages.info(request, f"Fetched data for {company_name} from Yahoo!")
                        elif created:
                                messages.info(request, f"Created manual entry for {company_name}")
                        
                        # saving the application
                        application = form.save(commit=False)
                        application.company = company
                        application.save()

                        messages.success(request, "Application added successfully!")
                        return redirect('company_list')
        else:
                form = ApplicationForm()
        
        # Case 2: Show list
        applications = Application.objects.all().order_by('-date_applied')

        context = {
                'form': form,
                'applications': applications
        }

        return render(request, 'tracker/company_list.html', context)