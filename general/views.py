from django.views.generic import TemplateView

from project.models import Technology
class HomeView(TemplateView):
    template_name = 'general/index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['technologies'] = Technology.objects.all()
        return context