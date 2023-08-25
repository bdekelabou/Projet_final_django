from django.urls import path
from . import views

from . import views

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('download_submitted_project/<int:assignment_id>/', views.download_submitted_project, name='download_submitted_project'),
    path('upload_project/', views.upload_project, name='upload_project'),
    path('upload_project/', views.upload_project, name='upload_project'),
    path('upload_processed_project/', views.upload_processed_project, name='upload_processed_project'),
    path('upload_project/', views.upload_project, name='upload_project'),

]
