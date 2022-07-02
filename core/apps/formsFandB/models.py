from django.db import models
from django_jalali.db import models as jmodels
from extensions.utils import jalali_converter
from apps.useraccount.models import Profile , Company

# Create your models here.
class ProductTypes(models.Model):
    ProductTypeTitle = models.CharField(max_length=200, null=True, verbose_name="نوع کالا")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "نوع کالا"
        verbose_name_plural = "انواع کالا"

    def __str__(self):
        return self.ProductTypeTitle

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class PackageTypes(models.Model):
    PackageTypeTitle = models.CharField(max_length=200, null=True, verbose_name="نوع بسته‌بندی")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "نوع بسته‌بندی"
        verbose_name_plural = "انواع بسته‌بندی"

    def __str__(self):
        return self.PackageTypeTitle

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class MeasuringUnits(models.Model):
    MeasuringUnitTitle = models.CharField(max_length=200, null=True, verbose_name="واحد اندازه‌گیری")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "واحد اندازه‌گیری"
        verbose_name_plural = "واحدهای اندازه‌گیری"

    def __str__(self):
        return self.MeasuringUnitTitle

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class CommodityCategories(models.Model):
    CommodityCategory = models.CharField(max_length=200, null=True, verbose_name="دسته‌بندی اصلی اقلام")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "دسته‌بندی اصلی اقلام"
        verbose_name_plural = "دسته‌بندی‌های اصلی اقلام"

    def __str__(self):
        return self.CommodityCategory

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class CommoditySubCategories(models.Model):
    CommoditySubCategory = models.CharField(max_length=200, null=True, verbose_name="دسته‌بندی فرعی اقلام")
    CommodityCatID = models.ForeignKey(CommodityCategories, on_delete=models.CASCADE, verbose_name="دسته‌بندی اصلی")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "دسته‌بندی فرعی اقلام"
        verbose_name_plural = "دسته‌بندی‌های فرعی اقلام"

    def __str__(self):
        return self.CommoditySubCategory

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class Brands(models.Model):
    BrandName = models.CharField(max_length=200, null=True, verbose_name="نام برند")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return self.BrandName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class ProviderTypes(models.Model):
    ProviderTypeTitle = models.CharField(max_length=200, null=True, verbose_name="نوع تامین کننده")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "نوع تامین کننده"
        verbose_name_plural = "انواع تامین کننده"

    def __str__(self):
        return self.ProviderTypeTitle

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class Providers(models.Model):
    ProviderName = models.CharField(max_length=200, null=True, verbose_name="نام تامین کننده")
    ProviderTypeID = models.ForeignKey(ProviderTypes, on_delete=models.CASCADE, verbose_name="نوع تامین کننده")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "تامین کننده"
        verbose_name_plural = "تامین کنندگان"

    def __str__(self):
        return self.ProviderName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class Commodities(models.Model):
    CommodityName = models.CharField(max_length=200, null=True, verbose_name="نام قلم کالا")
    CommodityCatID = models.ForeignKey(CommodityCategories, on_delete=models.CASCADE, verbose_name="دسته‌بندی اصلی قلم کالا")
    CommoditySubCatID = models.ForeignKey(CommoditySubCategories, on_delete=models.CASCADE, verbose_name="دسته‌بندی فرعی قلم کالا")
    BrandID = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name="برند")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "قلم کالا"
        verbose_name_plural = "لیست اقلام"

    def __str__(self):
        return self.CommodityName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class Roles(models.Model):
    RoleTitle = models.CharField(max_length=200, null=True, verbose_name="نام نقش")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "نقش"
        verbose_name_plural = "نقش‌ها"

    def __str__(self):
        return self.RoleTitle

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class FAgents(models.Model):
    AgentFirstName = models.CharField(max_length=200, null=True, verbose_name="نام مسئول")
    AgentLastName = models.CharField(max_length=200, null=True, verbose_name="نام خانوادگی مسئول")
    AgentRoleID = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name="نقش")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "مسئول"
        verbose_name_plural = "مسئول‌ها"

    def __str__(self):
        return self.AgentFirstName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class Procurements(models.Model):
    CommodityID =  models.ForeignKey(Commodities, on_delete=models.CASCADE, verbose_name="قلم کالا")
    UnitPrice = models.FloatField(null=True, verbose_name="قیمت واحد")
    PackageTypeID =  models.ForeignKey(PackageTypes, on_delete=models.CASCADE, verbose_name="نوع بسته‌بندی")
    MeasuringUnitID =  models.ForeignKey(MeasuringUnits, on_delete=models.CASCADE, verbose_name="واحد اندازه‌گیری")
    ProviderID =  models.ForeignKey(Providers, on_delete=models.CASCADE, verbose_name="تامین‌کننده")
    Price = models.FloatField(null=True, verbose_name="قیمت")
    PackageCount = models.IntegerField(null=True, verbose_name="تعداد")
    PackageUnitValue =  models.FloatField(null=True, verbose_name="مقدار در بسته‌بندی")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "خرید"
        verbose_name_plural = "لیست خرید"

    def __str__(self):
        return str(self.CommodityID)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class Recipes(models.Model):
    Creator = models.CharField(max_length=200, null=True, verbose_name="ایجاد کننده")
    RecipeName = models.CharField(max_length=200, null=True, verbose_name="نام دستور پخت")
    LastVersionRecipeID = models.CharField(max_length=200, null=True, verbose_name="آیدی آخرین نسخه")
    StartingYear = models.CharField(max_length=20, null=True, verbose_name="سال شروع")
    ProductTypeID =  models.ForeignKey(ProductTypes, on_delete=models.CASCADE, verbose_name="نوع کالا")
    Version = models.CharField(max_length=200, null=True, verbose_name="شماره نسخه")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "دستور پخت"
        verbose_name_plural = "دستورهای پخت"

    def __str__(self):
        return self.RecipeName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class RecipeIngredients(models.Model):
    RecipeID =  models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name="دستور پخت")
    CommodityID =  models.ForeignKey(Commodities, on_delete=models.CASCADE, verbose_name="قلم کالا")
    MeasuringUnitID =  models.ForeignKey(MeasuringUnits, on_delete=models.CASCADE, verbose_name="واحد اندازه‌گیری")
    Quantity = models.FloatField(null=True, verbose_name="مقدار")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "جزئیات دستور پخت"
        verbose_name_plural = "جزئیات دستورهای پخت"

    def __str__(self):
        return str(self.RecipeID) + ' ' + str(self.CommodityID)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class Inventories(models.Model):
    InventoryName = models.CharField(max_length=200, null=True, verbose_name="نام انبار")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "انبار"
        verbose_name_plural = "انبارها"

    def __str__(self):
        return self.InventoryName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class InventoryList(models.Model):
    InventoryID =  models.ForeignKey(Inventories, on_delete=models.CASCADE, verbose_name="انبار")
    ProcurementID =  models.ForeignKey(Procurements, on_delete=models.CASCADE, verbose_name="ردیف خرید")
    RemainingPackageCount = models.IntegerField(null=True, verbose_name="تعداد باقی‌مانده")
    UpdateDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ به روز رسانی")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "اقلام انبار"
        verbose_name_plural = "لیست انبار"

    def __str__(self):
        return str(self.InventoryID) + ' ' + str(self.ProcurementID) + ' ' + str(self.RemainingPackageCount) + ' ' + str(self.UpdateDate)

    def jEntryDate(self):
        return jalali_converter(self.UpdateDate)
    jEntryDate.short_description = "تاریخ به روز رسانی"


