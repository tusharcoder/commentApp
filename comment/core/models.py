# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-08T13:24:36+05:30
# @Email:  tamyworld@gmail.com
# @Filename: models.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-08T13:38:19+05:30



from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Comment(models.Model):
    """class for the model comment"""
    text = models.CharField(max_length=150)
    author = models.CharField(max_length=200)
    def __unicode__(self):
        return self.author+": "+self.text
