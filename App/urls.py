from django.conf.urls import url
from .views import RestaurantView, RestaurantDetailsView
from .views import MenuView, MenuDetailsView

urlpatterns = [
    url(r'^$', RestaurantView.as_view()),
    url(r'^(?P<pk>[0-9]+)', RestaurantDetailsView.as_view()),
    url(r'^menu/$', MenuView.as_view()),
    url(r'^menu/(?P<pk>[0-9]+)', MenuDetailsView.as_view()),
]