from django.contrib import admin
from django.urls import path

# Settings project file import
from django.conf import settings
from django.conf.urls.static import static

from platzigram import views as localviews
from posts import views as postviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world/", localviews.hello_world),
    path("sorted-numbers/", localviews.sorted_numbers),
    path("welcome/<int:age>/<str:name>/", localviews.welcome),
    path("posts/", postviews.list_posts),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Adds the media static path to the urlpatterns
