"""inventory_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from ecomapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path ("", views.dashboard_view),
    path ("dashboard/", views.dashboard_view, name="dashboard"),
    path ("customer/", views.customer_role_view,name="customer"),
    path ("delete/<int:id>/", views.delete_data,name="deletedata"),
    path ("<int:id>/", views.update_data,name="updatedata"),
    path ("managecustomer/", views.products_view,name="managecustomer"),
    path ("manageproduct/", views.customer_role_view,name="manageproduct"),
    path ("addproduct/", views.customer_role_view,name="addproduct"),
    path ("categories/", views.customer_role_view,name="categories"),
    path ("subcategory/", views.customer_role_view,name="subcategory"),
    path ("images/", views.customer_role_view,name="images"),
    path ("createinvoice/", views.customer_role_view,name="createinvoice"),
    path ("invoicelist/", views.customer_role_view,name="invoicelist"),
    path ("sendemail/", views.customer_role_view,name="sendemail"),
    path ("emaillist/", views.customer_role_view,name="emaillist"),
    path ("createnewoffer/", views.customer_role_view,name="createnewoffer"),
    path ("offerlist/", views.customer_role_view,name="offerlist"),
    path ("companylist/", views.customer_role_view,name="companylist"),
    path ("companyregistration/", views.customer_role_view,name="companyregistration"),
    path ("bill/", views.customer_role_view,name="bill"),
    path ("employeeoverview/", views.customer_role_view,name="employeeoverview"),
    path ("createpurchaseorder/", views.customer_role_view,name="createpurchaseorder"),
    path ("purchaselist/", views.customer_role_view,name="purchaselist"),
    path ("createrepairorder/", views.customer_role_view,name="createrepairorder"),
    path ("repairlist", views.customer_role_view,name="repairlist"),
    path ("salelist/", views.customer_role_view,name="salelist"),
    path ("makesale/", views.customer_role_view,name="makesale"),
    path ("managesales/", views.customer_role_view,name="managesales"),
    path ("addsale/", views.customer_role_view,name="addsale"),
    path ("salesbydates/", views.customer_role_view,name="salesbydates"),
    path ("monthlysales/", views.customer_role_view,name="monthlysales"),
    path ("dailysales/", views.customer_role_view,name="dailysales"),
    
    path ("customer/", views.customer_role_view,name="customer"),
    path ("customer/", views.customer_role_view,name="customer"),




] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
