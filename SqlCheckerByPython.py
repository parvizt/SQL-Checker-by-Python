import pyodbc
import pandas as pd

# تنظیمات اتصال به SQL Server
server = '.'
database = 'master'
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;')

# دریافت لیست دیتابیس‌ها
cursor = conn.cursor()
cursor.execute("SELECT name FROM sys.databases WHERE database_id > 4;")
databases = [row.name for row in cursor.fetchall()]

# نمایش لیست دیتابیس‌ها
print("دیتابیس‌های موجود:")
for db in databases:
    print(db)

# انتخاب دیتابیس توسط کاربر
selected_database = input("لطفاً نام دیتابیس مورد نظر خود را وارد کنید: ")

# اتصال به دیتابیس انتخاب شده
conn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={selected_database};Trusted_Connection=yes;')
cursor = conn.cursor()

# دریافت لیست جداول دیتابیس انتخاب شده
cursor.execute("SELECT name FROM sys.tables;")
tables = [row.name for row in cursor.fetchall()]

# نمایش لیست جداول
print(f"جداول موجود در دیتابیس '{selected_database}':")
for table in tables:
    print(table)

# اجرای SELECT TOP (1000) بر روی جدول انتخاب شده و نمایش نتایج به صورت فریم داده
selected_table = input("لطفاً نام جدول مورد نظر خود را وارد کنید: ")
query = f"SELECT TOP 1000 * FROM {selected_table};"
df = pd.read_sql(query, conn)

# نمایش فریم داده به صورت جدول
print(f"نتایج در جدول '{selected_table}':")
print(df)

# بستن اتصال به دیتابیس
conn.close()
