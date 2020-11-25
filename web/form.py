


from django import forms
from .models import Comment, UserBook ,  Post

class CommentForm(forms.ModelForm):
    model = Comment
    fields = 'comment'
    class Meta:
        model = Comment
        fields = {'comment': forms.Textarea(attrs={'class': 'form-control w-100'})}


class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['data_posted', 'postedBy']



