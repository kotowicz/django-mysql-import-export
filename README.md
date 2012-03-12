# 0) this is version 0.1 of my django mysql import / export app.

# 1) clone this directory and rename it to 'importexport'

# 2) configure settings.py file:

```
INSTALLED_APPS = (
    ...
    'importexport',
)
```

# path to mysqldump program?

```
MYSQLDUMP = "/usr/local/bin/mysqldump"
```

# 3) configure urls.py file:

```
urlpatterns += patterns('',
    # this url line needs to come before the admin line!
    (r'^admin/import-export/', include('importexport.urls')),
    (r'^admin/', include(admin.site.urls)),
)
```
