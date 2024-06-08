"""Serializers for enrollment model."""

from rest_framework import serializers

from course.models import Enrollment
from course.rest.serializers.courses import CourseListSerializer


class EnrollmentListSerializer(serializers.ModelSerializer):
    course = CourseListSerializer(read_only=True)
    course_id = serializers.IntegerField(
        write_only=True,
    )

    class Meta:
        model = Enrollment
        fields = (
            "id",
            "uid",
            "course",
            "course_id",
            "student",
            "duration",
            "enrolled",
        )
        read_only_fields = (
            "id",
            "uid",
        )

    def create(self, validated_data):
        user = self.context.get("request").user
        course_id = validated_data.get("course_id", None)
        enrolled = (
            Enrollment()
            .get_all_actives()
            .filter(student_id=user.id, course_id=course_id)
        )
        if enrolled.exists():
            return enrolled.first()
        enrollment = Enrollment.objects.create(
            student_id=user.id,
            course_id=course_id,
        )
        return enrollment


class EnrollmentDetailSerializer(EnrollmentListSerializer):
    class Meta(EnrollmentListSerializer.Meta):
        fields = EnrollmentListSerializer.Meta.fields + (
            "created_at",
            "updated_at",
        )
        read_only_fields = EnrollmentListSerializer.Meta.read_only_fields + ()
