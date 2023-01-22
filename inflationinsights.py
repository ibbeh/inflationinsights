import requests
import json
import tkinter as tk
from tkinter import *

def on_submit():
    print("Submitted")
    try:
        bank_balance = entry.get()
        country_code = entry2.get()
        print("Bank Balance: ", bank_balance)
        print("Country Code: ", country_code)
    except:
        print("Error: The inputs you have given are invalid. Please give a float value for bank balanace and a string for country code.")

    labelx.destroy()
    labely.destroy()
    labelz.destroy()
    labelq.destroy()

    
    def predict_future_value(balance, country_code, sp500_rate):
        # Use World Bank API to retrieve inflation rate
        url = f'https://api.worldbank.org/v2/country/{country_code}/indicator/FP.CPI.TOTL.ZG?format=json'
        response = requests.get(url)
        inflation_data = json.loads(response.text)
        inflation_rate = inflation_data[1][0]['value']

        inflation_rate = inflation_rate / 100

        print()

        # Predict future value of balance in 1 month, 6 months, 1 year, 5 years, and 10 years
        future_values = {}
        current_balance = balance
        future_values['1 month'] = current_balance * abs((1 - inflation_rate/12))
        current_balance = future_values['1 month']
        future_values['6 months'] = current_balance * abs((1 - inflation_rate/2))
        current_balance = future_values['6 months']
        future_values['1 year'] = current_balance * abs((1 - inflation_rate))
        current_balance = future_values['1 year']
        future_values['5 years'] = current_balance * abs((1 - inflation_rate)**5)
        current_balance = future_values['5 years']

    
        future_values['10 years'] = current_balance * abs((1 - inflation_rate)**10)
        
        # Predict future value of investment in S&P 500 ETF
        sp500_values = {}
        current_balance = balance
        sp500_values['1 month'] = current_balance * (1 + sp500_rate/12) * abs((1 - inflation_rate/12))
        current_balance = sp500_values['1 month']
        sp500_values['6 months'] = current_balance * (1 + sp500_rate/2) * abs((1 - inflation_rate/2))
        current_balance = sp500_values['6 months']
        sp500_values['1 year'] = current_balance * (1 + sp500_rate) * abs((1 - inflation_rate))
        current_balance = sp500_values['1 year']
        sp500_values['5 years'] = current_balance * (1 + sp500_rate)**5 * abs((1 - inflation_rate)**5)
        current_balance = sp500_values['5 years']
        sp500_values['10 years'] = current_balance * (1 + sp500_rate)**10 * abs((1 - inflation_rate)**10)
        
        # Compare future value of investment in bank account vs S&P 500 ETF

        future_values["1 month"] = round(future_values["1 month"], 2)
        future_values["6 months"] = round(future_values["6 months"], 2)
        future_values["1 year"] = round(future_values["1 year"], 2)
        future_values["5 years"] = round(future_values["5 years"], 2)
        future_values["10 years"] = round(future_values["10 years"], 2)

        sp500_values["1 month"] = round(sp500_values["1 month"], 2)
        sp500_values["6 months"] = round(sp500_values["6 months"], 2)
        sp500_values["1 year"] = round(sp500_values["1 year"], 2)
        sp500_values["5 years"] = round(sp500_values["5 years"], 2)
        sp500_values["10 years"] = round(sp500_values["10 years"], 2)

        print("Future value of investment in bank account:")
        print()
        print(future_values)
        print()
        print("Future value of investment in S&P 500 ETF:")
        print()
        print(sp500_values)
        print()
        print("In 1 month, If you invested your money in the S&P 500, the value of your money would be $"+ str(sp500_values['1 month'] - future_values['1 month'])+ " more than if you kept your money in a bank account. ")
        print()
        print("In 6 months, If you invested your money in the S&P 500, the value of your money would be $"+ str(sp500_values['6 months'] - future_values['6 months'])+ " more than if you kept your money in a bank account. ")
        print()
        print("In 1 year, If you invested your money in the S&P 500, the value of your money would be $"+ str(sp500_values['1 year'] - future_values['1 year'])+ " more than if you kept your money in a bank account. ")
        print()
        print("In 5 years, If you invested your money in the S&P 500, the value of your money would be $"+ str(sp500_values['5 years'] - future_values['5 years'])+ " more than if you kept your money in a bank account. ")
        print()
        print("In 10 years, If you invested your money in the S&P 500, the value of your money would be $"+ str(sp500_values['10 years'] - future_values['10 years'])+ " more than if you kept your money in a bank account. ")



        label1 = tk.Label(root, text="Future value of investment in bank account:", font=("Helvetica", 15), fg="blue")
        label1.place(x=100, y=250)
        label2 = tk.Label(root, text=future_values, font=("Helvetica", 15), fg="red")
        label2.place(x=50, y=300)
        label3 = tk.Label(root, text="Future value of investment in S&P 500 ETF:", font=("Helvetica", 15), fg="blue")
        label3.place(x=100, y=350)
        label4 = tk.Label(root, text=sp500_values, font=("Helvetica", 15), fg="red")
        label4.place(x=50, y=400)
        label5 = tk.Label(root, text="In 1 month, If you invested your money in the S&P 500, the value of your money would be $"+ str(round((sp500_values['1 month'] - future_values['1 month']), 2))+ " more than if you kept your money in a bank account. ", font=("Helvetica", 15), fg="green")
        label5.place(x=50, y=450)
        label6 = tk.Label(root, text="In 6 months, If you invested your money in the S&P 500, the value of your money would be $"+ str(round((sp500_values['6 months'] - future_values['6 months']), 2))+ " more than if you kept your money in a bank account. ", font=("Helvetica", 15), fg="green")
        label6.place(x=50, y=500)
        label7 = tk.Label(root, text="In 1 year, If you invested your money in the S&P 500, the value of your money would be $"+ str(round((sp500_values['1 year'] - future_values['1 year']), 2))+ " more than if you kept your money in a bank account. ", font=("Helvetica", 15), fg="green")
        label7.place(x=50, y=550)
        label8 = tk.Label(root, text="In 5 years, If you invested your money in the S&P 500, the value of your money would be $"+ str(round((sp500_values['5 years'] - future_values['5 years']), 2))+ " more than if you kept your money in a bank account. ", font=("Helvetica", 15), fg="green")
        label8.place(x=50, y=600)
        label9 = tk.Label(root, text="In 10 years, If you invested your money in the S&P 500, the value of your money would be $"+ str(round((sp500_values['10 years'] - future_values['10 years']), 2))+ " more than if you kept your money in a bank account. ", font=("Helvetica", 15), fg="green")
        label9.place(x=50, y=650)


    print("This program  uses the inflation rate to predict the future value of a bank balance over different time frames.")
    print()
    print("The future value of a bank balance is the amount of money that it will be worth in the future if it is left in the bank account and does not earn any interest.")
    print()
    print("It also predicts the future value of an investment in the S&P 500 ETF over different time frames using the average rate of return of the S&P 500 ETF as a measure of how the value of the investment increases over time.")
    print()
    print("The program compares the future value of the investment in the bank account with the future value of the investment in the S&P 500 ETF over different time frames, it does not predict the future value of a bank account that is invested in an S&P 500 ETF.")
    print()
    #balance = float(input("Enter your current bank balance: "))
    #country_code = input("Enter your country code: ")
    sp500_rate = 0.10
    predict_future_value(float(bank_balance), country_code, sp500_rate)


