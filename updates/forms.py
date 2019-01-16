from django import forms

from .models import Update as UpdateModel


class UpdateModelForm(forms.ModelForm):
    class Meta:
        model = UpdateModel
        fields = [
            'user',
            'content',
            'image',
        ]

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content, image = data.get("content"), data.get("image", None)
        if not content and image:
            raise forms.ValidationError("Content or Image is required")
        return super().clean()
