from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name = 'home'),
    path('book/new/', views.book_create, name='book_create'),
    path('book/list/', views.book_list, name='book_list'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('book/<int:id>/edit', views.book_update, name='book_update'),
    path('book/<int:id>/delete', views.book_delete, name='book_delete')
]
