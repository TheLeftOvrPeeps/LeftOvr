from django.db import models


class Customer(models.Model):
    firstName = models.CharField(max_length=250)
    lastName = models.CharField(max_length=250)
    idNum = models.CharField(max_length=13)
    email = models.CharField(max_length=500)
    passWords = models.CharField(max_length=500)
    custAddress = " "

    def __str__(self):
        return self.firstName + ' ' + self.lastName + '   ' + self.custAddress + '   ' + self.idNum

class Restaurant(models.Model):
    busName = models.CharField(max_length=500)
    busAddress = models.CharField(max_length=500)
    einNum = models.CharField(max_length=9)
    busEmail = models.CharField(max_length=750)
    busPassWords = models.CharField(max_length=500)

    def __str__(self):
        return self.busName + '  ' + self.busAddress + '   ' + self.einNum

class Meals(models.Model):
    mealType = models.CharField(max_length=500)
    mealAvail = models.CharField(max_length=1000)

    def __str__(self):
        return self.mealAvail + ' ' + self.mealType

class slots(models.Model):
    meal = models.ForeignKey(Meals, on_delete=models.CASCADE)

    def __str__(self):
        return self.meal

class contactUs(models.Model):
    nameC = models.CharField(max_length=1000)
    emailC = models.CharField(max_length=1000)
    phoneC = models.CharField(max_length=11)
    messageC = models.CharField(max_length=4000)

    def __str__(self):
        return self.nameC + '  ' + self.emailC + '  ' + self.phoneC + '  ' + self.messageC
