from django.template.loader import get_template
# from rest_framework.decorators import api_view
from PIL import Image
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
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

from django.core.exceptions import ValidationError
from django.core.validators import validate_email

from django.utils.translation import override
import json
import os
from django.http import HttpResponse
from datetime import datetime as dt


def home(request):
    if request.method == 'POST':
        form = myform(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('send')
    else:
        form = myform()

    return render(request, 'index.html', {'form': form})


def multimail1(request):
    file = mymodel.objects.last()
    with open('media/'+str(file.file), 'r') as file:
        csvdata = list(map(lambda x: x[1], csv.reader(file)))[1:]
    messages = list()
    for item in csvdata:
        subject = "Welcome to Kratosolutions."
        from_email = settings.EMAIL_HOST_USER
        to = item
        content = {'email': to}
        content["image_url"] = request.build_absolute_uri(reverse("image_load"))
        print(content)
        html_content = get_template('mail_template.html')
        html_content = html_content.render(content)
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        messages.append(msg)
    connection = get_connection().send_messages(messages)
    return HttpResponseRedirect('thanks')


def greet(request):
    return HttpResponse('Mail Sent Successfully')


# class SendTemplateMailView(APIView):

#     def post(self, request, *args, **kwargs):
#         target_user_email = request.data.get('email')
#         mail_template = get_template("mail_template.html")
#         context_data_is = dict()
#         context_data_is["image_url"] = request.build_absolute_uri(
#             ("render_image"))
#         url_is = context_data_is["image_url"]
#         context_data_is['url_is'] = url_is
#         html_detail = mail_template.render(context_data_is)
#         subject, from_email, to = "Greetings !!",  'hariharan@kratosolutions.com',  [
#             'sk.hari0805@gmail.com']
#         msg = EmailMultiAlternatives(subject, html_detail, from_email, to)
#         msg.content_subtype = 'html'
#         msg.send()
#         return Response({"success": True})


# @api_view()
# def render_image(request):
#     if request.method == 'PUT':
#         image = Image.new('RGB', (20, 20))
#         response = HttpResponse(content_type="image/png",
#                         status=status.HTTP_200_OK)
#         user = UserModel.objects.get(id=1)
#         user.status = True
#         user.save()
#         image.save(response, "PNG")
#         return response


def image_load(request):
    print("\nImage Loaded\n")
    red = Image.new('RGB', (1, 1))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    return response