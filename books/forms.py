from django import forms


class BookModelForm(forms.ModelForm):
    class Meta:
        fields = '__all__'

