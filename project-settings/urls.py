from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import app.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
urlpatterns = [
    path("", app.views.index, name="index"),
    path("cta/", app.views.cta, name="cta"),
    path("custom-form/", app.views.custom_form, name="custom-form"),
    path("html-model/", app.views.template, name="test"),
    path("db/", app.views.db, name="db"),
    path("admin/", admin.site.urls),
]