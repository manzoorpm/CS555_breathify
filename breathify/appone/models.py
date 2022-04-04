from django.db import models
from django.conf import settings


# Create your models here.

class user(models.Model):
	user_levels = (
		('Beginer','Beginer'),
		('Intermediate','Intermediate'),
		('Expert','Expert'),
	)
	user_object = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
	phone = models.CharField(max_length=200, null=True)
	user_level = models.CharField(max_length=200, null=True, choices=user_levels)
	date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
	total_score = models.CharField(max_length=200, null=True)

class activity(models.Model):

	game_levels = (
		('Level 1','Level 1'),
		('Level 2','Level 2'),
		('Level 3','Level 3'),
		('Level 4','Level 4'),
		('Level 5','Level 5'),
	)
	user = models.ForeignKey(user, null=True, on_delete= models.SET_NULL)
	game_level = models.CharField(max_length=200, null=True, choices=game_levels)
	activity_points = models.CharField(max_length=200, null=True)
