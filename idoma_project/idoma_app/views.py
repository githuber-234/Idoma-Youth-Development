from django.views.generic import TemplateView, FormView, ListView
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, VolunteerForm, MemberForm, PartnershipForm
from .models import News, Events, Gallery, ForumTopic, Project
from django.shortcuts import render, redirect

class HomeView(TemplateView):
    template_name = 'idoma_app/home.html'

class AboutView(TemplateView):
    template_name = 'idoma_app/about.html'

class CultureAndTraditionView(TemplateView):
    template_name = 'idoma_app/culture-and-tradition.html'

class CommunityView(TemplateView):
    template_name = 'idoma_app/community.html'

class ProjectsView(ListView):
    model = Project
    template_name = 'idoma_app/projects.html'
    context_object_name = 'projects'
    ordering = ['-created_at']

class NewsView(ListView):
    model = News
    template_name = 'idoma_app/news.html'
    context_object_name = 'news_list'
    ordering = ['-date_posted']

class EventsView(ListView):
    template_name = 'idoma_app/events.html'
    model = Events

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['upcoming_events'] = Events.objects.filter(status='upcoming').order_by('date')[:5]
        context['past_events'] = Events.objects.filter(status='past').order_by('-date')[:5]
        context['gallery_images'] = Gallery.objects.all().order_by('-uploaded_at')[:30]
        return context

class GetInvolvedView(FormView):
    template_name = 'idoma_app/get-involved.html'
    success_url = '/get-involved/'

    def get(self, request, *args, **kwargs):
        context = {
            'contact_form': ContactForm(),
            'member_form': MemberForm(),
            'volunteer_form': VolunteerForm(),
            'partnership_form': PartnershipForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        if 'contact_submit' in request.POST:
            form = ContactForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                subject = "Idoma Youth Development Initiative - Contact"
                full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"
                send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['idomadevelopmentinitiative@gmail.com'])
                return redirect(self.success_url)

        elif 'member_submit' in request.POST:
            form = MemberForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                reason = form.cleaned_data['reason']
                subject = "Idoma Youth Development Initiative - Member Application"
                full_message = f"From: {name} <{email}>\n\nReason:\n{reason}"
                send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['idomadevelopmentinitiative@gmail.com'])
                return redirect(self.success_url)

        elif 'volunteer_submit' in request.POST:
            form = VolunteerForm(request.POST)
            if form.is_valid():
                form.save()
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                skills = form.cleaned_data['skills']
                subject = "Idoma Youth Development Initiative - Volunteer"
                full_message = f"From: {name} <{email}>\n\nSkills:\n{skills}"
                send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['idomadevelopmentinitiative@gmail.com'])
                return redirect(self.success_url)
            
        elif 'partnership_submit' in request.POST:
            form = PartnershipForm(request.POST)
            if form.is_valid():
                form.save()
                organization = form.cleaned_data['organization']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']
                subject = "Idoma Youth Development Initiative - Partnership"
                full_message = f"From: {organization} <{email}>\n\nMessage:\n{message}"
                send_mail(subject, full_message, settings.DEFAULT_FROM_EMAIL, ['idomadevelopmentinitiative@gmail.com'])
                return redirect(self.success_url)

        context = {
            'contact_form': ContactForm(request.POST),
            'member_form': MemberForm(request.POST),
            'volunteer_form': VolunteerForm(request.POST),
            'partnership_form': PartnershipForm(request.POST),
        }
        return render(request, self.template_name, context)

class WomenYouthForumView(ListView):
    model = ForumTopic
    template_name = 'idoma_app/women_youth_forums.html'
    context_object_name = 'topics'
    ordering = ['-created_at'][:15]

    def post(self, request, *args, **kwargs):
        author = request.POST.get('author')
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            ForumTopic.objects.create(
                title=title,
                content=content,
                author=author
            )
        return redirect('women-youth-forum')
