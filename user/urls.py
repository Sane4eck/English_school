from django.urls import path, include

from user.views import UserApiView, TeacherStatusUpdateView

urlpatterns = [
    path('user/', UserApiView.as_view()),
    path('user/<int:pk>/', UserApiView.as_view()),
    path('update-teacher-status/<int:pk>/', TeacherStatusUpdateView.as_view(), name='update-teacher-status'),


]