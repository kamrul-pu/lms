"""URLs Mappings for courses."""

from django.urls import path

from course.rest.views.courses import CourseList, CourseDetail


urlpatterns = [
    path("", CourseList.as_view(), name="course-list"),
    path("/<slug:slug>", CourseDetail.as_view(), name="course-detail"),
]
