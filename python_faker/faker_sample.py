
# ------- Customers,CreditCards,CreditCardTransactions -------

from faker import Faker
import pyodbc
from datetime import datetime
import random

#-------
# CONFIG
#-------
SERVER = r"LAPTOP-U54ODU7A"
DATABASE = r"Banking_System_Project1"

CUSTOMER_COUNT = 3000
CUSTOMER_WITH_CARDS = 1200
CARD_MIN = 0
CARD_MAX = 3
TRANSACTION_MIN = 7
TRANSACTION_MAX = 25

fake =Faker(["uz_UZ"])

#---------------
# SQL CONNECTION
#---------------
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

#-----------------
# INSERT Customers
#-----------------
print('Inserting customers...')

insert_customers = """
INSERT INTO dbo.Customers
(FullName, DOB, Email, PhoneNumber, Address, NationalID, TaxID,
EmploymentStatus, AnnualIncome, CreatedAt, UpdatedAt)
OUTPUT INSERTED.CustomerID
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
"""

employement_status_list = ["Employed","Unemployed","Student","Self-Employed","Retired"]

customer_ids = []

for _ in range(CUSTOMER_COUNT):
    fullname = fake.name()
    dob = fake.date_of_birth(minimum_age = 18, maximum_age = 80)
    email = fake.email()
    phone_number = fake.phone_number()
    addres = fake.address()
    national_id = fake.ssn()
    tax_id = str(fake.random_number(9))
    employement = random.choice(employement_status_list)
    annual_income = round(random.uniform(1500,200000), 2)
    created_at = datetime.now()
    updated_at = datetime.now()

    cursor.execute(insert_customers,(fullname,dob,email,phone_number,addres,national_id,tax_id,employement,annual_income,created_at,updated_at))    
    new_id = cursor.fetchone()[0]
    customer_ids.append(new_id)
    conn.commit()
    print(f"{len(customer_ids)} customers inserted successfully!")


#------------------
#INSERT CREDITCARDS
#------------------
print('Insering CreditCards...')

insert_card = """
INSERT INTO dbo.CreditCards
(CustomerID, CardNumber, CardType, CVV, ExpiryDate, Limit, Status)
OUTPUT INSERTED.CardID
VALUES (?, ?, ?, ?, ?, ?, ?)
"""

card_type_list = ["Visa","MasterCard","UzCard","Humo"]
card_status_list = ["Active","Inactive","Blocked","Expired","Closed"]

customers_with_cards = random.sample(customer_ids,CUSTOMER_WITH_CARDS)

card_ids = []

for cust in customers_with_cards:
    num_cards = random.randint(CARD_MIN,CARD_MAX)
    for _ in range(num_cards):
        card_number = fake.credit_card_number()
        card_type = random.choice(card_type_list)
        cvv = random.randint(100,999)
        expiry_date = fake.date_between(start_date='today',end_date='+4y')
        limit = round(random.uniform(500,10000),2)
        status = random.choice(card_status_list)

        cursor.execute(insert_card,(cust,card_number,card_type,cvv,expiry_date,limit,status))
        card_id = cursor.fetchone()[0]
        if card_id: # NULL bo'lmasligiga ishonch
            card_ids.append(card_id)
            conn.commit()
            print(f"{len(card_ids)} credit cards inserted successfully!")


#-----------------------------
#INSERT CREDITCARDTRANSACTIONS
#-----------------------------
print('Inserting CreditCardTransactions...')

insert_creditcardtransaction = """
INSERT INTO dbo.CreditCardTransactions
(CardID, Merchant, Amount, Currency,  TransactionDate, Status)
VALUES (?, ?, ?, ?, ?, ?)
"""
currency_list = ["USD", "EUR", "GBP", "UZS"]
transaciton_status = ["Completed","Pending","Failed"]
transaction_count = 0 

for card_id in card_ids:

    if not card_id:
        continue
    
    t_count = random.randint(TRANSACTION_MAX,TRANSACTION_MAX)
    for _ in range(t_count):
        merchant = fake.company()
        amount = round(random.uniform(50,1000),2)
        currency = random.choice(currency_list)
        status = random.choice(transaciton_status)
        trx_date = fake.date_between(start_date = '-2y', end_date = 'today')
        
        cursor.execute(insert_creditcardtransaction,(card_id,merchant,amount,currency,trx_date,status))
        transaction_count += 1

conn.commit()
cursor.close()
conn.close()

print(f"{transaction_count} credit card transactions inserted successfully!")
print("ALL DATA DONE!")
