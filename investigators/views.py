from django.shortcuts import render,redirect
from crime_reporting import models
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
# Create your views here.
def inv_dashboard(request):
    uname = request.session.get('semail')
    if not uname:
        return redirect('login') 
        
    try:
        inv = models.Investigator.objects.get(inv_email=uname)
        inv_id = inv.inv_id

        # Counts by status
        assigned_count = models.CaseAssignment.objects.filter(fk_invest_id=inv_id, assigned_status='assigned').count()
        under_review_count = models.CaseAssignment.objects.filter(fk_invest_id=inv_id, assigned_status='Under Review').count()
        in_investigation_count = models.CaseAssignment.objects.filter(fk_invest_id=inv_id, assigned_status='In Investigation').count()
        
        # Closed includes Resolved and Closed
        resolved_count = models.CaseAssignment.objects.filter(fk_invest_id=inv_id, assigned_status='Resolved').count()
        closed_count = models.CaseAssignment.objects.filter(fk_invest_id=inv_id, assigned_status='Closed').count()
        total_closed = resolved_count + closed_count

        # Data for charts
        status_labels = ['Assigned', 'Under Review', 'In Investigation', 'Resolved', 'Closed']
        status_counts = [assigned_count, under_review_count, in_investigation_count, resolved_count, closed_count]

        context = {
            'inv': inv,
            'assigned_count': assigned_count,
            'under_review_count': under_review_count,
            'in_investigation_count': in_investigation_count,
            'total_closed': total_closed,
            'status_labels': status_labels,
            'status_counts': status_counts
        }
        return render(request,'inv_home/investigator.html', context)
    except models.Investigator.DoesNotExist:
        messages.error(request, "Investigator profile not found.")
        return redirect('login')

def change_password_inv(request):
    return render(request,'inv_home/change_pass.html')
def update_password_inv(request):
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
        return redirect('change_password_inv')

def profile_invesigator(request):
    uname=request.session['semail']
    inv=models.Investigator.objects.get(inv_email=uname)
    context={
        'cdata':inv
    }
    return render(request,'inv_home/profile.html',context)

def profile_edit_nvesigator(request):
    uname=request.session['semail']
    inv=models.Investigator.objects.get(inv_email=uname)
    context={
        'cdata':inv
    }
    return render(request,'inv_home/edit_profile.html',context)

def update_inv_profile(request):
    name=request.POST['full_name']
    email=request.POST['user_email']
    phno=request.POST['user_phone']
    address=request.POST['user_address']
    location=request.POST['user_location']
    gender=request.POST['user_gender']
    cid=request.POST['iid']
    inv=models.Investigator.objects.get(inv_id=cid)
    uname=inv.inv_email
    log_data=models.Login.objects.get(username=uname)
    inv.inv_full_name=name
    inv.inv_email=email
    inv.inv_phone=phno
    inv.inv_address=address
    inv.inv_location=location
    inv.inv_gender=gender
    inv.save()
    
    log_data.username=email
    log_data.save()
    
    request.session['semail'] = email
    
    messages.success(request,"Profile updated successfully")
    return redirect('profile_invesigator')

def crime_assigned(request):
    uname=request.session['semail']
    inv=models.Investigator.objects.get(inv_email=uname)
    inv_id=inv.inv_id
    inv_data=models.CrimeReports.objects.raw("select * from crime_reports as cr join crime_category as c on c.category_id=cr.fk_category_id join users as u on u.user_id=cr.fk_user_id join case_assignment as ca on ca.fk_report_id=cr.crime_report_id where ca.fk_invest_id=%s",[inv_id])
    context={
        'rlist':inv_data
    }

    return render(request,'inv_home/crime_assigned.html',context)
def crime_location_view(request,cid):
    crime = models.CrimeReports.objects.get(crime_report_id=cid)

    context = {
        'crime': crime
    }
    return render(request,'inv_home/crime_location.html',context)
def crime_evidence_inv(request,cid):
    evidence=models.CrimeEvidence.objects.filter(fk_crime_report_id=cid)
    context={
        'crime_id':cid,
        'elist':evidence
            }
    return render(request,'inv_home/crime_evidence.html',context)
def save_evidence_investigator(request):
    evidence_name=request.POST['fname']
    evidence_type=request.POST['ftype']
    evidence_date=request.POST['ev_date']
    crime_id=request.POST['cid']
    crime=models.CrimeReports.objects.get(crime_report_id=crime_id)
    user_id=crime.fk_user_id

    if request.method == 'POST' and request.FILES['ev_file']:
        evidence = request.FILES['ev_file']
        extension = evidence.name.split('.')[-1]
        fss = FileSystemStorage()
        timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
        file_name = f'Evidence_inve/{timestamp}.{extension}'
        file = fss.save(file_name, evidence)
    evidence_data=models.CrimeEvidence(fk_crime_report_id=crime_id,evidence_file_name=evidence_name,evidence_file_type=evidence_type,evidence_uploaded_date=evidence_date,fk_crime_user_id=user_id,evidence_file=file,uploaded_by='investigator')
    evidence_data.save()
    messages.success(request,"Evidence saved successfully")
    return redirect(crime_evidence_inv,cid=crime_id)

