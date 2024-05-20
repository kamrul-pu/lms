"""Serializers for category model."""

from rest_framework import serializers


from course.models import Category


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "id",
            "uid",
            "name",
            "slug",
            "description",
            "icon_class",
            "serial_number",
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
        fields = CategoryListSerializer.Meta.fields + (
            "image",
            "created_at",
        )

    def update(self, instance, validated_data):
        user = self.context.get("request").user
        instance.updated_by_id = user.id
        return super().update(instance, validated_data)
