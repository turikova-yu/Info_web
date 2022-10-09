from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Home)
admin.site.register(Portfolio)

class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [SkillInline]




