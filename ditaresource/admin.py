from django.contrib import admin
from .models import (
    Client,
    Specialist,
    Issue,
    Tutor,
    TutorAvailability,
    Unitss,
    TutorUnitss,
    ClientTutorSession,
)

# Register your models here.
admin.site.register(Client)
admin.site.register(Specialist)
admin.site.register(Issue)
admin.site.register(Tutor)
admin.site.register(TutorAvailability)
admin.site.register(Unitss)
admin.site.register(TutorUnitss)
admin.site.register(ClientTutorSession)
