from django import forms

from apps.shortener.models import ShortUrl


class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ["full"]
        widgets = {
            "full": forms.URLInput(attrs={"placeholder": "Full URL"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full'].label = ""