def edit_evidence(request,edid):
    evidence=models.CrimeEvidence.objects.get(crime_evidence_id=edid)
    context={
        'edata':evidence
    }
    return render(request,'inv_home/evidence_edit.html',context)
def update_evidence_details(request):
    evidence_name=request.POST['fname']
    evidence_type=request.POST['ftype']
    evidence_date=request.POST['ev_date']
    crime_id=request.POST['cid']
    ev_id=request.POST['eid']
    evidence=models.CrimeEvidence.objects.get(crime_evidence_id=ev_id)
    evidence.fk_crime_report_id=crime_id
    evidence.evidence_file_name=evidence_name
    evidence.evidence_file_type=evidence_type
    evidence.evidence_uploaded_date=evidence_date
    evidence.save()
    messages.success(request,"Evidence Details updated successfully")
    return redirect(crime_evidence_inv,cid=crime_id)
def update_evidence(request):
    crime_id=request.POST['cid']
    ev_id=request.POST['eid']
    edata=models.CrimeEvidence.objects.get(crime_evidence_id=ev_id)
    if request.method == 'POST' and request.FILES['ev_file']:
        evidence = request.FILES['ev_file']
        extension = evidence.name.split('.')[-1]
        fss = FileSystemStorage()
        timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
        file_name = f'Evidence_inve/{timestamp}.{extension}'
        file = fss.save(file_name, evidence)
        edata.evidence_file=file
        edata.save()
        messages.success(request,"Evidence updated successfully")
        return redirect(crime_evidence_inv,cid=crime_id)


def delete_evidence(request,eid):
    edata=models.CrimeEvidence.objects.get(crime_evidence_id=eid)
    crime_id=edata.fk_crime_report_id
    edata.delete()
    messages.success(request,"Evidence updated successfully")
    return redirect(crime_evidence_inv,cid=crime_id)
def investigation_note_save(request):
    inv_note=request.POST['inv_note']
    inv_status=request.POST['status']
    inv_date=request.POST['note_date']
    crime_id=request.POST['cid']
    uname=request.session['semail']
    inv=models.Investigator.objects.get(inv_email=uname)
    inv_id=inv.inv_id
    inv_data=models.InvestigationNotes(fk_report_id_notes=crime_id,fk_notes_officer_id=inv_id,investigation_note=inv_note,note_created_date=inv_date,investigation_status=inv_status)
    inv_data.save()
    crime=models.CrimeReports.objects.get(crime_report_id=crime_id)
    crime.crime_report_status=inv_status
    crime.save()
    case=models.CaseAssignment.objects.get(fk_report_id=crime_id)
    case.assigned_status=inv_status
    case.save()
    messages.success(request,"Investigation saved successfully")
    return redirect(investigation_note,cid=crime_id)

def edit_investigation_note(request,nid):
    note=models.InvestigationNotes.objects.get(investigation_note_id=nid)
    context={
        'note':note
    }
    return render(request,'inv_home/edit_investigation_note.html',context)
def update_note(request):
    inv_note=request.POST['inv_note']
    inv_status=request.POST['status']
    inv_date=request.POST['note_date']
    note_id=request.POST['nid']
    crime_id=request.POST['cid']
    note=models.InvestigationNotes.objects.get(investigation_note_id=note_id)
    note.investigation_note=inv_note
    note.note_created_date=inv_date
    note.investigation_status=inv_status
    note.save()
    messages.success(request,"Investigation updated successfully")
    return redirect(investigation_note,cid=crime_id)
def delete_investigation_note(request,nid):
    note=models.InvestigationNotes.objects.get(investigation_note_id=nid)
    crime_id=note.fk_report_id_notes
    note.delete()
    messages.success(request,"Investigation deleted successfully")
    return redirect(investigation_note,cid=crime_id)

# ----------------- Reporting Views -----------------
from django.db.models.functions import TruncMonth
from django.db.models import Count
import json
from django.core.serializers.json import DjangoJSONEncoder

