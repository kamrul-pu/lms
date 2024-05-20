from django.urls import path, include

urlpatterns = [
    path("", include("course.rest.urls.courses"), name="courses"),
    path("/category", include("course.rest.urls.category"), name="category"),
]
