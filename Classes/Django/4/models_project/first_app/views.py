from django.shortcuts import render
from .models import AccessRecord, Webpage

# Create your views here.


def index(request):
    access_records = AccessRecord.objects.all()
    processed_records = []

    for record in access_records:
        processed_records.append({"name": str(record.name), "date": str(record.date)})

    context = {"access_records": processed_records}
    return render(request, "index.html", context)
