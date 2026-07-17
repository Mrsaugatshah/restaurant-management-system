from django.urls import path
from . import views

urlpatterns = [
    path("tables/", views.tables_views, name="tables_view_url"),
    path("menu/<int:table_id>/", views.menu_views, name="menu_view_url"),
    path("kitchen/dashboard/", views.kitchen_dashboard_view, name="kitchen_dashboard_view_url"),
]