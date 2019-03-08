from django.db import models

class Minerals(models.Model):
    name = models.TextField()
    image_filename = models.TextField()
    image_caption = models.TextField()
    category = models.TextField()
    formula = models.TextField()
    strunz_classification = models.TextField()
    color = models.TextField()
    crystal_system = models.TextField()
    unit_cell = models.TextField()
    crystal_symmetry = models.TextField()
    cleavage = models.TextField()
    mohs_scale_hardness = models.TextField()
    luster = models.TextField()
    streak = models.TextField()
    diaphaneity = models.TextField()
    optical_properties = models.TextField()
    refractive_index = models.TextField()
    crystal_habit = models.TextField()
    specific_gravity = models.TextField()

    class Meta:
        ordering = ['name',]
