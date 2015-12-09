from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
# Create your views here.
from main.models import State, City, StateCapital
from django.template import RequestContext
from main.forms import ContactForm, CityEditForm, StateEditForm, StateCapitalEditForm
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.models import User
#list views
#detail views
#create view
#edit view
#delete view
#make the view --> make the url


def city_list_cas(request):

    context = {}

    city_list = CityCas.objects.all()
    

def api_state_list(request):

    states = State.objects.all()

    api_dict = {}

    state_list = []

    api_dict['states'] = state_list

    for state in states:
        cities = state.city_set.all()[:30]

        city_list = []

        for city in cities:
            city_list.append({'name': city.name, 'pk': city.pk})

        try:
            state_list.append({'name': state.name,
                               'abbrev': state.abbrev,
                               'map': state.state_map.url,
                               'capital': state.statecapital.name,
                               'votes': state.votes,
                               'pk': state.pk,
                               # 'cities': [city for city in state.city_set.all()[:30]],
                               'cities': city_list,
                               })
        except:
            print state.name
    return JsonResponse(api_dict)


def ajax_state_list(request):

    context = {}

    return render_to_response('ajax_state_list.html', context, context_instance=RequestContext(request))


def api_city_list(request):

    cities = City.objects.all()

    api_dict = {}

    city_list = []

    api_dict['cities'] = city_list

    for city in cities:
        try:
            city_list.append({'zip_code': city.zip_code,
                              'lat': city.lat,
                              'lon': city.lon,
                              })
        except:
            print city.name
    return JsonResponse(api_dict)


def ajax_city_list(request):

    context = {}

    return render_to_response('ajax_city_list.html', context, context_instance=RequestContext(request))


def vote(request, pk):

    vote_type = request.GET.get('vote_type', None)
    user = User.objects.get(pk=request.user.pk)
    state = State.objects.get(pk=pk)
    userprofile = user.userprofile

    if vote_type == 'up':
        if userprofile in state.downvotes.all():
            state.downvotes.remove(userprofile)
        
        state.upvotes.add(userprofile)

    if vote_type == 'down':
        if userprofile in state.upvotes.all():
            state.downvotes.add(userprofile)

        state.downvotes.add(userprofile)
#'UpVote: %s, DownVotes: %s' % (state.upvotes.all().count(), state.downvotes.all().count())
    return HttpResponseRedirect('/state_list/')


def state_list(request): #request pretty much always has to be there, you are going through all the objects

    context = {}

    states = State.objects.all().order_by('-upvotes_count')

    context['states'] = states
    #template -> context dictionary -> context_instance variable
    return render_to_response('state_list.html', context, context_instance=RequestContext(request))


def state_detail(request, pk): #purpose is to show detailed view of a specific object
    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    return render_to_response('state_detail.html', context, context_instance=RequestContext(request))


def statecapital_detail(request, pk):
    context = {}

    state_capital = StateCapital.objects.get(pk=pk)

    context['state_capital'] = state_capital

    return render_to_response('state_detail.html', context, context_instance=RequestContext(request))


def statecapital_create(request):
    context = {}

    context['request'] = request.method

    context['statecapital'] = StateCapital.objects.all()

    if request.method == 'POST':
        name = request.GET.get('name', None)
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)

        if state_id != None:
            state = State.objects.get(pk=state_id)
        else:
            state = State.objects.get(name='Texas')

        the_statecapital, created = StateCapital.objects.get_or_create(name=name)

        the_statecapital.pop = pop
        the_statecapital.lat = lat
        the_statecapital.lon = lon

        the_statecapital.save()

        context['created'] = created

    elif request.method == 'GET':
            print "it was a GET request"

    return render_to_response('statecapital_create.html', context, context_instance=RequestContext(request))


def statecapital_edit(request, pk):

    context = {}

    statecapital = StateCapital.objects.get(pk=pk)

    form = StateCapitalEditForm(request.POST or None, instance=statecapital)

    context['StateCapital'] = statecapital
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('statecapital_edit.html', context, context_instance=RequestContext(request))


def state_search(request):

    context = {}

    context['request'] = request

    #context['get_vars'] = request.GET['a']

    #context['get_vars'] = request.GET.get('a', None)

    state = request.GET.get('state', None)

    state = request.POST.get('state', None)

    if state != None:
        states = State.objects.filter(name__icontains=state)
    else:
        states = State.objects.all()

    context['states'] = states

    return render_to_response('state_search.html', context, context_instance=RequestContext(request))


def city_search(request):

    context = {}

    context['request'] = request

    city = request.GET.get('city', None)

    if city != None:
        cities = City.objects.filter(name__icontains=city)
    else:
        cities = City.objects.all()

    context['cities'] = cities

    return render_to_response('city_search.html', context, context_instance=RequestContext(request))


def city_detail(request, pk):
    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city

    return render_to_response('city_detail.html', context, context_instance=RequestContext(request))


def city_create(request):

    context = {}

    context['request'] = request.method

    context['states'] = State.objects.all()

    if request.method == 'POST':
        name = request.GET.get('name', None)
        county = request.GET.get('county', None)
        zip_code = request.GET.get('zip_code', None)
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)
        state_id = request.POST.get('state', None)

        if state_id != None:
            state = State.objects.get(pk=state_id)
        else:
            state = State.objects.get(name='Texas')

        the_city, created = City.objects.get_or_create(name=name)

        the_city.county = county
        the_city.zip_code = zip_code
        the_city.latitude = latitude
        the_city.longitude = longitude

        the_city.save()

        context['created'] = created

    elif request.method == 'GET':
            print "it was a GET request"

    return render_to_response('city_create.html', context, context_instance=RequestContext(request))


def city_edit(request, pk):

    context = {}

    city = City.objects.get(pk=pk)

    form = CityEditForm(request.POST or None, instance=city)

    context['city'] = city
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('city_edit.html', context, context_instance=RequestContext(request))

        #return render_to_response('city_edit.html', context, context_instance=RequestContext(request))


def state_create(request):
    context = {}

    context['request'] = request.method

    context['states'] = State.objects.all()

    if request.method == 'POST':
        name = request.GET.get('name', None)
        county = request.GET.get('county', None)
        zip_code = request.GET.get('zip_code', None)
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)
        state_id = request.POST.get('state', None)

        if state_id != None:
            state = State.objects.get(pk=state_id)
        else:
            state = State.objects.get(name='Texas')

        the_state, created = State.objects.get_or_create(name=name)

        the_state.county = county
        the_state.zip_code = zip_code
        the_state.latitude = latitude
        the_state.longitude = longitude

        the_state.save()

        context['created'] = created

    elif request.method == 'GET':
            print "it was a GET request"

    return render_to_response('state_create.html', context, context_instance=RequestContext(request))


def state_edit(request, pk):

    context = {}

    state = State.objects.get(pk=pk)

    form = StateEditForm(request.POST or None, instance=state)

    context['state'] = state
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('state_edit.html', context, context_instance=RequestContext(request))

        #return render_to_response('state_edit.html', context, context_instance=RequestContext(request))


def contact_view(request):

    context = {}

    form = ContactForm()

    context['form'] = form

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail('STATES SIT MESSAGE FROM %s' % name,
                      message,
                      email,
                      [settings.EMAIL_HOST_USER],
                      fail_silently=False
                      )
            context['message'] = "email sent"
        else:
            context['message'] = form.errors

    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form

    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))