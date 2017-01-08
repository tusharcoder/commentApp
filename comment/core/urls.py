# @Author: Tushar Agarwal(tusharcoder) <tushar>
# @Date:   2017-01-08T13:45:26+05:30
# @Email:  tamyworld@gmail.com
# @Filename: urls.py
# @Last modified by:   tushar
# @Last modified time: 2017-01-08T14:23:08+05:30
from django.conf.urls import url
from .views import *

urlpatterns = [
url(r'^comments/$',CommentList.as_view(),name="get_all_comments"),
url(r'^comments/(?P<pk>[0-9]+)/$',CommentDetail.as_view()),
]
