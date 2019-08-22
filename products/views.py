from django.shortcuts import render,get_object_or_404,redirect
from.models import Product
from django.contrib.auth.decorators import login_required
def home(request):
    product=Product.objects
    return render(request,'products/home.html',{'product':product})
@login_required(login_url='/register/')
def create(request):
    if request.method=='POST':
        if request.POST['title'] and  request.FILES['image'] and  request.POST['budget'] and  request.POST['duration'] and  request.POST['discription']:
            product=Product()
            product.title=request.POST['title']
            product.image=request.FILES['image']
            product.budget = request.POST['budget']
            product.duration = request.POST['duration']
            product.discription = request.POST['discription']
            product.hunter=request.user
            product.save()
            return redirect('/products/'+ str(product.id))


        else:
            return render(request, 'products/create.html',{'error':'please fill all the field'})
    else:
        return render(request,'products/create.html')


def detail(request,product_id):
    product=get_object_or_404(Product,pk=product_id)
    return render(request,'products/detail.html',{'product':product})
# Create your views here.
