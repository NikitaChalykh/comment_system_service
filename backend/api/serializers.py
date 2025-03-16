from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from articles.models import Article, Comment, User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            'email'
        )

    def validate(self, data):
        if data.get('username') == 'me':
            raise serializers.ValidationError('Username is incorrect!')
        return data

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ReadUserSerializer(serializers.ModelSerializer):
    '''
    Added a serializer for read-only usage for better API display
    in Redoc, it could be done using the initial_data dictionary -
    but I kept this solution.
    '''

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        exclude = ('author',)


class ReadArticleSerializer(serializers.ModelSerializer):
    '''
    As with the user example, I added a serializer for read-only usage
    for a more readable API display of authors.
    '''

    author = ReadUserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        exclude = ('nested_level', 'author', 'article', 'main_comment')


class ReadCommentSerializer(serializers.ModelSerializer):
    author = ReadUserSerializer(read_only=True)
    nested_comments = RecursiveField(
        required=False, many=True, allow_null=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
