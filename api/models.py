from django.db import models


class Video(models.Model):
    titulo = models.CharField(max_length=100, blank=False, null=False)
    descricao = models.CharField(max_length=1000, blank=False, null=False)
    url = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.titulo
