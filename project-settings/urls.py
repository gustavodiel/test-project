from django.urls import path, include
from django.contrib import admin
import app.views, auth0.views, forms.views, tic_tac_toe.views, smart_home.views

admin.autodiscover()

urlpatterns = [
    path("", app.views.index, name="index"),
    path("tictactoe/", tic_tac_toe.views.tic_tac_toe, name="tic-tac-toe"),
    path("embed-form/", forms.views.embed_form, name="embed-form"),
    path("custom-form/", forms.views.custom_form, name="custom-form"),
    path("populate-personas/", forms.views.populate_personas, name="populate-personas"),
    path("login/", auth0.views.login, name="login"),
    path("logout/", auth0.views.logout),
    path("", include('django.contrib.auth.urls')),
    path("", include('social_django.urls')),
    path("dashboard/", smart_home.views.dashboard, name="dashboard"),
    path("settings/", smart_home.views.settings, name="settings"),
    path("join/", smart_home.views.join, name="join"),
    path("join-account/", smart_home.views.join_account, name="join-account"),
    path("create-account/", smart_home.views.create_account, name="create-account"),
    path("<str:microcontroller_token>", smart_home.views.microcontroller, name="microcontroller"),
    path("<str:microcontroller_token>/update", smart_home.views.update_microcontroller, name="update-microcontroller"),
    path("<str:microcontroller_token>/device", smart_home.views.device_settings, name="device-settings"),
    path("<str:microcontroller_token>/destroy", smart_home.views.destroy_microcontroller, name="destroy-microcontroller"),
    path("update-pins/", smart_home.views.update_device, name="update-pins"),
    path("add-microcontroller/", smart_home.views.add_microcontroller, name="add-microcontrollers"),
    path("populate-microcontroller/", smart_home.views.populate_microcontroller, name="populate-microcontroller"),
]
