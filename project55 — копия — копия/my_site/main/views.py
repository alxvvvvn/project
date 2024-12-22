from django.shortcuts import render, redirect 
results = {'A': 0, 'B': 0, 'C': 0}

def initialize_results(request):
    if 'results' not in request.session:
        request.session['results'] = {'A': 0, 'B': 0, 'C': 0}

def update_results(request, answer):
    if answer in request.session['results']:
        request.session['results'][answer] += 1



def index(request):
    return render(request, "main/index.html")

def page(request):
    return render(request, "main/page.html")


def page1(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path2')
    return render(request, 'main/page1.html', {'question': 'В своей профессиональной деятельности я хотел бы:', 'results': request.session['results']})  


def page2(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path3')
    return render(request, 'main/page2.html', {'question': 'Будущее человечества формируется через:', 'results': request.session['results']})

def page3(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path4')
    return render(request, 'main/page3.html', {'question': 'Если я стану лидером, то в первую очередь сосредоточусь на:', 'results': request.session['results']})

def page4(request): 
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path5')
    return render(request, 'main/page4.html', {'question': 'В книге или кинофильме меня больше всего привлекает:', 'results': request.session['results']})

def page5(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path6')
    return render(request, 'main/page5.html', {'question':'В людях для меня важнее всего:', 'results': request.session['results']})

def page6(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path7')
    return render(request, 'main/page6.html', {'question':'В свободное время мне бы хотелось:', 'results': request.session['results']})

def page7(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path8')
    return render(request, 'main/page7.html', {'question':'Меня больше всего привлекают обсуждения на следующие темы:', 'results': request.session['results']})

def page8(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path9')
    return render(request, 'main/page8.html', {'question':'Если бы в моей школе существовало всего три кружка, я бы предпочел:', 'results': request.session['results']})

def page9(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path10')
    return render(request, 'main/page9.html', {'question':'В школе важно акцентировать внимание на:', 'results': request.session['results']})

def page10(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path11')
    return render(request, 'main/page10.html', {'question':'Мне хотелось бы работать:', 'results': request.session['results']})

def page11(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path12')
    return render(request, 'main/page11.html', {'question':'Основная задача школы заключается в том, чтобы:', 'results': request.session['results']})

def page12(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path13')
    return render(request, 'main/page12.html', {'question':'Главное в жизни:', 'results': request.session['results']})

def page13(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path14')
    return render(request, 'main/page13.html', {'question':'Больше всего мне нравятся уроки:', 'results': request.session['results']})

def page14(request):
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('path15')
    return render(request, 'main/page14.html', {'question':'Мне было бы интереснее:', 'results': request.session['results']})

def page15(request): 
    initialize_results(request)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        if answer in request.session['results']:
            update_results(request, answer)
            return redirect('results')
    return render(request, 'main/page15.html', {'question':'В свободное время мне нравится:', 'results': request.session['results']})

def results(request):
    initialize_results(request)
    results = request.session.get('results', {'A': 0, 'B': 0, 'C': 0})
    return render(request, "main/results.html", {'results': results})