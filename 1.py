#input
capital = float(input("Enter the capital "))
rate = float(input("Enter the rate without % ex:5.25 "))
years = int(input("Enter the number of years "))

#process
interest = capital * rate / 100 * years

#output
print("calculated interest is", interest)

