from django import forms

class MyForm(forms.Form):
    comment = forms.CharField(label='Коментарий к изображению', max_length=100)
    file_path = forms.FileField(label='выберите файл для загрузки', required=True, allow_empty_file=False )
