from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

#User
class User(AbstractUser):
    pass

# Working file
class DataFile(models.Model):
    user=models.ForeignKey('User', on_delete=models.CASCADE)
    workingfile = models.FileField(upload_to='data_files')
    date_created = models.DateTimeField(auto_now_add=True)
    dashboard = models.ForeignKey('Dashboard')

# dashboards
class Dashboard(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, unique=True)

    class Meta:
        unique_together = ('user',
                           'title', )

# charts

class Charts(models.Model):
    data = models.ForeignKey('DataFile', on_delete = models.CASCADE)
    dashboard = models.ForeignKey('dashboard', on_delete=models.CASCADE)
    X = models.CharField(max_length=60)
    Y = models.CharField(max_length=60)
    chart_type = models.CharField(max_length=60,
                                  choices=[
        ('bar', 'bar'),
        ('pie', 'pie'),
        ('line', 'line'),
        ('doughnut', 'doughnut'),
                                  ]
                                  )
    pass