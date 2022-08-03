from django.shortcuts import render, redirect
from .models import Memo
from django.shortcuts import get_object_or_404
from .forms import MemoForm
from django.views.decorators.http import require_POST

# Create your views here.
def index(request):
    memos = Memo.objects.all().order_by('-updated_datetime')
    return render(request, 'memo/index.html', {'memos': memos})

def detail(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)    
    return render(request, 'memo/detail.html', {'memo': memo})

def new_memo(request):
    if request.method == "POST":
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo:index')
    else:   
        form = MemoForm
    return render(request, 'memo/new_memo.html', {'form': form })

@require_POST #request.method=POSTの時のみ実行される
def delete_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect('memo:index')    

def edit_memo(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    if request.method == "POST":
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo:index')
    else:
        form = MemoForm(instance=memo)
    return render(request, 'memo/edit_memo.html', {'form': form, 'memo':memo })