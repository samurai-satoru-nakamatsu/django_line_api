from django.views.generic import TemplateView

from webhook.models import WebhookEventObject


class HomeView(TemplateView):
    template_name = 'dashboard/home/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['webhook_event_objects'] = WebhookEventObject.objects.all()
        return context
