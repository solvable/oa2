from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
from PIL import Image
import os
# Create your models here.

class Project(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete="CASCADE")
    nickname = models.CharField(max_length=100)
    carMake = models.CharField(max_length=20, blank=True)
    carModel = models.CharField(max_length=50, blank=True)
    carYear = models.CharField(max_length=4, blank=True)
    stereoMake = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)
    featuredImage = models.ImageField(upload_to='photos/%Y/%m/%d', default='/static/img/project.jpg')
    thumbImage = models.ImageField(upload_to='photos/%Y/%m/%d', default='/static/img/project.jpg', blank=True)

    slug = models.SlugField(max_length=50, blank=True)


    def save(self, *args, **kwargs):
        super(Project, self).save()
        thumbSize = (400,300)
        featuredSize = (800,600)
        slug = slugify(self.nickname)

        # resize image and save a thumbnail
        file = self.featuredImage.path
        thumbfile = self.thumbImage.path

        thumb = Image.open(thumbfile)
        featuredImage = Image.open(file)

        featuredImage = image.resize(featuredSize, Image.ANTIALIAS)
        thumb= image.thumbnail(thumbSize, Image.ANTIALIAS)
        self.thumbImage.path =  thumb.save()
        self.featuredImage.path = featuredImage.save()

        super(Project, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.slug)

    def __str__(self):
        return str(self.slug)

    # def get_absolute_url(self):
    #     return reverse("project_detail", kwargs={"id": self.id})
    #
    # def edit_url(self):
    #     return reverse("project_edit", kwargs={"id":self.id})
    #
    class Meta:
     ordering = ["-created", "-modified"]

class ProjectImages(models.Model):

    project = models.ForeignKey(Project, related_name='images', on_delete="CASCADE")
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    isFeatured = models.BooleanField(default=False)