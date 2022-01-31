from django.urls import path, include

from nprofile.views import HomePageView,FeedbackView

urlpatterns = [
    path('', HomePageView.as_view(), name="HomePageView"),
    path('FeedbackView/', FeedbackView.as_view(), name="FeedbackView"),
]
