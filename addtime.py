#Function Start with 12 hour clock (AM/PM), Duration in hours and minutes, day of the week(Optional)

def addtime(hourone, hourtwo, day):
    
    #Split hour number from AM/PM
    hour,time = hourone.split()
    
    totalhour = float(hour) + float(hourtwo)
    time = time.upper
    results = ""
    
   
        
    #AM/PM actions
    if time == "PM":
    
        if totalhour >= 12:
            
            print(totalhour, "AM", "Next day")
        if totalhour < 12:
            print(totalhour, "PM")
        

    elif time == "AM":
        if totalhour > 12:
            
            print(totalhour, "PM")
        if totalhour <= 12:
            print(totalhour, "AM")
            

        
    
    
            
    
        
            

        
 

        

    