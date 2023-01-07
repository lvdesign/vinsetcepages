from django import forms
from django.core.files.uploadedfile import InMemoryUploadedFile
from .humanize import naturalsize

from .models import Vin


# Form Comment
class CommentForm(forms.Form):
    comment = forms.CharField(
        required=True,
        max_length=141,
        min_length=1,
        strip=True
        )


# vin Form
class VinForm(forms.ModelForm):

    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)
    image = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'image'

    class Meta:
        model = Vin
        fields =  ['title','slug', 'description', 'tips', 'score', 'tag', 'category', 'image' ] # '__all__'
    # size
    def clean(self):
        cleaned_data = super().clean()
        pic = cleaned_data.get('image')
        if pic is None : return
        if len(pic) > self.max_upload_limit:
            self.add_error('image', "File must be < "+self.max_upload_limit_text+" bytes")

    # convert upload file to a cover
    def save(self, commit=True):
        instance = super(VinForm, self).save(commit=False)
        f = instance.image
        if isinstance(f, InMemoryUploadedFile):
            # Extract data from the form to the model
            bytearr = f.read()
            instance.content_type = f.content_type
            instance.image = bytearr #

        if commit:
            instance.save()
        return instance
