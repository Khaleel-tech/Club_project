from django.apps import AppConfig


class ClubinchargeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ClubIncharge'

    def ready(self):
        import ClubIncharge.templatetags.custom_filters
