from django.urls import path
from . import views
app_name = "ticketing"
urlpatterns = [
    path('tickets/', views.tickets, name='tickets'),
    path('ticket/<int:ticket_id>', views.ticket_by_id, name='ticket_by_id'),
    path('ticketsubmit/', views.ticketsubmit, name='ticketsubmit')
]
