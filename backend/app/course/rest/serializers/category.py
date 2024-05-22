"""Serializers for category model."""

from rest_framework import serializers


from course.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    total_courses = serializers.IntegerField(
        read_only=True,
    )

    class Meta:
        model = Category
        fields = (
            "id",
            "uid",
            "name",
            "slug",
            "image",
            "description",
            "icon_class",
            "serial_number",
            "total_courses",
        )
        read_only_fields = (
            "id",
            "uid",
        )

    def create(self, validated_data):
        user = self.context.get("request").user
        validated_data["entry_by_id"] = user.id
        return super().create(validated_data)


class CategoryDetailSerializer(CategoryListSerializer):
    class Meta(CategoryListSerializer.Meta):
        fields = CategoryListSerializer.Meta.fields + ("created_at",)

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        instance.updated_by_id = user.id
        return super().update(instance, validated_data)
