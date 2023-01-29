# cheking user is a staff or not
def staff_middleware(get_response):

    def middleware(request):
        response = get_response(request)
        return response

    return middleware


# cheking user is a superuser or not
def superAdmin_middleware(get_response):

    def middleware(request):
        response = get_response(request)
        return response

    return middleware
