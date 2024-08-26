from django.urls import path
from .views import *
from . import views


urlpatterns = [
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
    path('',LoginPage),
]