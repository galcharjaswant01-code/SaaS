import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import pagevisits
this_dir = pathlib.Path(__file__).resolve().parent

def home_view(request, *args, **kwargs):
    return about_view(request, *args, **kwargs)
    
def about_view(requset, *args, **kwargs):
    qs = pagevisits.objects.all()
    page_qs = pagevisits.objects.filter(path=requset.path)
    try:
        percent = (page_qs.count() * 100.0) / qs.count()
    except:
        percent = 0
    html_ = "home.html"
    my_title = 'my page title'
    my_context = {
        'page_title' : my_title,
        'page_visits_count' : page_qs.count(),
        'percent': percent,
        'total_visits_count' : qs.count()
    }
    
    pagevisits.objects.create(path = requset.path)
    return render(requset, html_, my_context)

def my_home_page_view(request, *args, **kwargs):
    my_title = 'my page title'
    my_context = {
        'page_title' : my_title
    }
    html_ = 'home.html'
# """
#     <!DOCTYPE html>
# <html lang="en">
# <head> 
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
#     <h1>{page_title}he part of mind</h1>
# </body>
# </html>
# """.format(**my_context)# page_title = my_title
    
    # html_file_path = this_dir / 'home.html'
    # html_ = html_file_path.read_text()
    return HttpResponse(html_)

