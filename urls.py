from django.conf.urls.defaults import *
from importexport.views import *

# users need to be logged in
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('importexport.views',
  url(r'^$', login_required(importexport_index), name="index_importexport"),
  url(r'^database/export/', login_required(export_database), name="export_database"),
  url(r'^database/import/', login_required(import_database), name="import_database"),
  url(r'^media/export/', login_required(export_media), name="export_mediaroot"),
)

