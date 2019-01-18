from django.db import models


class Kickstarter(models.Model):
    """To create model Kickstarter."""

    kickstarter_id = models.CharField(max_length=1024, primary_key=True)
    name = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    main_category = models.CharField(max_length=1024)
    currency = models.CharField(max_length=1024)
    deadline = models.CharField(max_length=1024)
    goal = models.CharField(max_length=1024)
    launched = models.CharField(max_length=1024)
    pledged = models.CharField(max_length=1024)
    state = models.CharField(max_length=1024)
    backers = models.CharField(max_length=1024)
    country = models.CharField(max_length=1024)
    usd_pledged = models.CharField(max_length=1024)
    usd_pledged_real = models.CharField(max_length=1024)
    usd_goal_real = models.CharField(max_length=1024)

    def __str__(self):
        return '{}'.format(self.name)
