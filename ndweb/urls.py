from django.conf.urls.defaults import *
from ndweb.views import main_page

urlpatterns = patterns('',
   (r'^$', main_page),
)