from django.views.generic import ListView
from .models import Produto


class IndexListView(ListView):
    template_name = 'index.html'
    model = Produto
    paginate_by = 2  # Total de elementos por página
    ordering = 'id'  # Ordernar por
