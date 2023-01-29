from django.contrib import admin
from django.urls import path,include
"""
The function in its first agrument will always take Http request as its first parameter
and it has to return an HttpResponse that can be a HTML 
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('StudyTogetherBody.urls'))
]
