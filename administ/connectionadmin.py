import pyodbc

server = 'DESKTOP-NPVGVRM'
database = 'MShop'
username = 'sa'
password = 'sa'
driver = '{SQL Server}' # Driver you need to connect to the database
port = '8000'

def loginStaff(email,password):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_login_staff '"+str(email)+"', '"+str(password)+"'"
    cur.execute(sql)
    result = cur.fetchone()
    return result

def getStaffMainInfo(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_Staff_MainInfo "+str(id)
    cur.execute(sql)
    result = cur.fetchone()
    return result

def getAllUser():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_User"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getAllRole():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_Role"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getAllPermission():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_Permission"
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

def insertProduct(name,cate,manu,sup,price,descript):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_insert_Product N'"+str(name)+"', N'"+str(descript)+"', "+str(price)+", "+str(cate)+", "+str(manu)+", "+str(sup)
    cur.execute(sql)
    cur.commit()

def updateProduct(name,cate,manu,sup,price,descript,id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_update_Product "+str(id)+", N'"+str(name)+"', N'"+str(descript)+"', "+str(price)+", "+str(cate)+", "+str(manu)+", "+str(sup)
    print(sql)
    cur.execute(sql)
    cur.commit()

def deleteProduct(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_delete_Product "+str(id)
    cur.execute(sql)
    cur.commit()

def getCategory():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_all_Category"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getManufactory():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_all_Manufactory"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getSupplier():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_all_Supplier"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def selectProduct():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_all_Product"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getStaffPermission(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_PermissionStaff " + str(id)
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getOrder():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_all_Order"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getOrderDetailInOrder(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_OrderDetailInOrder "+str(id)
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getAllStatus():
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_all_Status"
    cur.execute(sql)
    result = cur.fetchall()
    return result

def getOrderStatus(id):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_select_OrderStatus "+str(id)
    cur.execute(sql)
    result = cur.fetchone()
    return result

def updateStatus(orderid, statusid, updateby):
    conn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+
                 ';PWD='+password+';Trusted_Connection=yes')

    cur = conn.cursor()
    sql = "exec sp_insert_StatusUpdate "+str(orderid)+", "+str(statusid)+", "+str(updateby)
    cur.execute(sql)
    cur.commit()


    