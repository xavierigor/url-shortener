from django import forms

from apps.shortener.models import ShortUrl


class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ["full"]
        widgets = {
            "full": forms.TextInput(attrs={"placeholder": "Full URL", "autocomplete": "off"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['full'].label = ""
