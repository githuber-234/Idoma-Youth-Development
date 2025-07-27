from django.urls import path
from .views import (HomeView, AboutView, CultureAndTraditionView, 
                    ProjectsView, NewsView, EventsView, 
                    GetInvolvedView, CommunityView, WomenYouthForumView)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('culture-and-tradition/', CultureAndTraditionView.as_view(), name='culture-and-tradition'),
    path('community/', CommunityView.as_view(), name='community'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('news/', NewsView.as_view(), name='news'),
    path('events/', EventsView.as_view(), name='events'),
    path('get-involved/', GetInvolvedView.as_view(), name='get-involved'),
    path('women-youth-forum/', WomenYouthForumView.as_view(), name='women-youth-forum'),
]