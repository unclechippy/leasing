from django.http import HttpResponse
from django.template import loader

#dashboard
def dashboard(request):
    template = loader.get_template('lease.html')
    return HttpResponse(template.render({}, request))

def lease(request, lease_id):
    #try:
    #    lease = Lease.objects.get(pk=lease_id)
    #except Lease.DoesNotExist:
    #        raise Http404("Lease does not exist")
    lease = get_object_or_404(Lease, pk=lease_id)
    context = {
        "lease" : lease
    }
    return render(request, "leases/lease.html", context)

def new_lease(request):
    template = loader.get_template('new_lease.html')
    return HttpResponse(template.render({}, request))

def charge(request, charge_id):
    pass
