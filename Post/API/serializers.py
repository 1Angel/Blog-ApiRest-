from rest_framework import  serializers

from Post.models import Post, Comentarios

class ComentarioSerializer(serializers.ModelSerializer):
    usuario = serializers.StringRelatedField(source='user.username', read_only=True)
    class Meta:
        model = Comentarios
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    usuario = serializers.PrimaryKeyRelatedField(source='user.username', read_only=True)
    post_comentario = ComentarioSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = "__all__"