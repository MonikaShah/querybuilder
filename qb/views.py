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

    district_selected = None
    subdistrict_selected = None
    village_selected = None
    school_selected = None
    schcd_selected = None
    villagecode_selected =None
    schoolcode_selected =None

    # schcd = 0
    # dcd = 0
    # bcd =0
    # vcd=0
    # toal_popu =0
    # tot_m = 0
    # tot_f = 0
    # tot_work_f = 0
    # tot_work_m =0
    # vilcod=0
    # schcod=0
    # schmgt =0
    
    
    num_school = School1617Codes.objects.all().count()
    # schoolgen = SchoolGeneral1617.objects.all()
    # mahaddwgen = MahaDdw.objects.all()
    num_boys_school = SchoolGeneral1617.objects.filter(schtype='1').count()
    num_girls_school= SchoolGeneral1617.objects.filter(schtype='2').count()
    num_coed_school= SchoolGeneral1617.objects.filter(schtype='3').count()
    dname = School1617Codes.objects.order_by('distname').values('distname').distinct()

    # bname= School1617Codes.objects.filter(distname=district_selected).distinct('block_name')

    if request.method == "POST":
        district_selected = None
        subdistrict_selected = None
        village_selected = None
        school_selected = None
        villagecode_selected = None
        schoolcode_selected = None
        dcd = 0
        bcd =0
        vcd=0
        toal_popu =0
        tot_m = 0
        tot_f = 0
        tot_work_f = 0
        tot_work_m =0
        schmgt =0
        # district_selected = request.POST.get("data")
        district_selected = request.POST.get("dist_select")
        subdistrict_selected = request.POST.get("subdist_select")
        village_selected = request.POST.get("village_select")
        school_selected = request.POST.get("school_select")
        villagecode_selected = request.POST.get("villagecode_select")
        schoolcode_selected = request.POST.get("schoolcode_select")
        # showchart = request.POST.get("show")
      
        
    context = {
            'num_school': num_school,
            'num_boys_school':num_boys_school,
            'num_girls_school':num_girls_school,
            'num_coed_school':num_coed_school,
            'dname':dname,
            
            
            'bname': School1617Codes.objects.filter(distname=district_selected).distinct('block_name'),
            'vname' : School1617Codes.objects.filter(block_name=subdistrict_selected).filter(distname=district_selected).distinct('village_name'),
            'sname' : School1617Codes.objects.filter(village_name=village_selected).filter(block_name=subdistrict_selected).filter(distname=district_selected).distinct('school_name'),
            'vilcod' : School1617Codes.objects.filter(village_name=village_selected).filter(block_name=subdistrict_selected).filter(distname=district_selected).distinct('village_code'),
            'schcode' : School1617Codes.objects.filter(school_name=school_selected).filter(village_name=village_selected).filter(block_name=subdistrict_selected).filter(distname=district_selected).distinct('school_code'),
                   
            'district_selected':district_selected,
            'subdistrict_selected':subdistrict_selected,
            'village_selected':village_selected,
            'school_selected':school_selected,
            'villagecode_selected':villagecode_selected,
            'schoolcode_selected':schoolcode_selected,
            # 'showchart':showchart,
            
        
            # 'dcd':School1617Codes.objects.values_list('district_code',flat=True).get(school_name=school_selected,village_name=village_selected,block_name=subdistrict_selected,distname=district_selected),
            # 'bcd':School1617Codes.objects.values_list('block_code',flat=True).get(school_name=school_selected,village_name=village_selected,block_name=subdistrict_selected,distname=district_selected),
               
            # 'tot_popu':MahaDdw.objects.values_list('tot_p',flat=True).get(census_2011code=villagecode_selected),
            # 'tot_m':MahaDdw.objects.values_list('tot_m',flat=True).get(census_2011code=villagecode_selected),
            # 'tot_f':MahaDdw.objects.values_list('tot_f',flat=True).get(census_2011code=villagecode_selected),
            # 'tot_work_m':MahaDdw.objects.values_list('tot_work_m',flat=True).get(census_2011code=villagecode_selected),
            # 'tot_work_f':MahaDdw.objects.values_list('tot_work_f',flat=True).get(census_2011code=villagecode_selected),
              
            # 'schmgt':SchoolGeneral1617.objects.values_list('schmgt',flat=True).get(schcd=schoolcode_selected),
            # 'schcat':SchoolGeneral1617.objects.values_list('schcat',flat=True).get(schcd=schoolcode_selected),
            # 'schtype':SchoolGeneral1617.objects.values_list('schtype',flat=True).get(schcd=schoolcode_selected),
            # 'lowclass':SchoolGeneral1617.objects.values_list('lowclass',flat=True).get(schcd=schoolcode_selected),
            # 'highclass':SchoolGeneral1617.objects.values_list('highclass',flat=True).get(schcd=schoolcode_selected),
            
        }

      
 # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context)

