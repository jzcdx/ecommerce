from db_utils import DBH
#general utilities
def get_cart_info(product_dict):
    res_list = []
    dbh = DBH()
    for id in product_dict:
        cur = dbh.get_product(id)
        res_list.append(cur)
    return res_list