root = tk.Tk()
root.title("Inflation Insights")
root.geometry("1600x800")

labelx = tk.Label(root, text="This program  uses the inflation rate to predict the future value of a bank balance over different time frames.", font=("Helvetica", 15))
labelx.place(x=100, y=300)
labely = tk.Label(root, text="The future value of a bank balance is the amount of money that it will be worth in the future if it is left in the bank account and does not earn any interest.", font=("Helvetica", 15))
labely.place(x=100, y=350)
labelz = tk.Label(root, text="It also predicts the future value of an investment in the S&P 500 ETF over different time frames \n using the average rate of return of the S&P 500 ETF as a measure of how the value of the investment increases over time.", font=("Helvetica", 15))
labelz.place(x=100, y=450)
labelq = tk.Label(root, text="The program compares the future value of the investment in the bank account with the future value of the investment \n in the S&P 500 ETF over different time frames, it does not predict the future value of a bank account that is invested in an S&P 500 ETF.", font=("Helvetica", 15))
labelq.place(x=100, y=550)

title = tk.Label(root, text="Inflation Insights", font=("Helvetica", 42))
title.pack(pady=10)

# Create a new frame to hold the label and entry widgets for bank balance
frame1 = tk.Frame(root)
frame1.pack(side=LEFT, anchor='n')

label1 = tk.Label(frame1, text="Enter your bank balance:", font=("Helvetica", 18))
label1.grid(row=1, column=1, padx=10, pady=10)

entry = tk.Entry(frame1, width=50)
entry.grid(row=2, column=1, padx=10, pady=10)

# Create a new frame to hold the label and entry widgets for country code
frame2 = tk.Frame(root)
frame2.pack(side=LEFT, anchor='n')

label2 = tk.Label(frame2, text="Enter your country code:", font=("Helvetica", 18))
label2.grid(row=1, column=1, padx=10, pady=10)

entry2 = tk.Entry(frame2, width=50)
entry2.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()
submit_button.place(x=300, y=200)


root.mainloop()


