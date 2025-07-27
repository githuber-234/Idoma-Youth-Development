from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    link = models.URLField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Events(models.Model):
    STATUS_CHOICES = [
        ('upcoming', 'Upcoming'),
        ('past', 'Past'),
        ('cancelled', 'Cancelled'),
    ]
    name = models.CharField(max_length=255)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='upcoming')
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    reason = models.TextField(blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Member: {self.name} - {self.email}"

class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    skills = models.TextField(blank=True)
    signed_up_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Volunteer: {self.name} - {self.email}"
    
class Partnership(models.Model):
    organization = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.organization} ({self.email})"    

class ForumTopic(models.Model):
    author = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Project(models.Model):
    project_name = models.CharField(max_length=100)
    project_content = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)