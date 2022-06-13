from .models import *

class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user_profile', 'profile']
