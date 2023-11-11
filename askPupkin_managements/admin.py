from django.contrib import admin
from askPupkin_models.models import *

admin.site.register(Profile)
admin.site.register(Tag)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Like)