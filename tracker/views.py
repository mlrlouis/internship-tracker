from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ApplicationForm, ApplicationEditForm
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
                        company, created = Company.objects.get_or_create(name=company_name)
                        
                        # If company is new and a symbol exists -> get Yahoo data
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

        stats = {
                'total': applications.count(),
                'saved': applications.filter(status='saved').count(),
                'applied': applications.filter(status='applied').count(),
                'interview': applications.filter(status='interview').count(),
                'offer': applications.filter(status='offer').count(),
                'rejected': applications.filter(status='rejected').count(),
        }

        context = {
                'form': form,
                'applications': applications,
                'stats': stats
        }

        return render(request, 'tracker/company_list.html', context)

def delete_application(request, application_id):
        # Get the application or show 404 error if not found
        application = get_object_or_404(Application, id=application_id)

        # Delete it only if the request is a POST
        if request.method == 'POST':
                company_name = application.company.name
                application.delete()
                messages.success(request, f"Application for {company_name} deleted successfully!")
        
        return redirect('company_list')

def edit_application(request, application_id):
        application = get_object_or_404(Application, id=application_id)

        if request.method == 'POST':
                form = ApplicationEditForm(request.POST, instance=application)
                
                if form.is_valid():
                        form.save()
                        messages.success(request, f"Application for {application.company.name} got updated!")
                        return redirect('company_list')
        else:
                form = ApplicationEditForm(instance=application)
        
        return render(request, 'tracker/application_edit.html', {
                'form': form,
                'application': application
        })