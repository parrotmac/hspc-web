from django.http import HttpResponse
from django.core import serializers

from simple_rest import Resource
from simple_rest.auth.decorators import admin_required

from .models import Event


class EventsApi(Resource):

    def get(self, request, event_id=None, **kwargs):
        json_serializer = serializers.get_serializer('json')()
        if event_id:
            events = json_serializer.serialize(Event.objects.filter(pk=event_id))
        else:
            events = json_serializer.serialize(Event.objects.all())
        return HttpResponse(events, content_type='application/json', status=200)

    @admin_required
    def post(self, request, *args, **kwargs):

        if id in request.POST:
            # Updating
            event_instance = Event.objects.get(id=request.POST.get('id'))
        else:
            event_instance = Event()

        event_instance.category = request.POST.get('category')
        event_instance.title = request.POST.get('title')
        event_instance.hidden_date = request.POST.get('hidden_date')
        event_instance.display_date = request.POST.get('display_date')
        event_instance.location = request.POST.get('location')
        event_instance.event_details = request.POST.get('event_details')
        event_instance.phone_number=request.POST.get('phone_number')

        event_instance.save()

        return HttpResponse(status=201)

    @admin_required
    def delete(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        event.delete()
        return HttpResponse(status=200)
