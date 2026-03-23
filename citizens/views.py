from django.shortcuts import render,redirect
from crime_reporting import models
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
from datetime import date
import json
import os
from django.conf import settings

# Create your views here.
def citizen(request):
    uname = request.session['semail']
    user = models.Users.objects.get(user_email=uname)
    uid = user.user_id
    
    total_crimes = models.CrimeReports.objects.filter(fk_user_id=uid).count()
    pending_crimes = models.CrimeReports.objects.filter(fk_user_id=uid, crime_report_status='requested').count()
    processing_crimes = models.CrimeReports.objects.filter(fk_user_id=uid, crime_report_status__in=['Under Review', 'In Investigation']).count()
    completed_crimes = models.CrimeReports.objects.filter(fk_user_id=uid, crime_report_status__in=['Resolved', 'Closed']).count()
    
    # recent 5 reports with category details
    recent_reports = models.CrimeReports.objects.raw("select * from crime_reports as cr join crime_category as c on c.category_id=cr.fk_category_id where fk_user_id=%s order by crime_report_date desc limit 5", [uid])

    context = {
        'total_crimes': total_crimes,
        'pending_crimes': pending_crimes,
        'processing_crimes': processing_crimes,
        'completed_crimes': completed_crimes,
        'recent_reports': recent_reports
    }
    return render(request, 'citizen/citizen.html', context)
def change_password_citizen(request):
    return render(request,'citizen/change_pass.html')
def update_password_citizen(request):
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
        return redirect('change_password_citizen')
def profile_citizen(request):
    uname=request.session['semail']
    citizen=models.Users.objects.get(user_email=uname)
    context={
        'cdata':citizen
    }
    return render(request,'citizen/profile.html',context)
def profile_edit_citizen(request):
    uname=request.session['semail']
    citizen=models.Users.objects.get(user_email=uname)
    context={
        'cdata':citizen
    }
    return render(request,'citizen/edit_profile.html',context)

def update_cprofile(request):
    name=request.POST['full_name']
    email=request.POST['user_email']
    phno=request.POST['user_phone']
    address=request.POST['user_address']
    location=request.POST['user_location']
    gender=request.POST['user_gender']
    cid=request.POST['iid']
    citizen=models.Users.objects.get(user_id=cid)
    uname=citizen.user_email
    log_data=models.Login.objects.get(username=uname)
    citizen.full_name=name
    citizen.user_email=email
    citizen.user_phone=phno
    citizen.user_address=address
    citizen.user_location=location
    citizen.user_gender=gender
    citizen.save()
    
    log_data.username=email
    log_data.save()
    
    request.session['semail'] = email
    
    messages.success(request,"Profile updated successfully")
    return redirect('profile_citizen')


def add_crime(request):
    category=models.CrimeCategory.objects.all()
    context={
        'clist':category
    }
    return render(request,'crime/add_crime.html',context)
def save_crime(request):
    uname=request.session['semail'] 
    citizen=models.Users.objects.get(user_email=uname)
    category_id = request.POST['category']
    title = request.POST['title']
    description = request.POST['description']
    location = request.POST['location']
    latitude = request.POST['latitude']
    longitude = request.POST['longitude']
    date = request.POST['cdate']
    crime=models.CrimeReports(
        fk_user_id=citizen.user_id,
            fk_category_id=category_id,
            crime_report_title=title,
            crime_description=description,
            crime_report_location=location,
            crime_report_latitude=latitude,
            crime_report_longitude=longitude,
            crime_report_date=date,
    )
    crime.save()
    return redirect('crime_citizen')
def crime_citizen(request):
    uname = request.session['semail']
    user = models.Users.objects.get(user_email=uname)
    crime = models.CrimeReports.objects.raw("select * from crime_reports as c join crime_category as cat on cat.category_id=c.fk_category_id where c.fk_user_id=%s",[user.user_id])
    return render(request, 'crime/crime.html', {
        'crime': crime
    })
def edit_reported_crimes(request,cid):
    uname=request.session['semail']
    category=models.CrimeCategory.objects.all()
    crime=models.CrimeReports.objects.get(crime_report_id=cid)
    context={
        'crime':crime,
        'categories':category

    }
    return render(request,'crime/crime_edit.html',context)
