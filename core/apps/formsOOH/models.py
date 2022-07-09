from django.db import models
from django_jalali.db import models as jmodels
from extensions.utils import jalali_converter
from apps.useraccount.models import Profile , Company

# Create your models here.
class IranProvinces(models.Model):
    ProvinceName = models.CharField(max_length=200, null=True, verbose_name="نام منطقه")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "منطقه"
        verbose_name_plural = "مناطق"

    def __str__(self):
        return self.ProvinceName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class Cities(models.Model):
    CityName = models.CharField(max_length=200, null=True, verbose_name="نام شهر")
    ProvinceID = models.ForeignKey(IranProvinces, on_delete=models.CASCADE, verbose_name="منطقه")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "شهر"
        verbose_name_plural = "شهرها"

    def __str__(self):
        return self.CityName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class BoardTypes(models.Model):
    BoardType = models.CharField(max_length=200, null=True, verbose_name="نوع تابلو")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "نوع تابلو"
        verbose_name_plural = "انواع تابلو"

    def __str__(self):
        return self.BoardType

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class LocationTypes(models.Model):
    LocationTypeName = models.CharField(max_length=200, null=True, verbose_name="نوع جایگاه")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "نوع جایگاه"
        verbose_name_plural = "انواع جایگاه"

    def __str__(self):
        return self.LocationTypeName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"



class Locations(models.Model):
    LocationName = models.CharField(max_length=200, null=True, verbose_name="نام جایگاه")
    LocationCode = models.CharField(max_length=200, null=True, verbose_name="کد جایگاه")
    LocationTypeID = models.ForeignKey(LocationTypes, on_delete=models.CASCADE, verbose_name="نوع جایگاه")
    Longitude = models.FloatField(null=True, verbose_name="طول جغرافیایی")
    Latitude = models.FloatField(null=True, verbose_name="عرض جغرافیایی")
    CityID = models.ForeignKey(Cities, on_delete=models.CASCADE, verbose_name="شهر")
    ActivityStatus = models.BooleanField(max_length=5, null=True, verbose_name="فعال/غیرفعال")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "جایگاه"
        verbose_name_plural = "جایگاه‌ها"

    def __str__(self):
        return self.LocationName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class Boards(models.Model):
    BoardCode = models.CharField(max_length=200, null=True, verbose_name="کد تابلو")
    BoardTypeID = models.ForeignKey(BoardTypes, on_delete=models.CASCADE, verbose_name="نوع تابلو")
    LocationID = models.ForeignKey(Locations, on_delete=models.CASCADE, verbose_name="جایگاه")
    BoardScore = models.CharField(max_length=20, null=True, verbose_name="امتیاز تابلو")
    BoardDescription = models.CharField(max_length=200, null=True, verbose_name="توضیحات تابلو")
    Dimenstions = models.CharField(max_length=200, null=True, verbose_name="ابعاد")
    PlacementComments = models.CharField(max_length=200, null=True, verbose_name="نظرات")
    Area = models.CharField(max_length=20, null=True, verbose_name="ناحیه")
    ActivityStatus = models.BooleanField(max_length=5, null=True, verbose_name="فعال/غیرفعال")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "تابلو"
        verbose_name_plural = "تابلوها"

    def __str__(self):
        return self.BoardCode

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class Customers(models.Model):
    CustomerName = models.CharField(max_length=200,unique=True, null=True, verbose_name="نام مشتری")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتریان"

    def __str__(self):
        return self.CustomerName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class AgentPaymentMethods(models.Model):
    AgentPaymentMethodName = models.CharField(max_length=200, null=True, verbose_name="نام روش پرداخت")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "روش پرداخت به مسئول"
        verbose_name_plural = "روش‌های پرداخت به مسئولان"

    def __str__(self):
        return self.AgentPaymentMethodName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class Agents(models.Model):
    AgentFirstName = models.CharField(max_length=200, null=True, verbose_name="نام مسئول فروش")
    AgentLastName = models.CharField(max_length=200, null=True, verbose_name="نام خانوادگی مسئول فروش")
    AgentPhone = models.CharField(max_length=200, null=True, verbose_name="شماره تلفن مسئول")
    AgentMail = models.CharField(max_length=200, null=True, verbose_name="ایمیل مسئول")
    PositionID = models.IntegerField(null=True, verbose_name="آیدی سطح")
    AgentCode = models.IntegerField(null=True, verbose_name="کد مسئول")
    AgentPaymentMethodID = models.ForeignKey(AgentPaymentMethods, on_delete=models.CASCADE, verbose_name="روش پرداخت به مسئول")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "مسئول"
        verbose_name_plural = "مسئول‌ها"

    def __str__(self):
        return str(self.AgentFirstName) + ' ' + str(self.AgentLastName)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class SalesPackages(models.Model):
    PackageName = models.CharField(max_length=200, null=True, verbose_name="نام پکیج فروش")
    AgentNameID = models.ForeignKey(Agents, on_delete=models.CASCADE, verbose_name="مسئول فروش")
    ActivityStatus = models.BooleanField(max_length=5, null=True, verbose_name="فعال/غیرفعال")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "پکیج فروش"
        verbose_name_plural = "پکیج‌های فروش"

    def __str__(self):
        return self.PackageName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class PackageDetailsPerBoard(models.Model):
    PackageID = models.ForeignKey(SalesPackages, on_delete=models.CASCADE, verbose_name="پکیج فروش")
    BoardID = models.ForeignKey(Boards, on_delete=models.CASCADE, verbose_name="تابلو")
    ActivityStatus = models.BooleanField(max_length=5, null=True, verbose_name="فعال/غیرفعال")
    DeactivationDate = models.DateField(max_length=200, null=True, verbose_name="تاریخ میلادی غیرفعال شدن")
    DeactivationDateJalali = jmodels.jDateField(max_length=200, null=True, verbose_name="تاریخ شمسی غیرفعال شدن")
    ActivationDate = models.DateField(max_length=200, null=True, verbose_name="تاریخ میلادی فعال شدن")
    ActivationDateJalali = jmodels.jDateField(max_length=200, null=True, verbose_name="تاریخ شمسی فعال شدن")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "تابلو در پکیج"
        verbose_name_plural = "تابلوها در پکیج‌ها"

    def __str__(self):
        return str(self.PackageID) + str(self.BoardID)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class Contracts(models.Model):
    ContractNumber = models.CharField(max_length=10,blank=True, null=True, verbose_name="شماره قرارداد")
    CustomerID = models.ForeignKey(Customers,blank=True,null=True, on_delete=models.CASCADE, verbose_name="مشتری")
    PrePayment = models.FloatField(null=True,blank=True, verbose_name="مبلغ پیش پرداخت")
    ContractPrice = models.FloatField(max_length=200, null=True,blank=True, verbose_name="مبلغ کل قرارداد")
    ContractConfirmDate = models.DateField(max_length=200, null=True, blank=True,verbose_name="تاریخ میلادی ثبت قرارداد")
    ContractConfirmDateJalali = jmodels.jDateField(max_length=200, blank=True,null=True, verbose_name="تاریخ شمسی ثبت قرارداد")
    IsCancelled = models.BooleanField(default=False, verbose_name="فسخ شده")
    IsExpanded = models.BooleanField(default=False, verbose_name="تمدید شده")
    ValueAddedTax = models.BooleanField(default=False,verbose_name="مالیات بر ارزش افزوده")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    AgentNameID = models.ForeignKey(Agents, on_delete=models.CASCADE,null=True,blank=True, verbose_name="مسئول فروش")
    CancelingDate = models.DateField(max_length=200, null=True, blank=True,verbose_name="تاریخ میلادی فسخ")
    CancelingDateJalali = jmodels.jDateField(max_length=200, null=True,blank=True, verbose_name="تاریخ شمسی فسخ")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "قرارداد"
        verbose_name_plural = "قراردادها"

    def __str__(self):
        return self.ContractNumber

    def getid(self):
        return self.id

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class ContractDetailsPerBoard(models.Model):

    ContractID = models.ForeignKey(Contracts,on_delete=models.CASCADE,null=True, blank=True,verbose_name="قرارداد")
    BoardID = models.ForeignKey(Boards, on_delete=models.CASCADE,null=True, blank=True,verbose_name="تابلو")
    BoardContractPrice = models.FloatField(null=True,blank=True, verbose_name="مبلغ قرارداد تابلو")
    DailyPrice = models.FloatField(max_length=200, null=True,blank=True, verbose_name="مبلغ روزشمار تابلو در قرارداد")
    ContractStart = models.DateField(max_length=200, null=True,blank=True, verbose_name="تاریخ میلادی شروع اکران")
    JalaliStart = jmodels.jDateField(max_length=200, null=True,blank=True, verbose_name="تاریخ شمسی شروع اکران")
    ContractFinish = models.DateField(max_length=200, null=True,blank=True, verbose_name="تاریخ میلادی پایان اکران")
    JalaliFinish = jmodels.jDateField(max_length=200, null=True,blank=True, verbose_name="تاریخ شمسی پایان اکران")
    AgentNameID = models.ForeignKey(Agents, on_delete=models.CASCADE,blank=True, null=True,verbose_name="مسئول فروش")
    ContractYearBase = models.CharField(max_length=200, null=True,blank=True, verbose_name="سال پایه قرارداد")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True,blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "تابلو در قرارداد"
        verbose_name_plural = "تابلوها در قراردادها"

    def __str__(self):
        return str(self.ContractID) + str(self.BoardID)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

