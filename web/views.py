from django.shortcuts import render
from django.views import generic
from django.contrib import messages
from web.forms import UploadForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import time
from django.http import JsonResponse
from .models import Photo
from django.http import HttpResponse
from web import controllers
import os

def handleAjaxUpload(request):
    try:
        filePath = ""
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            print("hwew",form)
            form.save()
            return JsonResponse({
                "code": 201,
                "message": "Image uploaded successfully"
            })
        else:
            return JsonResponse({
                "status": 400,
                "message": form.errors["image"]
            })
    except Exception as e:
        return JsonResponse({
            "code": 500,
            "message": e
        })        


class UploadView(generic.View):
    def get(self, *args, **kwargs):
        form = UploadForm()
        imageSrc = "/media/default.png"
        photo = Photo.objects.last()
        if photo:
            imageSrc = photo.image.url
        return render(self.request, "web/index.html",  {
            "form": form,
            "imageSrc": imageSrc
        })

    def post(self, *args, **kwargs):
        if self.request.is_ajax():
            return handleAjaxUpload(self.request)
        form = UploadForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            filename = self.request.FILES['image'].name
            filePath ="media/input/"+filename
            print(filePath)
            if os.path.exists(filePath):
                os.remove(filePath)
            form.save()
            messages.success(self.request, "Image Uploaded")
        else:
            messages.error(self.request, "Failed uploading image")
        
        return redirect(reverse_lazy("index"))


def rangeResult(request):
    try:
        
        fromRoll = request.GET.get('from')
        toRoll = request.GET.get('to')
        fromRoll = fromRoll.upper()
        toRoll = toRoll.upper()
        generated = controllers.rangeresult(fromRoll,toRoll)
        notfnd = ""
        for item in generated:
            notfnd = notfnd + " " + str(item)
        msg = "Success -Range Transcript Generated and some Not found roll No. are"+notfnd
        return render(request, "web/success.html",{"success":msg})
    except Exception as e:
        return render(request, "web/error.html",{"success":e}) 
    
def generateTranscript(request):
    try:
        controllers.overAllmarksheet()
        return render(request, "web/success.html",{"success":"Success - Transcript Generated"})
    except Exception as e:
        return render(request, "web/error.html",{"success":e}) 

