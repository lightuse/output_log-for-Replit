# output log

#Importing the datetime to get the current date and time
from datetime import datetime

#This function will log each multi game run to include the date/time and the details of the run
def output_log(number: int):
    file = open("log.txt", "a")
    #Create a date/time object to get the current date and time
    now = datetime.now()
    #Formatting the output of the date and time to dd/mm/YY H:M:S
    string_datetime = now.strftime("%d/%m/%Y %H:%M:%S")
    file.write("\ndate and time = " + string_datetime)
    file.write("\nprice = " + str(number))

#This function is created to play a single game and print out the results after each roll.
def order_one(records: list):
    number = 128
    output_log(number)

#The main function as the point of entry
def main():

    print("Running one sample order in full:")
    records = [
    ]
    order_one(records)

if __name__ == "__main__":
    main()