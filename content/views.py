from django.shortcuts import render
from .models import Project
from .forms import ContactForm
# Create your views here.

def get_all_projects_list(request):
    projects = Project.objects.all()
    return render(request, 'content/projects_list.html', {
        'projects':projects
    })

def contact_view(request):
    form = ContactForm()
    return render(request, "content/contact.html", {"form": form})
