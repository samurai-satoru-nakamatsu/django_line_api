from django.views.generic import TemplateView

from dashboard.models import Message


class HomeView(TemplateView):
    template_name = 'dashboard/home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = Message.objects.all()
        return context
