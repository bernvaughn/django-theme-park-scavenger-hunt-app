from django.db import models

class Board(models.Model):
    pass

class Task(models.Model):
    # technically a one-to-many relationship
    board = models.ManyToManyField(
        Board,
        through='TaskToBoard',
        related_name='tasks')

class TaskToBoard(models.Model):
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=False)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=False)
    position_x = models.IntegerField(null=False)
    position_y = models.IntegerField(null=False)

    class Meta:
        unique_together = (
            'board', 'position_x', 'position_y')