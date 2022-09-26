from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name: str='index.html'

class AboutPageView(TemplateView):
    template_name: str='about.html'