import datetime

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

from django.views import generic

from .models import Lease

#dashboard
#def dashboard(request):
#    template = loader.get_template('dashboard.html')
#    return HttpResponse(template.render({}, request))

class IndexView(generic.ListView):
    template_name = 'dashboard.html'
    context_object_name = 'leases'

    def get_queryset(self):
        """Return the lease list."""
        return Lease.objects.order_by('-name')[:5]

"""def lease(request, lease_id):
    #try:
    #    lease = Lease.objects.get(pk=lease_id)
    #except Lease.DoesNotExist:
    #        raise Http404("Lease does not exist")
    lease = get_object_or_404(Lease, pk=lease_id)
    context = {
        "lease" : lease
    }
    return render(request, "leases/lease.html", context)"""

class DetailView(generic.DetailView):
    model = Lease
    template_name = 'lease.html'

def new_lease(request):
    if request.method == "POST":
        name = request.POST['name']
        start_date = datetime.datetime.strptime(request.POST.get('start-date'), '%Y-%m-%d')
        end_date = datetime.datetime.strptime(request.POST.get('end-date'), '%Y-%m-%d')
        lease = Lease(name=name, start_date=start_date, end_date=end_date)
        lease.save()
        #return HttpResponse('Saved!')
        return redirect('lease', pk=lease.pk)
    else:
        template = loader.get_template('new_lease.html')
        return HttpResponse(template.render({}, request))

def charge(request, charge_id):
    pass
