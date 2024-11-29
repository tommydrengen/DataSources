import sqlite3
import pandas as pd

conn = sqlite3.connect('database_file')
cursor = conn.cursor()

orders_df = pd.read_csv('files/orders.csv')
products_df = pd.read_csv('files/products.csv')
restocks_df = pd.read_csv('files/restocks.csv', )
start_inventory_df = pd.read_csv('files/start_inventory.csv')
suppliers_df = pd.read_csv('files/suppliers.csv')

#products_df.rename(columns={"id":"product_id","name":"name", "categories":"c", "price":"p", "description":"d", "im_url":"iu"})
#products_df.rename(columns={""})
products_df.columns = ['product_id','name','categories','price','brand','description','im_url']
products_df.to_sql(name='products', con=conn)
print(products_df)



# Create empty DataFrames for `ordersnormalized` and `orderlines`
ordersnormalized = pd.DataFrame(columns=['order_id', 'dato', 'customer_id', 'status'])
orderlines = pd.DataFrame(columns=['order_id', 'product_id'])

for i in range(20):#range(len(orders_df)):  # Loop through each row
    # Append normalized order data
    ordersnormalized = pd.concat([
        ordersnormalized,
        pd.DataFrame({
            'order_id': [i + 1],  # R indexes start at 1
            'dato': [orders_df.iloc[i]['date']],  # Format date to 'YYYY-MM-DD'
            'customer_id': [orders_df.iloc[i]['customer_id']],
            'status': [orders_df.iloc[i]['status']]
        })
    ], ignore_index=True)

    # Split the order items (assuming it's a comma-separated string)
    #print("Hello")
    mid_string = str(orders_df.iloc[i]['products']).split(',')
    print(mid_string)

# write orderlines
    for j in range(0, len(mid_string) - 1):  # Mimic 2:length(mid_string[[1]])-1
        print((i + 1, mid_string[j]))
        orderlines = pd.concat([
            orderlines,
            pd.DataFrame({
                'order_id': [i + 1],
                'product_id': [mid_string[j]]
            })
        ], ignore_index=True)

# View the DataFrames
print(ordersnormalized)
print(orderlines)


# prepare writing dataframes to sql tables:
# validate...
print(products_df)




#check dataframes ordersnormalized & orderlines
print("ordersnormalized:")
print(ordersnormalized)
print("orderlines:")
print(orderlines)
print("restocks:")
print(restocks_df)

# skriv til sql
ordersnormalized.to_sql(name = 'ordersnormalized', con = conn )
orderlines.to_sql(name = 'orderlines', con = conn)
restocks_df.to_sql(name = 'restocks', con = conn)
suppliers_df.to_sql(name = 'suppliers', con = conn)
start_inventory_df.to_sql(name = 'start_inventory', con = conn)

# add new table inventory:

cursor.execute("CREATE TABLE inventory(dato date, product_id varchar, quantity INTEGER)")
cursor.execute("INSERT INTO inventory SELECT '2001-01-01', product_id, quantity FROM start_inventory")
cursor.execute("SELECT '2001-01-01', product_id, quantity FROM start_inventory")

res = cursor.fetchall()
print(res)