from django.template.loader import get_template
from PIL import Image
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.core.mail import BadHeaderError, get_connection
from django.http import HttpResponse, HttpResponseRedirect
import csv
from django.urls import reverse
from greetapp.forms import myform
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import os
from sendgrid import SendGridAPIClient
from django.conf import settings
from sendgrid.helpers.mail import Content, Email, Mail, To


def home(request):
    if request.method == 'POST':
        form = myform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('send')
    else:
        form = myform()

    return render(request, 'index.html', {'form': form})

def multimail2(request):
    file = mymodel.objects.last()
    with open('media/'+str(file.file), 'r') as file:
        csvdata = list(map(lambda x: x[1], csv.reader(file)))[1:]
    for item in csvdata:
        subject = "Welcome to Kratosolutions."
        from_email = Email('hariharan@kratosolutions.com')
        item = item
        to_email = To(item)
        content = {'email': to_email}
        content["image_url"] = request.build_absolute_uri("Opened")
        html_content = get_template('mail_template.html')
        html_content = html_content.render(content)
        text_content = strip_tags(html_content)
        msg = Mail(from_email, to_email, subject, text_content)
        msg.add_content(html_content, "text/html")
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY).send(msg)
    return HttpResponseRedirect('thanks')


def Opened(request):
    red = Image.new('RGB', (1, 1))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    return response

def greet(request):
    return HttpResponse('Mail Sent Successfully')

# import logging

# logging.basicConfig(filename='logs.txt',
#             filemode='w',
#             level=logging.INFO)
