from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Send an email after form is saved
            mailsend(form)

    else:
        form = ContactForm()

    return render(request, 'engineers/index.html', {'form': form})


def mailsend(form):
    # Extract cleaned data from the form
    name = form.cleaned_data['name']
    email = form.cleaned_data['email']
    comment = form.cleaned_data['comment']

    send_mail(
        subject='Thank you for contacting me!',
        message=f'Hi {name},\n\nThank you for your message:\n"{comment}"\nWe will get back to you soon.',
        from_email='shantanumahin@gmail.com',  # Replace with your actual email
        recipient_list=[email],
        fail_silently=False,
    )
    
# def send_mail_view(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # Call mailsend function
#             mailsend(form)
#             return HttpResponse('Thank you for your message.')
#     else:
#         form = ContactForm()

#     return render(request, 'engineers/index.html', {'form': form})