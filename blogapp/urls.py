from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('blogs/', views.BlogListView, name='blogs'),
    path('blog/<int:_id>', views.BlogDetailView, name='blog'),
]
