from django.shortcuts import render
from .models import Project
from .forms import ContactForm
from django.core.mail import send_mail
# Create your views here.

def get_all_projects_list(request):
    projects = Project.objects.all()
    return render(request, 'content/projects_list.html', {
        'projects':projects
    })

def contact_view(request):
    if request.method == "POST":
        # send the message
        form = ContactForm(request.POST)

        if form.is_valid():
            print("Sending email")

            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"This is an email from your contact page\nName:{name}\nEmail:{email}\nMessage:{message}"

            send_mail(
                "Email from " + name,
                message,
                email,
                ['feroxtestemail@gmail.com']
            )
        else:
            print("Invalid data on the form")
    else:
        # display the page
        form = ContactForm()

    return render(request, "content/contact.html", {"form": form})
