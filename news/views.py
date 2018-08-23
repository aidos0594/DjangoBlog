from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Comments
from news.forms import CommentForm


def news_list(request):
    """Вывод всех статьей
    """
    news = News.objects.all()
    return render(request, "news/news_list.html", {"news": news})


def new_single(request, pk):
    """Вывод полной статьи
    """
    new = get_object_or_404(News, id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.new = new
            form.save()
            return redirect(new_single, pk)
    else:
        comments = Comments.objects.filter(new=pk, moderation=True)
        form = CommentForm()
        return render(request, "news/new_single.html",
                      {'new': new,
                       'comments': comments,
                       'form': form})
