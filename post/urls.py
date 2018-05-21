from django.conf.urls import url
from post import views
urlpatterns=[
    url(r'^$',views.index_view),
    url(r'index.html/$',views.index_view),
    url(r'page/(\d+)/$',views.index_view),
    url(r'post/details/(\d+)/$',views.post_details_view),
    url(r'category/(\d+)/$',views.category_details_view),
    url(r'archive/(\d+)/(\d+)/$',views.archive_details_view),
    url(r'search/$',views.search_view)
]
