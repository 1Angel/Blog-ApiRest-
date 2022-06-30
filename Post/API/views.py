from Post.API.serializers import PostSerializer, ComentarioSerializer
from Post.models import Post, Comentarios
from rest_framework import generics
from rest_framework import permissions
from Post.API.pagination import paginacion
from rest_framework import filters

from Post.API.permissions import IsOwner, IsPostUser

#post
class PostCreate(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

class PostGet(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = paginacion

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']


class PostById(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsPostUser, permissions.IsAuthenticated]


#Comentarios
class ComentarioPost(generics.CreateAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class ComentarioGet(generics.ListAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer
    pagination_class = paginacion

class ComentarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comentarios.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [IsOwner, permissions.IsAuthenticated]