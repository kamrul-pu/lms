"""Serailizers for Course Model."""

"""Serializers for category model."""

from rest_framework import serializers

from core.rest.serializers.user import UserListSerializer

from course.rest.serializers.category import CategoryListSerializer
from course.models import Course


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = (
            "id",
            "uid",
            "name",
            "slug",
            "sub_title",
            "image",
            "category",
            "instructor",
            "level",
            "duration",
            "price",
            "discount_percentage",
            "total_price",
        )
        read_only_fields = (
            "id",
            "uid",
        )

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["entry_by_id"] = user.id
        return super().create(validated_data)


class CourseDetailSerializer(CourseListSerializer):
    instructor = UserListSerializer()
    category = CategoryListSerializer()

    class Meta(CourseListSerializer.Meta):
        fields = CourseListSerializer.Meta.fields + (
            "description",
            "image",
            "created_at",
        )

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        instance.updated_by_id = user.id
        return super().update(instance, validated_data)
