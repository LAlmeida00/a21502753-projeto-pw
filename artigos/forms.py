from django import forms    # formulários Django
from .models import User, Post, PostImage, Comment, Rating

class UserForm(forms.ModelForm):
    class Meta:
        model = User                                        # classe para a qual é o formulário
        fields = ['user']                                   # inclui no form todos os campos da classe User.


class PostForm(forms.ModelForm):
    image_post = forms.ImageField()

    class Meta:
        model = Post                                        # classe para a qual é o formulário
        fields = ['titulo', 'texto', 'image_post']          # inclui no form todos os campos da classe Post.

    def save(self, user=None, commit=True):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment                                         # classe para a qual é o formulário
        fields = '__all__'                                      # inclui no form todos os campos da classe Comment.
