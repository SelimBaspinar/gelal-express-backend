from django.contrib import admin
from .models import MatchTable, Message, Role, User

class UserAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Surname', 'Username','Gender','Birthday','Role','Phone','Email','Password') 



class RoleAdmin(admin.ModelAdmin):
    list_display = ('Edit', 'Delete', 'Add')

class MatchTableAdmin(admin.ModelAdmin):
    list_display = ('U_Id', 'OU_Id', 'M_Id')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('M_Id', 'Content', 'WhoSend','Date')

admin.register(User,UserAdmin)
admin.register(Role,RoleAdmin)
admin.register(MatchTable,MatchTableAdmin)
admin.register(Message,MessageAdmin)