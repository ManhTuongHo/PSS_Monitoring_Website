from django.contrib import admin
from .models import Hub, UserProfile, Panel, Load, LoadStatus, PanelStatus, PowerExchange, PaymentStatus

admin.site.register(Hub)
admin.site.register(UserProfile)
admin.site.register(Panel)
admin.site.register(Load)
admin.site.register(LoadStatus)
admin.site.register(PanelStatus)
admin.site.register(PowerExchange)
admin.site.register(PaymentStatus)