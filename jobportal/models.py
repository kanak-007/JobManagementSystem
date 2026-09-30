from django.db import models
from django.contrib.auth.models import User


class Job(models.Model):

    title = models.CharField(max_length=200)

    company = models.CharField(max_length=200)

    location = models.CharField(max_length=100)

    description = models.TextField()

    salary = models.CharField(max_length=100, blank=True)

    job_type = models.CharField(max_length=50)

    skills = models.CharField(max_length=300)

    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Application(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )
    

    applicant_name = models.CharField(
        max_length=100
    )

    email = models.EmailField()

    phone = models.CharField(
        max_length=15
    )

    resume = models.FileField(
        upload_to='resumes/',
        blank=True,
        null=True
    )

    applied_date = models.DateTimeField(
        auto_now_add=True
    )
    status = models.CharField(
    max_length=30,
    choices=[
        ('Applied', 'Applied'),
        ('Under Review', 'Under Review'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    ],
    default='Applied'
)

    def __str__(self):
        return self.applicant_name + " - " + self.job.title
    
class SavedJob(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    saved_date = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('user', 'job')

    def __str__(self):
        return self.user.username + " - " + self.job.title