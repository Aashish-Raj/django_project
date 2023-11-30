from django.shortcuts import render,redirect
from .models import user_detail,Address,ai_data
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# for user login

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        print(username)
        print(password)

        user=authenticate(request,username=username,password=password)
        if user is not None:
             login(request,user)
             if(user.is_staff):
                messages.success(request, ' login successfully')
                return redirect("show_data")
             else:
                messages.success(request, ' login successfully')
                return render(request,"user_profile.html")
                 
        
        else:
            
            messages.success(request, 'invalid credientials')
            return render(request,"login_user.html")
      
    return render(request,"login_user.html")

# for user logout
def logout_user(request):
    logout(request)
    messages.success(request, ' logout successfully')
    return redirect("login_user")
    
     

# for input user data
@login_required(login_url="/")
def input_data(request):

    if(request.user.is_staff):

        print("input page called")
        if request.method=="POST":
            

            print("submit button clicked")

            email=request.POST["email"]
            fname=request.POST["fname"]
            lname=request.POST["lname"]
            contact=request.POST["contact"]
            house_no=request.POST["h_no"]
            city=request.POST["city"]
            state1=request.POST["state"]
            country=request.POST["country"]
            username=request.POST["username"]
            password=request.POST["password"]

            #  email validate
            if (user_detail.objects.filter(email=email).exists()):
                messages.success(request, 'mail already exists')
                return render(request,"input_page.html")
            
            #  username validate
            if (User.objects.filter(username =username).exists()):
                messages.success(request, 'username already exists')
                return render(request,"input_page.html")
            
            else:

                #save user credientials
                user=User.objects.create_user(username=username,password=password)
                user.save()

                # fetch current id for the user
                id1=User.objects.get(username=user).id

                # for i in user:
                #      print(i)
                # print(id1)

                # # crete user database object
                user_obj=user_detail(fname=fname,email=email,lname=lname,contact=contact,users_id=user)
                user_obj.save()

                # # Create address object 
                address_obj = Address(users_id=user_obj, house_no=house_no, city=city, state=state1,Country=country)
                address_obj.save()

                print(email," ",fname," ",lname," ",contact," ",house_no," ",city," ",state1," ",country)
                messages.success(request, 'user added successfully')


                return render(request,"input_page.html")
          
        return render(request,"input_page.html")
    
    else:
        return redirect("logout_user")


# for show user data

@login_required(login_url="/")
def show_data(request):

    if(request.user.is_staff):
        obj=user_detail.objects.all().order_by('id') 

        paginator=Paginator(obj,5)
        page_number=request.GET.get('page')
        serviceDatafinal=paginator.get_page(page_number)


        # page_number1=int(page_number)

        # if(paginator.has_previous):
        #     next_page=[1,2,3]

        # elif (page_number1+3)>=paginator.num_pages:
        #     next_page=[paginator.num_pages-3,paginator.num_pages-2,paginator.num_pages-1]
        # else:
        #     next_page=[paginator.next_page_number+1,paginator.next_page_number+2,paginator.next_page_number+3]
    
    else:
        return redirect("logout_user")
    

    
    


    return render(request,"show_data.html",{"context":serviceDatafinal})

# for delete data
def user_delete(request,id):
    obj=user_detail.objects.get(id=id)
    obj.delete()
    messages.success(request, 'data deleted successfully')
    return redirect('/show_data')

# for update user data
@login_required(login_url="/")
def user_update(request, id):

    if(request.user.is_staff):
            if request.method=="POST":
                print("update button clicked")        

                # fetch data from template
                email=request.POST["email"]
                fname=request.POST["fname"]
                lname=request.POST["lname"]
                contact=request.POST["contact"]
                house_no=request.POST["h_no"]
                city=request.POST["city"]
                state1=request.POST["state"]
                country=request.POST["country"]

                print(email," ",fname," ",lname," ",contact," ",house_no," ",city," ",state1," ",country)

                # fetch data from database
                user_details=user_detail.objects.get(id=id)
                address_details=Address.objects.get(users_id=id)

                print(user_details.fname)

                # update data in database# crete user database object
                user_details.fname=fname
                user_details.email=email
                user_details.lname=lname
                user_details.contact=contact
                # user_details(fname=fname,email=email,lname=lname,contact=contact)
                user_details.save()

                # update address object 
                # address_details(house_no=house_no, city=city, state=state1,Country=country)
                address_details.house_no=house_no
                address_details.city=city
                address_details.state=state1
                address_details.Country=country
                
                address_details.save()

                print("data updated")
                messages.success(request, 'data updated successfully')

                # redirect to show data page
                return redirect('/show_data')
    


            user_details=user_detail.objects.get(id=id)
            address_details=Address.objects.get(users_id=id)
            print("update page called")
            return render(request, "update_data.html", {"user_details": user_details,"address_details":address_details})

    else:
        return redirect("logout_user")






    # print("update function called for id ",id)

    # return redirect("/show_data")

# for input user  ai data
@login_required(login_url="/")
def input_ai_data(request):
    print("input  ai page called")

    if request.method=="POST":
        print(" button clicked")        

        # fetch data from template
        name=request.POST["name"]
        model_name=request.POST["model_name"]
        secret_key=request.POST["secret_key"]

        print(name," ",model_name," ",secret_key)

        # fetch user name
        # ai_obj=ai_data.objects. request.user
        ai_obj=ai_data(name=name,openai_model=model_name,key=secret_key,users_id=request.user)
        ai_obj.save()
        messages.success(request, 'data added successfully')

        # 
    
    return render(request, "ai_detail.html")
    # if request.method=="POST":



def err_404_view(request,exception):
    return render(request,"404.html")

   


