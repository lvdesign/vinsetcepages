from django.views.generic import TemplateView

from vins.models import Vin 


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs,)
        context['vins'] = Vin.objects.all()
        
        context['me'] = 'Hello'
        context['images'] = Vin.objects.all()
        return context


class AboutPageView(TemplateView):
    template_name = 'about.html'


class OfflinePageView(TemplateView):
    template_name = 'offline.html'
    