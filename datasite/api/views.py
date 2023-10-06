from django.shortcuts import render

from .forms import DatasetForm
from .models import DataSamples
import numpy as np

def parseMolecules(molecules):
    moleculeList = list(molecules)
    info = {}
    result =[[],[],[]]
    totalTypes = 0

    # Go through every entry in the data sample
    for entity in moleculeList:
        # get the molecule type string
        molecule = entity.license_plate.split("-")[0]

        if molecule not in info:
            info[molecule] = [entity.unnormalized_read_counts,1]
        else:
            info[molecule][0] += entity.unnormalized_read_counts
            info[molecule][1] += 1
        totalTypes += entity.unnormalized_read_counts

    for key in info:
        info[key][0] = np.format_float_positional(100 * (info[key][0] / totalTypes), precision=3, unique=False,fractional=False,trim='k')
        info[key][1] = np.format_float_positional(100 * (info[key][1] / len(moleculeList)), precision=3, unique=False,fractional=False,trim='k')
    
        result[0].append(key)
        result[1].append(info[key][0])
        result[2].append(info[key][1])
    
    return result

def index(request):
    if request.method == "POST":
        form = DatasetForm(request.POST)
        if form.is_valid():
            dataSet_id = form.data["dataSet"]
            molecules = DataSamples.objects.filter(dataset_id=dataSet_id)
            info = parseMolecules(molecules)
            context = {"form":form,"labels":info[0],"counts_data":info[1],"unique_counts_data":info[2]}
            return render(request, 'index.html', context)
    else:
        form = DatasetForm()
        return render(request, 'index.html', {"form":form})

def load_molecules(request):
    dataSet_id = request.GET.get("dataSet")
    molecules = DataSamples.objects.filter(dataset_id=dataSet_id)
    context = {"molecules":molecules}
    return render(request, "chart.html", context)