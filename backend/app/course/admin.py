"Add Course related models in the admin panel"

from django.contrib import admin


from course.models import Category, Course, Enrollment, Lesson, Video


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "name",
        "icon_class",
        "serial_number",
    )


admin.site.register(Category, CategoryAdmin)


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "name",
        "level",
        "course_status",
    )


admin.site.register(Course, CourseAdmin)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "duration",
        "enrolled",
    )


admin.site.register(Enrollment, EnrollmentAdmin)


class LessonAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "serial_number",
    )


admin.site.register(Lesson, LessonAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "uid",
        "serial_number",
        "preview",
    )


admin.site.register(Video, VideoAdmin)
