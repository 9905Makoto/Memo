from django.shortcuts import render
from .models import Memo
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    memos = Memo.objects.all().order_by('-updated_datetime')
    return render(request, 'memo/index.html', {'memos': memos})

def detail(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)    
    return render(request, 'memo/detail.html', {'memo': memo})

def new_memo(request):
    return render(request, 'memo/new_memo.html')    