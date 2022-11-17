from django.contrib import admin

from .models import *

admin.site.register(Candidate)
admin.site.register(Recruiter)
admin.site.register(Post)
admin.site.register(Application)
