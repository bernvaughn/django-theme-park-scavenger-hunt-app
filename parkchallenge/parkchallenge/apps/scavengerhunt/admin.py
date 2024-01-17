from django.contrib import admin
from parkchallenge.apps.scavengerhunt import models

# TODO: create inlines and stuff

admin.site.register(models.Board)
admin.site.register(models.Task)
admin.site.register(models.TaskToBoard)
