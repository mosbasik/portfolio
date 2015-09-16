
class Themer(object):

    # desired cookie will be available in every django view
    def process_request(self, request):
        if request.method == 'GET':
            theme = request.GET.get('theme', None)
            if (theme is not None) and (theme in ['light', 'dark']):
                request.COOKIES['theme'] = theme
        # will only add cookie if request does not have it already
        if 'theme' not in request.COOKIES:
            request.COOKIES['theme'] = 'dark'

    # desired cookie will be available in every HttpResponse parser (browser)
    def process_response(self, request, response):
        theme = request.GET.get('theme', None)
        if (theme is not None) and (theme in ['light', 'dark']):
            max_age = 6 * 30 * 24 * 60 * 60  # six months in seconds
            response.set_cookie('theme', value=theme, max_age=max_age)
        return response
