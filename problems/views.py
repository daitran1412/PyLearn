from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from subprocess import Popen
import subprocess
from list import Problems

tokens = []

@login_required(login_url='login')
def editor(request, problem_id):
    try:
        Problems[problem_id - 1]
    except IndexError:
        return HttpResponse("Không có bài tập này!")
    return render(request, "problems/editor.html", {
        "title": Problems[problem_id - 1]["title"],
        "description": Problems[problem_id - 1]["description"],
        "id": Problems[problem_id - 1]["id"],
        "starter": Problems[problem_id - 1]["starter"]
    })

@login_required(redirect_field_name='login')
def run(request):
    code = request.GET["code"]
    problem = int(request.GET["problem"])

    with open("solution.py", "w") as solution:
        solution.write(code)

    if problem == 1:
        run = Popen(["python", "-m", "unittest", "-q", "tests.charInput_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 2:
        run = Popen(["python", "-m", "unittest", "-q", "tests.fib_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 3:
        run = Popen(["python", "-m", "unittest", "-q", "tests.compare_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 4:
        run = Popen(["python", "-m", "unittest", "-q", "tests.divisors_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 5:
        run = Popen(["python", "-m", "unittest", "-q", "tests.removeDuplicates_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 6:
        run = Popen(["python", "-m", "unittest", "-q", "tests.listOverlap_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 7:
        run = Popen(["python", "-m", "unittest", "-q", "tests.palindrome_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 8:
        run = Popen(["python", "-m", "unittest", "-q", "tests.checkPrimality_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 9:
        run = Popen(["python", "-m", "unittest", "-q", "tests.reverseWord_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 10:
        run = Popen(["python", "-m", "unittest", "-q", "tests.birthdayDic_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 11:
        run = Popen(["python", "-m", "unittest", "-q", "tests.variance_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 12:
        run = Popen(["python", "-m", "unittest", "-q", "tests.dec5_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)
    elif problem == 13:
        run = Popen(["python", "-m", "unittest", "-q", "tests.dictionary_check"], stdout=subprocess.PIPE,  stderr=subprocess.STDOUT)

    test = run.communicate()[0].decode("utf-8")
    output = "<br>".join(str(test).split("\\n"))

    msg = ''

    if 'OK' in test:
        msg = 'Tất cả test đều đúng! Bạn đã hoàn thành bài tập!'
    elif 'FAILED (failures=1)' in test:
        msg = 'Có 1 test chưa đúng! Hãy kiểm tra kết quả!'
    elif 'FAILED (failures=2)' in test:
        msg = 'Có 2 test chưa đúng! Hãy kiểm tra kết quả!'
    elif 'FAILED (failures=3)' in test:
        msg = 'Chưa có test nào đúng! Hãy kiểm tra kết quả!'
    else:
        msg = 'Có lỗi xảy ra trong bài làm! Xin hãy thử lại!'

    return JsonResponse({'msg': msg, 'output': output})

    
