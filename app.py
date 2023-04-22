#!/usr/bin/env python
# coding: utf-8

# In[5]:


#pip install flask_cors


# In[6]:


#pip install --upgrade python
# conda update python


# In[7]:


from flask import Flask, request, render_template
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("model.pk2", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods = ["GET", "POST"])
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Departure_Time"]
        Day = int(pd.to_datetime(date_dep).day)
        Month = int(pd.to_datetime(date_dep).month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep).hour)
        Dep_min = int(pd.to_datetime(date_dep).minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        #date_arr = request.form["Arrival_Time"]
        #Arrival_hour = int(pd.to_datetime(date_arr).hour)
        #Arrival_min = int(pd.to_datetime(date_arr).minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        #dur_hour = abs(Arrival_hour - Dep_hour)
        #dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Direct = int(request.form["Direct"])
        # print(Total_stops)

        Transit = 0
        #Transit=int(request.form["Transit"])

        #Baggage = 0
        Baggage=int(request.form['Baggage'])

        Quarter = 3
        #Quarter=int(request.form['Quarter'])

        # Month
        #Month=int(request.form['Month'])

        # Airline
        # AIR ASIA = 0 (not in column)
        airline=request.form['Airline']
        if(airline=='Air New Zealand'):
            Air_New_Zealand = 1
            Jetstar = 0
            Sounds_Air = 0

        elif (airline=='Jetstar'):
            Air_New_Zealand = 0
            Jetstar = 1
            Sounds_Air = 0
            
        elif (airline=='Sounds Air'):
            Air_New_Zealand = 0
            Jetstar = 0
            Sounds_Air = 1
            
        else:
            Air_New_Zealand = 0
            Jetstar = 0
            Sounds_Air = 0     

        # Source
 
        Source = request.form["Departure_Airport"]
        if (Source == 'Auckland'):
            Dep_Auckland = 1
            Dep_ChristChurch = 0
            Dep_Queenstown = 0
            Dep_Wellington = 0

        elif (Source == 'ChristChurch'):
            Dep_Auckland = 0
            Dep_ChristChurch = 1
            Dep_Queenstown = 0
            Dep_Wellington = 0

        elif (Source == 'Queenstown'):
            Dep_Auckland = 0
            Dep_ChristChurch = 0
            Dep_Queenstown = 1
            Dep_Wellington = 0

        elif (Source == 'Wellington'):
            Dep_Auckland = 0
            Dep_ChristChurch = 0
            Dep_Queenstown = 0
            Dep_Wellington = 1

        else:
            Dep_Auckland = 0
            Dep_ChristChurch = 0
            Dep_Queenstown = 0
            Dep_Wellington = 0

        # print(s_Delhi,
        #     s_Kolkata,
        #     s_Mumbai,
        #     s_Chennai)

        # Destination
        # Banglore = 0 (not in column)
        Source = request.form["Arrival_Airport"]
        if (Source == 'Auckland'):
            Arr_Auckland = 1
            Arr_ChristChurch = 0
            Arr_Dunedin = 0
            Arr_Nelson  = 0
            Arr_New_Plymouth_Airport=0
            Arr_Palmerston=0
            Arr_Queenstown=0
            Arr_Wellington=0
            Arr_Hawkes=0
        
        elif (Source == 'ChristChurch'):
            Arr_Auckland = 0
            Arr_ChristChurch = 1
            Arr_Dunedin = 0
            Arr_Nelson  = 0
            Arr_New_Plymouth_Airport=0
            Arr_Palmerston=0
            Arr_Queenstown=0
            Arr_Wellington=0
            Arr_Hawkes=0
            
        elif (Source == 'Dunedin'):
            Arr_Auckland = 0
            Arr_ChristChurch = 0
            Arr_Dunedin = 1
            Arr_Nelson  = 0
            Arr_New_Plymouth_Airport=0
            Arr_Palmerston=0
            Arr_Queenstown=0
            Arr_Wellington=0
            Arr_Hawkes=0
            
        elif (Source == 'Nelson'):
            Arr_Auckland = 0
            Arr_ChristChurch = 0
            Arr_Dunedin = 0
            Arr_Nelson  = 1
            Arr_New_Plymouth_Airport=0
            Arr_Palmerston=0
            Arr_Queenstown=0
            Arr_Wellington=0
            Arr_Hawkes=0
            
        elif (Source == 'New Plymouth Airport'):
            Arr_Auckland = 0
            Arr_ChristChurch = 0
            Arr_Dunedin = 0
            Arr_Nelson  = 0
            Arr_New_Plymouth_Airport=1
            Arr_Palmerston=0
            Arr_Queenstown=0
            Arr_Wellington=0
            Arr_Hawkes=0
            
        elif (Source == 'Palmerston'):
            Arr_Auckland = 0
            Arr_ChristChurch = 0
            Arr_Dunedin = 0
            Arr_Nelson  = 0
            Arr_New_Plymouth_Airport=0
            Arr_Palmerston=1
            Arr_Queenstown=0
            Arr_Wellington=0
            Arr_Hawkes=0
            
        elif (Source == 'Queenstown'):
            Arr_Auckland = 0
            Arr_ChristChurch = 0
            Arr_Dunedin = 0
            Arr_Nelson  = 0
            Arr_New_Plymouth_Airport=0
            Arr_Palmerston=0
            Arr_Queenstown=1
            Arr_Wellington=0
            Arr_Hawkes=0
            
        elif (Source == 'Wellington'):
            Arr_Auckland = 0
            Arr_ChristChurch = 0
            Arr_Dunedin = 0
            Arr_Nelson  = 0
            Arr_New_Plymouth_Airport=0
            Arr_Palmerston=0
            Arr_Queenstown=0
            Arr_Wellington=1
            Arr_Hawkes=0
            
            
        elif (Source == "Hawkes"):
            Arr_Auckland = 0
            Arr_ChristChurch = 0
            Arr_Dunedin = 0
            Arr_Nelson  = 0
            Arr_New_Plymouth_Airport=0
            Arr_Palmerston=0
            Arr_Queenstown=0
            Arr_Wellington=0
            Arr_Hawkes=1
                 
        else:
            Arr_Auckland = 0
            Arr_ChristChurch = 0
            Arr_Dunedin = 0
            Arr_Nelson  = 0
            Arr_New_Plymouth_Airport=0
            Arr_Palmerston=0
            Arr_Queenstown=0
            Arr_Wellington=0
            Arr_Hawkes=0

        # print(
        #     d_Cochin,
        #     d_Delhi,
        #     d_New_Delhi,
        #     d_Hyderabad,
        #     d_Kolkata
        # )
        

    #     ['Total_Stops', 'Journey_day', 'Journey_month', 'Dep_hour',
    #    'Dep_min', 'Arrival_hour', 'Arrival_min', 'Duration_hours',
    #    'Duration_mins', 'Airline_Air India', 'Airline_GoAir', 'Airline_IndiGo',
    #    'Airline_Jet Airways', 'Airline_Jet Airways Business',
    #    'Airline_Multiple carriers',
    #    'Airline_Multiple carriers Premium economy', 'Airline_SpiceJet',
    #    'Airline_Trujet', 'Airline_Vistara', 'Airline_Vistara Premium economy',
    #    'Source_Chennai', 'Source_Delhi', 'Source_Kolkata', 'Source_Mumbai',
    #    'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
    #    'Destination_Kolkata', 'Destination_New Delhi']


    #Index(['Direct'--direct, 'Transit--no', 'Baggage', 'Day', 'Month', 'Quarter',
      # 'Air New Zealand', 'Jetstar', 'Sounds Air', 'Dep_Auckland',
       #'Dep_ChristChurch', 'Dep_Queenstown', 'Dep_Wellington', 'Arr_Auckland',
       #'Arr_ChristChurch', 'Arr_Dunedin', 'Arr_Hawkes', 'Arr_Nelson',
       #'Arr_New Plymouth Airport', 'Arr_Palmerston', 'Arr_Queenstown',
      # 'Arr_Wellington'],
     # dtype='object')
        
        prediction=model.predict([[
            Direct,
            Transit,
            Baggage,
            Month,
            Day,
            Quarter,
            Air_New_Zealand,
            Jetstar,
            Sounds_Air,
            Dep_Auckland,
            Dep_ChristChurch,
            Dep_Queenstown,
            Dep_Wellington,
            Arr_Auckland,
            Arr_ChristChurch,
            Arr_Dunedin,
            Arr_Hawkes,
            Arr_Nelson,
            Arr_New_Plymouth_Airport,
            Arr_Palmerston,
            Arr_Queenstown,
            Arr_Wellington
        ]])

        output=round(prediction[0],2)

        return render_template('index.html',prediction_text="Your Flight price is $. {}".format(output))


    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)


# In[ ]:




