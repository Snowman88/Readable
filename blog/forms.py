from django import forms
from django.forms import Textarea, CharField, TextInput
from .models import Post, Comment, Tag
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
# from django.forms.models import inlineformset_factory


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


class TagAreaForm(forms.Form):
    tags = forms.CharField(widget=forms.Textarea(attrs={'rows': "2", }))

    class Meta:
        pass

# PostTagFormSet = inlineformset_factory(Post, Tag)
