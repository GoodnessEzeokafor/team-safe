# add pagination
from rest_framework.pagination import(
	LimitOffsetPagination,
	PageNumberPagination,
)



class PageLimitOffsetPagination(LimitOffsetPagination):
	default = 4
	default_limit = 10
	

class IncidencePageNumberPagination(PageNumberPagination):
	page_size = 2
	