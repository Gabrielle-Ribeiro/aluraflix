from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from api.models import Video
from api.serializer import VideoSerializer


class VideoViewSet(viewsets.ModelViewSet):
    """Exibe todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            return Response({
                "message": "Erro! Não foi possível encontrar o vídeo."
            },
                status=status.HTTP_404_NOT_FOUND)
        return Response({
            "message": "Deletado com sucesso!"
        },
            status=status.HTTP_200_OK)
