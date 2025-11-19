# blog/forms.py

from django import forms

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget = forms.TextInput(
            attrs={"class":"form-control comment-author","placeholder":"Your Name",}
        ),
    )
    body = forms.CharField(
        widget = forms.Textarea(
            attrs = {"class":"form-control comment-body","placeholder":"Leave a comment!"}
        )
    )
