"""URLs Mappings for Enrollments"""

from django.urls import path
from course.rest.views.enrollment import EnrollmentList, EnrollmentDetail

urlpatterns = [
    path("", EnrollmentList.as_view(), name="enrollment-list"),
    path("/<uuid:uid>", EnrollmentDetail.as_view(), name="enrollment-detail"),
]
