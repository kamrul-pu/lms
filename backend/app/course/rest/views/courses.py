"""Views related to Course model"""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.permissions import IsAdminUser, IsAuthenticated

from course.rest.serializers.courses import CourseListSerializer, CourseDetailSerializer
from course.models import Course, Category


class CourseList(ListCreateAPIView):
    queryset = Course().get_all_actives()
    serializer_class = CourseListSerializer
    permission_classes = ()

    def get_queryset(self):
        queryset = self.queryset
        name: str = self.request.query_params.get("name", None)
        category_name: str = self.request.query_params.get("category", None)
        if category_name:
            category = Category.objects.filter(name__icontains=category_name).first()
        if category_name and category:
            queryset = queryset.filter(category_id=category.id)
        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsAuthenticated(),)
        return (IsAdminUser(),)


class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset = Course().get_all_actives().select_related("category", "instructor")
    serializer_class = CourseDetailSerializer
    permission_classes = ()
    lookup_field = "slug"

    def get_permissions(self):
        if self.request.method == "GET":
            return (IsAuthenticated(),)
        return (IsAdminUser(),)
