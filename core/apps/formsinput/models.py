from django.db import models
from django_jalali.db import models as jmodels

# Create your models here.
class ProductTypes(models.Model):
    ProductTypeTitle = models.CharField(max_length=200, null=True, verbose_name="نوع کالا")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "نوع کالا"
        verbose_name_plural = "انواع کالا"

    def __str__(self):
        return self.ProductTypeTitle

class PackageTypes(models.Model):
    PackageTypeTitle = models.CharField(max_length=200, null=True, verbose_name="نوع بسته‌بندی")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "نوع بسته‌بندی"
        verbose_name_plural = "انواع بسته‌بندی"

    def __str__(self):
        return self.PackageTypeTitle


class MeasuringUnits(models.Model):
    MeasuringUnitTitle = models.CharField(max_length=200, null=True, verbose_name="واحد اندازه‌گیری")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "واحد اندازه‌گیری"
        verbose_name_plural = "واحدهای اندازه‌گیری"

    def __str__(self):
        return self.MeasuringUnitTitle


class CommodityCategories(models.Model):
    CommodityCategory = models.CharField(max_length=200, null=True, verbose_name="دسته‌بندی اصلی اقلام")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "دسته‌بندی اصلی اقلام"
        verbose_name_plural = "دسته‌بندی‌های اصلی اقلام"

    def __str__(self):
        return self.CommodityCategory


class CommoditySubCategories(models.Model):
    CommoditySubCategory = models.CharField(max_length=200, null=True, verbose_name="دسته‌بندی فرعی اقلام")
    CommodityCatID = models.ForeignKey(CommodityCategories, on_delete=models.CASCADE, verbose_name="دسته‌بندی اصلی")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "دسته‌بندی فرعی اقلام"
        verbose_name_plural = "دسته‌بندی‌های فرعی اقلام"

    def __str__(self):
        return self.CommoditySubCategory


class Brands(models.Model):
    BrandName = models.CharField(max_length=200, null=True, verbose_name="نام برند")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "برند"
        verbose_name_plural = "برندها"

    def __str__(self):
        return self.BrandName


class ProviderTypes(models.Model):
    ProviderTypeTitle = models.CharField(max_length=200, null=True, verbose_name="نوع تامین کننده")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "نوع تامین کننده"
        verbose_name_plural = "انواع تامین کننده"

    def __str__(self):
        return self.ProviderTypeTitle


class Providers(models.Model):
    ProviderName = models.CharField(max_length=200, null=True, verbose_name="نام تامین کننده")
    ProviderTypeID = models.ForeignKey(CommodityCategories, on_delete=models.CASCADE, verbose_name="نوع تامین کننده")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "تامین کننده"
        verbose_name_plural = "تامین کنندگان"

    def __str__(self):
        return self.ProviderName



class Commodities(models.Model):
    CommodityName = models.CharField(max_length=200, null=True, verbose_name="نام قلم کالا")
    CommodityCatID = models.ForeignKey(CommodityCategories, on_delete=models.CASCADE, verbose_name="دسته‌بندی اصلی قلم کالا")
    CommoditySubCatID = models.ForeignKey(CommoditySubCategories, on_delete=models.CASCADE, verbose_name="دسته‌بندی فرعی قلم کالا")
    BrandID = models.ForeignKey(Brands, on_delete=models.CASCADE, verbose_name="برند")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "قلم کالا"
        verbose_name_plural = "لیست اقلام"

    def __str__(self):
        return self.CommodityName



class Roles(models.Model):
    RoleTitle = models.CharField(max_length=200, null=True, verbose_name="نام نقش")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "نقش"
        verbose_name_plural = "نقش‌ها"

    def __str__(self):
        return self.RoleTitle


class FAgents(models.Model):
    AgentFirstName = models.CharField(max_length=200, null=True, verbose_name="نام مسئول")
    AgentLastName = models.CharField(max_length=200, null=True, verbose_name="نام خانوادگی مسئول")
    AgentRoleID = models.ForeignKey(Roles, on_delete=models.CASCADE, verbose_name="نقش")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "مسئول"
        verbose_name_plural = "مسئول‌ها"

    def __str__(self):
        return self.AgentFirstName,self.AgentLastName


class Procurements(models.Model):
    CommodityID =  models.ForeignKey(Commodities, on_delete=models.CASCADE, verbose_name="قلم کالا")
    UnitPrice = models.FloatField(null=True, verbose_name="قیمت واحد")
    PackageTypeID =  models.ForeignKey(PackageTypes, on_delete=models.CASCADE, verbose_name="نوع بسته‌بندی")
    MeasuringUnitID =  models.ForeignKey(MeasuringUnits, on_delete=models.CASCADE, verbose_name="واحد اندازه‌گیری")
    ProviderID =  models.ForeignKey(Providers, on_delete=models.CASCADE, verbose_name="تامین‌کننده")
    Price = models.FloatField(null=True, verbose_name="قیمت")
    PackageCount = models.IntegerField(null=True, verbose_name="تعداد")
    PackageUnitValue =  models.FloatField(null=True, verbose_name="مقدار در بسته‌بندی")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "خرید"
        verbose_name_plural = "لیست خرید"

    def __str__(self):
        return self.CommodityID



