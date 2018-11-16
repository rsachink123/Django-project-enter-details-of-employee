from django.shortcuts import render
from django.views import generic
from genericviews.forms import PersonForm
from genericviews.models import Person
def makeentry(request):
    if request.method=='POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name','')
            company_name = request.POST.get('company_name','')
            location = request.POST.get('location', '')
            email = request.POST.get('email', '')
            mobile = request.POST.get('mobile', '')
            desc = request.POST.get('desc', '')
        person = Person(name = name,desc=desc,company_name=company_name,location=location,email=email,mobile=mobile)
        person.save()
        form = PersonForm()
        return render(request,'makeentry.html',{'form':form})
    else:
        form = PersonForm()
        return render(request,'makeentry.html',{'form':form})
class IndexView(generic.ListView):
    context_object_name = 'list'
    template_name = 'index.html'
    def get_queryset(self):
        return Person.objects.all()
class DetailsView(generic.DetailView):
    model = Person
    template_name = 'details.html'
