from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static


from .import views

urlpatterns = [

    path('', views.index, name='index'),
    path('new_post/', views.new_post, name='new_post'),
    path('single_post/<int:post_id>', views.single_post, name='single_post'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('account/', include('django.contrib.auth.urls')),
    # path('profile/', views.user_profile, name='profile'),
    path('user_profile/', views.user_profile, name='profile'),
    path('profile_edit/<int:user_id>', views.profile_edit, name='profile_edit'),
    path('search_results/', views.search_results, name='search_results'),
    path('rate/<pk>', views.rate_post, name='rate_post'),
    path('api/posts/', views.Postlist.as_view()),
    path('api/profile/', views.Profilelist.as_view()),
    path('api_links/', views.api_links, name='api_links'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
