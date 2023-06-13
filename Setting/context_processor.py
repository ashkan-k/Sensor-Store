from Setting.models import Setting


def get_default_setting_variables(request):
    settings = {}
    for key, value in dict(Setting.objects.values_list('key', 'value')).items():
        settings[key] = value

    context = {
        'settings': settings
    }
    return context
