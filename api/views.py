
from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status
from .serializers import CartItemSerializer
from .models import customer,Purchase#,Shipping



@api_view(["POST"])
def customerapp(request):
    try:
        Customer_Name = request.data.get('name',None)
        Email= request.data.get('email',None)
        Mobile_Number= request.data.get('mobile',None)
        City=request.data.get('city',None)
        customer.objects.create(Customer_Name=Customer_Name, Email=Email,Mobile_Number=Mobile_Number,City=City)
        data = customer.objects.all().values()
        print(data)
        predictions = {
                    'Mssage':'customer data created sucessfuly',
                    'data':data

                }
        print("predictions:",predictions)
    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    return Response(predictions)


@api_view(["POST"])
def Purchaseapp(request):
    try:
        Customer_Name = request.data.get('name',None)
        Email= request.data.get('email',None)
        Mobile_Number= request.data.get('mobile',None)
        City=request.data.get('city',None)
        Product_Name = request.data.get('p_name',None)
        Quantity= request.data.get('quantity',None)
        Pricing= request.data.get('pricing',None)
        MRP=request.data.get('mrp',None)
        #customer_ptr_id=request.data.get('c_id',None)
        #if int(Pricing)<int(MRP):
        Purchase.objects.create(Customer_Name=Customer_Name, Email=Email,Mobile_Number=Mobile_Number,City=City,Product_Name=Product_Name, Quantity=Quantity,Pricing=Pricing,MRP=MRP,)
        data = Purchase.objects.all().values()
        print(data)
        predictions = {
                'Mssage':'Purchase data created sucessfuly',
                'data':data

            }
        """
        else:
            predictions = {
                    'Mssage':'Pricing must be less than MRP',
                }

        """
        print("predictions:",predictions)
    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }
    return Response(predictions)
    """
@api_view(["POST"])
def Shippingapp(request):
    
    try:
        
        Address = request.data.get('address',None)
        Pincode= int(request.data.get('pin',None))
        
        
        Shipping.objects.create(Address=Address, Pincode=Pincode)
        data = Shipping.objects.all().values()
        print(data)
        predictions = {
                'Mssage':'Created sucessfuly',
                'data':data

            }
        
        print("predictions:",predictions)

    except Exception as e:
        predictions = {
            'error' : '2',
            "message": str(e)
        }

    return Response(predictions)
    """