from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

from rounds.models import Round, Puzzle

optional = dict(blank=True, null=True)


class Team(User):
    name = models.CharField(max_length=50)
    extra_credit = models.IntegerField(default=0)
    rounds_unlocked = models.ManyToManyField(Round, **optional)
    puzzles_solved = models.ManyToManyField(Puzzle, **optional)
    last_unlock = models.DateTimeField(default=settings.HUNT_START_TIME)
    
    # could calculate number of unsolved puzzles available to the team
