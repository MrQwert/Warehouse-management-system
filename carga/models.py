from django.db import models
from .csv_importer import import_products_from_csv


class CSV(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='csv_subidos/')
    fecha_carga = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        import_products_from_csv(self.archivo.path)
