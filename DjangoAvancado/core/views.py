from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .models import Servico, Funcionario
from .forms import ContatoForm
from django.contrib import messages

# Traduções
# from django.utils.translation import ugettext
# from django.utils import translation


class IndexView(FormView):
    template_name = "index.html"  # Isso já é o render()
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        # lang = translation.get_language()  # Pegar a linguagem usada no navegador.
        context['servicos'] = Servico.objects.order_by("?").all()  # ? -> Ordenando por qualquer campo.
        context['funcionarios'] = Funcionario.objects.all()
        # context['lang'] = lang
        # translation.activate(lang)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class TesteView(TemplateView):
    template_name = "teste.html"
