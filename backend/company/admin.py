from django.contrib import admin

from company.models import Company, Ticket, Works


# Register your models here.

admin.site.register(Company)
admin.site.register(Works)
admin.site.register(Ticket)
