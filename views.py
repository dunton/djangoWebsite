from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import ContactForm
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context
from django.contrib import messages


# Create your views here.

def index(request):
    #return render(request, 'index.html')
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name',
                '' )
            contact_email = request.POST.get(
                'contact_email',
                '' )
            form_content = request.POST.get('content', '')

            template = get_template('contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
                })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Ryan's Webpage" + '',
                ['ryandunton1@gmail.com'],
                headers = {'Reply-To': contact_email}
            )
            email.send()
            return redirect('index')


    return render(request, 'index.html', {
        'form': form_class,
        })

def contact(request):
    #return render(request, 'index.html')
    return render(request, 'contact.html')
    
def resume(request):
    return render(request, 'resume.html')

def blog(request):
    return render(request, 'blog.html')

def pictures(request):
    return render(request, 'pictures.html')
