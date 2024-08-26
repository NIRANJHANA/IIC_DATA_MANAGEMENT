from django.shortcuts import render
from django.db.models import Count
from .models import FacultyMember, StudentMember
from collections import defaultdict

def UserHome(request):

    return render(request, 'user_home.html')

def UserEdcCourse(request):
    
    return render(request, 'user_edc_courseAvailable.html')

def UserEdcLearning(request):
    
    return render(request, 'user_edc_myLearning.html')

def UserEdcHome(request):
    
    return render(request, 'user_edc_home.html')

def UserIICAbout(request):
    
    return render(request, 'user_iic_about.html')

def UserIICAchievements(request):

    return render(request, 'user_iic_achievement.html')

def UserIICActivity(request):
    
    return render(request, 'user_iic_activity.html')


"""def UserIICCouncil(request):
    # Retrieve and order faculty members by 'sl_no'
    faculty_members = FacultyMember.objects.order_by('sl_no')
    
    # Calculate rowspan for the 'category' field
    category_rowspan = defaultdict(int)
    for member in faculty_members:
        category_rowspan[member.category] += 1

    # Assign rowspan and reset for next category
    for member in faculty_members:
        member.rowspan = category_rowspan[member.category]
        category_rowspan[member.category] = 0  # Reset to avoid duplication

    # Retrieve student members
    student_members = StudentMember.objects.all()

    context = {
        'faculty_members': faculty_members,
        'student_members': student_members,
    }
    return render(request, 'user_iic_council.html', context)"""

def UserIICGlance(request):
    
    return render(request, 'user_iic_glance.html')
    
def UserIICProofUpload(request):

    return render(request, 'user_iic_proofUpload.html')

def UserSelfDriven(request):
    
    return render(request, 'user_iic_selfDriven.html')

def UserStartupCourseAvailable(request):
    
    return render(request, 'user_startup_courseAvailable.html')

def UserStartupHome(request):
    
    return render(request, 'user_startup_home.html')

def UserStartupLearning(request):
    
    return render(request, 'user_startup_myLearning.html')

def UserIICSelfdrivenForm(request):
    
    return render(request, 'user_iic_selfDriven_form.html')

def UserIICCouncil(request):
    faculty_members = FacultyMember.objects.all().order_by('sl_no')
    student_members = StudentMember.objects.all().order_by('sl_no')

    context = {
        'faculty_members': faculty_members,
        'student_members': student_members,
    }
    return render(request, 'user_iic_council.html', context)

def LoginPage(request):
    
    return render(request, 'login.html')

