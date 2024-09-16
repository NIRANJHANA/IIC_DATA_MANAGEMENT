from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('',LoginPage),
    path('UserHome/', UserHome),
    path('UserEdcHome/',UserEdcHome),
    path('UserEdcCourse/',UserEdcCourse),
    path('UserEdcLearning/',UserEdcLearning),
    path('UserIICAbout/',UserIICAbout),
    path('UserIICAchievements/',UserIICAchievements),
    path('UserIICActivity/',UserIICActivity),
    path('UserIICCouncil/',views.UserIICCouncil, name='council'),
    path('UserIICGlance/',UserIICGlance),
    path('UserIICProofUpload/',UserIICProofUpload),
    path('UserSelfDriven/',UserSelfDriven),
    path('UserStartupCourseAvailable/',UserStartupCourseAvailable),
    path('UserStartupHome/',UserStartupHome),
    path('UserStartupLearning/',UserStartupLearning),
    path('UserIICSelfdrivenForm/',UserIICSelfdrivenForm),
    path('AdminDashboard/', AdminDashboard),
    path('AdminReviewers/', AdminReviewers),
    path('AdminDepartments/', AdminDepartments),
    path('AdminSpecialLab/', AdminSpecialLab),
    path('AdminClubs/', AdminClubs),
    path('AdminEvents/', AdminEvents),
    path('Proof/',event_create_view),
    path('UserIICCreateEventForm/',UserIICCreateEventForm),
    path('superadmin-dashboard/', superadmin_dashboard, name='superadmin_dashboard'),
]