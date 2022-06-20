from django.shortcuts import render
from .models import Ticket
from django.http import HttpResponse
from .forms import ticketform
from .models import Ticket,TicketStatus

def tickets(request):
    tickets = Ticket.objects.order_by('-created_at')[:5]
    return render(request,'apps/ticketing/templates/ticketing/tickets.html', {'tickets': tickets})
def ticket_by_id(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'apps/ticketing/templates/ticketing/ticket_by_id.html', {'ticket':ticket})

def ticketsubmit(request):
    form = ticketform()

    # form.fields['ip_address'].initial = ip_address
    if request.POST:
        form = ticketform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            # obj.ip_address = ip_address
            # obj.save()
            # return redirect('/')
    context ={}
    context['form']= form
    return render(request, "apps/ticketing/templates/ticketing/ticketsubmit.html", context)
