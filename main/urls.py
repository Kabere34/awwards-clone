from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static


from .import views

urlpatterns = [

    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    # path('rate/(?P<pk>\d+)', views.rate_post, name='rate_post'),
    path('api/posts/', views.Postlist.as_view()),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
