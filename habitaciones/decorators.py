from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

def dev_login_required(view_func):
    @login_required
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.groups.filter(name='Developers').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Acceso restringido a desarrolladores.")
    return _wrapped_view
