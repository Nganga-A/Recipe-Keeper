from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    cooking_instructions = models.TextField()
    difficulty = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    difficulty_level = models.CharField(max_length=6, choices=difficulty)
    
    def __str__(self):
        return self.title
