from django.db import models
from django.utils import timezone

# Create your models here.
class Company(models.Model):
        #Base-Info
        name = models.CharField(max_length=200)
        website = models.URLField(blank=True, null=True)

        #API-Data
        industry = models.CharField(max_length=200, blank=True, null=True)
        description = models.TextField(blank=True, null=True)
        employee_count = models.CharField(max_length=100, blank=True, null=True)
        revenue = models.CharField(max_length=100, blank=True, null=True)
        country = models.CharField(max_length=100, blank=True, null=True)
        logo_url= models.URLField(blank=True, null=True)

        def __str__(self):
                return self.name

class Application(models.Model):
        #Status Choices for the dropdown menu
        STATUS_CHOICES = [
                ('saved', 'Saved'),
                ('applied', 'Applied'),
                ('interview', 'Interview'),
                ('rejected', 'Rejected'),
                ('offer', 'Offer'),
                ('accepted', 'Accepted'),
        ]

        company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='applications')
        role = models.CharField(max_length=200)

        country = models.CharField(max_length=100)

        status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='saved')
        job_link = models.URLField(blank=True, null=True)
        date_applied = models.DateField(default=timezone.now)
        notes = models.TextField(blank=True, null=True)

        def __str__(self):
                return f"{self.role} at {self.company.name}"