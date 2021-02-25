import pyodbc

server = 'DESKTOP-NPVGVRM'
database = 'MShop'
username = 'sa'
password = 'sa'
driver = '{SQL Server}' # Driver you need to connect to the database
port = '8000'

def getCate():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_all_Category"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def searchProduct(pages,search):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_search_all "+str(pages)+", N'"+str(search)+"'"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getProduct(pages):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_all_Product_page "+str(pages)
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getProductCate(pages,category_id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_search_category "+str(pages)+", "+str(category_id)
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getProductPrice(pages,min,max):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_search_price "+str(pages)+", "+str(min)+", "+str(max)
    print(sql)
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getProductMainInfo(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_Product_main_info " + str(id)
    print(sql)
    cur.execute(sql)
    result = cur.fetchone()
    return result

def getProductSpecifications(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_CategoryItemValue_Product "+str(id)
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getProductImageList(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_listImage "+str(id)
    cur.execute(sql)
    result = cur.fetchall()
    return result

def createCustomer(name, email, phone, address, password):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_insert_Customer N'"+str(name)+"', N'"+str(email)+"', '"+str(phone)+"', N'"+str(address)+"', '"+str(password)+"'"
    cur.execute(sql)
    cur.commit()
    try:
        result = cur.fetchone()
        return result
    except Exception as e:
        print(e)

def createOrders(id,address,description,payby):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_insert_Order "+str(id)+",N'"+str(address)+"',N'"+str(description)+"','"+str(payby)+"'"
    cur.execute(sql)
    cur.commit()
    
def createOrdersDetail(productID,customerID,counts,cost):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_insert_OrderDetail "+str(productID)+","+str(customerID)+","+str(counts)+","+str(cost)
    cur.execute(sql)
    cur.commit()
    
def login(email,password):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_login '"+str(email)+"', '"+str(password)+"'"
    cur.execute(sql)
    result = cur.fetchone()
    return result

def getCustomerMainInfo(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_Customer_MainInfo "+str(id)
    cur.execute(sql)
    result = cur.fetchone()
    return result

def getCustomerOrders(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_Customer_Orders "+str(id)
    cur.execute(sql)
    result = cur.fetchall()
    return result