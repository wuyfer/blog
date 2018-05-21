from haystack import indexes
from post.models import Post

class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    # 给title设置索引
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return self.get_model().objects.order_by('-created').all()
