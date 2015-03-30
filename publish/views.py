from django.shortcuts import render
from subprocess import check_call

from publish import commands

def test(request):
    return render(request, 'publish/test.html', dict(result=commands.test()))

def publish(request):
    if commands.test():
        commands.publish()
        return render(request, 'publish/publish.html', {})
