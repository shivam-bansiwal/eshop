from django.db import models

class Seller(models.Model):
    name=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    email=models.EmailField(default=None,null=True,blank=True)
    phone=models.CharField(max_length=20,default=None,null=True,blank=True)
    bankname=models.CharField(max_length=20,default=None,null=True,blank=True)
    ifscCode=models.CharField(max_length=20,default=None,null=True,blank=True)
    accountNumber=models.CharField(max_length=20,default=None,null=True,blank=True)
    total=models.IntegerField(default=None,null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.name

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+" "+self.name

class Brand(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+" "+self.name

class Product(models.Model):
    name= models.CharField(max_length=50)
    desc= models.TextField()
    stock=models.BooleanField(default=False)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    basePrice=models.IntegerField()
    discount=models.IntegerField(default=0,null=True,blank=True)
    finalPrice=models.IntegerField(default=0,null=True,blank=True)
    red= models.BooleanField(default=False,null=True,blank=True)
    green= models.BooleanField(default=False,null=True,blank=True)
    black= models.BooleanField(default=False,null=True,blank=True)
    white= models.BooleanField(default=False,null=True,blank=True)
    pink= models.BooleanField(default=False,null=True,blank=True)
    xs= models.BooleanField(default=False,null=True,blank=True)
    s= models.BooleanField(default=False,null=True,blank=True)
    l= models.BooleanField(default=False,null=True,blank=True)
    m= models.BooleanField(default=False,null=True,blank=True)
    xl= models.BooleanField(default=False,null=True,blank=True)
    xl= models.BooleanField(default=False,null=True,blank=True)
    img1= models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    img2= models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    img3= models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    img4= models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    img5= models.ImageField(upload_to='images/',default=None,null=True,blank=True)
    date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)+" "+self.name

class Buyer(models.Model):
    name=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    email=models.EmailField(default=None,null=True,blank=True)
    phone=models.CharField(max_length=20,default=None,null=True,blank=True)
    address1=models.CharField(max_length=20,default=None,null=True,blank=True)
    address2=models.CharField(max_length=20,default=None,null=True,blank=True)
    city=models.CharField(max_length=20,default=None,null=True,blank=True)
    state=models.CharField(max_length=20,default=None,null=True,blank=True)
    pin=models.CharField(max_length=20,default=None,null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.name

class Cart(models.Model):
    buyer=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    total=models.IntegerField()
    color=models.CharField(max_length=10,default=None)
    size=models.CharField(max_length=10,default=None)

    def __str__(self):
        return str(self.id)+" "+self.buyer.name

class Checkout(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    total=models.IntegerField()
    name=models.CharField(max_length=20,default=None)
    phone=models.CharField(max_length=20,default=None)
    email=models.CharField(max_length=20,default=None)
    address1=models.CharField(max_length=30)
    address2=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pin=models.CharField(max_length=30)
    notes=models.TextField(default=None)
    mode=models.CharField(max_length=30,default=None)

    def __str__(self):
        return str(self.id)


class Wishlist(models.Model):
    user=models.ForeignKey(Buyer,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    msg=models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.name