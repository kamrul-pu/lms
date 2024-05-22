from django.urls import path, include

urlpatterns = [
    path("/all", include("course.rest.urls.courses"), name="courses"),
    path("/category", include("course.rest.urls.category"), name="category"),
    path("/enrollments", include("course.rest.urls.enrollment"), name="enrollment"),
]
