from django.shortcuts import render
from django.http import HttpResponse
from django.db  import connection
from .models import School1617Codes,SchoolGeneral1617,MahaDdw
from django.template import loader
from django.views.generic import TemplateView, ListView
from qb import views


def index(request):
    #return HttpResponse("Hello, world. You're at the school index.")

    class IndexView(ListView):
        # model = School1617Codes
        # form_class = DistrictForm
        # # success_url = 'templates/'
        template_view = 'templates/School1617Codes/index.html'

        def get_queryset(self):
            return School1617Codes.objects.all()

#         def village(request, vcd):
# #        # person = get_object_or_404(Person, id=person)
#             return render(request, 'qb/templates/village.html', {'vcd': vcd})
       


    class AboutView(TemplateView):
        template_view = 'templates/School1617Codes/about.html'

# def village_info(request,vcd):
#     return render(request,'qb/templates/village_info.html',{vcd})


 
 
# Generate counts of some of the school codes
    # cursor = connection.cursor()

    district_selected = None
    subdistrict_selected = None
    village_selected = None
    school_selected = None
    schcd_selected = None
    schcd = 0
    vcode = 0
    dcd = 0
    bcd =0
    vcd=0
    vdd =0
    toal_p =0
    
    num_school = School1617Codes.objects.all().count()
    # schoolgen = SchoolGeneral1617.objects.all()
    # mahaddwgen = MahaDdw.objects.all()
    num_boys_school = SchoolGeneral1617.objects.filter(schtype='1').count()
    num_girls_school= SchoolGeneral1617.objects.filter(schtype='2').count()
    num_coed_school= SchoolGeneral1617.objects.filter(schtype='3').count()
    dname = School1617Codes.objects.order_by('distname').values('distname').distinct()

    if request.method == "POST":
        # Filter parmaeters by selected region, but only on a POST
        district_selected = request.POST.get("dist_select")
        subdistrict_selected = request.POST.get("subdist_select")
        village_selected = request.POST.get("village_select")
        school_selected = request.POST.get("school_select")
        # vdd = request.POST.get("vilcod")
        # tot_p = cursor.callproc('tot_p',[vdd and tot_p])
        
        
    context = {
            'num_school': num_school,
            'num_boys_school':num_boys_school,
            'num_girls_school':num_girls_school,
            'num_coed_school':num_coed_school,
            'dname':dname,
            
            
            'bname': School1617Codes.objects.filter(distname=district_selected).distinct('block_name'),
            'vname' : School1617Codes.objects.filter(block_name=subdistrict_selected).distinct('village_name'),
            'sname' : School1617Codes.objects.filter(village_name=village_selected).distinct('school_name'),
            
            'district_selected':district_selected,
            'subdistrict_selected':subdistrict_selected,
            'village_selected':village_selected,
            'school_selected':school_selected,
            # 'value1':vdd,
                  
        
            'dcd':School1617Codes.objects.values_list('district_code',flat=True).get(school_name=school_selected),
            'bcd':School1617Codes.objects.values_list('block_code',flat=True).get(school_name=school_selected),
            'vcd':School1617Codes.objects.values_list('village_code',flat=True).get(school_name=school_selected),               
            'schcd':School1617Codes.objects.values_list('school_code',flat=True).get(school_name=school_selected),
            'tot_p':"vcd",
            # 'tot_p': cursor.callproc('tot_p',[vcd and tot_p]),
            # 'tot_p': MahaDdw.objects.filter(census_2011code='value1').count(),
           

            # 'vdd':School1617Codes.objects.get_queryset
            # 'tot_p': MahaDdw.objects.values_list('tot_p',flat=True).get(census_2011code=vdd),
            # 'tot_popo': MahaDdw.objects.filter(census_2011code=vcd).distinct(toal_p),
            # for tot_p in MahaDdw.objects.raw('SELECT tot_p FROM qb_mahaddw WHERE census_2011code = %s', [vcd]):
            #     print(toal_p)
        
        }

      
 # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)

  

    # if form.is_valid():
    #     dist_selected = form.cleaned_data['value']
    #     values = request.POST.getlist()
    #     print(values)
    #     return render(request, 'index.html',{'dist_selected': dist_selected})
        
