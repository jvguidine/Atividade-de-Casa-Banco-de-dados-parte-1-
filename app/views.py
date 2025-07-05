import platform
import socket
from datetime import datetime
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from app.models import Person
from django.shortcuts import render, redirect
from .forms import PersonForm
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy

# View 1 - Hello World (FBV)
def hello_view(request):
    response = { "message": "Hello, World!" }
    return JsonResponse(response)

# View 1 - Hello World (CBV)
class BaseHelloView(View):
    base_message = "Hello, World from CBV!"

    def get(self, request):
        return JsonResponse({
            'message': f'{self.base_message} - {datetime.now()}!'
        })

class HelloWorldView(BaseHelloView):
    base_message = "Hello, World!"

class ServerInfoView(View):
    def get(self, request):
        hostname = socket.gethostname()
        python_version = platform.python_version()
        return JsonResponse({
            'python_version': python_version,
            'hostname': hostname
        })

class WelcomeView(TemplateView):
    template_name = "app/welcome.html" 

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context['name'] = self.request.GET.get('name', 'Visitante')
        return context

class PeopleView(View):
    def get(self, request):
        gender = request.GET.get('gender')
        people = Person.objects.all()
        if gender:
            people = people.filter(gender=gender)
        data = [{'name': p.name, 'age': p.age, 'gender': p.gender} for p in people]
        return JsonResponse({'people': data})

class PersonCreateView(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'app/person_form.html'
    success_url = reverse_lazy('person_list')

class PersonUpdateView(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'app/person_form.html'
    success_url = reverse_lazy('person_list')
