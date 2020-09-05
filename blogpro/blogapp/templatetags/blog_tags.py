from blogapp.models import Post
from django import template
register = template.Library()


#for simple tag exmple only aplicable for count 

#@register.simple_tag
#def total_posts():
#   return Post.objects.count() 


#for inclusion tag example only aplicable for recent and oldest post calculation and show

@register.inclusion_tag('blogapp/latest_posts123.html')
def show_latest_posts():
    latest_posts=Post.objects.order_by('-publish')[:5]
    return {'latest_posts':latest_posts}


from django.db.models import Count
#@register.assignment_tag
@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]