# articles/urls.py
from django.urls import path

from .views import (
    VinCreateView,
    VinUpdateView,
    VinDeleteView,
    VinDetailView,
    VinListView,
    CommentDeleteView,
    CategoryListView,
    CategoryDetailView,
    TagListView,
    TagDetailView,
    AddFavoriteView,
    DeleteFavoriteView,
    ServiceWorker,
    stream_file,
)

app_name = 'vins'

urlpatterns = [
    path('new/', VinCreateView.as_view(), name='vin_new'),  # new
    path('<int:pk>/edit/', VinUpdateView.as_view(), name='vin_edit'),
    path('<int:pk>/delete/', VinDeleteView.as_view(), name='vin_delete'),
    path('<slug:slug>/', VinDetailView.as_view(), name='vin_detail'),
    path('post_image/<int:pk>', stream_file, name='post_image'),  # Pic image
    path('', VinListView.as_view(), name='vin_list'),
]

urlpatterns += [
    path('<slug:slug>/comment/', VinDetailView.as_view(), name='vin_comment_create'),
    path('comment/<int:pk>/delete', CommentDeleteView.as_view(), name='vin_comment_delete'),
]

urlpatterns += [
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]

urlpatterns += [
    path('tag/', TagListView.as_view(), name='tag_list'),
    path('tag/<slug:slug>/', TagDetailView.as_view(), name='tag_detail'),
]

urlpatterns += [
    path('<int:pk>/favorite', AddFavoriteView.as_view(), name='vin_favorite'),
    path('<int:pk>/unfavorite', DeleteFavoriteView.as_view(), name='vin_unfavorite'),
]

urlpatterns += [
    path('', ServiceWorker.as_view(), name="sw"),
]
