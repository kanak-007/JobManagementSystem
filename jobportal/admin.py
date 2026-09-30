from django.contrib import admin
from .models import Job, Application, SavedJob


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'company',
        'location',
        'job_type',
        'salary',
        'posted_date'
    )

    search_fields = (
        'title',
        'company',
        'location'
    )


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = (
        'applicant_name',
        'job',
        'email',
        'status',
        'applied_date'
    )

    list_filter = (
        'status',
        'applied_date'
    )

    search_fields = (
        'applicant_name',
        'email',
        'job__title'
    )


@admin.register(SavedJob)
class SavedJobAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'job',
        'saved_date'
    )

    search_fields = (
        'user__username',
        'job__title'
    )