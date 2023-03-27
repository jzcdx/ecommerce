from db_utils import DBH
import decimal
#general utilities
def get_product_rows(product_dict):
    if (not product_dict):
        return None;
    
    res_list = []
    dbh = DBH()
    for id in product_dict:
        cur = dict(dbh.get_product(id))
        cur["total"] = decimal.Decimal(str(product_dict[id])) * decimal.Decimal(str(cur["price"]))
        cur["qtty"] = product_dict[id]
        res_list.append(cur)
    return res_list

def get_cart_info(product_info):
    print("getting cart info")
    res_dict = {"total": 0, "items": 0};
    
    for product in product_info:
        res_dict["total"] += product["total"]
        res_dict["items"] += product["qtty"]
    return res_dict

"""
pd = {1: 2, 3: 5}
temp = get_cart_info(pd)
for i in temp:
    print(i)

print("here: " , temp[1]["total"])

x = decimal.Decimal('21.99')
y = decimal.Decimal('5')
print(x * y)
"""