from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template('lease.html')
    return HttpResponse(template.render({}, request))

def lease(request, lease_id)
    try:
        lease = Lease.objects.get(pk=lease_id)
    except:
        Lease.DoesNotExist:
            raise Http404("Lease does not exist")
    context = {
        "lease" : lease
    }
    return render(request, "leases/lease.html", context)
