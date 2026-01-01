# Currency Converter

This is a simple command-line based currency converter written in Python. The program converts a given amount from one currency to another using predefined exchange rates stored in a dictionary. The conversion is done by first converting the source currency into USD and then converting it into the target currency.

The program supports the following currencies: USD (US Dollar), INR (Indian Rupee), EURO (Euro), YEN (Japanese Yen), and GBP (British Pound). If the user enters a currency that is not supported, the program safely displays an error message and stops the conversion.

The user is prompted to enter the amount, the source currency, and the target currency. All currency inputs are converted to uppercase to avoid case-sensitivity issues. If the conversion is successful, the final converted amount is displayed with two decimal places.

To run the program, clone the repository using:
git clone https://github.com/shivaamsingh/currency-converter.git

Navigate to the project folder:
cd currency-converter

Run the program using:
python currency_converter.py

Example:
Currency Converter
Currencies Supported: USD, INR, EURO, YEN, GBP

Enter amount: 100
From Currency: USD
To Currency: INR

100.00 USD = 8999.00 INR

This project is written in Python 3 and is intended for beginners to understand basic concepts such as functions, dictionaries, conditional statements, and user input handling.

Author: Shivam Singh  
GitHub: https://github.com/shivaamsingh

