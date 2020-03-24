from django.shortcuts import render
from django.http import HttpResponse
from django.db  import connection
from .models import School1617Codes,SchoolGeneral1617,MahaDdw
from django.template import loader

def village_info(request, vcd):

      return render(request, 'qb/templates/village.html', {'vcd': vcd})

             # Render the HTML template village.html with the data in the context variable
 

