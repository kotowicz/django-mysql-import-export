# A) ABOUT

This is version 0.1 of my simple django mysql import / export app. 

# B) SETUP

* clone this directory and rename it to 'importexport'
* configure settings.py file
** add application to `INSTALLED_APPS`

```
INSTALLED_APPS = (
    ...
    'importexport',
)
```

** set path to mysqldump program:

```
MYSQLDUMP = "/usr/local/bin/mysqldump"
```

* configure urls.py file:

```
urlpatterns += patterns('',
    # this url line needs to come before the admin line!
    (r'^admin/import-export/', include('importexport.urls')),
    (r'^admin/', include(admin.site.urls)),
)
```

