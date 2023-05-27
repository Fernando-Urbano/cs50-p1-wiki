from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search", views.search, name="search"),
    path("random", views.random_entry, name="random_entry"),
    path("create", views.create_entry, name="create_entry"),
    path("save-new", views.save_new, name="save_new"),
    path("edit", views.edit_entry, name="edit_entry"),
    path("save-edit", views.save_edit, name="save_edit"),
]
