from django.contrib import admin

from .models import Job
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    exclude = ('creater',)
    list_display = ('position_name', 'creater', )

    def get_queryset(self, request):
        if request.user.is_superuser:
            return Job.objects.all()
        else:
            return Job.objects.filter(creater=request.user)

    def get_list_display(self, request):
        if request.user.is_superuser:
            return ('position_name', 'creater', )
        else:
            return('position_name',)

    def save_model(self, request, obj, form, change):
        obj.creater = request.user
        obj.save()


admin.site.register(Job, JobAdmin)
