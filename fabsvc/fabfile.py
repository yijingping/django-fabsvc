from fabric.api import env, run
from fabric.decorators import task
from fabric.tasks import execute

env.hosts = ['tiger@192.168.10.96','tiger@192.168.10.85',]

@task
def status(hsmap):
    res = []
    for item in hsmap['%s@%s' % (env.user, env.host)]:
        try:
            item.description = run('sudo svstat %s' % item.path)
        except Exception as e:
            item.description = str(e)

    return res

@task
def action(service, action_name):
    if action_name == 'start':
        res = run('sudo svc -u %s' % service.path)
    elif action_name == 'stop':
        res = run('sudo svc -k %s' % service.path)
    else:
        res = ''

    return res

def get_status(hsmap):
    env.hosts = hsmap.keys() 
    res = execute(status, hsmap)
    return res

def do_action(service, action_name):
    env.hosts = [service.host.name]
    res = execute(action, service, action_name)
    return res

if __name__ == "__main__":
    get_status()
