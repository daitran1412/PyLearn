from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse, JsonResponse
from subprocess import Popen
import subprocess
from .forms import CreateUserForm
from .models import Passed
from list import Problems

# Create your views here.

def welcome(request):
    return render(request, 'main/welcome.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tạo tài khoản thành công!')
                return redirect('login')
        context = {'form': form}
        return render(request, 'main/register.html', context)
    
def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                django_login(request, user)
                messages.success(request, ('Đăng nhập thành công!'))
                return redirect('home')
            else:
                messages.error(request, ('Tên đăng nhập hoặc mật khẩu không đúng!'))
                return redirect('login')
        return render(request, 'main/login.html')

def logout(request):
    django_logout(request)
    return redirect('welcome')

@login_required(login_url='login')
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url='login')
def problems(request):
    problems = Problems.copy()
    for prob in problems:
        if Passed.objects.filter(user_id=request.user.id, problem_id=prob['id']).exists():
            prob['passed'] = True
        else:
            prob['passed'] = False
    return JsonResponse(problems, safe=False)

@login_required(login_url='login')
def editor(request, problem_id):
    try:
        Problems[problem_id - 1]
    except IndexError:
        return HttpResponse("Không có bài tập này!")
    return render(request, "main/editor.html", {
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

    output = run.communicate()[0].decode("utf-8")

    msg = ''
    passed = False

    if 'OK' in output:
        msg = 'Tất cả test đều đúng! Bạn đã hoàn thành bài tập!'
        passed = True
    elif 'FAILED (failures=1)' in output:
        msg = 'Có 1 test chưa đúng! Hãy kiểm tra kết quả!'
    elif 'FAILED (failures=2)' in output:
        msg = 'Có 2 test chưa đúng! Hãy kiểm tra kết quả!'
    elif 'FAILED (failures=3)' in output:
        msg = 'Chưa có test nào đúng! Hãy kiểm tra kết quả!'
    else:
        msg = 'Có lỗi xảy ra trong bài làm! Xin hãy thử lại!'

    response = {
        'msg': msg,
        'output': output,
        'passed': passed
    }

    if passed is True:
        passed = Passed(user_id=request.user.id, problem_id=problem)
        passed.save()

    return JsonResponse(response)
