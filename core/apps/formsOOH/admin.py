from django.contrib import admin
from .models import OBoardTypes,OTariff,OOperation,OContractorPayment,OBoards,OContractor,OOperationType,OContracts,OContractDetailsPerBoard,OCustomers,OLocations,Contracts,Agents,Customers,Cities,IranProvinces, BoardTypes,LocationTypes,Locations,Boards,ContractDetailsPerBoard,PackageDetailsPerBoard,SalesPackages,CustomerPaymentMethod,Installment,AgentPaymentMethods
# Register your models here.

class IranProvincesAdmin(admin.ModelAdmin):
    list_display = ('ProvinceName','jEntryDate')
    search_fields = ('ProvinceName','jEntryDate')
admin.site.register(IranProvinces, IranProvincesAdmin)

class BoardTypesAdmin(admin.ModelAdmin):
    list_display = ('BoardType','jEntryDate')
    search_fields = ('BoardType','jEntryDate')
admin.site.register(BoardTypes, BoardTypesAdmin)

class OBoardTypesAdmin(admin.ModelAdmin):
    list_display = ('BoardType','jEntryDate')
    search_fields = ('BoardType','jEntryDate')
admin.site.register(OBoardTypes, OBoardTypesAdmin)

class LocationTypesAdmin(admin.ModelAdmin):
    list_display = ('LocationTypeName','jEntryDate')
    search_fields = ('LocationTypeName','jEntryDate')
admin.site.register(LocationTypes, LocationTypesAdmin)

class LocationsAdmin(admin.ModelAdmin):
    list_display = ('LocationName','LocationCode','LocationTypeID','Longitude','Latitude','CityID','ActivityStatus','jEntryDate')
    search_fields = ('LocationName','LocationCode','LocationTypeID','Longitude','Latitude','CityID','ActivityStatus','jEntryDate')
admin.site.register(Locations, LocationsAdmin)

class OLocationsAdmin(admin.ModelAdmin):
    list_display = ('LocationName','LocationCode','LocationTypeID','Longitude','Latitude','CityID','jEntryDate')
    search_fields = ('LocationName','LocationCode','LocationTypeID','Longitude','Latitude','CityID','jEntryDate')
admin.site.register(OLocations, OLocationsAdmin)

class CitiesAdmin(admin.ModelAdmin):
    list_display = ('CityName','ProvinceID','jEntryDate')
    search_fields = ('CityName','ProvinceID','jEntryDate')
admin.site.register(Cities, CitiesAdmin)

class BoardsAdmin(admin.ModelAdmin):
    list_display = ('BoardCode','BoardTypeID','LocationID','BoardScore','BoardDescription','Dimenstions','PlacementComments','Area','ActivityStatus','jEntryDate')
    search_fields = ('BoardCode','BoardTypeID','LocationID','BoardScore','BoardDescription','Dimenstions','PlacementComments','Area','ActivityStatus','jEntryDate')
admin.site.register(Boards, BoardsAdmin)

class OBoardsAdmin(admin.ModelAdmin):
    list_display = ('BoardCode','BoardTypeID','LocationID','Area','jEntryDate')
    search_fields = ('BoardCode','BoardTypeID','LocationID','Area','jEntryDate')
admin.site.register(OBoards, OBoardsAdmin)

class CustomersAdmin(admin.ModelAdmin):
    list_display = ('CustomerName','jEntryDate')
    search_fields = ('CustomerName','jEntryDate')
admin.site.register(Customers, CustomersAdmin)

class OCustomersAdmin(admin.ModelAdmin):
    list_display = ('CustomerName','jEntryDate')
    search_fields = ('CustomerName','jEntryDate')
admin.site.register(OCustomers, OCustomersAdmin)

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

class OContractsAdmin(admin.ModelAdmin):
    list_display = ('ContractNumber','CustomerID','jEntryDate')
    search_fields = ('ContractNumber','CustomerID','jEntryDate')
admin.site.register(OContracts, OContractsAdmin)

class ContractDetailsPerBoardAdmin(admin.ModelAdmin):
    list_display = ('ContractID','BoardID','BoardContractPrice','DailyPrice','ContractStart','JalaliStart','ContractFinish','JalaliFinish','AgentNameID','ContractYearBase','jEntryDate')
    search_fields = ('ContractID','BoardID','BoardContractPrice','DailyPrice','ContractStart','JalaliStart','ContractFinish','JalaliFinish','AgentNameID','ContractYearBase','jEntryDate')
admin.site.register(ContractDetailsPerBoard, ContractDetailsPerBoardAdmin)

class OContractDetailsPerBoardAdmin(admin.ModelAdmin):
    list_display = ('ContractID','BoardID','jEntryDate')
    search_fields = ('ContractID','BoardID','jEntryDate')
admin.site.register(OContractDetailsPerBoard, OContractDetailsPerBoardAdmin)

class OOperationTypeAdmin(admin.ModelAdmin):
    list_display = ('OperationType','jEntryDate')
    search_fields = ('OperationType','jEntryDate')
admin.site.register(OOperationType, OOperationTypeAdmin)

class OContractorAdmin(admin.ModelAdmin):
    list_display = ('Contractor','ContractorType','jEntryDate')
    search_fields = ('Contractor','ContractorType','jEntryDate')
admin.site.register(OContractor, OContractorAdmin)

class OContractorPaymentAdmin(admin.ModelAdmin):
    list_display = ('ContractorID','PaymentFee','PaymentDateJalali','jEntryDate')
    search_fields = ('ContractorID','PaymentFee','PaymentDateJalali','jEntryDate')
admin.site.register(OContractorPayment, OContractorPaymentAdmin)


class OOperationAdmin(admin.ModelAdmin):
    list_display = ('OperationTypeID','ContractDetailsID','ContractorID','OperationDateJalali','OperationFee','OperationTariff','jEntryDate')
    search_fields = ('OperationTypeID','ContractDetailsID','ContractorID','OperationDateJalali','OperationFee','OperationTariff','jEntryDate')
admin.site.register(OOperation, OOperationAdmin)

class OTariffAdmin(admin.ModelAdmin):
    list_display = ('CityID','TariffActivationDate','TariffDeactivationDate')
    search_fields = ('CityID','TariffActivationDate','TariffDeactivationDate')
admin.site.register(OTariff, OTariffAdmin)

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
    list_display = ('ContractID','Installment','InstallmentNumber','CustomerPaymentMethodID','PaymentDate','PaymentDateJalali','jEntryDate')
    search_fields = ('ContractID','Installment','InstallmentNumber','CustomerPaymentMethodID','PaymentDate','PaymentDateJalali','jEntryDate')
admin.site.register(Installment, InstallmentAdmin)
