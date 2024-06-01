
from django.db import models
from django.db.models  import JSONField

class Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    # creator = models.ForeignKey('auth.User', related_name='Group', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']


class Sub_Group(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    # creator = models.ForeignKey('auth.User', related_name='Sub_Group', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Product(models.Model):
    name = models.CharField(max_length=100)
    shortCode = models.CharField(max_length=10, null=True)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    group = models.ForeignKey('Group', on_delete=models.CASCADE)
    subgroup = models.ForeignKey('Sub_Group', on_delete=models.CASCADE)
    # creator = models.ForeignKey('auth.User', related_name='Product', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Product_Detail(models.Model):
    count = models.CharField(max_length=100)
    sell_price = models.CharField(max_length=100)
    cost_price = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    productType = models.ForeignKey('Product_type', on_delete=models.CASCADE)
    # creator = models.ForeignKey('auth.User', related_name='Product_Detail', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Product_type(models.Model):
    quantity = models.IntegerField()
    unit = models.CharField(max_length=100)
    # creator = models.ForeignKey('auth.User', related_name='Product_type', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']


class Item(models.Model):
    itemCode = models.CharField(max_length=100)
    Serial_No = models.CharField(max_length=100)
    Manufacture_date = models.DateTimeField(auto_now_add=True)
    expired_period = models.CharField(max_length=100)
    expired_pediod_type = models.CharField(max_length=100)
    itemCode = models.CharField(max_length=100)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    damage = models.ForeignKey('Damage', on_delete=models.CASCADE)
    # creator = models.ForeignKey('auth.User', related_name='Item', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']


class Damage(models.Model):
    details = models.CharField(max_length=100)
    dateTime = models.DateTimeField(auto_now_add=True)
    reportedDateTime = models.DateTimeField(auto_now_add=True)
    # creator = models.ForeignKey('auth.User', related_name='Damage', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = JSONField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']


class Supplier(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    notes = models.CharField(max_length=100)
    rating = models.CharField(max_length=100)
    vat_no = models.CharField(max_length=100)
    companyname = models.CharField(max_length=100)
    profileimage = models.CharField(max_length=100)
    # creator = models.ForeignKey('auth.User', related_name='Supplier', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    telephone = models.ForeignKey('Telephone', related_name='Telephone1', on_delete=models.CASCADE)
    mobile = models.ForeignKey('Telephone', related_name='Telephone2', on_delete=models.CASCADE)
    fax = models.ForeignKey('Telephone', related_name='Telephone3', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Location(models.Model):
    longatied = models.CharField(max_length=100)
    latatidue = models.CharField(max_length=100)
    # creator = models.ForeignKey('auth.User', related_name='Location', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-id']


class Address(models.Model):
    Street = models.CharField(max_length=100)
    postalcode = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state_code = models.CharField(max_length=100)
    # creator = models.ForeignKey('auth.User', related_name='Address', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']


class Telephone(models.Model):
    Country_Code = models.CharField(max_length=100)
    Mobile_number = models.CharField(max_length=100)
    # creator = models.ForeignKey('auth.User', related_name='Telephone', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']
