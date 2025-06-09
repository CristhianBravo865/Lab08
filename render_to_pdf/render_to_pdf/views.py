import datetime
from django.http import Http404
from . import renderers
from django.views import View
from django.http import HttpResponse
from django.template.loader import get_template
from render_to_pdf.renderers import render_to_pdf
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        template = get_template('pdfs/invoice.html')
        context = {
            'today': "Today", 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'invoice_id': 123,
        }
        html = template.render(context)
        pdf= render_to_pdf('pdfs/invoice.html', context) 
        return HttpResponse(pdf, content_type='application/pdf')
