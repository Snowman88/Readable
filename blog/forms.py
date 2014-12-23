from django import forms
from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Hidden


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    # post = forms.ModelChoiceField(queryset=Post.objects.all(),
    #         widget=forms.HiddenInput())
    helper = FormHelper()
    helper.form_method = 'POST'
    # helper.form_action = 'comment_new'
    helper.add_input(Submit(name='saveBtn', value='Save', css_class='btn-primary'))
    # helper.add_input(Hidden("post_id", ""))

    class Meta:
        model = Comment
        fields = ('text', )
