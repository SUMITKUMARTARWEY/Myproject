from django.conf.urls import url,include
from .views import user,city,university,country,provider,facility

from django.conf.urls.static import static

urlpatterns =[
			url(r'^user/list/$',user.list.as_view(),name='user_list'),			
			url(r'^user/show/(?P<pk>[0-9]+)$',user.show.as_view(),name="user_show"),
			url(r'^country/list/',country.list.as_view(),name='country_list'),
			url(r'country/show/(?P<pk>[0-9]+)$',country.show.as_view(),name='country_show'),
			url(r'^city/list/$',city.list.as_view(),name='city_list'),			
			url(r'^city/show/(?P<pk>[0-9]+)$',city.show.as_view(),name="city_show"),
			url(r'^university/list/',university.list.as_view(),name='trip_list'),
			url(r'^university/show/(?P<pk>[0-9]+)$',university.show.as_view(),name='trip_show'),
			url(r'^provider/list/',provider.list.as_view(),name='trip_list'),
			url(r'^provider/show/(?P<pk>[0-9]+)$',provider.show.as_view(),name='trip_show'),
			url(r'^facility/list/',facility.list.as_view(),name='trip_list'),
			url(r'^facility/show/(?P<pk>[0-9]+)$',facility.show.as_view(),name='trip_show'),
			]

