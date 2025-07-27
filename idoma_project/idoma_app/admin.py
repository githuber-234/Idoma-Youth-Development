from django.contrib import admin
from .models import (Events, News, Member, Volunteer,
                    Partnership, Gallery, ForumTopic,
                    Project)


@admin.register(Events)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'status', 'image')

@admin.register(Gallery)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'uploaded_at')

@admin.register(News)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'link', 'date_posted')

@admin.register(ForumTopic)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'content', 'created_at')

@admin.register(Project)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'project_name', 'project_content', 'created_at')

@admin.register(Member)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'reason', 'joined_at')

@admin.register(Volunteer)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'skills', 'signed_up_at')

@admin.register(Partnership)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization', 'email', 'message', 'submitted_at')


