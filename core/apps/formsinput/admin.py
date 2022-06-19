from django.contrib import admin
from .models import ProductTypes, PackageTypes, MeasuringUnits, CommodityCategories, CommoditySubCategories, Brands, ProviderTypes, Providers, Commodities, Roles, FAgents, Procurements, Recipes, RecipeIngredients,Inventories,InventoryList,Outputs, Inputs, Sales, Orders

# Register your models here.

class ProductTypesAdmin(admin.ModelAdmin):
    list_display = ('ProductTypeTitle','EntryDate')
    search_fields = ('ProductTypeTitle','EntryDate')
admin.site.register(ProductTypes, ProductTypesAdmin)


class PackageTypesAdmin(admin.ModelAdmin):
    list_display = ('PackageTypeTitle','EntryDate')
    search_fields = ('PackageTypeTitle','EntryDate')
admin.site.register(PackageTypes, PackageTypesAdmin)


class MeasuringUnitsAdmin(admin.ModelAdmin):
    list_display = ('MeasuringUnitTitle','EntryDate')
    search_fields = ('MeasuringUnitTitle','EntryDate')
admin.site.register(MeasuringUnits, MeasuringUnitsAdmin)


class CommodityCategoriesAdmin(admin.ModelAdmin):
    list_display = ('CommodityCategory','EntryDate')
    search_fields = ('CommodityCategory','EntryDate')
admin.site.register(CommodityCategories, CommodityCategoriesAdmin)


class CommoditySubCategoriesAdmin(admin.ModelAdmin):
    list_display = ('CommoditySubCategory','CommodityCatID','EntryDate')
    search_fields = ('CommoditySubCategory','CommodityCatID','EntryDate')
admin.site.register(CommoditySubCategories, CommoditySubCategoriesAdmin)


class BrandsAdmin(admin.ModelAdmin):
    list_display = ('BrandName','EntryDate')
    search_fields = ('BrandName','EntryDate')
admin.site.register(Brands, BrandsAdmin)


class ProviderTypesAdmin(admin.ModelAdmin):
    list_display = ('ProviderTypeTitle','EntryDate')
    search_fields = ('ProviderTypeTitle','EntryDate')
admin.site.register(ProviderTypes, ProviderTypesAdmin)


class ProvidersAdmin(admin.ModelAdmin):
    list_display = ('ProviderName','ProviderTypeID','EntryDate')
    search_fields = ('ProviderName','ProviderTypeID','EntryDate')
admin.site.register(Providers, ProvidersAdmin)


class CommoditiesAdmin(admin.ModelAdmin):
    list_display = ('CommodityName','CommodityCatID','CommoditySubCatID','BrandID','EntryDate')
    search_fields = ('CommodityName','CommodityCatID','CommoditySubCatID','BrandID','EntryDate')
admin.site.register(Commodities, CommoditiesAdmin)


class RolesAdmin(admin.ModelAdmin):
    list_display = ('RoleTitle','EntryDate')
    search_fields = ('RoleTitle','EntryDate')
admin.site.register(Roles, RolesAdmin)


class FAgentsAdmin(admin.ModelAdmin):
    list_display = ('AgentFirstName','AgentLastName','AgentRoleID','EntryDate')
    search_fields = ('AgentFirstName','AgentLastName','AgentRoleID','EntryDate')
admin.site.register(FAgents, FAgentsAdmin)


class ProcurementsAdmin(admin.ModelAdmin):
    list_display = ('CommodityID','UnitPrice','PackageTypeID','MeasuringUnitID','ProviderID','Price','PackageCount','PackageUnitValue','EntryDate')
    search_fields = ('CommodityID','UnitPrice','PackageTypeID','MeasuringUnitID','ProviderID','Price','PackageCount','PackageUnitValue','EntryDate')
admin.site.register(Procurements, ProcurementsAdmin)


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('Creator','RecipeName','LastVersionRecipeID','StartingYear','ProductTypeID','Version','EntryDate')
    search_fields = ('Creator','RecipeName','LastVersionRecipeID','StartingYear','ProductTypeID','Version','EntryDate')
admin.site.register(Recipes, RecipesAdmin)


class RecipeIngredientsAdmin(admin.ModelAdmin):
    list_display = ('RecipeID','CommodityID','MeasuringUnitID','Quantity','EntryDate')
    search_fields = ('RecipeID','CommodityID','MeasuringUnitID','Quantity','EntryDate')
admin.site.register(RecipeIngredients, RecipeIngredientsAdmin)


class InventoriesAdmin(admin.ModelAdmin):
    list_display = ('InventoryName','EntryDate')
    search_fields = ('InventoryName','EntryDate')
admin.site.register(Inventories, InventoriesAdmin)


class InventoryListAdmin(admin.ModelAdmin):
    list_display = ('InventoryID','ProcurementID','RemainingPackageCount','UpdateDate')
    search_fields = ('InventoryID','ProcurementID','RemainingPackageCount','UpdateDate')
admin.site.register(InventoryList, InventoryListAdmin)


class OutputsAdmin(admin.ModelAdmin):
    list_display = ('DeliveryAgent','ProcurementID','FromInventoryID','TransferedDate','TransferedDateJalali','TransferedQuantity','EntryDate')
    search_fields = ('DeliveryAgent','ProcurementID','FromInventoryID','TransferedDate','TransferedDateJalali','TransferedQuantity','EntryDate')
admin.site.register(Outputs, OutputsAdmin)


class InputsAdmin(admin.ModelAdmin):
    list_display = ('TransfereeAgent','ProcurementID','ToInventoryID','TransferedDate','TransferedDateJalali','TransferedQuantity','EntryDate')
    search_fields = ('TransfereeAgent','ProcurementID','ToInventoryID','TransferedDate','TransferedDateJalali','TransferedQuantity','EntryDate')
admin.site.register(Inputs, InputsAdmin)


class SalesAdmin(admin.ModelAdmin):
    list_display = ('FoodName','FoodPrice','Quantity','RecipeID','EntryDate')
    search_fields = ('FoodName','FoodPrice','Quantity','RecipeID','EntryDate')
admin.site.register(Sales, SalesAdmin)

class OrdersAdmin(admin.ModelAdmin):
    list_display = ('ItemCategory','Unitprice','ItemType','Hour','OrderDate')
    search_fields = ('ItemCategory','Unitprice','ItemType','Hour','OrderDate')
admin.site.register(Orders, OrdersAdmin)
