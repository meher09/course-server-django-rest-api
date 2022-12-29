from django.db import models

# Create your models here.


class Course(models.Model):
    title = models.CharField(verbose_name='Course Name', max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    enrollment = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Milestone(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='course',
    )

    title = models.CharField(verbose_name='Milestone Name', max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    assignement = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Module(models.Model):
    milestone = models.ForeignKey(
        Milestone, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='Module Name', max_length=100)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    module = models.ForeignKey(
        Module, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(verbose_name='Video Title', max_length=100)
    yotube_link = models.CharField(
        verbose_name="Youtube Video", max_length=100)
    duration = models.FloatField(null=True, blank=True)
    created = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=250)
    designation = models.CharField(max_length=150)
    facebook = models.URLField(max_length=200)
    image = models.URLField(max_length=250)

    def __str__(self):
        return self.name



class AllowedUser(models.Model):
    email = models.CharField(max_length=255, unique=True)
    facebook_id = models.CharField(max_length=255, unique=True)
    
    def __str__(self):
        return self.email
