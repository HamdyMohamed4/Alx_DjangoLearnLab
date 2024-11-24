from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Article

# View to create an article
@permission_required('app_name.can_create', raise_exception=True)
def create_article(request):
    if request.method == "POST":
        # Handle article creation logic
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content)
        return redirect('article_list')  # Redirect to list of articles
    return render(request, 'create_article.html')

# View to edit an article
@permission_required('app_name.can_edit', raise_exception=True)
def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == "POST":
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect('article_list')
    return render(request, 'edit_article.html', {'article': article})

# View to view an article
@permission_required('app_name.can_view', raise_exception=True)
def view_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'view_article.html', {'article': article})

# View to delete an article
@permission_required('app_name.can_delete', raise_exception=True)
def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    article.delete()
    return redirect('article_list')

