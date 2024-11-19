# urls.py (project's main urls.py)
from django.contrib import admin
from django.urls import path, include
from student.views.student_view import StudentView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('student/', include('student.student_url')),
    path('student/', StudentView.as_view(), name='student_all'),
    path('student/<int:s_id>/', StudentView.as_view(), name= 'student_detail')
]
