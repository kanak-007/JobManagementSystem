from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Job, Application, SavedJob


def home(request):

    jobs = Job.objects.all().order_by('-posted_date')

    # Get search values from URL
    search_query = request.GET.get('search', '')
    location_query = request.GET.get('location', '')
    job_type_query = request.GET.get('job_type', '')


    # Search by job title
    if search_query:
        jobs = jobs.filter(
            title__icontains=search_query
        )


    # Search by location
    if location_query:
        jobs = jobs.filter(
            location__icontains=location_query
        )


    # Filter by job type
    if job_type_query:
        jobs = jobs.filter(
            job_type__iexact=job_type_query
        )


    return render(request, 'home.html', {

        'jobs': jobs,

        'search_query': search_query,

        'location_query': location_query,

        'job_type_query': job_type_query

    })


def job_details(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    return render(request, 'job_details.html', {
        'job': job
    })


def apply_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('login')

    job = Job.objects.get(id=job_id)

    if request.method == 'POST':

        # Prevent duplicate application
        existing_application = Application.objects.filter(
            user=request.user,
            job=job
        ).first()

        if existing_application:
            messages.warning(
                request,
                'You have already applied for this job.'
            )
            return redirect('my_applications')

        Application.objects.create(
            user=request.user,
            job=job,
            applicant_name=request.POST.get('applicant_name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            resume=request.FILES.get('resume')
        )

        return render(
            request,
            'application_success.html',
            {'job': job}
        )

    return render(
        request,
        'application_form.html',
        {'job': job}
    )

def my_applications(request):

    if not request.user.is_authenticated:
        return redirect('login')

    applications = Application.objects.filter(
        user=request.user
    ).select_related('job').order_by('-applied_date')

    return render(request, 'my_applications.html', {
        'applications': applications
    })
    
def dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    saved_jobs_count = SavedJob.objects.filter(
        user=request.user
    ).count()

    applications_count = Application.objects.filter(
        user=request.user
    ).count()

    total_jobs_count = Job.objects.count()

    return render(request, 'dashboard.html', {
        'saved_jobs_count': saved_jobs_count,
        'applications_count': applications_count,
        'total_jobs_count': total_jobs_count
    })
    
def view_application(request, application_id):
    if not request.user.is_authenticated:
        return redirect('login')

    application = Application.objects.filter(
        id=application_id,
        user=request.user
    ).select_related('job').first()

    if application is None:
        return redirect('my_applications')

    return render(request, 'application_details.html', {
        'application': application
    })

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(
            request,
            'Registration successful. Please login.'
        )

        return redirect('login')

    return render(request, 'register.html')


def user_login(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            return redirect('home')

        messages.error(
            request,
            'Invalid username or password.'
        )

        return redirect('login')

    return render(request, 'login.html')
def user_logout(request):
    logout(request)

    return redirect('home')
def save_job(request, job_id):

    if not request.user.is_authenticated:
        return redirect('login')

    job = Job.objects.get(id=job_id)

    SavedJob.objects.get_or_create(
        user=request.user,
        job=job
    )

    return redirect('job_details', job_id=job.id)
def saved_jobs(request):

    if not request.user.is_authenticated:
        return redirect('login')

    saved_jobs = SavedJob.objects.filter(
        user=request.user
    ).select_related('job').order_by('-saved_date')

    return render(request, 'saved_jobs.html', {
        'saved_jobs': saved_jobs
    })
def remove_saved_job(request, job_id):

    if not request.user.is_authenticated:
        return redirect('login')

    SavedJob.objects.filter(
        user=request.user,
        job_id=job_id
    ).delete()

    return redirect('saved_jobs')
def admin_dashboard(request):

    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('home')

    total_jobs = Job.objects.count()

    total_applications = Application.objects.count()

    applied_count = Application.objects.filter(
        status='Applied'
    ).count()

    under_review_count = Application.objects.filter(
        status='Under Review'
    ).count()

    shortlisted_count = Application.objects.filter(
        status='Shortlisted'
    ).count()

    selected_count = Application.objects.filter(
        status='Selected'
    ).count()

    rejected_count = Application.objects.filter(
        status='Rejected'
    ).count()
    
    recent_applications = Application.objects.select_related(
        'job',
        'user'
    ).order_by('-applied_date')[:10]

    return render(request, 'admin_dashboard.html', {
        'total_jobs': total_jobs,
        'total_applications': total_applications,
        'applied_count': applied_count,
        'under_review_count': under_review_count,
        'shortlisted_count': shortlisted_count,
        'selected_count': selected_count,
        'rejected_count': rejected_count,
        'recent_applications': recent_applications,
    })
    
def add_job(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('home')

    if request.method == 'POST':
        Job.objects.create(
            title=request.POST.get('title'),
            company=request.POST.get('company'),
            location=request.POST.get('location'),
            description=request.POST.get('description'),
            salary=request.POST.get('salary'),
            job_type=request.POST.get('job_type'),
            skills=request.POST.get('skills')
        )

        return redirect('admin_dashboard')

    return render(request, 'add_job.html')
def manage_jobs(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('home')

    jobs = Job.objects.all().order_by('-posted_date')

    return render(request, 'manage_jobs.html', {
        'jobs': jobs
    })
def edit_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('home')

    job = Job.objects.get(id=job_id)

    if request.method == 'POST':
        job.title = request.POST.get('title')
        job.company = request.POST.get('company')
        job.location = request.POST.get('location')
        job.description = request.POST.get('description')
        job.salary = request.POST.get('salary')
        job.job_type = request.POST.get('job_type')
        job.skills = request.POST.get('skills')

        job.save()

        return redirect('manage_jobs')

    return render(request, 'edit_job.html', {
        'job': job
    })
def delete_job(request, job_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('home')

    job = Job.objects.get(id=job_id)

    if request.method == 'POST':
        job.delete()
        return redirect('manage_jobs')

    return render(request, 'delete_job.html', {
        'job': job
    })
def update_application_status(request, application_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('home')

    application = Application.objects.get(id=application_id)

    if request.method == 'POST':
        new_status = request.POST.get('status')

        if new_status in [
            'Applied',
            'Under Review',
            'Shortlisted',
            'Rejected',
            'Selected'
        ]:
            application.status = new_status
            application.save()

        return redirect('admin_dashboard')

    return redirect('admin_dashboard')
def admin_view_application(request, application_id):
    if not request.user.is_authenticated:
        return redirect('login')

    if not request.user.is_staff:
        return redirect('home')

    application = Application.objects.filter(
        id=application_id
    ).select_related('job', 'user').first()

    if application is None:
        return redirect('admin_dashboard')

    return render(request, 'admin_application_details.html', {
        'application': application
    })