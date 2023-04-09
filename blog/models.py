import os
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import User


# to validate if the uploaded photo is .jpg or .png
def validate_file_extension(value):
    # getting file's extension
    ext = os.path.splitext(value.name)[1]
    valid_extensions = [".jpg", ".png"]

    if not ext.lower() in valid_extensions:
        raise ValidationError("Unsupported file extension. ")


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.FileField(upload_to='files/user_avatar/', null=True, blank=True,
                              validators=[validate_file_extension])
    description = models.CharField(max_length=512, null=False, blank=False)

    def __str__(self):
        return self.user.username


class Article(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/article_cover/', null=False, blank=False,
                             validators=[validate_file_extension])
    content = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128, null=False, blank=False)
    cover = models.FileField(upload_to='files/category_cover/', null=False, blank=False,
                             validators=[validate_file_extension])

    def __str__(self):
        return self.title
