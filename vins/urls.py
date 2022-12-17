# articles/urls.py
from django.urls import path, reverse_lazy, reverse

from . import views

app_name = 'vins'

urlpatterns = [
    path('new/', views.VinCreateView.as_view(), name='vin_new'),  # new
    path('<slug:slug>/edit/', views.VinUpdateView.as_view(), name='vin_edit'),
    path('<slug:slug>/delete/', views.VinDeleteView.as_view(), name='vin_delete'),  # new

    path('<slug:slug>/', views.VinDetailView.as_view(), name='vin_detail'),
    path('', views.VinListView.as_view(), name='vin_list'),
]

# vins/(?P<slug>[-a-zA-Z0-9_]+)/comment/(?P<pk>[0-9]+)/delete$
urlpatterns += [  
    path('<slug:slug>/comment/', views.CommentCreateView.as_view(), name='vin_comment_create'),
    path('comment/<int:pk>/delete', views.CommentDeleteView.as_view(), name='vin_comment_delete'),
]

urlpatterns += [     
    path('category/', views.CategoryListView.as_view(), name='category_list'),  
    path('category/<slug:slug>/', views.CategoryDetailView.as_view(), name='category_detail'),    
]

urlpatterns += [ 
    path('tag/', views.TagListView.as_view(), name='tag_list'), 
    path('tag/<slug:slug>/', views.TagDetailView.as_view(), name='tag_detail'),    
]

urlpatterns += [ 
    path('<int:pk>/favorite', views.AddFavoriteView.as_view(), name='vin_favorite'),
    path('<int:pk>/unfavorite', views.DeleteFavoriteView.as_view(), name='vin_unfavorite'),
]

urlpatterns += [
    path('', views.ServiceWorker.as_view(), name="sw"),
]
