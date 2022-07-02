from django.contrib import admin
from .models import Contracts,Agents,Customers,Cities,IranProvinces, BoardTypes,LocationTypes,Locations,Boards,ContractDetailsPerBoard,PackageDetailsPerBoard,SalesPackages,CustomerPaymentMethod,Installment,AgentPaymentMethods
# Register your models here.
class IranProvincesAdmin(admin.ModelAdmin):
    list_display = ('ProvinceName','jEntryDate')
    search_fields = ('ProvinceName','jEntryDate')
admin.site.register(IranProvinces, IranProvincesAdmin)

class BoardTypesAdmin(admin.ModelAdmin):
    list_display = ('BoardType','jEntryDate')
    search_fields = ('BoardType','jEntryDate')
admin.site.register(BoardTypes, BoardTypesAdmin)

class LocationTypesAdmin(admin.ModelAdmin):
    list_display = ('LocationTypeName','jEntryDate')
    search_fields = ('LocationTypeName','jEntryDate')
admin.site.register(LocationTypes, LocationTypesAdmin)

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('LocationName','LocationCode','LocationTypeID','Longitude','Latitude','CityID','ActivityStatus','jEntryDate')
    search_fields = ('LocationName','LocationCode','LocationTypeID','Longitude','Latitude','CityID','ActivityStatus','jEntryDate')
admin.site.register(Locations, LocationsAdmin)

class CitiesAdmin(admin.ModelAdmin):
    list_display = ('CityName','ProvinceID','jEntryDate')
    search_fields = ('CityName','ProvinceID','jEntryDate')
admin.site.register(Cities, CitiesAdmin)

class BoardsAdmin(admin.ModelAdmin):
    list_display = ('BoardCode','BoardTypeID','LocationID','BoardScore','BoardDescription','Dimenstions','PlacementComments','Area','ActivityStatus','jEntryDate')
    search_fields = ('BoardCode','BoardTypeID','LocationID','BoardScore','BoardDescription','Dimenstions','PlacementComments','Area','ActivityStatus','jEntryDate')
admin.site.register(Boards, BoardsAdmin)

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('CustomerName','jEntryDate')
    search_fields = ('CustomerName','jEntryDate')
admin.site.register(Customers, CustomersAdmin)

class AgentsAdmin(admin.ModelAdmin):
    list_display = ('AgentFirstName','AgentLastName','PositionID','AgentCode','jEntryDate')
    search_fields = ('AgentFirstName','AgentLastName','PositionID','AgentCode','jEntryDate')
admin.site.register(Agents, AgentsAdmin)

class AgentPaymentMethodsAdmin(admin.ModelAdmin):
    list_display = ('AgentPaymentMethodName','jEntryDate')
    search_fields = ('AgentPaymentMethodName','jEntryDate')
admin.site.register(AgentPaymentMethods, AgentPaymentMethodsAdmin)

class ContractsAdmin(admin.ModelAdmin):
    list_display = ('ContractNumber','CustomerID','PrePayment','ContractPrice','ContractConfirmDate','ContractConfirmDateJalali','IsCancelled','IsExpanded','ValueAddedTax','jEntryDate','AgentNameID','CancelingDate','CancelingDateJalali')
    search_fields = ('ContractNumber','CustomerID','PrePayment','ContractPrice','ContractConfirmDate','ContractConfirmDateJalali','IsCancelled','IsExpanded','ValueAddedTax','jEntryDate','AgentNameID','CancelingDate','CancelingDateJalali')
admin.site.register(Contracts, ContractsAdmin)

class ContractDetailsPerBoardAdmin(admin.ModelAdmin):
    list_display = ('ContractID','BoardID','BoardContractPrice','DailyPrice','ContractStart','JalaliStart','ContractFinish','JalaliFinish','AgentNameID','ContractYearBase','jEntryDate')
    search_fields = ('ContractID','BoardID','BoardContractPrice','DailyPrice','ContractStart','JalaliStart','ContractFinish','JalaliFinish','AgentNameID','ContractYearBase','jEntryDate')
admin.site.register(ContractDetailsPerBoard, ContractDetailsPerBoardAdmin)

class SalesPackagesAdmin(admin.ModelAdmin):
    list_display = ('PackageName','AgentNameID','ActivityStatus','jEntryDate')
    search_fields = ('PackageName','AgentNameID','ActivityStatus','jEntryDate')
admin.site.register(SalesPackages, SalesPackagesAdmin)

class PackageDetailsPerBoardAdmin(admin.ModelAdmin):
    list_display = ('PackageID','BoardID','ActivityStatus','DeactivationDate','DeactivationDateJalali','ActivationDate','ActivationDateJalali','jEntryDate')
    search_fields = ('PackageID','BoardID','ActivityStatus','DeactivationDate','DeactivationDateJalali','ActivationDate','ActivationDateJalali','jEntryDate')
admin.site.register(PackageDetailsPerBoard, PackageDetailsPerBoardAdmin)

class CustomerPaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('CustomerPaymentMethodName','jEntryDate')
    search_fields = ('CustomerPaymentMethodName','jEntryDate')
admin.site.register(CustomerPaymentMethod, CustomerPaymentMethodAdmin)

class InstallmentAdmin(admin.ModelAdmin):
    list_display = ('ContractID','InstallmentNumber','InstallmentNumber','CustomerPaymentMethodID','PaymentDate','PaymentDateJalali','jEntryDate')
    search_fields = ('ContractID','InstallmentNumber','InstallmentNumber','CustomerPaymentMethodID','PaymentDate','PaymentDateJalali','jEntryDate')
admin.site.register(Installment, InstallmentAdmin)
