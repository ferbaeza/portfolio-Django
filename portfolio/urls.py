from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns=[
    path('<int:project_id>', views.preview_project, name='preview_project'),
]