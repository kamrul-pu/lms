"""URLs mappings for category."""

from django.urls import path


from course.rest.views.category import CategoryList, CategoryDetail


urlpatterns = [
    path("", CategoryList.as_view(), name="category-list"),
    path("/<slug:slug>", CategoryDetail.as_view(), name="category-detail"),
]
