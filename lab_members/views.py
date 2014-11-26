from django.views.generic import DetailView, ListView
from lab_members.models import Scientist

class ScientistListView(ListView):
    model = Scientist
    queryset = Scientist.objects.all()

class ScientistDetailView(DetailView):
    model = Scientist
