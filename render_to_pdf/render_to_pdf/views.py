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
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" %("12341231")
            content= "inline; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found", status=404, content_type='text/plain')
