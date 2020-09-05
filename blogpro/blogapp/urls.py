from django.urls import path
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [ 
    path('', views.post_list_view),
    path('tag/(?p<tag_slug>[-\w]+)/', views.post_list_view,name='post_list_by_tag_name'),
    path('(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/', views.post_detail_view,name='post_detail'),
    path('search/',views.search,name='search'),
    path('contactus/',views.Contact_us_view),
    path('sports/',views.Sports),
    path('movies/',views.Movie),
    path('star/',views.Star_view),
    path('world/',views.World_view),
    path('travel/',views.Travel_view),
    path('education/',views.Education_view),
    path('cricket/',views.Cricket_view),
   

          ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

