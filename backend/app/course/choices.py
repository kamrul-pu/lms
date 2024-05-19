from django.db.models import TextChoices


class CourseLevel(TextChoices):
    BEGINNER = "BEGINEER", "Beginner"
    INTERMEDIATE = "Intermediate", "Intermediate"
    ADVANCED = "ADVANCED", "Advanced"
    UNDEFINED = "UNDEFINED", "Undefined"


class CourseStatus(TextChoices):
    PUBLISHED = "PUBLISHED", "Published"
    DRAFT = "DRAFT", "Draft"
