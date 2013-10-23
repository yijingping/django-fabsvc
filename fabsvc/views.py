import re
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from functools import wraps
from fabsvc import fabfile
from fabsvc.models import Service

running_pattern = re.compile(r'.* up .*\d+ seconds')
stoped_pattern = re.compile(r'.* down \d+ seconds, normally up')

def get_state(desc):
    print desc
    if running_pattern.match(desc):
        state = 'running'
    elif stoped_pattern.match(desc): 
        state = 'stoped'
    else:
        state = 'error'

    return state

def login_required(raw_func):
    @wraps(raw_func)
    def inner_func(request, *args, **kwargs):
        if request.user.is_authenticated():
            return raw_func(request, *args, **kwargs)
        else:
            return HttpResponseRedirect('/admin/' % request.path)

    return inner_func

@login_required
def index(request):
    # return format
    G = request.GET
    data_format = G.get('format', '')
    svcs = Service.objects.all()

    # host service map
    hsmap = {}
    for item in svcs:
        host = item.host.name
        if hsmap.get(host):
            hsmap[host].append(item)
        else:
            hsmap[host] = [item]

    if hsmap:
        fabfile.get_status(hsmap)

    # group service map
    gsmap = {}
    for item in svcs:
        group = item.group.name
        if gsmap.get(group):
            gsmap[group].append(item)
        else:
            gsmap[group] = [item]

    # json data
    groups = [] 
    for k,v in gsmap.iteritems():
        services = []
        for item in v:
            state = get_state(item.description)
            if state in ['running']:
                action = {'name': 'stop', 'url': '/fabsvc/service/?id=%s&action=stop' % item.pk }
            elif state in ['stoped', 'error']:
                action = {'name': 'start', 'url': '/fabsvc/service/?id=%s&action=start' % item.pk }

            services.append({
                'state': state, 
                'description': item.description,
                'name': item.name,
                'host': item.host.name,
                'actions': [action],
            })
        groups.append({
            'name': k,
            'services': services,
        })

    res = {'ret': 0, 'groups': groups} 

    if data_format == 'json':
        return HttpResponse(json.dumps(res))
    else:
        return render_to_response('fabsvc/index.html', res)

@login_required
def service(request):
    G = request.GET
    sid = int(G.get('id'))
    action = G.get('action')
    svc = Service.objects.get(pk=sid)
    res = fabfile.do_action(svc, action)
    return HttpResponse(json.dumps(res))

    
