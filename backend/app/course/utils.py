"""Utils functions for course app."""


# Media File Prefixes
def get_media_path_prefix(instance, filename):
    return f"videos/{instance.lesson.course.slug}/{instance.slug}/{filename}"