def inv_monthly_reports(request):
    uname = request.session.get('semail')
    if not uname:
        return redirect('login') 
    
    try:
        inv = models.Investigator.objects.get(inv_email=uname)
        inv_id = inv.inv_id
        
        # Get IDs of crimes assigned to this investigator
        assigned_ids = models.CaseAssignment.objects.filter(fk_invest_id=inv_id).values_list('fk_report_id', flat=True)
        
        # Group by month for these crimes
        reports = models.CrimeReports.objects.filter(crime_report_id__in=assigned_ids).annotate(month=TruncMonth('crime_report_date')).values('month').annotate(c=Count('crime_report_id')).order_by('month')
        
        months = []
        counts = []
        table_data = []

        for r in reports:
            if r['month']:
                m_str = r['month'].strftime('%B %Y')
                months.append(m_str)
                counts.append(r['c'])
                table_data.append({'month': m_str, 'count': r['c']})
                
        context = {
            'months': months,
            'counts': counts,
            'table_data': table_data 
        }
        return render(request, 'inv_home/reports/monthly_report.html', context)
    except models.Investigator.DoesNotExist:
        messages.error(request, "Investigator profile not found.")
        return redirect('login')

def inv_category_stats_report(request):
    uname = request.session.get('semail')
    if not uname:
        return redirect('login') 
        
    try:
        inv = models.Investigator.objects.get(inv_email=uname)
        inv_id = inv.inv_id
        
        assigned_ids = models.CaseAssignment.objects.filter(fk_invest_id=inv_id).values_list('fk_report_id', flat=True)
        
        categories = models.CrimeCategory.objects.all()
        stats = []
        labels = []
        total_data = []
        
        for cat in categories:
            # Filter crimes by category AND being assigned to this investigator
            total = models.CrimeReports.objects.filter(crime_report_id__in=assigned_ids, fk_category_id=cat.category_id).count()
            
            resolved = models.CrimeReports.objects.filter(crime_report_id__in=assigned_ids, fk_category_id=cat.category_id, crime_report_status='Resolved').count()
            closed = models.CrimeReports.objects.filter(crime_report_id__in=assigned_ids, fk_category_id=cat.category_id, crime_report_status='Closed').count()
            pending = total - (resolved + closed)
            
            stats.append({
                'name': cat.category_name,
                'total': total,
                'resolved': resolved + closed,
                'pending': pending
            })
            
            labels.append(cat.category_name)
            total_data.append(total)

        context = {
            'stats': stats,
            'labels': labels,
            'total_data': total_data
        }
        return render(request, 'inv_home/reports/category_stats.html', context)
    except models.Investigator.DoesNotExist:
        messages.error(request, "Investigator profile not found.")
        return redirect('login')
def investigation_note(request,cid):
    inv=models.InvestigationNotes.objects.filter(fk_report_id_notes=cid)
    context={
        'crime_id':cid,
        'idata':inv
    }
    return render(request,'inv_home/investigation_note.html',context)
def save_investigation_note(request):
    uname=request.session['semail']
    investigator=models.Investigator.objects.get(inv_email=uname)
    cid = request.POST['cid']
    inv_note=request.POST['inv_note']
    inv_status=request.POST['status']
    inv_date=request.POST['note_date']
    inv=models.InvestigationNotes(
    investigation_note=inv_note,
    investigation_status=inv_status,
    note_created_date=inv_date,
    fk_report_id_notes=cid,
    fk_notes_officer_id=investigator.inv_id
    )
    inv.save()
    return redirect('investigation_note',cid=cid)
def edit_investigation_note(request,nid):
    uname = request.session['semail']
    
    investigator = models.Investigator.objects.get(inv_email=uname)
    note = models.InvestigationNotes.objects.get(investigation_note_id=nid)

    context = {
        'note': note
    }
    return render(request, 'inv_home/edit_investigation_note.html', context)
def update_investigation_note(request):
    nid = request.POST['nid']
    inv_note = request.POST['inv_note']
    inv_status = request.POST['status']
    inv_date = request.POST['note_date']
    cid = request.POST['cid']
    note = models.InvestigationNotes.objects.get(investigation_note_id=nid)
    note.investigation_note = inv_note
    note.investigation_status = inv_status
    note.note_created_date = inv_date
    note.save()
    return redirect('investigation_note', cid=cid)
def delete_investigation_note(request,nid,cid):
    note = models.InvestigationNotes.objects.get(
        investigation_note_id=nid
    )
    note.delete()
    return redirect('investigation_note', cid=cid)
def inv_crime_laws(request):
    category=models.CrimeCategory.objects.all()
    crime_law=models.CrimeLaw.objects.raw("select * from crime_law as c join crime_category as ca on ca.category_id=c.fk_crime_cat_id")

    context={   
        'clist':category,
        'laws':crime_law
    }
    return render(request, 'inv_home/inv_crime_laws.html',context)




