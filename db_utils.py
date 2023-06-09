from sqlalchemy import create_engine, URL, text, Table, MetaData, Column, Integer, String, Double, select, delete, update, insert
import os

class DBH: #database helper
    def __init__(self):
        url_object = URL.create(
            "postgresql+psycopg2",
            username="postgres",
            password=os.environ['pg_pw_local'],  # DO NOT ESCAPE THIS PASSWORD 
            host="localhost",
            database="ecommerce_test"
        )   
        self.engine = create_engine(url_object)

        metadata_obj = MetaData()
        self.product = Table(
            "product",
            metadata_obj,
            Column("id", Integer),
            Column("name", String(30)),
            Column("price", Double),
            Column("stock", String),
            Column("picture", String),
        )

    def get_all_products(self):
        with self.engine.connect() as conn:
            stmt = select(self.product)
            res = conn.execute(stmt)
            rows = res.mappings().all()
            conn.close();
            
            return rows;

    def get_product(self, product_id):
        with self.engine.connect() as conn:
            stmt = select(self.product).where(self.product.c.id == product_id);
            res = conn.execute(stmt)
            #print(type(res.mappings().all()))
            
            rows = res.mappings().all()
            conn.close();
            if (rows):
                row = rows[0];
            else:
                row = None;
            return row;
#dbh = DBH()