class Recipes(models.Model):
    Creator = models.CharField(max_length=200, null=True, verbose_name="ایجاد کننده")
    RecipeName = models.CharField(max_length=200, null=True, verbose_name="نام دستور پخت")
    LastVersionRecipeID = models.CharField(max_length=200, null=True, verbose_name="آیدی آخرین نسخه")
    StartingYear = models.CharField(max_length=20, null=True, verbose_name="سال شروع")
    ProductTypeID =  models.ForeignKey(ProductTypes, on_delete=models.CASCADE, verbose_name="نوع کالا")
    Version = models.CharField(max_length=200, null=True, verbose_name="شماره نسخه")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "دستور پخت"
        verbose_name_plural = "دستورهای پخت"

    def __str__(self):
        return self.RecipeName


class RecipeIngredients(models.Model):
    RecipeID =  models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name="دستور پخت")
    CommodityID =  models.ForeignKey(Commodities, on_delete=models.CASCADE, verbose_name="قلم کالا")
    MeasuringUnitID =  models.ForeignKey(MeasuringUnits, on_delete=models.CASCADE, verbose_name="واحد اندازه‌گیری")
    Quantity = models.FloatField(null=True, verbose_name="مقدار")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "جزئیات دستور پخت"
        verbose_name_plural = "جزئیات دستورهای پخت"

    def __str__(self):
        return self.RecipeID,self.CommodityID


class Inventories(models.Model):
    InventoryName = models.CharField(max_length=200, null=True, verbose_name="نام انبار")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "انبار"
        verbose_name_plural = "انبارها"

    def __str__(self):
        return self.InventoryName


class InventoryList(models.Model):
    InventoryID =  models.ForeignKey(Inventories, on_delete=models.CASCADE, verbose_name="انبار")
    ProcurementID =  models.ForeignKey(Procurements, on_delete=models.CASCADE, verbose_name="ردیف خرید")
    RemainingPackageCount = models.IntegerField(null=True, verbose_name="تعداد باقی‌مانده")
    UpdateDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ به روز رسانی")

    class Meta:
        verbose_name = "اقلام انبار"
        verbose_name_plural = "لیست انبار"

    def __str__(self):
        return self.InventoryID,self.ProcurementID,self.RemainingPackageCount,self.UpdateDate


class Outputs(models.Model):
    DeliveryAgent =  models.ForeignKey(FAgents, on_delete=models.CASCADE, verbose_name="مسئول تحویل")
    ProcurementID =  models.ForeignKey(Procurements, on_delete=models.CASCADE, verbose_name="ردیف خرید")
    FromInventoryID =  models.ForeignKey(Inventories, on_delete=models.CASCADE, verbose_name="انبار")
    TransferedDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ میلادی خروج")
    TransferedDateJalali = jmodels.jDateTimeField(max_length=200, null=True, verbose_name="تاریخ شمسی خروج")
    TransferedQuantity = models.FloatField(null=True, verbose_name="مقدار")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "خروجی"
        verbose_name_plural = "خروجی‌ها"

    def __str__(self):
        return self.ProcurementID,self.FromInventoryID,self.TransferedDateJalali



class Inputs(models.Model):
    TransfereeAgent =  models.ForeignKey(FAgents, on_delete=models.CASCADE, verbose_name="مسئول تحویل")
    ProcurementID =  models.ForeignKey(Procurements, on_delete=models.CASCADE, verbose_name="ردیف خرید")
    ToInventoryID =  models.ForeignKey(Inventories, on_delete=models.CASCADE, verbose_name="انبار")
    TransferedDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ میلادی خروج")
    TransferedDateJalali = jmodels.jDateTimeField(max_length=200, null=True, verbose_name="تاریخ شمسی خروج")
    TransferedQuantity = models.FloatField(null=True, verbose_name="مقدار")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "ورودی"
        verbose_name_plural = "ورودی‌ها"

    def __str__(self):
        return self.ProcurementID,self.ToInventoryID,self.TransferedDateJalali



class Sales(models.Model):
    FoodName = models.CharField(max_length=200, null=True, verbose_name="نام غذا")
    FoodPrice = models.FloatField(max_length=200, null=True, verbose_name="قیمت غذا")
    Quantity = models.FloatField(null=True, verbose_name="مقدار")
    RecipeID =  models.ForeignKey(Recipes, on_delete=models.CASCADE, verbose_name="دستور پخت")
    EntryDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "فروش"
        verbose_name_plural = "فروش"

    def __str__(self):
        return self.FoodName,self.Quantity,self.EntryDate


class Orders(models.Model):
    ItemCategory = models.CharField(max_length=200, null=True, verbose_name="دسته‌بندی آیتم")
    Unitprice  = models.CharField(max_length=200, null=True, verbose_name="قیمت واحد")
    ItemType = models.CharField(max_length=200, null=True, verbose_name="نوع آیتم")
    Hour = models.CharField(max_length=200, null=True, verbose_name="ساعت")
    OrderDate = models.DateTimeField(max_length=200, null=True, verbose_name="تاریخ ثبت رکورد")

    class Meta:
        verbose_name = "سفارشات"
        verbose_name_plural = "سفارشات"

    def __str__(self):
        return self.OrderDate,self.Hour,self.ItemCategory
