from django.db import models

optional = dict(blank=True, null=True)

# We do NOT store much metadata about rounds or puzzles in the database, and DEFINITELY not puzzle answers. 
# This is just to track relationships between teams and puzzles/rounds.
# It's up to the template/puzzle page designers to include a {% if is_solved %}.


class Round(models.Model):
    slug = models.SlugField()
    order = models.PositiveSmallIntegerField()


class Puzzle(models.Model):
    slug = models.SlugField()
    round = models.ForeignKey(Round)
    is_meta = models.BooleanField(default=False)
    is_roundsolution = models.BooleanField(default=False)
    
    # post save hook for tracking hunt state, where unlock algorithm gets run
