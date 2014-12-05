from django.views.generic import DetailView, ListView
from lab_members.models import Scientist

class ScientistListView(ListView):
    model = Scientist

    def get_context_data(self, **kwargs):
        context = super(ScientistListView, self).get_context_data(**kwargs)
        context['current_list'] = Scientist.objects.filter(current=True)
        context['alumni_list'] = Scientist.objects.filter(current=False)
        return context

class ScientistDetailView(DetailView):
    model = Scientist
