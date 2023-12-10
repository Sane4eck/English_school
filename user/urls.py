from django.urls import path
from user.views import UserApiView, TeacherStatusUpdateView, UserCreateApiView

urlpatterns = [
    path('user/', UserApiView.as_view()),
    path('user-registration/', UserCreateApiView.as_view()),
    path('user/<int:pk>/', UserApiView.as_view()),
    path('update-teacher-status/<int:pk>/', TeacherStatusUpdateView.as_view(), name='update-teacher-status'),
]