class Outputs(models.Model):
    DeliveryAgent =  models.ForeignKey(FAgents, on_delete=models.CASCADE,null=True, blank=True, verbose_name="مسئول تحویل")
    ProcurementID =  models.ForeignKey(Procurements, on_delete=models.CASCADE,null=True, blank=True, verbose_name="ردیف خرید")
    FromInventoryID =  models.ForeignKey(Inventories, on_delete=models.CASCADE,null=True, blank=True, verbose_name="انبار")
    TransferedDate = models.DateField(max_length=200, null=True, verbose_name="تاریخ میلادی خروج")
    TransferedDateJalali = jmodels.jDateField(max_length=200, null=True, verbose_name="تاریخ شمسی خروج")
    TransferedQuantity = models.FloatField(null=True, verbose_name="مقدار")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "خروجی"
        verbose_name_plural = "خروجی‌ها"

    def __str__(self):
        return str(self.ProcurementID) + ' ' + str(self.FromInventoryID) + ' ' + str(self.TransferedDateJalali)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"



class Inputs(models.Model):
    TransfereeAgent =  models.ForeignKey(FAgents, on_delete=models.CASCADE,null=True, blank=True, verbose_name="مسئول تحویل")
    ProcurementID =  models.ForeignKey(Procurements, on_delete=models.CASCADE, null=True, blank=True,verbose_name="ردیف خرید")
    ToInventoryID =  models.ForeignKey(Inventories, on_delete=models.CASCADE, null=True, blank=True,verbose_name="انبار")
    TransferedDate = models.DateField(max_length=200, null=True, blank=True, verbose_name="تاریخ میلادی خروج")
    TransferedDateJalali = jmodels.jDateField(max_length=200, null=True, blank=True, verbose_name="تاریخ شمسی خروج")
    TransferedQuantity = models.FloatField(null=True, blank=True, verbose_name="مقدار")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "ورودی"
        verbose_name_plural = "ورودی‌ها"

    def __str__(self):
        return str(self.ProcurementID) + ' ' + str(self.ToInventoryID) + ' ' + str(self.TransferedDateJalali)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"



class Sales(models.Model):
    FoodName = models.CharField(max_length=200, null=True, verbose_name="نام غذا")
    FoodPrice = models.FloatField(max_length=200, null=True, verbose_name="قیمت غذا")
    Quantity = models.FloatField(null=True, verbose_name="مقدار")
    RecipeID =  models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name="دستور پخت")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "فروش"
        verbose_name_plural = "فروش"

    def __str__(self):
        return str(self.FoodName) + ' ' + str(self.Quantity) + ' ' + str(self.EntryDate)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class Orders(models.Model):
    ItemCategory = models.CharField(max_length=200, null=True, verbose_name="دسته‌بندی آیتم")
    Unitprice  = models.CharField(max_length=200, null=True, verbose_name="قیمت واحد")
    ItemType = models.CharField(max_length=200, null=True, verbose_name="نوع آیتم")
    Hour = models.CharField(max_length=200, null=True, verbose_name="ساعت")
    OrderDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "سفارشات"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return str(self.OrderDate) + ' ' + str(self.Hour) + ' ' + str(self.ItemCategory)

    def jEntryDate(self):
        return jalali_converter(self.OrderDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"
