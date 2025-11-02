from .models import CartItem

def cart_items_count(request):
    if request.user.is_authenticated:
        # Since we don't have user field, use session key for all users
        session_key = request.session.session_key
        if not session_key:
            request.session.create()
            session_key = request.session.session_key
        count = CartItem.objects.filter(session_key=session_key).count()
    else:
        session_key = request.session.session_key
        if session_key:
            count = CartItem.objects.filter(session_key=session_key).count()
        else:
            count = 0
    return {'cart_items_count': count}