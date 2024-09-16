from django.shortcuts import render, redirect
from .models import FacultyMember, StudentMember
from .forms import *
from django.db.models import Count
from collections import defaultdict
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import User
import requests

def event_create_view(request):
    if request.method == "POST":
        event_form = EventForm(request.POST)
        proof_forms = [EventProofForm(request.POST, request.FILES, prefix=str(i)) for i in range(10)]  # For 10 proofs

        if event_form.is_valid() and all([pf.is_valid() for pf in proof_forms]):
            event = event_form.save()

            # Save proofs
            for proof_form in proof_forms:
                proof = proof_form.save(commit=False)
                proof.event = event
                proof.uploaded_by = request.user
                proof.save()

            return redirect('event_list')  # or any success URL

    else:
        event_form = EventForm()
        proof_forms = [EventProofForm(prefix=str(i)) for i in range(10)]

    return render(request, 'user_iic_proofUpload.html', {'event_form': event_form, 'proof_forms': proof_forms})

def UserIICCreateEventForm(request):
    return render(request, 'admin_iic_createEvent.html')

'''def verify_google_token(token):
    try:
        response = requests.get(f"https://oauth2.googleapis.com/tokeninfo?id_token={token}")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        # Handle request exceptions
        print(f"Error verifying token: {e}")
        return {}
'''

'''def determine_user_type(email):
    # Implement your logic to determine user type based on email or other criteria
    if 'example.com' in email:
        return 'admin'
    else:
        return 'user'
'''

'''
def google_signin(request):
    token = request.POST.get('id_token')
    user_info = verify_google_token(token)
    email = user_info.get('email')

    # Get or create the user
    user, created = User.objects.get_or_create(username=email, defaults={'email': email})

    if created:
        # Determine user type based on your logic
        user_type = determine_user_type(email)
        User.objects.create(user=user, user_type=user_type)
    else:
        # Update user profile if needed
        user_profile = User.objects.get(user=user)
        if not user_profile.user_type:
            user_type = determine_user_type(email)
            user_profile.user_type = user_type
            user_profile.save()

    # Authenticate the user
    user = authenticate(request, username=email)
    if user:
        login(request, user)
        # Redirect based on user type
        user_profile = User.objects.get(user=user)
        if user_profile.user_type == 'admin':
            return redirect('/admin-dashboard')
        elif user_profile.user_type == 'superadmin':
            return redirect('/superadmin-dashboard')
        elif user_profile.user_type == 'reviewer':
            return redirect('/reviewer-dashboard')
        else:
            return redirect('/UserHome')
    else:
        # If authentication fails, redirect to login
        return redirect('/login')

'''

'''def user_dashboard(request):
    user_profile = User.objects.get(user=request.user)
    if user_profile.user_type == 'admin':
        return render(request, 'admin_iic_home.html')
    elif user_profile.user_type == 'superadmin':
        return render(request, 'superadmin_dashboard.html')
    elif user_profile.user_type == 'reviewer':
        return render(request, 'reviewer_dashboard.html')
    else:
        return render(request, 'user_home.html')
'''

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


def admin_dashboard(request):
    # Logic for the admin dashboard
    return render(request, 'admin_dashboard.html')

def superadmin_dashboard(request):
    # Logic for the superadmin dashboard
    return render(request, 'superadmin_dashboard.html')

def AdminDashboard(request):
    
    return render(request, 'admin_iic_dashboard.html')

def AdminReviewers(request):
    
    return render(request, 'admin_iic_reviewers.html')

def AdminDepartments(request):
    
    return render(request, 'admin_iic_departments.html')

def AdminSpecialLab(request):
    
    return render(request, 'admin_iic_slb.html')

def AdminClubs(request):
    
    return render(request, 'admin_iic_clubs.html')

def AdminEvents(request):
    
    return render(request, 'admin_iic_events.html')