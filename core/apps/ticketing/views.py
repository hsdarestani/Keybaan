from django.shortcuts import render
from .models import Ticket
from django.http import HttpResponse
from .forms import ticketform
from .models import Ticket,TicketStatus
from django.contrib import messages
from django.contrib.auth.models import User
from apps.useraccount.models import Profile
from django.contrib.auth.decorators import login_required

@login_required
def tickets(request):


    tickets = Ticket.objects.filter(created_by=request.user).order_by('-created_at')[:5]
    return render(request,'apps/ticketing/templates/ticketing/tickets.html', {'tickets': tickets})

@login_required
def ticket_by_id(request, ticket_id):
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'apps/ticketing/templates/ticketing/ticket_by_id.html', {'ticket':ticket})

@login_required
def ticketsubmit(request):
    form = ticketform()
    users = User.objects.all()
    # form.fields['ip_address'].initial = ip_address
    if request.POST:
        user = request.user
        form = ticketform(request.POST)
        if form.is_valid():
            print(request.POST)
            obj = form.save(commit=False)
            obj.created_by = user
            obj.save()
            messages.success(request,'پیام شما با موفقیت ارسال گردید.')
            # obj.ip_address = ip_address
            # obj.save()
            # return redirect('/')
        else:
            print(form.errors.as_data())
    context ={
        'form':form,
        'users':users,
    }

    return render(request, "apps/ticketing/templates/ticketing/ticketsubmit.html", context)
