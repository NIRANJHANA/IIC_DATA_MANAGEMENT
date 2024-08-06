from django.urls import path
from .views import *

urlpatterns = [
    path('UserHome/', UserHome),
    path('UserEdcHome/',UserEdcHome),
    path('UserEdcCourse/',UserEdcCourse),
    path('UserEdcLearning/',UserEdcLearning),
    path('UserIICAbout/',UserIICAbout),
    path('UserIICAchievements/',UserIICAchievements),
    path('UserIICActivity/',UserIICActivity),
    path('UserIICCouncil/',UserIICCouncil),
    path('UserIICGlance/',UserIICGlance),
    path('UserIICProofUpload/',UserIICProofUpload),
    path('UserSelfDriven/',UserSelfDriven),
    path('UserStartupCourseAvailable/',UserStartupCourseAvailable),
    path('UserStartupHome/',UserStartupHome),
    path('UserStartupLearning/',UserStartupLearning),
]