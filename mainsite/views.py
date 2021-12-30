from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import Contact, Projects
from .forms import ContactForm
from django.views.generic import CreateView
import environ
from templated_email import send_templated_mail
env = environ.Env()
environ.Env.read_env()

# Create your views here.

def Index(request):
    return render(request, 'mainwebsite/index.html')

class contact(CreateView):
    form_class=ContactForm
    template_name='mainwebsite/contact.html'
    success_url ='/thankyou'

    def form_valid(self, form):
        contactEmail=form.cleaned_data.get('email')
        contactSubject=form.cleaned_data.get('subject')
        contactName=form.cleaned_data.get('name')
        contactPhone=form.cleaned_data.get('contact')
        contactMessage=form.cleaned_data.get('message')
        send_templated_mail(
            template_name='thankyou',
            from_email='shubhamjadhav190@gmail.com',
            recipient_list=[contactEmail],
            context={
                'subject':"Thanks for having interest in my profile",
                'name':contactName
            })
        send_templated_mail(
            template_name='newinterest',
            from_email='<no-reply@portfolio.com>',
            recipient_list=['shubhamjadhav190@gmail.com'],
            context={
                'subject':contactSubject,
                'email':contactEmail,
                'phone':contactPhone,
                'name':contactName,
                'message':contactMessage,
            })
        return super().form_valid(form)

def project(request):   
    return render(request, 'mainwebsite/project.html')

def about(request):
    cerf=Projects.objects.all()
    return render(request, 'mainwebsite/about.html', {'cerf':cerf})

def thankyou(request):   
    return render(request, 'mainwebsite/thankyou.html')