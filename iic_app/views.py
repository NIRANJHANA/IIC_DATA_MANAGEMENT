from django.shortcuts import render

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

def UserIICCouncil(request):
    
    return render(request, 'user_iic_council.html')

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

