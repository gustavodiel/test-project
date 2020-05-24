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
    path("trk/", app.views.trk_callback, name="rd-trk"),
    path("tictactoe/", app.views.tic_tac_toe, name="tic-tac-toe"),


    path("auth/callback/", app.views.auth_callback, name="rd-auth"),
    path("populate-personas/", app.views.populate_personas, name="populate-personas"),

    
    path("admin/", admin.site.urls)
]
