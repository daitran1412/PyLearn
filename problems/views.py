from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from library.list import Problems
# Create your views here.

@login_required(login_url='login')
def editor(request, problem_id):
    try:
        Problems[problem_id - 1]
    except IndexError:
        return HttpResponse("Không có bài tập này!")
    return render(request, "problems/editor.html", {
        "title": Problems[problem_id - 1]["title"],
        "description": Problems[problem_id - 1]["description"],
        "problem_id": Problems[problem_id - 1]["id"],
        "starter": Problems[problem_id - 1]["starter"]
    })

def compile(request):
    pass