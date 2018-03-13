from django.conf.urls import url, include
from django.contrib import admin
from medicines import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^medicines/', include('medicines.urls')),
]
