from django.contrib import admin
from .models import Contracts,Agents,Customers,Cities,IranProvinces, BoardTypes,Locations,Boards,ContractDetailsPerBoard,PackageDetailsPerBoard,SalesPackages,CustomerPaymentMethod,Installment
# Register your models here.
class IranProvincesAdmin(admin.ModelAdmin):
    list_display = ('ProvinceName','EntryDate')
    search_fields = ('ProvinceName','EntryDate')
admin.site.register(IranProvinces, IranProvincesAdmin)

class BoardTypesAdmin(admin.ModelAdmin):
    list_display = ('BoardType','EntryDate')
    search_fields = ('BoardType','EntryDate')
admin.site.register(BoardTypes, BoardTypesAdmin)

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('LocationName','LocationCode','LocationTypeID','Longitude','Latitude','CityID','ActivityStatus','EntryDate')
    search_fields = ('LocationName','LocationCode','LocationTypeID','Longitude','Latitude','CityID','ActivityStatus','EntryDate')
admin.site.register(Locations, LocationsAdmin)

class CitiesAdmin(admin.ModelAdmin):
    list_display = ('CityName','ProvinceID','EntryDate')
    search_fields = ('CityName','ProvinceID','EntryDate')
admin.site.register(Cities, CitiesAdmin)

class BoardsAdmin(admin.ModelAdmin):
    list_display = ('BoardCode','BoardTypeID','LocationID','BoardScore','BoardDescription','Dimenstions','PlacementComments','Area','ActivityStatus','EntryDate')
    search_fields = ('BoardCode','BoardTypeID','LocationID','BoardScore','BoardDescription','Dimenstions','PlacementComments','Area','ActivityStatus','EntryDate')
admin.site.register(Boards, BoardsAdmin)

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('CustomerName','EntryDate')
    search_fields = ('CustomerName','EntryDate')
admin.site.register(Customers, CustomersAdmin)

class AgentsAdmin(admin.ModelAdmin):
    list_display = ('AgentFirstName','AgentLastName','PositionID','AgentCode','EntryDate')
    search_fields = ('AgentFirstName','AgentLastName','PositionID','AgentCode','EntryDate')
admin.site.register(Agents, AgentsAdmin)

class ContractsAdmin(admin.ModelAdmin):
    list_display = ('ContractNumber','CustomerID','PrePayment','ContractPrice','ContractConfirmDate','ContractConfirmDateJalali','IsCancelled','IsExpanded','ValueAddedTax','EntryDate','AgentNameID','CancelingDate','CancelingDateJalali')
    search_fields = ('ContractNumber','CustomerID','PrePayment','ContractPrice','ContractConfirmDate','ContractConfirmDateJalali','IsCancelled','IsExpanded','ValueAddedTax','EntryDate','AgentNameID','CancelingDate','CancelingDateJalali')
admin.site.register(Contracts, ContractsAdmin)

class ContractDetailsPerBoardAdmin(admin.ModelAdmin):
    list_display = ('ContractID','BoardID','BoardContractPrice','DailyPrice','ContractStart','JalaliStart','ContractFinish','JalaliFinish','AgentNameID','ContractYearBase','EntryDate')
    search_fields = ('ContractID','BoardID','BoardContractPrice','DailyPrice','ContractStart','JalaliStart','ContractFinish','JalaliFinish','AgentNameID','ContractYearBase','EntryDate')
admin.site.register(ContractDetailsPerBoard, ContractDetailsPerBoardAdmin)

class SalesPackagesAdmin(admin.ModelAdmin):
    list_display = ('PackageName','AgentNameID','ActivityStatus','EntryDate')
    search_fields = ('PackageName','AgentNameID','ActivityStatus','EntryDate')
admin.site.register(SalesPackages, SalesPackagesAdmin)

class PackageDetailsPerBoardAdmin(admin.ModelAdmin):
    list_display = ('PackageID','BoardID','ActivityStatus','DeactivationDate','DeactivationDateJalali','ActivationDate','ActivationDateJalali','EntryDate')
    search_fields = ('PackageID','BoardID','ActivityStatus','DeactivationDate','DeactivationDateJalali','ActivationDate','ActivationDateJalali','EntryDate')
admin.site.register(PackageDetailsPerBoard, PackageDetailsPerBoardAdmin)

class CustomerPaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('CustomerPaymentMethodName','EntryDate')
    search_fields = ('CustomerPaymentMethodName','EntryDate')
admin.site.register(CustomerPaymentMethod, CustomerPaymentMethodAdmin)

class InstallmentAdmin(admin.ModelAdmin):
    list_display = ('ContractID','InstallmentNumber','InstallmentNumber','CustomerPaymentMethodID','PaymentDate','PaymentDateJalali','EntryDate')
    search_fields = ('ContractID','InstallmentNumber','InstallmentNumber','CustomerPaymentMethodID','PaymentDate','PaymentDateJalali','EntryDate')
admin.site.register(Installment, InstallmentAdmin)
