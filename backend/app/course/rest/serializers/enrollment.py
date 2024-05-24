"""Serializers for enrollment model."""

from rest_framework import serializers

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
