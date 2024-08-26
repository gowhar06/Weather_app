# Wheather App Development using Python
# Importing all required libraries

from tkinter import *
from tkinter import ttk
import requests

# Function Call 
def get_data():
    city = city_name.get()
    try:
        # Request weather data from the API
        data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8783508a81114c2ca97693ae68954766").json()
        
        if data["cod"] == 200:  # Check if the response is successful
            climate_label.config(text="Climate: " + data["weather"][0]["main"])
            description_label.config(text="Description: " + data["weather"][0]["description"])
            temp_label.config(text="Temp: " + str(round(data["main"]["temp"] - 273.15, 2)) + " °C")
            temp_min_label.config(text="Temp Min: " + str(round(data["main"]["temp_min"] - 273.15, 2)) + " °C")
            temp_max_label.config(text="Temp Max: " + str(round(data["main"]["temp_max"] - 273.15, 2)) + " °C")
            humidity_label.config(text="Humidity: " + str(data["main"]["humidity"]) + "%")
            pressure_label.config(text="Pressure: " + str(data["main"]["pressure"]) + " hPa")
        else:
            # Handle errors, such as city not found
            climate_label.config(text="Error: " + data["message"])
            description_label.config(text="")
            temp_label.config(text="")
            temp_min_label.config(text="")
            temp_max_label.config(text="")
            humidity_label.config(text="")
            pressure_label.config(text="")
    # Is used to handle error in handling the data        
    except Exception as e:
        climate_label.config(text="Error: Unable to retrieve data")
        description_label.config(text=str(e))
        temp_label.config(text="")
        temp_min_label.config(text="")
        temp_max_label.config(text="")
        humidity_label.config(text="")
        pressure_label.config(text="") 

# Initializing the main window
win = Tk()
win.title("Indian Weather App")
win.config(bg="blue")
win.geometry("500x500")


# Title Label
name_label = Label(win, text="Indian Weather App", font=("Times New Roman", 30), bg="blue", fg="white")
name_label.place(x=25, y=50, height=50, width=450)

# City Selection Combobox
city_name = StringVar()
list_name = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
    "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra",
    "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu",
    "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal", "Andaman and Nicobar Islands",
    "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep", "National Capital Territory of Delhi",
    "Puducherry"
]
com = ttk.Combobox(win, values=list_name, font=("Times New Roman", 20), textvariable=city_name)
com.place(x=25, y=120, height=50, width=450)
com.set("Select State")  # Default text for combobox

# Weather Information Labels
climate_label = Label(win, text="Weather Climate: N/A", font=("Times New Roman", 15), bg="blue", fg="white", anchor="w")
climate_label.place(x=25, y=260, height=30, width=450)

description_label = Label(win, text="Weather Description: N/A", font=("Times New Roman", 15), bg="blue", fg="white", anchor="w")
description_label.place(x=25, y=290, height=30, width=450)

temp_label = Label(win, text="Temp: N/A", font=("Times New Roman", 15), bg="blue", fg="white", anchor="w")
temp_label.place(x=25, y=320, height=30, width=450)

temp_min_label = Label(win, text="Temp Min: N/A", font=("Times New Roman", 15), bg="blue", fg="white", anchor="w")
temp_min_label.place(x=25, y=350, height=30, width=450)

temp_max_label = Label(win, text="Temp Max: N/A", font=("Times New Roman", 15), bg="blue", fg="white", anchor="w")
temp_max_label.place(x=25, y=380, height=30, width=450)

humidity_label = Label(win, text="Humidity: N/A", font=("Times New Roman", 15), bg="blue", fg="white", anchor="w")
humidity_label.place(x=25, y=410, height=30, width=450)

pressure_label= Label(win, text="Pressure: N/A", font=("Times New Roman", 15), bg="blue", fg="white", anchor="w")
pressure_label.place(x=25, y=440, height=30, width=450)

# Done Button
done_button = Button(win, text="Done", font=("Times New Roman", 30), command=get_data)
done_button.place(x=200, y=190, height=50, width=100)

# Run the main loop
win.mainloop()