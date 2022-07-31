from django.contrib import admin
from .models.blog import Blog, BlogCategory, ReplyComment, Comment
from .models.company_data import CompanyData, AboutCompany, SocialAccounts

admin.site.register(BlogCategory)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(ReplyComment)
admin.site.register(AboutCompany)
admin.site.register(CompanyData)
admin.site.register(SocialAccounts)
