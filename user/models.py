from django.db import models




class Role(models.Model):
    Dashboard=models.BooleanField()


    def _str_(self):
        return self.R_Id 

          
class User(models.Model):
    Name = models.CharField(max_length=120)
    Surname = models.CharField(max_length=120)
    Username = models.CharField(max_length=120)
    Gender = models.CharField(max_length=120)
    Birthday = models.DateField()
    Role = models.ForeignKey(Role,related_name="roles",on_delete=models.CASCADE)
    Phone = models.CharField(max_length=120)
    Email = models.CharField(max_length=120)
    Password = models.CharField(max_length=500)


    def _str_(self):
        return self.U_Id    

class MatchTable(models.Model):
    U_Id =  models.ForeignKey(User,related_name="users1",on_delete=models.CASCADE)
    OU_Id =  models.ForeignKey(User,related_name="users2",on_delete=models.CASCADE)
    M_Id = models.CharField(max_length=120,primary_key=True)
    MakeDealU = models.BooleanField(default=False)
    MakeDealOU = models.BooleanField(default=False)
    Product =models.CharField(max_length=1200,default="")
    ProductImg = models.CharField(max_length=1200,default="")
    ProductName = models.CharField(max_length=1200,default="")


    def _str_(self):
        return self.U_Id



class Message(models.Model):
    M_Id = models.ForeignKey(MatchTable,related_name="matchtables",on_delete=models.CASCADE)
    Content = models.TextField()
    WhoSend = models.ForeignKey(User,related_name="users3",on_delete=models.CASCADE)
    Date = models.TextField()


    def _str_(self):
        return self.M_Id



