from post.models import *
from django.db.models import *

def sidebar_context_processor(request):
    context={}
    context['category']=Post.objects.values('category','category__name').annotate(count=Count('*'))
    row = get_archive()
    context['archive']=row
    context['recent']=Post.objects.order_by('-created').all()[:5]
    return context

def get_archive():
    from django.db import connection, transaction
    cursor = connection.cursor()
    query = 'select substr(p.created,1,4) year,substr(p.created,6,2) month,count(*) countnum from post_post p group by substr(p.created,1,4) ,substr(p.created,6,2)'
    cursor.execute(query)
    row = cursor.fetchall()
    return row