def update_reported_crimes(request):
    category_id = request.POST['categ']
    title = request.POST['title']
    description = request.POST['description']
   
    date = request.POST['cdate']
    cid=request.POST['crime_id']
    crime=models.CrimeReports.objects.get(crime_report_id=cid)
    crime.fk_category_id=category_id
    crime.crime_report_title=title
    crime.crime_description=description
   
    crime.crime_report_date=date
    crime.save()
    return redirect('crime_citizen')
def delete_reported_crimes(request,cid):
    crime=models.CrimeReports.objects.get(crime_report_id=cid)
    crime.delete()
    return redirect('crime_citizen')
def evidence_citizen(request,cid):
    crime = models.CrimeReports.objects.get(crime_report_id=cid)
    evidence_list = models.CrimeEvidence.objects.filter(fk_crime_report_id=cid)

    return render(request, 'crime/crime_evidence.html', {
        'cid': cid,
        'crime': crime,
        'evidence': evidence_list
    })
def save_evidence(request):
    evidence_name=request.POST['fname']
    evidence_type=request.POST['ftype']
    evidence_date=request.POST['ev_date']
    cid=request.POST['cid']
    crime=models.CrimeReports.objects.get(crime_report_id=cid)
    user_id=crime.fk_user_id

    if request.method == 'POST' and request.FILES['ev_file']:
        evidence = request.FILES['ev_file']
        extension = evidence.name.split('.')[-1]
        fss = FileSystemStorage()
        timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
        file_name = f'Evidence_citizen/{timestamp}.{extension}'
        file = fss.save(file_name, evidence)
    evidence_data=models.CrimeEvidence(fk_crime_report_id=cid,evidence_file_name=evidence_name,evidence_file_type=evidence_type,evidence_uploaded_date=evidence_date,fk_crime_user_id=user_id,evidence_file=file,uploaded_by='investigator')
    evidence_data.save()
    messages.success(request,"Evidence saved successfully")
    return redirect(evidence_citizen,cid=cid)
def edit_evidence_citizen(request, eid):
    evidence = models.CrimeEvidence.objects.get(crime_evidence_id=eid)

    return render(request, 'crime/evidence_edit.html', {
        'e': evidence
    })
def update_evidence(request):
    if request.method == 'POST':
        eid = request.POST['eid']
        evidence = models.CrimeEvidence.objects.get(crime_evidence_id=eid)
        evidence.evidence_file_name = request.POST['fname']
        evidence.evidence_file_type = request.POST['ftype']
        evidence.evidence_uploaded_date = request.POST['ev_date']
        if request.FILES.get('ev_file'):
            file = request.FILES['ev_file']
            extension = file.name.split('.')[-1]
            fss = FileSystemStorage()
            timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
            file_name = f'Evidence/{timestamp}.{extension}'
            uploaded_file = fss.save(file_name, file)
            evidence.evidence_file = uploaded_file

        evidence.save()

        messages.success(request, "Evidence updated successfully")

        return redirect('evidence_citizen', cid=evidence.fk_crime_report_id)
def delete_evidence(request, eid):
    evidence = models.CrimeEvidence.objects.get(crime_evidence_id=eid)
    cid = evidence.fk_crime_report_id
    evidence.delete()
    return redirect('evidence_citizen', cid=cid)
def citizen_crime_laws(request):
    category=models.CrimeCategory.objects.all()
    crime_law=models.CrimeLaw.objects.raw("select * from crime_law as c join crime_category as ca on ca.category_id=c.fk_crime_cat_id")

    context={   
        'clist':category,
        'laws':crime_law
    }
    return render(request, 'citizen/crime_law.html',context)
def citizen_law_description(request):

    folder_path = os.path.join(settings.BASE_DIR, 'law_description')

    all_laws = []

    for file in os.listdir(folder_path):
        if file.endswith('.json'):
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                data = json.load(f)
                all_laws.extend(data)

    context = {
        'laws': all_laws
    }

    return render(request, 'citizen/citizen_law_description.html', context)


