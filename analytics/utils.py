# In this Utility manager, we will manage how to get the IP address from User.


def get_client_ip(request):
    """Function searching for User IP address, and returning it"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', None)
    return ip
