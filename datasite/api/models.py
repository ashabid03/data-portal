from django.db import models

class DatasetDirectory(models.Model):
    dataset_id = models.IntegerField(primary_key=True)
    dataset_name = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return "%s" % self.dataset_name

    class Meta:
        managed = False
        db_table = 'dataset_directory'

class DataSamples(models.Model):
    license_plate = models.TextField(blank=True, null=True)
    seq = models.TextField(blank=True, null=True)
    unnormalized_read_counts = models.IntegerField(blank=True, null=True)
    isomirmap_flags = models.TextField(blank=True, null=True)
    mintmap_flags = models.TextField(blank=True, null=True)
    minrmap_flags = models.TextField(blank=True, null=True)
    yrfmap_flags = models.TextField(blank=True, null=True)
    dataset_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'data_samples'

    def __str__(self) -> str:
        return "Molecule: %s\t Read Counts: %d" % (self.license_plate, self.unnormalized_read_counts)
    
    