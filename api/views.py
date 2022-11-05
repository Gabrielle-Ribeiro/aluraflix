from rest_framework import viewsets
from api.models import Video
from api.serializer import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """Exibe todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

