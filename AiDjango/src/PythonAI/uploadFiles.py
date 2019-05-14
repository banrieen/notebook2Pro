from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

from somewhere import handle_upload_file

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST,request.FILES)
        if form.is_valid():
            handle_upload_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request,'upload.html',{'form':form})