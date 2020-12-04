from django.shortcuts import render
from django.http import FileResponse
from django.views.generic import View
import io

# ReportLab
from reportlab.pdfgen import canvas

# EasyPrint
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse
from weasyprint import HTML


class IndexView(View):

    def get(self, request, *args, **kwargs):
        # Weasyprint usa html para fazer o pdf.
        # Cria um arquivo para receber os dados e gerar o PDF.
        buffer = io.BytesIO()

        # Criar o arquivo pdf
        pdf = canvas.Canvas(buffer)

        # Insere 'coisas' no pdf
        pdf.drawString(100, 100, "Geek University")  # x, y, text

        # Quando acabamos de inserir coisas no PDF
        pdf.showPage()
        pdf.save()

        # Por fim, retornamos o buffer para o inicio do arquivo
        buffer.seek(0)

        # Inicia o download automaticamente
        # return FileResponse(buffer, as_attachment=True, filename="relatorio1.pdf")

        # Abre o PDF direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')


class Index2View(View):

    def get(self, request, *args, **kwargs):
        texto = ['Geek University', 'Evolua seu lado geek', 'Programação Web com Python e Dango']
        html_string = render_to_string('relatorio.html', {'texto': texto})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/relatorio2.pdf')

        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # Faz o download do arquivo PDF
            # response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf"'

            # Abre o PDF direto no navegador
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'
        return response
