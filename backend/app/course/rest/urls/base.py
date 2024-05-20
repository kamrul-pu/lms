from django.urls import path, include

urlpatterns = [
    path("/category", include("course.rest.urls.category"), name="category"),
]
