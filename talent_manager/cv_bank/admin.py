from django.contrib import admin
from django import forms

# Register your models here.
from .models import Collabs, Skills, Roles

class CollabForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CollabForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].help_text = 'In lowercase please'
        self.fields['last_name'].help_text = 'In lowercase please'
        self.fields['resume'].required = False

    class Meta:
        model = Collabs
        exclude =('',)

class CollaboratorAdmin(admin.ModelAdmin):
    form = CollabForm
    fieldsets = (
        ('Personal details',{
            'fields':('first_name','last_name',),
        }),
        ('Professional details',{
            'fields':('roles','skills','resume',),
        }),
    )

    list_display = ("last_name", "first_name","get_roles","get_skills","resume")


admin.site.register(Roles)
admin.site.register(Skills)
#admin.site.register(Collabs)
admin.site.register(Collabs,CollaboratorAdmin)

admin.site.index_title = "Talent Manager"
admin.site.index_header = "Talent Manager admin"
admin.site.site_title = "django admin"
