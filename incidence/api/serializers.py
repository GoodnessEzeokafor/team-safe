from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField

from drf_extra_fields.geo_fields import  PointField
from incidence.models import ( 
 	Incidence,
)

DETAIL_URL  = HyperlinkedIdentityField(
		view_name = 'incidence-api:detail',
		lookup_field = 'slug'
	)

UPDATE_URL = HyperlinkedIdentityField(
		view_name = 'incidence-api:update',
		lookup_field = 'slug'
)

class IncidenceListSerializer(ModelSerializer):
	url = DETAIL_URL
	class Meta:
		model = Incidence
		fields = [
			'id', 
			'url',
			'name',  	
			'description',
			'created', 
			'updated',	
			'location', 
		]

#incidence Create Serializer
class IncidenceCreateSerializer(ModelSerializer):
	location = PointField()
	class Meta:
		model = Incidence
		fields = [
		'name',
		'description',
		'created',
		'location',
		]



# Incidence Detail Serializer
class IncidenceDetailSerializer(ModelSerializer):
	update_url = UPDATE_URL
	class Meta:
		model 	= Incidence
		fields 	=[
			'id',
			'update_url'
			'name',
			'slug',
			'description',
			'created',
			'updated',
			'location',
		]



# class StateSerializer(ModelSerializer):
# 	class Meta:
# 		model 	= State
# 		fields 	= [
# 			'id_0', 
# 			'iso',	
# 			'name_0', 
# 			'id_1',  
# 			'name_1', 
# 			'hasc_1', 
# 			'ccn_1', 
# 			'cca_1', 	
# 			'type_1' ,	
# 			'engtype_1', 
# 			'nl_name_1', 
# 			'varname_1', 
# 			'geom',
				   	
# 		]

	# class IncidenceDetailSerializer(ModelSerializer):
	# 	class Meta:
	# 		model 	= Incidence
	# 		fields 	=[
	# 			'id',
	# 			'name',
	# 			'slug',
	# 			'description',
	# 			'created',
	# 			'updated',
	# 			'location',
	# 		]

# # Incidence Update Serializer
# class IncidenceUpdateSerializer(ModelSerializer):
# 	class Meta:
# 		model = Incidence
# 		fields = []

# class IncidenceDestroySerializer(ModelSerializer):
# 	pass

# Inclidence Delete Serializer