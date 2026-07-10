from functools import wraps
from django.http import HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

def role_required(roles):
    

    def decorator(view_func):
    
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
        # Ensure user is authenticated
            if not request.user.is_authenticated:
               return redirect('login_view_url')
            
        # Check custom attribute (e.g., a boolean flag like 'is_premium')
            if request.user.role not in roles:
              raise PermissionDenied("Access denied")
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
