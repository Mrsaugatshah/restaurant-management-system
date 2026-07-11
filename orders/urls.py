from django.urls import path
from . import views

urlpatterns = [
    path("tables/", views.tables_views, name="tables_view_url"),
    path("menu<table_id>/", views.menu_views, name="menu_view_url"),
]