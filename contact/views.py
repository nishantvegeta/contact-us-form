from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import ContactForm
from django.template.loader import render_to_string
# Create your views here.


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)


        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('contact/emails/contactform.html', {
                'name': name,
                'email' : email,
                'content': content
            })

            send_mail('contact form', content, email, ['nishantkumpakha03@gamil.com'], html_message=html)

            return redirect('index')
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form' : form})