class CustomerPaymentMethod(models.Model):
    CustomerPaymentMethodName = models.CharField(max_length=200, null=True, verbose_name="نام روش پرداخت")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "روش پرداخت"
        verbose_name_plural = "روش‌های پرداخت"

    def __str__(self):
        return self.CustomerPaymentMethodName

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"


class Installment(models.Model):

    ContractID = models.ForeignKey(Contracts, on_delete=models.CASCADE,null=True,blank=True, verbose_name="قرارداد")
    Installment = models.FloatField(null=True,blank=True, verbose_name="مبلغ قسط")
    InstallmentNumber = models.IntegerField(null=True,blank=True, verbose_name="نوبت قسط")
    CustomerPaymentMethodID = models.ForeignKey(CustomerPaymentMethod,blank=True,null=True, on_delete=models.CASCADE, verbose_name="روش پرداخت")
    PaymentDate = models.DateField(max_length=200, null=True,blank=True, verbose_name="تاریخ میلادی پرداخت")
    PaymentDateJalali = jmodels.jDateField(max_length=200, null=True,blank=True, verbose_name="تاریخ شمسی پرداخت")
    EntryDate = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="تاریخ ثبت رکورد")
    Company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name="شرکت")
    EntryAgent = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="ثبت کننده")

    class Meta:
        verbose_name = "قسط"
        verbose_name_plural = "اقساط"

    def __str__(self):
        return str(self.ContractID) + ' ' + str(self.InstallmentNumber)

    def jEntryDate(self):
        return jalali_converter(self.EntryDate)
    jEntryDate.short_description = "تاریخ ثبت رکورد"

    def Installment_set(self):
        return self.Installment_set.all()
