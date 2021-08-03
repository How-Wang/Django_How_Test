from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello_views(request):
    name = request.GET['name']
    # name = 'david'
    return render(request,"say_hello.html",locals())
    #return HttpResponse("hello")
def input_show_name_views(request):
    if request.method == 'POST':
        name = request.POST['username']
        if name == 'Howard' or name == "Howie":
            return HttpResponse('Hello '+ name)
        else:
            return HttpResponse('Who you are ?')
    #else:
    elif request.method == 'GET':
        return render(request, "input_show_name.html")
def copy_names_views(request):
    if request.method == 'POST':
        return HttpResponse('Hello ')
    elif request.method == 'GET':
        return render(request, "copy_names.html")
