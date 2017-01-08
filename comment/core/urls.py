# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-08T13:45:26+05:30
# @Email:  tamyworld@gmail.com
# @Filename: urls.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-08T13:53:11+05:30
from django.conf.urls import url
from .views import *

urlpatterns = [
url(r'^comment',CommentList.as_view(),name="get_all_comments"),
]
