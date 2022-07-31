from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import  LimitOffsetPagination
from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from services_app.permissions import IsAdminOrReadOnly

from company_app.serializers.blogserializers import ( BlogSlz, BlogBreifSlz,
                                                    BlogCategorySlz,
                                                    CommentSlz,
                                                    )

from company_app.models.blog import Blog, BlogCategory, Comment

# Blog toifalari chiqarish uchun
class BlogCategoryList(generics.ListAPIView):
    model = BlogCategory
    serializer_class = BlogCategorySlz
    queryset = BlogCategory.objects.all()

#categoriyaga tegishli bloglar
class CategoryBlogsList(generics.ListAPIView):
    model = Blog
    serializer_class = BlogSlz

    def get_queryset(self, *args, **kwargs):
        pk = int(self.kwargs['pk'])
        category = BlogCategory.objects.get(pk=pk)
        blogs = category.blog.all()
        #blogs = Blog.objects.filter(category=pk)
        return blogs

class BlogList(generics.ListAPIView):
    pagination_class = LimitOffsetPagination()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['title', 'category', 'snippet']
    serializer_class = BlogBreifSlz
    queryset = Blog.objects.all()

class BlogDetail(generics.RetrieveAPIView):
    serializer_class = BlogSlz
    queryset = Blog.objects.all()

#blog ga tegishli izohlar
class CommentsView(APIView):
    permission_classes = IsAdminOrReadOnly

    def get(self,*args, **kwargs):
        pk = int(self.kwargs['pk'])
        blog = Blog.objects.get(pk=pk)
        comments = blog.comment.all()
        # reply_comments = comments.filter(is_reply=True)
        commentslz = CommentSlz(comments, many=True)

        return Response(data = {
            'comments' : commentslz.data,
        })

class AddComment(generics.CreateAPIView):
    model = Comment
    serializer_class = CommentSlz

