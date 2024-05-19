"""Course Related Models."""

from django.db import models
from django.utils import timezone

from versatileimagefield.fields import VersatileImageField

from common.models import BaseModelWithUID, NameSlugDescriptionBaseModel
from course.choices import CourseLevel, CourseStatus
from course.utils import get_media_path_prefix


class Category(NameSlugDescriptionBaseModel):
    image = VersatileImageField(
        "Category_Image",
        upload_to="categories",
        blank=True,
    )
    icon_class = models.CharField(
        max_length=50,
    )
    serial_number = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.name} - {self.icon_class}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Course(NameSlugDescriptionBaseModel):
    sub_title = models.CharField(
        max_length=200,
    )
    image = VersatileImageField(
        "Course_Image",
        upload_to="courses",
        blank=True,
    )
    instructor = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="instructor_courses",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name="category_courses",
    )
    level = models.CharField(
        choices=CourseLevel,
        max_length=20,
        default=CourseLevel.UNDEFINED,
    )
    course_status = models.CharField(
        choices=CourseStatus,
        max_length=20,
        default=CourseStatus.DRAFT,
    )
    duration = models.DurationField(
        null=True,
        blank=True,
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )
    discount_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=0.0,
    )
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.0,
    )

    def calculate_discounted_price(self):
        discount_amount = (self.discount_percentage / 100) * self.price
        discounted_price = self.price - discount_amount
        return max(discounted_price, 0)

    def save(self, *args, **kwargs):

        self.total_price = self.calculate_discounted_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.slug}"

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Enrollment(BaseModelWithUID):
    course = models.ForeignKey(
        Course,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="course_enrollments",
    )
    student = models.ForeignKey(
        "core.User",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="student_enrollments",
    )
    duration = models.DurationField(
        default=timezone.timedelta(days=365),
    )
    enrolled = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Enrollment"
        verbose_name_plural = "Enrollments"

    def __str__(self):
        # return f"{self.user.username} enrolled in {self.course.title}"
        return f"{self.student.first_name} enrolled in {self.course.name}"


class Lesson(NameSlugDescriptionBaseModel):
    serial_number = models.PositiveIntegerField()
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="course_lessons",
    )

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"


class Video(NameSlugDescriptionBaseModel):
    serial_number = models.PositiveIntegerField()
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        related_name="lesson_videos",
    )
    video_file = models.FileField(upload_to=get_media_path_prefix)
    duration = models.DurationField(
        blank=True,
        null=True,
    )
    preview = models.BooleanField(default=False)

    def __str__(self):
        return {self.name}
