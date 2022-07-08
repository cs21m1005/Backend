from django.db import models



class customer(models.Model):
	customer_ptr_id=id
	Customer_Name = models.CharField(max_length=200)
	Email = models.CharField(max_length=300)
	Mobile_Number = models.CharField(max_length=10)
	City=models.CharField(max_length=200)


class Purchase(customer):
	Purchase_id=id
	Product_Name = models.CharField(max_length=200)
	Quantity = models.CharField(max_length=15)
	Pricing = models.CharField(max_length=30)
	MRP=models.CharField(max_length=30)
	pcustomer_id = models.ForeignKey(
        customer,
        related_name='Purchase',
        on_delete=models.CASCADE
        )

"""
class Shipping(Purchase):
	Address=models.CharField(max_length=500)
	Pincode=models.CharField(max_length=6)
"""