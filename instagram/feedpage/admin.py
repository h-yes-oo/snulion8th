from django.contrib import admin
from .models import Feed, FeedComment, Like

admin.site.register(Feed)
admin.site.register(FeedComment)
admin.site.register(Like)

