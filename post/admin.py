from django.contrib import admin

from .models import Category, Comment, CommentResponse ,Post

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 3

class CommentResponseInline(admin.StackedInline):
    model = CommentResponse
    extra = 3

class PostInline(admin.StackedInline):
    model = Post
    extra = 2

class CategoryAdmin(admin.ModelAdmin):
    inlines = [PostInline,]

class CommentAdmin(admin.ModelAdmin):
    inlines = [CommentResponseInline,]

class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline,]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
