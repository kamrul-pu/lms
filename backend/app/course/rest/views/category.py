"""Views for category model"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from course.models import Category
from course.rest.serializers.category import (
    CategoryListSerializer,
    CategoryDetailSerializer,
)


class CategoryList(ListCreateAPIView):
    permission_classes = ()
    serializer_class = CategoryListSerializer
    queryset = Category().get_all_actives()

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsAuthenticated(),)
        return (IsAdminUser(),)

    def get_queryset(self):
        queryset = self.queryset
        name = self.request.query_params.get("name", None)
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = ()
    serializer_class = CategoryDetailSerializer
    queryset = Category().get_all_actives()
    lookup_field = "slug"

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsAuthenticated(),)
        return (IsAdminUser(),)
