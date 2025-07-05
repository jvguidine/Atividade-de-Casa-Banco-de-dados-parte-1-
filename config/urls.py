from django.contrib import admin
from django.urls import path
from app.views import ServerInfoView, HelloWorldView, WelcomeView, PeopleView, PersonCreateView, PersonUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', HelloWorldView.as_view(), name='hello'),
    path('server-info/', ServerInfoView.as_view(), name='server_info'),
    path('welcome/', WelcomeView.as_view(), name='welcome'),
    path('people/', PeopleView.as_view(), name='person_list'),
    path('person/create/', PersonCreateView.as_view(), name='person_create'),
    path('person/<int:pk>/edit/', PersonUpdateView.as_view(), name='person_edit'),
]