from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Athlete, Team, Coach
from django.urls import reverse


def index(request):
    team_list = Team.objects.order_by('name')[:5]
    # output = [{'id': t.id, 'name': t.name} for t in team_list]
    template = loader.get_template('django_app/index.html')
    context = {
        'team_list': team_list,
    }
    return HttpResponse(template.render(context, request))
    
def coaches(request, team_id):
    template = loader.get_template('django_app/coaches.html')
    coach_list = Coach.objects.filter(teams__id=team_id)
    context = {
        'coach_list': coach_list,
    }
    return HttpResponse(template.render(context, request))


def team_detail(request, team_id):
    if request.method == 'GET':
        template = loader.get_template('django_app/team_detail.html')
        team = Team.objects.filter(id=team_id)
        context = {
            'team': team[0],
        }
        return HttpResponse(template.render(context, request))
    else:
        updated_team_name = request.POST['team_name']
        team = Team.objects.get(id=team_id)
        team.name = updated_team_name
        team.save()
        return HttpResponseRedirect(reverse('index'))
