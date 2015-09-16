
def themer(request):
    result = {}
    if request.COOKIES['theme'] == 'light':
        result['active_theme'] = 'light'
        result['active_theme_name'] = 'Solarized Light'
        result['inactive_theme'] = 'dark'
        result['inactive_theme_name'] = 'Solarized Dark'
    else:
        result['active_theme'] = 'dark'
        result['active_theme_name'] = 'Solarized Dark'
        result['inactive_theme'] = 'light'
        result['inactive_theme_name'] = 'Solarized Light'
    return result
