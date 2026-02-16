from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
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
                        messages.error(request, "Please check your input.")
        else:
                form = ApplicationForm()
        
        # Case 2: Show list
        all_aps = Application.objects.all()

        applications = Application.objects.all()

        # Filter 1: by status
        status_filter = request.GET.get('status')
        if status_filter:
                applications = applications.filter(status=status_filter)

        # Filter 2: by country
        country_filter = request.GET.get('country')
        if country_filter and country_filter != 'ALL':
                applications = applications.filter(country=country_filter)

        # sort
        sort_by = request.GET.get('sort')
        if sort_by == 'oldest':
                applications = applications.order_by('date_applied')
        elif sort_by == 'country':
                applications = applications.order_by('country')
        elif sort_by == 'company':
                applications = applications.order_by('company__name')
        elif sort_by == 'status':
                applications = applications.order_by('status')
        else:
                applications = applications.order_by('-date_applied')

        # Get list of available countries for the filter dropdown
        unique_countries = Application.objects.values_list('country', flat=True).distinct()
        available_countries = sorted([c for c in unique_countries if c])
        
        stats = {
                'total': all_aps.count(),
                'saved': all_aps.filter(status='saved').count(),
                'applied': all_aps.filter(status='applied').count(),
                'interview': all_aps.filter(status='interview').count(),
                'rejected': all_aps.filter(status='rejected').count(),
                'offer': all_aps.filter(status='offer').count(),
                'accepted': all_aps.filter(status='accepted').count(),
        }

        context = {
                'form': form,
                'applications': applications,
                'stats': stats,
                'available_countries': available_countries,
                'current_status': status_filter,
                'current_country': country_filter,
                'current_sort': sort_by,
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
                query_string = request.GET.urlencode()
                base_url = reverse('company_list')

                if query_string:
                        return redirect(f"{base_url}?{query_string}")
        return redirect('company_list')

def edit_application(request, application_id):
        application = get_object_or_404(Application, id=application_id)

        if request.method == 'POST':
                form = ApplicationEditForm(request.POST, instance=application)
                
                if form.is_valid():
                        form.save()
                        messages.success(request, f"Application for {application.company.name} got updated!")
                        query_string = request.GET.urlencode()
                        base_url = reverse('company_list')

                        if query_string:
                                return redirect(f"{base_url}?{query_string}")
                return redirect('company_list')
        else:
                form = ApplicationEditForm(instance=application)
        
        return render(request, 'tracker/application_edit.html', {
                'form': form,
                'application': application
        })