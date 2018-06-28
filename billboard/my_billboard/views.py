from django.shortcuts import render
from django.http import HttpResponse
from .models import Add_board
import time


def index(request):
    date_added = time.strftime("%Y/%m/%d")
    query_title = request.POST.get("q1")
    query_text = request.POST.get("q2")
    query_author = request.POST.get("q3")
    print(query_title,query_text,query_author)
    all_boards = ''
    if query_author and query_text and query_title:
        get_board = Add_board(title=query_title, text= query_text, author=query_author)
        get_board.save()
        all_boards = Add_board.objects.all()
    context = {
        "all_boards": all_boards,
        "date_added": date_added
    }
    return render(request,'my_billboard/home.html',context)
# Create your views here.
