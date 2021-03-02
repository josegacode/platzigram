from django.contrib import admin
from django.urls import path
from platzigram import views as localviews
from posts import views as postviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("hello-world/", localviews.hello_world),
    path("sorted-numbers/", localviews.sorted_numbers),
    path("welcome/<int:age>/<str:name>/", localviews.welcome),
    path("posts/", postviews.list_posts),
]
