from django.db import models

class Menu(models.Model):
    menu_name=models.CharField(max_length=50)
    menu_price=models.IntegerField()

    def __str__(self):
        return self.menu_name


class Option(models.Model):
    menu=models.ForeignKey(Menu, on_delete=models.CASCADE)
    option_name=models.CharField(max_length=50)
    option_price=models.IntegerField()

    def __str__(self):
        return f"{self.option_name}_{self.option_price}원"
    