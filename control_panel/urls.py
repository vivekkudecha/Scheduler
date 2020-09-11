from django.urls import path
from . import views

urlpatterns = [

    # Home Page, Dashboard, Index, Home, Default
    path('' , views.index, name = 'Index'),
    path('index' , views.index, name = 'IndexAlt'),
    path('home' , views.index, name = 'HomeAlt'),
    path('default' , views.index, name = 'DefaultAlt'),

    #Members & Department
    path('department' , views.member_dept, name = 'MembersDepartment'),
    path('members' , views.member_dept, name = 'MembersAlt'),
    path('dept' , views.member_dept, name = 'DepartmentAlt'),

    #Device
    path('device' , views.device, name = 'Device'),
    path('mobile' , views.device, name = 'DeviceAlt'),
    
    #Database
    path('database' , views.database, name = 'Database'),
    path('db' , views.database, name = 'DatabaseAlt'),

    #Payments
    path('payment' , views.payment, name = 'Payment'),
    path('pay' , views.payment, name = 'PaymentAlt'),
]
