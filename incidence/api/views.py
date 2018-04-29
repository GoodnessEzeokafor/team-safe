'''
	In views.py I will create all the views related to the api
'''
from django.db.models import Q  
from rest_framework.generics import (
	CreateAPIView,
	DestroyAPIView,
	ListAPIView,
	UpdateAPIView,
	RetrieveAPIView,
	RetrieveUpdateAPIView,


) 
# generic view
from .serializers import(
	IncidenceCreateSerializer,
 	IncidenceListSerializer,
 	IncidenceDetailSerializer,

)

from rest_framework.filters import (
	SearchFilter,
	OrderingFilter
)

#rest framework permissions
from rest_framework.permissions import (
	AllowAny,
	IsAuthenticated,
	IsAdminUser,
	IsAuthenticatedOrReadOnly
)


# getting the database model defined in incidence/models
from incidence.models import (
	Incidence,
)

# add paginations
from .pagination import IncidencePageNumberPagination

# rest  incidence create view
class IncidenceCreateApiView(CreateAPIView):
	queryset = Incidence.objects.all()
	serializer_class = IncidenceCreateSerializer


# rest detail view
class IncidenceDetailApiView(RetrieveAPIView):
	queryset  = Incidence.objects.all()
	serializer_class = IncidenceDetailSerializer
	lookup_field  = 'slug'


# rest incidence delete view
class IncidenceDeleteApiView(DestroyAPIView):
	queryset = Incidence.objects.all()
	serializer_class = IncidenceDetailSerializer
	lookup_field = 'slug'
	permission_classes = [
		IsAuthenticated,
		IsAdminUser
	]


# rest incidence list view
class IncidenceListApiView(ListAPIView):
	'''
		For The Incidence Model
	'''
	queryset = Incidence.objects.all()
	serializer_class = IncidenceListSerializer
	filter_backends = [SearchFilter]
	search_fields 	= ['name',]
	pagination_class = IncidencePageNumberPagination

	def get_queryset(self, *args, **kwargs):
		'''
			Creating a query search filter
		'''
		queryset_list =Incidence.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset_list = queryset_list.filter(
				Q(name__icontains=query)|
				Q(description__contains=query)
			).distinct()

		return queryset_list



# rest incidence update view	
class IncidenceUpdateApiView(RetrieveUpdateAPIView):
	queryset = Incidence.objects.all()
	serializer_class = IncidenceDetailSerializer
	lookup_field = 'slug'
	permission_classes = [
		IsAuthenticated,
		IsAdminUser
	]

	# def perform_update(self, serializer):
	# 	serializer.save(user=self.request.user)

# class StateListApiView(ListAPIView):
# 	'''
# 		For The State Model
# 	'''
# 	queryset = State.objects.all()
# 	serializer_class = StateSerializer



# # re state detail view
# class StateDetailApiView(RetrieveAPIView):
# 	queryset = State.objects.all()
# 	serializer_class = StateSerializer
# 	