from django.urls import path,include
from user.api import viewsets
from rest_framework.routers import DefaultRouter
from user.api import viewsets

router = DefaultRouter()
router.register('school-staffs',viewsets.SchoolStaffApiViewSet)
router.register('admin-school-staff',viewsets.AdminSchoolStaffApiViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('login',viewsets.CreateTokenView.as_view(),name='login')
]