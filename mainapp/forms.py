from django import forms
from django.core.exceptions import ValidationError
import os

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    # Разрешенные типы файлов
    valid_extensions = ['.jpg', '.png','.gif','.jpeg','.svg']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

class MyForm(forms.Form):
    comment = forms.CharField(label='Коментарий к изображению', max_length=100)

    file_path = forms.FileField(allow_empty_file=False,label='выберите файл для загрузки',\
                                validators=[validate_file_extension], widget=forms.ClearableFileInput(\
                                attrs={'label':'Прикрепите файл изображения','multiple': False, 'accept':'image/*'}))

