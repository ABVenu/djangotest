from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.blogsList, name="blogsList"),
    path("list/<int:id>/", views.blogDetails, name="blogDetails"),
]