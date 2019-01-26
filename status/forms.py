from django import forms

from .models import Status


class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > 240:
            raise forms.ValidationError("Content is too long")
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content')
        image = data.get("image")
        if not content and not image:
            raise forms.ValidationError("Content or Image is required")
        return super().clean(*args, **kwargs)
