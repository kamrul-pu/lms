"""Views Related to Enrollment."""

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from course.models import Enrollment

from course.rest.serializers.enrollment import (
    EnrollmentListSerializer,
    EnrollmentDetailSerializer,
)


class EnrollmentList(ListCreateAPIView):
    queryset = Enrollment().get_all_actives()
    permission_classes = (IsAuthenticated,)
    serializer_class = EnrollmentListSerializer

    def get_queryset(self):
        queryset = self.queryset
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return queryset
        return queryset.filter(student_id=user.id)


class EnrollmentDetail(RetrieveUpdateDestroyAPIView):
    queryset = Enrollment().get_all_actives()
    permission_classes = (IsAdminUser,)
    serializer_class = EnrollmentDetailSerializer
    lookup_field = "uid"
