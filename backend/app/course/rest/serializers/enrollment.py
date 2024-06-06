"""Serializers for enrollment model."""

from rest_framework import serializers
from rest_framework import status
from rest_framework.exceptions import APIException

from course.models import Enrollment


class EnrollmentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = (
            "id",
            "uid",
            "course",
            "student",
            "duration",
            "enrolled",
        )
        read_only_fields = (
            "id",
            "uid",
        )

    def validate(self, attrs):
        user = self.context.get("request").user
        course_id = attrs.get("course", None)
        enrolled = (
            Enrollment()
            .get_all_actives()
            .filter(student_id=user.id, course_id=course_id)
        )
        if enrolled.exists():
            raise serializers.ValidationError(
                detail="Student is already enrolled in this course",
                code=status.HTTP_400_BAD_REQUEST,
            )
        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["student_id"] = user.id
        return super().create(validated_data)


class EnrollmentDetailSerializer(EnrollmentListSerializer):
    class Meta(EnrollmentListSerializer.Meta):
        fields = EnrollmentListSerializer.Meta.fields + (
            "created_at",
            "updated_at",
        )
        read_only_fields = EnrollmentListSerializer.Meta.read_only_fields + ()
