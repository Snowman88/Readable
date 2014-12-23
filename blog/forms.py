from django import forms
from django.forms import Textarea
from .models import Post, Comment
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field, Hidden


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)

    def clean_title(self):
        title = self.cleaned_data["title"]
        if "うん" in title:
            raise forms.ValidationError("Inproper words in your text")
        return title


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
        widgets = {
            'text': Textarea(attrs={'rows': 5, }),
        }
