from django.db import models
# from datetime import datetime
from django.utils import timezone
# from django.db.models import Manager as GeoManager

from django.contrib.gis.db import models as gis_models

# importing slugify to slugify the urls
from django.utils.text import slugify
from django.urls import reverse #
from django.db.models.signals import pre_save

# Create your models here.


class Incidence(gis_models.Model):
	name  		= gis_models.CharField(max_length=200, help_text='Nature Of Incidence', blank=False)
	slug        = gis_models.SlugField(unique=True)
	description = gis_models.TextField(help_text='Write a description', blank=False)
	created 	= gis_models.DateField(auto_now_add=True)
	updated 	= gis_models.DateTimeField(auto_now=True)
	location 	= gis_models.PointField(srid=4326)
	objects 	= gis_models.Manager()

	def __str__(self):
		return str(self.name)




	def get_absolute_url(self):
		return reverse('incidence:incidence-detail', kwargs={"slug":self.slug})


def create_slug(instance, new_slug=None):
	slug  = slugify(instance.name)
	if new_slug is not None:
		slug  = new_slug
	qs = Incidence.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug  = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug	

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver,sender=Incidence)
	


