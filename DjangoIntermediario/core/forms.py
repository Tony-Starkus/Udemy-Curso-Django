from django import forms
from django.core.mail.message import EmailMessage
from .models import Produto


class ContatoForm(forms.Form):
    nome = forms.CharField(label="Nome", max_length=100)
    email = forms.EmailField(label="E-mail", max_length=100)
    assunto = forms.CharField(label="Assunto", max_length=120)
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f"Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}"

        mail = EmailMessage(subject="E-mail enviado pelo django2",
                            body=conteudo,
                            from_email="contato@seudominio.com.br",
                            to=['contato@seudominio.com.br'],  # É uma lista porque você pode enviar para vários emails.
                            headers={'Reply-To': email})  # Em caso de respostas, responder para esse email.
        mail.send()


class ProdutoModelForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'estoque', 'imagem']
