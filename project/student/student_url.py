
from django.urls import path
from .views import student_view  

urlpatterns = [
    path('insert_data/', student_view.insert_data, name='insert_data'),  
    path('get_data/', student_view.get_data, name='get_data'),  
    path('get_student_data/<int:s_id>/', student_view.get_student_data, name='get_student_data'),
    path('update_student/<int:s_id>/', student_view.update_student, name='update_student'),
    path('delete_student/<int:s_id>/', student_view.delete_student, name='delete_student'),
    
]
