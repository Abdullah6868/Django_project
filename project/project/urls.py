# urls.py (project's main urls.py)
from django.contrib import admin
from django.urls import path, include
from student.views.student_view import StudentView 
from student.views.education_history_view import EductionHistoryView
from student.views.certificate_view import CertificateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', StudentView.as_view(), name='student_all'),
    path('student/<int:s_id>/', StudentView.as_view(), name= 'student_detail'),

    # path('student/education_history/', EductionHistoryView.as_view(), name= 'all_student_eductaion_detail'),
    path('student/education_history/<int:s_id>', EductionHistoryView.as_view(), name= 'student_eductaion_detail'),
    path('student/<int:s_id>/education_history/<int:e_id>', EductionHistoryView.as_view(), name= 'student_eductaion_detail'),
   
    # path('student/certificate/', CertificateView.as_view(), name= 'all_student_eductaion_detail'),
    path('student/certificate/<int:s_id>', CertificateView.as_view(), name= 'student_certificate_detail'),
    path('student/<int:s_id>/certificate/<int:c_id>', CertificateView.as_view(), name= 'student_certificate_detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
