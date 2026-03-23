from django.shortcuts import render,redirect
from crime_reporting import models
from django.contrib import messages
from datetime import datetime
# Create your views here.
def admin(request):
    # Overview Counts
    new_cases = models.CrimeReports.objects.filter(crime_report_status='requested').count()
    pending_cases = models.CrimeReports.objects.filter(crime_report_status='Under Review').count()
    inprogress_cases = models.CrimeReports.objects.filter(crime_report_status='In Investigation').count()
    closed_cases = models.CrimeReports.objects.filter(crime_report_status__in=['Resolved', 'Closed']).count()

    # Analytics: Cases by Category
    categories = models.CrimeCategory.objects.all()
    cat_names = []
    cat_counts = []
    for cat in categories:
        c_count = models.CrimeReports.objects.filter(fk_category_id=cat.category_id).count()
        cat_names.append(cat.category_name)
        cat_counts.append(c_count)

    # Analytics: Cases by Status
    status_labels = ['New', 'Pending', 'In Progress', 'Resolved', 'Closed']
    status_counts = [
        models.CrimeReports.objects.filter(crime_report_status='requested').count(),
        models.CrimeReports.objects.filter(crime_report_status='Under Review').count(),
        models.CrimeReports.objects.filter(crime_report_status='In Investigation').count(),
        models.CrimeReports.objects.filter(crime_report_status='Resolved').count(),
        models.CrimeReports.objects.filter(crime_report_status='Closed').count(),
    ]

    context = {
        'new_cases': new_cases,
        'pending_cases': pending_cases,
        'inprogress_cases': inprogress_cases,
        'closed_cases': closed_cases,
        'cat_names': cat_names,
        'cat_counts': cat_counts,
        'status_labels': status_labels,
        'status_counts': status_counts, 
    }
    return render(request,'admin/admin.html', context)

def change_password(request):
    return render(request,'admin/change_pass.html')
def update_password(request):
    npass=request.POST['npass']
    cpass=request.POST['cpass']
    uname=request.session['semail']
    log_data=models.Login.objects.get(username=uname)
    if npass==cpass:
        log_data.password=npass
        log_data.save()
        return redirect('login')
    else:
        messages.warning(request,"new password and confirm password are not matching")    
        return redirect('change_password')

def category(request):
    category=models.CrimeCategory.objects.all()
    context={
        'clist':category
    }
    return render(request,'category/category.html',context)

def category_save(request):
    category=request.POST['categ']
    description=request.POST['desc']
    existing_category = models.CrimeCategory.objects.filter(category_name=category).first()
    if existing_category:
        messages.warning(request,'category already exists!!!!!')
        return redirect('category')
    categ_data=models.CrimeCategory(category_name=category,category_dec=description)
    categ_data.save()
    messages.success(request,"category saved successfully")
    return redirect('category')

def delete_category(request,cid):
    category=models.CrimeCategory.objects.get(category_id=cid)
    category_count = models.CrimeReports.objects.filter(fk_category_id=cid).count()

    if category_count == 0:
        category.delete()
        messages.success(request, 'Deleted successfully!!!!')
        return redirect('category')
    else:
        messages.warning(request, 'Cannot delete category. Associated crime report exist.')
        return redirect('category')

def edit_category(request,cid):
    category=models.CrimeCategory.objects.get(category_id=cid)
    context={
        'categ':category
            }
    return render(request,'category/edit_category.html',context)

def update_category(request):    
    cat_name=request.POST['categ']
    description=request.POST['desc']
    categ_id=request.POST['cat_id']
    category=models.CrimeCategory.objects.get(category_id=categ_id)
    category.category_name=cat_name
    category.category_dec=description
    category.save()
    messages.success(request,"Category data updated successfully")
    return redirect('category')


def investigator(request):
    investigator=models.Investigator.objects.all()
    context={
        'ilist':investigator
    }
    return render(request,'investigator/investigator.html',context)
def new_investigator(request):
    return render(request,'investigator/new_investigator.html')

def investigator_save(request):
    name=request.POST['full_name']
    email=request.POST['user_email']
    phno=request.POST['user_phone']
    address=request.POST['user_address']
    location=request.POST['user_location']
    gender=request.POST['user_gender']
    password=request.POST['password']
    existing_user = models.Login.objects.filter(username=email).first()
    if existing_user:
        messages.warning(request,'Email Id already exists!!!!!')
        return redirect('new_investigator')
    investigator_data=models.Investigator(inv_full_name=name,inv_email=email,inv_phone=phno,inv_address=address,inv_location=location,inv_gender=gender,inv_role='investigator')
    investigator_data.save()
    log_data=models.Login(username=email,password=password,user_type='investigator',user_status='active')
    log_data.save()
    messages.success(request,"Investigator saved successfully")
    return redirect('investigator')

def edit_investigator(request,iid):
    investigator=models.Investigator.objects.get(inv_id=iid)
    context={
        'inv':investigator
            }
    return render(request,'investigator/edit_investigator.html',context)
