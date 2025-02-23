from django.shortcuts import render, redirect
from django.contrib import messages
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
            number = form.cleaned_data['number']
            message = form.cleaned_data['message']

            full_message = f"This is an email from your contact page\nName: {name}\nEmail: {email}\nPhone: {number}\nMessage: {message}"

            send_mail(
                "Email from " + name,
                full_message,
                email,
                ['jeremy.gurule@feroxaero.com']
            )

             # Display a success message using Django's messages framework
            messages.success(request, "Thank you for your message! We will get back to you soon.")

            # Redirect to the same page to clear the form and prevent resubmission
            return redirect('contact')  # Ensure 'contact' matches your URL pattern name for the contact page
        else:
            print("Invalid data on the form")
    else:
        # display the page
        form = ContactForm()

    return render(request, "content/contact.html", {"form": form})
