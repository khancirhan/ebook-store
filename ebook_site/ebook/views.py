from wsgiref.util import FileWrapper
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.http import FileResponse, Http404
from django.core.paginator import Paginator
from .models import EBook, Subject


def index(request):
    subjects = Subject.objects.all()[:6]

    context = {
        'subjects': subjects,
    }

    return render(request, 'ebook/index.html', context)


def ebooks(request, category, subject_id):
    subjects = Subject.objects.order_by('title')
    ebooks = EBook.objects.order_by('-date').filter(category=category)

    if subject_id != 0:
        ebooks = ebooks.filter(subject_id=subject_id)

    paginator = Paginator(ebooks, 6)
    page = request.GET.get('page')
    ebooks = paginator.get_page(page)

    context = {
        'subjects': subjects,
        'ebooks': ebooks,
        'category': category
    }

    return render(request, 'ebook/ebooks.html', context)


def ebook(request, category, ebook_id):
    subjects = Subject.objects.order_by('title')
    ebook = get_object_or_404(EBook, id=ebook_id)

    context = {
        'subjects': subjects,
        'ebook': ebook,
    }

    return render(request, 'ebook/ebook.html', context)


def search(request):
    ebooks = EBook.objects.order_by('-date')

    resultset = []

    if 'search' in request.GET:
        search_query = request.GET['search']

        if search_query:
            resultset = ebooks.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(authors__name__icontains=search_query)
            )

    paginator = Paginator(ebooks, 8)
    page = request.GET.get('page')
    ebooks = paginator.get_page(page)

    context = {
        'ebooks': resultset,
        'value': request.GET['search']
    }

    return render(request, 'ebook/search.html', context)


def subjects(request):
    subjects = Subject.objects.all()

    paginator = Paginator(subjects, 6)
    page = request.GET.get('page')
    subjects = paginator.get_page(page)

    context = {
        'subjects': subjects,
    }

    return render(request, 'ebook/subjects.html', context)


def preview(request, ebook_id):
    ebook = EBook.objects.get(id=ebook_id)

    try:
        response = FileResponse(ebook.file)
        response['Content-Disposition'] = f'inline; filename={ebook.title}.pdf'

        return response

    except FileNotFoundError:
        return Http404


def download(request, ebook_id):
    ebook = EBook.objects.get(id=ebook_id)

    try:
        response = FileResponse(ebook.file)
        response['Content-Disposition'] = f'attachment; filename={ebook.title}.pdf'
        return response

    except FileNotFoundError:
        return Http404
