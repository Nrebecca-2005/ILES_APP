from django.db import models
from django.conf import settings

class Evaluation(models.Model):
    placement = models.ForeignKey(
       'placements.InternshipPlacement', 
        on_delete=models.CASCADE,
        related_name='evaluations'
    )
    evaluator = models.ForeignKey(
        'users.CustomUser',
        on_delete=models.CASCADE,
        related_name='given_evaluations',
        null=True,
        blank=True
    )