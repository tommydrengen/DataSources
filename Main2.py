import pandas as pd
from mysql import connector
import sqlite3
con = sqlite3.connect("tutorial.db")

orders_df = pd.read_csv('files/orders.csv')
# Generate unique order IDs (if not present)
#if 'order_id' not in orders_df.columns:
 #   orders_df['order_id'] = range(1, len(orders_df) + 1)
# Create orderlines by separating product details
#orderlines_df = orders_df[['order_id', 'product_id']].copy()
products_df = pd.read_csv('files/products.csv')
restocks_df = pd.read_csv('files/restocks.csv')
start_inventory_df = pd.read_csv('files/start_inventory.csv')
suppliers_df = pd.read_csv('files/suppliers.csv')


con = connector.connect(user='root', password= 'Deter1dagSpecialisterne', host='localhost', database = 'northwind')
cursor = con.cursor()
products_df.to_sql('productstest',con)

results = cursor.stored_results()
print('end')


cursor.execute("Insert (a, b, c) Into Products")
# skriv til sql (aendr antal tabeller)
query = """select o.order_id, o.dato, ol.product_id, substr(p.name,1,50) name, substr(categories,1,20) category, p.price
       from
          ordersnormalized o,
          orderlines ol ,
          products p
      where
          o.order_id = ol.order_id
      and trim(p.id,' ')       = trim(ol.product_id,' ')
      order by
           category,
           price"""

# tranform  add column concatenate
orders_df.to_sql('orders', con, if_exists='append', index=False)
products_df.to_sql('products_df', con, if_exists='append', index=False)
restocks_df.to_sql('restocks_df', con, if_exists='append', index=False)
start_inventory_df.to_sql('start_inventory_df', con, if_exists='append', index=False)
suppliers_df.to_sql('suppliers_df',  con, if_exists='append', index=False)