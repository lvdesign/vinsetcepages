from django.urls import path
from .views import HomePageView, AboutPageView, OfflinePageView

#app_name='pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('offline/', OfflinePageView.as_view(), name='offline'),

]