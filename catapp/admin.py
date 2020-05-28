from django.contrib import admin

from .models import Breed
from .models import Cat
from .models import Human
from .models import Home

admin.site.register(Breed)
admin.site.register(Cat)
admin.site.register(Human)
admin.site.register(Home)