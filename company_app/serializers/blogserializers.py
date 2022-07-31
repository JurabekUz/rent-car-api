from rest_framework.serializers import ModelSerializer

from company_app.models.blog import Blog, BlogCategory, Comment

class BlogCategorySlz(ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = ('name',)

class BlogBreifSlz(ModelSerializer):
    category = BlogCategorySlz(many=True)
    class Meta:
        model = Blog
        fields = ('title', 'category', 'snippet', 'created_date')
        
class BlogSlz(ModelSerializer):
    category = BlogCategorySlz(many=True)
    class Meta:
        model = Blog
        fields = '__all__'

class CommentSlz(ModelSerializer):
    blog = BlogBreifSlz()
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ('id', 'blog', 'name', 'email', 'body', 'website', 'added_date')
