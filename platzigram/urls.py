from django.contrib import admin
from django.urls import path

# Settings project file import
from django.conf import settings
from django.conf.urls.static import static

from platzigram import views as localviews
from posts import views as postviews
from users import views as userviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world/", localviews.hello_world, name="hello_world"),
    path("sorted-numbers/", localviews.sorted_numbers, name="sort"),
    path("welcome/<int:age>/<str:name>/", localviews.welcome, name="welcome"),
    path("posts/", postviews.list_posts, name="feed"),
    path("users/login/", userviews.login_view, name="login"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adds the media static path to the urlpatterns
