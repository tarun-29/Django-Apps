"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from firstapp import views
# from fbvApp import views
# from cbvApp import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('students', views.StudentViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('nsApp.urls')),
]


# urlpatterns = [
#     # Class based views starts here
#     # path('students/', views.StudentList.as_view()),
#     # path('students/<int:pk>', views.StudentDetails.as_view()),    
#     # # Function based starts here
#     # # path('students/', views.student_list),
#     # # path('students/<int:pk>', views.student_detail),
#     # path('firstapp/', include('firstapp.urls')),
#     # path('demo/', include('demo.urls')),
#     path('admin/', admin.site.urls),
#     # path('auth/', obtain_auth_token)
# ]
