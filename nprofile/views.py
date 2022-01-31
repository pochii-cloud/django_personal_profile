from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView, FormView

from nprofile.models import Feedback


class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')


class FeedbackView(View):
    def get(self, request):
        return render(request, 'index.html')

    def post(self, request):
        name = request.POST.get('Name')
        email = request.POST.get('Email')
        subject = request.POST.get('Subject')
        message = request.POST.get('Message')
        feedback = Feedback()
        feedback.name = name
        feedback.email = email
        feedback.subject = subject
        feedback.message = message
        feedback.save()
        return HttpResponse("message received thankyou!!We will contact you soon")
