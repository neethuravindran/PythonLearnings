
import csv
import re
class Customer:
    def __init__(self, productname, customername, isblacklisted):
        self.productname = productname
        self.customername = customername
        self.isblacklisted = isblacklisted

    def createOrder(self, productname, productcode):
        if self.isblacklisted:
            raise CustomerNotAllowedException(
                "Customer is not allowed to create the order because it is blacklisted.")

        order = Order(productname, productcode)

        return order


class Order:
    def __init__(self, productname, productcode):
        self.productname = productname
        self.productcode = productcode



class CustomerNotAllowedException(Exception):
    def __init__(self, message, errors=None):
        # Call the base class constructor with the parameters it needs
        super().__init__(message)

        # Now for your custom code...
        self.errors = errors




csv_data = []
with open("FairDealCustomerData.csv") as f:
    reader = csv.reader(f)
    csv_data = list([r for r in reader])


fullname_data = list([data for data in csv_data if re.match(
    r"([a-zA-Z].+)\s(\w+)\s(\w+)", data[1].strip(), re.IGNORECASE)])

customerList = []
for data in fullname_data:
    customerList.append(Customer(productname=data[0].strip(
    ), customername=data[1].strip(), isblacklisted=bool(data[2].strip())))

customer = Customer(productname="Shampoo",
                    customername="Neethu Ravindran", isblacklisted=True)
customer.createOrder(customer.productname, customer.customername)