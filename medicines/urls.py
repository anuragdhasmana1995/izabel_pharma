from django.conf.urls import url
from . import views


app_name = 'medicines'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[A-Z,a-z]+)/$', views.DetailView.as_view(), name="product_list"),
]





