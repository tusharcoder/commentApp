# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-08T13:24:36+05:30
# @Email:  tamyworld@gmail.com
# @Filename: admin.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-08T13:35:09+05:30



from django.contrib import admin
from .models import Comment

# Register your models here.

admin.site.register(Comment)
