
from django.urls import path ,include
from .views import student_view  
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('student/', include('student.urls')),
    # path('insert_data/', student_view.insert_data, name='insert_data'),  
    # path('get_data/', student_view.get_data, name='get_data'),  
    # path('get_student_data/<int:s_id>/', student_view.get_student_data, name='get_student_data'),
    # path('update_student/<int:s_id>/', student_view.update_student, name='update_student'),
    # path('delete_student/<int:s_id>/', student_view.delete_student, name='delete_student'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
