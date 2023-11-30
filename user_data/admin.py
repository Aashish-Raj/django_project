from django.contrib import admin
from .models import user_detail,Address,ai_data
# Register your models here.

class user_data(admin.ModelAdmin):
    list_display=('id','email','fname','lname','contact','created_at','updated_at',"users_id")

admin.site.register(user_detail,user_data)

# address detail
class address_data(admin.ModelAdmin):
    list_display=("id",'house_no','city','state','Country','users_id')
admin.site.register(Address,address_data)



# address detail
class open_ai(admin.ModelAdmin):
    list_display=("id",'name','openai_model','key','users_id')
admin.site.register(ai_data,open_ai)




