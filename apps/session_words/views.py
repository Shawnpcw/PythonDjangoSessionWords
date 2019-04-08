from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    
    return render(request,'session_words/index.html')
def create(request):

    if 'color' not in request.session:
        request.session['color'] = ''
    if 'big' not in request.session:
        request.session['isbig'] = ''
    if 'allWords' not in request.session:
        request.session['allWords'] = [{}]

    request.session['word'] = request.POST['word']
    if request.POST['color'] == 'red':
        request.session['color'] = 'danger'
    elif request.POST['color'] == 'green':
        request.session['color'] = 'success'
    elif request.POST['color'] == 'blue':
        request.session['color'] = 'primary'
    
    if request.POST.get('isbig',True) != True:
        request.session['isbig'] = 23
    else:
        request.session['isbig'] = 12
    
    request.session['allWords'].append({
        'word':request.session['word'],
        'color':request.session['color'],
        'size':request.session['isbig']
    })

    return redirect('/')

def reset(request):
    del request.session['allWords']

    return redirect('/')