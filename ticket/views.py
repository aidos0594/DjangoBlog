from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from .models import Ticket
from .forms import AddTicketForm


class AddTicket(CreateView):
    """Добавление тикета
    """
    model = Ticket
    form_class = AddTicketForm
    template_name = 'ticket/add-ticket.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return redirect('/ticket/add-ticket/')

    def success_url(self):
        return redirect('/add-ticket/')

# class MyView(View):
#
#     def get(self, request, *args, **kwards):
#         return HttpResponse('Классы Django')
#
#
# class MyTemplateView(TemplateView):
#     template_name = 'ticket/add-ticket.html'
#
#     def get_context_data(self, **kwargs):
#         context = super(MyTemplateView, self).get_context_data(**kwargs)
#         context['text'] = 'Hi world!'
#         return context
