from django.urls import path, include

from nprofile.views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name="HomePageView"),
]
