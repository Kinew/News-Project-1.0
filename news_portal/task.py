from celery import shared_task
from .models import Post

@shared_task
def post_send(oid):
    post = Post.objects.get(pk = oid)
    post.complete = True
    post.save()