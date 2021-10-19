from django.db import models
# Create your models here.
# 
class Food(models.Model): 
    food_id = models.AutoField(primary_key=True) 
    food_name = models.TextField(null=False,blank=False) 
    food_rate = models.DecimalField(decimal_places=1,max_digits=4,null=False,blank=False) 
    food_desc = models.TextField(null=False,blank=False) 
    type = [ 
        ("Veg","veg"), 
        ("Non-Veg","non-veg"), 
        ("jain","jain"),
        ] 
    food_type = models.CharField(choices=type,max_length=20) 
    category =[ 
        ("Chinese","chinese"), 
        ("South-Indian","south-indian"), 
        ("Oriental","oriental"), 
        ("Italian","italian"), 
        ("Snacks","snacks"), 
        ("Juices","juices")
    ] 
    food_cat = models.CharField(choices=category,max_length=20)

