from django.shortcuts import render
from django.views.generic import TemplateView
from  .models import State, Incidence
from django.http import HttpResponse
from django.core.serializers import serialize

 # Create your views here.



class HomePage(TemplateView):
	template_name = 'index.html'


def State_datasets(request):
	#State has an attribute objects
	state = serialize('geojson', State.objects.all())
	return HttpResponse(state, content_type="json")

def Incidence_datasets(request):
	#Incidence has an attribute Object which we defined
	incidence = serialize('geojson', Incidence.Object.all())
	return HttpResponse(incidence, content_type="json")
