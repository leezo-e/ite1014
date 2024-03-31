score = int(input("Enter the integer score (0~100):"))
if score >= 95 :
    print ("you get A+.")

elif score >= 90 and score < 95 :
    print("You get A0.")

elif score >= 85 and score < 90 :
    print("You get B+.")

elif score >= 80 and  score < 85 :
    print("You get B0.")

elif score >= 75 and score < 80 :
    print ("You get C+.")

else : 
    print("You get F.")