def update_investigator(request):
    name=request.POST['full_name']
    email=request.POST['user_email']
    phno=request.POST['user_phone']
    address=request.POST['user_address']
    location=request.POST['user_location']
    gender=request.POST['user_gender']
    inv_id=request.POST['iid']
    investigator=models.Investigator.objects.get(inv_id=inv_id)
    inv_uname=investigator.inv_email
    
    existing_user = models.Login.objects.filter(username=email).first()
    if existing_user:
        messages.warning(request,'Email Id already exists!!!!!')
        return redirect('edit_investigator',iid=inv_id)
    log_data=models.Login.objects.get(username=inv_uname)
    uid=log_data.user_id
    log_data_uid=models.Login.objects.get(user_id=uid)
    log_data.username=email
    log_data.save()
    investigator.inv_full_name=name
    investigator.inv_email=email
    investigator.inv_phone=phno
    investigator.inv_address=address
    investigator.inv_location=location
    investigator.inv_gender=gender
    investigator.save()
    messages.success(request,"Investigator details updated successfully")
    return redirect('investigator')

def delete_investigator(request,iid):
    investigator=models.Investigator.objects.get(inv_id=iid)
    uname=investigator.inv_email
    investigator_count = models.CaseAssignment.objects.filter(fk_invest_id=iid).count()

    if investigator_count == 0:
        investigator.delete()
        log_data=models.Login.objects.get(username=uname)
        log_data.delete()
        messages.success(request, 'Deleted successfully!!!!')
        return redirect('investigator')
    else:
        messages.warning(request, 'Cannot delete investigator. Associated case assignment exist.')
        return redirect('investigator')

def citizens(request):
    citizens=models.Users.objects.raw("select * from users where user_role='citizen'")
    context={
        'clist':citizens
    }
    return render(request,'admin/citizens.html',context)
def reported_crimes(request):
    investigators=models.Investigator.objects.all()
    crime_reports=models.CrimeReports.objects.raw("select *, (select count(*) from investigation_notes where fk_report_id_notes = cr.crime_report_id) as note_count from crime_reports as cr join crime_category as c on c.category_id=cr.fk_category_id join users as u on u.user_id=cr.fk_user_id left join case_assignment as ca on cr.crime_report_id=ca.fk_report_id left join investigator as i on i.inv_id=ca.fk_invest_id")
    context={
        'clist':crime_reports,
        'ilist':investigators
    }
    return render(request,'admin/crime.html',context)
def crime_location(request,cid):
    crime = models.CrimeReports.objects.get(crime_report_id=cid)

    context = {
        'crime': crime
    }
    return render(request,'admin/crime_location.html',context)
def schedule_investigator(request,cid):
    return render(request,'admin/schedule_investigator.html')

def assign_investigator(request):
    if request.method == "POST":
        crime_id = request.POST["crime_id"]
        investigator_id = request.POST["investigator_id"]
        schedule=models.CaseAssignment(fk_report_id=crime_id,fk_invest_id=investigator_id,assigned_at=datetime.now(),assigned_status='assigned')
        schedule.save()
        crime_data=models.CrimeReports.objects.get(crime_report_id=crime_id)
        crime_data.crime_report_status='Under Review'
        messages.warning(request, 'Case Assigned to Investigator and case is under review')
        crime_data.save()
        return redirect('reported_crimes')

def investigation_note(request):
    notes=models.InvestigationNotes.objects.raw("select * from investigator i join  investigation_notes n on i.inv_id = n.fk_notes_officer_id join crime_reports c on c.crime_report_id=n.fk_report_id_notes ")
    context={
        'notes':notes,
    }
    return render(request,'admin/investigation_note.html',context)
def inv_note(request,cid):
    notes=models.InvestigationNotes.objects.raw("select * from investigator i join  investigation_notes n on i.inv_id = n.fk_notes_officer_id where n.fk_report_id_notes=%s",[cid])
    context={
        'notes':notes,
    }
    return render(request,'admin/investigation_note.html',context)
def crime_law(request):
    category=models.CrimeCategory.objects.all()
    crime_law=models.CrimeLaw.objects.raw("select * from crime_law as c join crime_category as ca on ca.category_id=c.fk_crime_cat_id")

    context={   
        'clist':category,
        'laws':crime_law
    }
    return render(request,'crime_law/crime_law.html',context)
def crime_law_save(request):
    category=request.POST['categ']
    crime_law=request.POST['law']
    existing_law = models.CrimeLaw.objects.filter(crime_law=crime_law).first()
    if existing_law:
        messages.warning(request,'Crime law already exists!!!!!')
        return redirect('crime_law')
    law_data=models.CrimeLaw(fk_crime_cat_id=category,crime_law=crime_law)
    law_data.save()
    messages.success(request,"crime law saved successfully")
    return redirect('crime_law')
def edit_crime_law(request, id):
    law = models.CrimeLaw.objects.get(crime_law_id=id)
    category = models.CrimeCategory.objects.all()

    context = {
        'law': law,
        'clist': category
    }
    return render(request, 'crime_law/edit_crime_law.html', context)
def update_crime_law(request):
    law_id = request.POST['law_id']
    category = request.POST['categ']
    crime_law = request.POST['law']
    id=request.POST['law']
    law = models.CrimeLaw.objects.get(crime_law_id=law_id)
    law.fk_crime_cat_id = category
    law.crime_law = crime_law
    law.save()
    messages.success(request, "Crime law updated successfully")
    return redirect('crime_law')
def delete_crime_law(request,id):
    law=models.CrimeLaw.objects.get(crime_law_id=id)
    law.delete()
    messages.success(request, "Crime law deleted successfully")
    return redirect('crime_law')


