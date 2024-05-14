from django.core.files.storage import default_storage
from django.shortcuts import render
from .models import FileUpload
from io import BytesIO
from django.http import HttpResponse
import pandas as pd
from .extract import *


# Create your views here.
def upload(request):
    uploaded_files = []
    if request.method == "POST":
        file = request.FILES.getlist('file[]')
        for i in file:
            saved_file = f"files/{default_storage.save(i.name, i)}"
            uploaded_files.append(saved_file)
            FileUpload.objects.create(file=i)
        data = FileUpload.objects.all()
        data_inf = processing(uploaded_files)
        return download_excel(data_inf)
    return render(request, "Templates/index.html", locals())


def download_excel(data_inf):
    response = HttpResponse(data_inf, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=my_data.xlsx'
    return response
