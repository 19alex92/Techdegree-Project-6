import json
import os
from django.shortcuts import render
from django.http import HttpResponse

from .models import Minerals


def index(request):
    return render(request, 'catalog/layout.html')


def mineral_list(request):
    minerals = Minerals.objects.all()
    return render(request, 'catalog/mineral_list.html')


def mineral_detail(request):
    return render(request, 'catalog/mineral_detail.html')


#def import_method(request):
#    filepath = os.path.dirname(__file__)
#    file_path = os.path.join(filepath, 'static/catalog/json/minerals.json')
#
#    with open(file_path, encoding="utf8") as json_file:
#        data = json.load(json_file)
#        for value in data:
#            value.setdefault('category', "")
#            value.setdefault('formula', "")
#            value.setdefault('strunz classification', "")
#            value.setdefault('color', "")
#            value.setdefault('crystal system', "")
#            value.setdefault('unit cell', "")
#            value.setdefault('crystal symmetry', "")
#            value.setdefault('cleavage', "")
#            value.setdefault('mohs scale hardness', "")
#            value.setdefault('luster', "")
#            value.setdefault('streak', "")
#            value.setdefault('diaphaneity', "")
#            value.setdefault('optical properties', "")
#            value.setdefault('refractive index', "")
#            value.setdefault('crystal habit', "")
#            value.setdefault('specific gravity', "")
#            value.setdefault('group', "")
#            d = Minerals(
#                name=value['name'],
#                image_filename=value['image filename'],
#                image_caption=value['image caption'],
#                category=value['category'],
#                formula=value['formula'],
#                strunz_classification=value['strunz classification'],
#                color=value['color'],
#                crystal_system=value['crystal system'],
#                unit_cell=value['unit cell'],
#                crystal_symmetry=value['crystal symmetry'],
#                cleavage=value['cleavage'],
#                mohs_scale_hardness=value['mohs scale hardness'],
#                luster=value['luster'],
#                streak=value['streak'],
#                diaphaneity=value['diaphaneity'],
#                optical_properties=value['optical properties'],
#                refractive_index=value['refractive index'],
#                crystal_habit=value['crystal habit'],
#                specific_gravity=value['specific gravity'],
#                group=value['group']
#            )
#            d.save()
#    return HttpResponse('Did it work?')