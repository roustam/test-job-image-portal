from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import ImageModel
from .forms import MyForm

def upload_view(request):

    if request.method == 'GET':
        image_form = MyForm()
        return render(request,'upload_form.html', {'form':image_form})
    if request.method == 'POST':
        image_form = MyForm(request.POST, request.FILES)
        if image_form.is_valid():
            uploaded_file=request.FILES['file_path']
            print('file type', uploaded_file.content_type)
            if uploaded_file.content_type[:5] == 'image': #dirty hack
                new_record = ImageModel.objects.create(
                img_comment = request.POST['comment'],
                img_file = request.FILES['file_path']
                )
                new_record.save()
            else:
                return HttpResponse("Ошибка. Разрешено загружать только файлы изображений.")
        else:
            return HttpResponse("Ошибка формы. Форма не валидна.")
            #print('form is not valid')
        return render(request,'upload_form.html', {'form':image_form})

def images_list_view(request):
    if request.method == 'GET':
        images_list = ImageModel.objects.all()
        return render(request,'images_list.html', {'images_list':images_list})
    else:
        return HttpResponse("Post-метод не разрешен.")
