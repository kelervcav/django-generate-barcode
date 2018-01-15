from django.shortcuts import render
import barcode
from barcode.writer import ImageWriter
from io import BytesIO
import base64


def barcode_generator(request):
    image = ''
    if request.method == 'POST' and request.POST.get('input_barcode'):
        text = request.POST.get('input_barcode')
        btype = request.POST.get('btype')

        # Generate barcode
        FORMAT = barcode.get_barcode_class(btype)
        code = FORMAT(text, writer=ImageWriter())

        buffer = BytesIO()
        code.write(buffer)
        image = base64.b64encode(buffer.getvalue())

    template_name = 'barcodes/barcode_generator.html'
    context = {
        'image': image,
    }
    return render(request, template_name, context)
