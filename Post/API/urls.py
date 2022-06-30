from django.contrib import admin
from django.urls import path, include
from Post.API.views import PostGet, PostCreate,PostDetail, PostById,ComentarioPost, ComentarioGet, ComentarioDetail
urlpatterns = [

    path('create/', PostCreate.as_view(), name='create'),
    path('list/', PostGet.as_view(), name='list'),
    path('list/<int:pk>', PostById.as_view(), name='post-id'),
    path('list/detail/<int:pk>', PostDetail.as_view(),name='post-detail'),

    path('comentario/create/', ComentarioPost.as_view(), name='comentario-create'),
    path('comentario/list/', ComentarioGet.as_view(), name='comentario-list'),
    path('comentario/list/<int:pk>', ComentarioDetail.as_view(), name='comentario-detail')
]
