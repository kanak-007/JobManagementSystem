from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from jobportal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('job/<int:job_id>/', views.job_details, name='job_details'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('job/<int:job_id>/save/', views.save_job, name='save_job'),
    path('saved-jobs/', views.saved_jobs, name='saved_jobs'),
    path('my-applications/', views.my_applications, name='my_applications'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path(
    'admin-dashboard/',
    views.admin_dashboard,
    name='admin_dashboard'
),
    path('admin-dashboard/add-job/', views.add_job, name='add_job'),
    path('admin-dashboard/manage-jobs/', views.manage_jobs, name='manage_jobs'),
    path(
    'admin-dashboard/edit-job/<int:job_id>/',
    views.edit_job,
    name='edit_job'
),
    path(
    'admin-dashboard/delete-job/<int:job_id>/',
    views.delete_job,
    name='delete_job'
),
    path(
        'job/<int:job_id>/remove-saved/',
        views.remove_saved_job,
        name='remove_saved_job'
    ),
    path(
        'application/<int:application_id>/',
        views.view_application,
        name='view_application'
    ),
    path(
    'application/<int:application_id>/update-status/',
    views.update_application_status,
    name='update_application_status'
),
    path(
    'admin-dashboard/application/<int:application_id>/',
    views.admin_view_application,
    name='admin_view_application'
),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)