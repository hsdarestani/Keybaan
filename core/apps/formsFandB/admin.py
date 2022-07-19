from django.contrib import admin
from .models import ProductTypes, PackageTypes, MeasuringUnits, CommodityType ,PriceList,ConvertingMeasureUnits ,CommodityCategories, CommoditySubCategories, Brands, ProviderTypes, Providers, Commodities, Roles, FAgents, Procurements, Recipes, RecipeIngredients,Inventories,InventoryList,Outputs, Inputs, Sales, Orders

# Register your models here.

class ProductTypesAdmin(admin.ModelAdmin):
    list_display = ('ProductTypeTitle','jEntryDate')
    search_fields = ('ProductTypeTitle','jEntryDate')
admin.site.register(ProductTypes, ProductTypesAdmin)


class PackageTypesAdmin(admin.ModelAdmin):
    list_display = ('PackageTypeTitle','jEntryDate')
    search_fields = ('PackageTypeTitle','jEntryDate')
admin.site.register(PackageTypes, PackageTypesAdmin)


class MeasuringUnitsAdmin(admin.ModelAdmin):
    list_display = ('MeasuringUnitTitle','jEntryDate')
    search_fields = ('MeasuringUnitTitle','jEntryDate')
admin.site.register(MeasuringUnits, MeasuringUnitsAdmin)


class CommodityCategoriesAdmin(admin.ModelAdmin):
    list_display = ('CommodityCategory','jEntryDate')
    search_fields = ('CommodityCategory','jEntryDate')
admin.site.register(CommodityCategories, CommodityCategoriesAdmin)


class CommoditySubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('CommoditySubCategory','CommodityCatID','jEntryDate')
    search_fields = ('CommoditySubCategory','CommodityCatID','jEntryDate')
admin.site.register(CommoditySubCategories, CommoditySubCategoriesAdmin)

class CommodityTypeAdmin(admin.ModelAdmin):
    list_display = ('CommodityTypeName','CommoditySubCatID','MeasuringUnitID','jEntryDate')
    search_fields = ('CommodityTypeName','CommoditySubCatID','MeasuringUnitID','jEntryDate')
admin.site.register(CommodityType, CommodityTypeAdmin)

class ConvertingMeasureUnitsAdmin(admin.ModelAdmin):
    list_display = ('ConvertingUnitName','MeasuringUnitID','ConvertingRatio','jEntryDate')
    search_fields = ('ConvertingUnitName','MeasuringUnitID','ConvertingRatio','jEntryDate')
admin.site.register(ConvertingMeasureUnits, ConvertingMeasureUnitsAdmin)

class BrandsAdmin(admin.ModelAdmin):
    list_display = ('BrandName','jEntryDate')
    search_fields = ('BrandName','jEntryDate')
admin.site.register(Brands, BrandsAdmin)


class ProviderTypesAdmin(admin.ModelAdmin):
    list_display = ('ProviderTypeTitle','jEntryDate')
    search_fields = ('ProviderTypeTitle','jEntryDate')
admin.site.register(ProviderTypes, ProviderTypesAdmin)


class ProvidersAdmin(admin.ModelAdmin):
    list_display = ('ProviderName','ProviderTypeID','jEntryDate')
    search_fields = ('ProviderName','ProviderTypeID','jEntryDate')
admin.site.register(Providers, ProvidersAdmin)


class CommoditiesAdmin(admin.ModelAdmin):
    list_display = ('PackageTypeID','CommodityTypeID','BrandID','jEntryDate')
    search_fields = ('PackageTypeID','CommodityTypeID','BrandID','jEntryDate')
admin.site.register(Commodities, CommoditiesAdmin)


class RolesAdmin(admin.ModelAdmin):
    list_display = ('RoleTitle','jEntryDate')
    search_fields = ('RoleTitle','jEntryDate')
admin.site.register(Roles, RolesAdmin)

class PriceListAdmin(admin.ModelAdmin):
    list_display = ('RecipeID','Price','ActivationDate','DeactivationDate','jEntryDate')
    search_fields = ('RecipeID','Price','ActivationDate','DeactivationDate','jEntryDate')
admin.site.register(PriceList, PriceListAdmin)

class FAgentsAdmin(admin.ModelAdmin):
    list_display = ('AgentFirstName','AgentLastName','AgentRoleID','jEntryDate')
    search_fields = ('AgentFirstName','AgentLastName','AgentRoleID','jEntryDate')
admin.site.register(FAgents, FAgentsAdmin)


class ProcurementsAdmin(admin.ModelAdmin):
    list_display = ('CommodityID','UnitPrice','PackageTypeID','MeasuringUnitID','ProviderID','Price','PackageCount','PackageUnitValue','jEntryDate')
    search_fields = ('CommodityID','UnitPrice','PackageTypeID','MeasuringUnitID','ProviderID','Price','PackageCount','PackageUnitValue','jEntryDate')
admin.site.register(Procurements, ProcurementsAdmin)


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('Creator','RecipeName','LastVersionRecipeID','StartingYear','ProductTypeID','Version','jEntryDate')
    search_fields = ('Creator','RecipeName','LastVersionRecipeID','StartingYear','ProductTypeID','Version','jEntryDate')
admin.site.register(Recipes, RecipesAdmin)


class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = ('RecipeID','CommodityID','MeasuringUnitID','Quantity','jEntryDate')
    search_fields = ('RecipeID','CommodityID','MeasuringUnitID','Quantity','jEntryDate')
admin.site.register(RecipeIngredients, RecipeIngredientsAdmin)


class InventoriesAdmin(admin.ModelAdmin):
    list_display = ('InventoryName','jEntryDate')
    search_fields = ('InventoryName','jEntryDate')
admin.site.register(Inventories, InventoriesAdmin)


class InventoryListAdmin(admin.ModelAdmin):
    list_display = ('InventoryID','CommodityID','ProcurementID','RemainingPackageCount','jEntryDate')
    search_fields = ('InventoryID','CommodityID','ProcurementID','RemainingPackageCount','jEntryDate')
admin.site.register(InventoryList, InventoryListAdmin)


class OutputsAdmin(admin.ModelAdmin):
    list_display = ('DeliveryAgent','CommodityID','ProcurementID','FromInventoryID','TransferedDate','TransferedDateJalali','TransferedQuantity','jEntryDate')
    search_fields = ('DeliveryAgent','CommodityID','ProcurementID','FromInventoryID','TransferedDate','TransferedDateJalali','TransferedQuantity','jEntryDate')
admin.site.register(Outputs, OutputsAdmin)


class InputsAdmin(admin.ModelAdmin):
    list_display = ('TransfereeAgent','CommodityID','ProcurementID','ToInventoryID','TransferedDate','TransferedDateJalali','TransferedQuantity','jEntryDate')
    search_fields = ('TransfereeAgent','CommodityID','ProcurementID','ToInventoryID','TransferedDate','TransferedDateJalali','TransferedQuantity','jEntryDate')
admin.site.register(Inputs, InputsAdmin)


class SalesAdmin(admin.ModelAdmin):
    list_display = ('FoodName','FoodPrice','Quantity','RecipeID','jEntryDate')
    search_fields = ('FoodName','FoodPrice','Quantity','RecipeID','jEntryDate')
admin.site.register(Sales, SalesAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('ItemCategory','Unitprice','ItemType','Hour','jEntryDate')
    search_fields = ('ItemCategory','Unitprice','ItemType','Hour','jEntryDate')
admin.site.register(Orders, OrdersAdmin)
