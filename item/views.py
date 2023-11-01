from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Item, Category
from.forms import NewItemForm, EditItemForm

# Create your views here.

def browse(req):
    query = req.GET.get('query', '')
    category_id = req.GET.get('category', 0)
    items = Item.objects.filter(is_sold= False)
    categories = Category.objects.all()

    if category_id:
        items = items.filter(category_id = category_id)

    if query:
        items = items.filter(Q(name__icontains= query) | Q(description__icontains= query))

    return render(req, 'item/items.html', {
        'items': items,
        'title': 'Browse Items',
        'query': query,
        'categories': categories,
        'category_id': int(category_id)
    })


def detail(req, pk):
    item = get_object_or_404(Item, pk= pk)
    related_items = Item.objects.filter(category= item.category, is_sold=False).exclude(pk= pk)[0:3]
    return render(req, 'item/detail.html', {
        'item': item,
        'related_items': related_items, 
    })

@login_required
def new(req):
    if req.method == 'POST':
        form = NewItemForm(req.POST, req.FILES)
        if form.is_valid():
            item = form.save(commit= False)
            item.created_by = req.user
            item.save()
            return redirect('item:detail', pk= item.id)
        
    else:
        form = NewItemForm()
        
    return render(req, 'item/form.html', {
        'form':form,
        'title': 'New Item' 
        })

@login_required
def delete(req, pk):
    item = get_object_or_404(Item, pk= pk, created_by= req.user)
    item.delete()

    return redirect('dashboard:index')

def edit(req, pk):
    item = get_object_or_404(Item, pk= pk, created_by= req.user)
    if req.method == 'POST':
        form = EditItemForm(req.POST, req.FILES, instance= item)
        if form.is_valid():
            form.save()
            return redirect('item:detail', pk= item.id)
    else:
        form = EditItemForm(instance= item)
    
    return render(req, 'item/form.html', {
        'form':form,
        'title': 'Edit Item'
    })

        