from django.urls import path

from company_app.views.blog_views import BlogCategoryList, BlogList, CategoryBlogsList, BlogDetail, AddComment, CommentsView
from company_app.views.company_views import AboutCompanyList, SocialAccountList, CompDataList

urlpatterns = [

    #blog view urls
    path('categories/', BlogCategoryList.as_view()),
    path('categories/<int:pk>/', CategoryBlogsList.as_view()),
    path('blogs/', BlogList.as_view()),
    path('blogs/<int:pk>/', BlogDetail.as_view()),
    path('blogs/addcomment/', AddComment.as_view()),
    path('blogs/<int:pk>/all-comments/', CommentsView.as_view()),

    # company_view urls
    path('about/', AboutCompanyList.as_view(), name='about'),
    path('social/', SocialAccountList.as_view()),
    path('compdata/', CompDataList.as_view()),

]