
from django.shortcuts import render
from .forms import Vechicle_Detail,Engine_Detail
from.models import *


def home(request):
  if request.method == "POST":
        form = Vechicle_Detail(request.POST)
        Form = Engine_Detail(request.POST)

        if form.is_valid() or Form.is_valid():
            SAP = form.cleaned_data['SAP_Code']
            ledger = form.cleaned_data['Ledger_Name']
            manufacture = form.cleaned_data['Manufacturer']
            model = form.cleaned_data['Model']
            v_type = form.cleaned_data['Vehicle_Type']
            dis = form.cleaned_data['Base_Km']
            RTO = form.cleaned_data['RTO']
            Myear = Form.cleaned_data['Model_year']
            CNO = Form.cleaned_data['Chassis_No']
            Ftype = Form.cleaned_data['Fuel_TYPE']
            ovn = Form.cleaned_data['old_vehicle_No']
            reg = Vechicle_Detail(SAP_Code=SAP, Ledger_Name=ledger, Manufacturer=manufacture, Model=model,
                                     Vehicle_Type=v_type,Base_Km=dis,RTO=RTO)
            Reg = Engine_Detail(Model_year=Myear, Chassis_No=CNO, Fuel_TYPE=Ftype, old_vehicle_No=ovn)
            reg.save()
            Reg.save()
            form = Vechicle_Detail()
            Form = Engine_Detail()
        return render(request, "index.html",{'form':form,'Form':Form})
  else:
      form = Vechicle_Detail()
      Form = Engine_Detail()
      return render(request,"index.html",{'form':form,'Form':Form})




# def engine(request):
#   if request.method == "POST":
#         Form = Engine_Detail(request.POST)
#         if Form.is_valid():
#             Myear = Form.cleaned_data['Model_year']
#             CNO = Form.cleaned_data['Chassis_No']
#             Ftype = Form.cleaned_data['Fuel_TYPE']
#             ovn = Form.cleaned_data['old_vehicle_No']
#             reg = Engine_Detail(Model_year=Myear, Chassis_No=CNO, Fuel_TYPE=Ftype, old_vehicle_No=ovn)
#             reg.save()
#             Form = Engine_Detail()
#         return render(request, "details.html", {'Form': Form})
#   else:
#     Form = Vechicle_Detail()
#     return render(request, "details.html", {'Form': Form})
