from django.contrib import admin
from candidates.models import CandidateJobMap
from .models import Job


class CandidateInLine(admin.TabularInline):
    model = CandidateJobMap

    def get_readonly_fields(self, request, obj):
        if request.user.is_superuser:
            return []
        else:
            return('candidate', )


class JobAdmin(admin.ModelAdmin):
    exclude = ('creater',)
    list_display = ('position_name', 'creater', )
    inlines = (CandidateInLine, )

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
        if not obj.pk:
            obj.creater = request.user
            obj.save()


admin.site.register(Job, JobAdmin)
