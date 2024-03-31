score = int(input("Enter the score (0~100%):"))
rank = int(input("Enter the ranking (0~100%):"))

if score >= 90 and rank <= 40 :
    print ("You get A+.")

elif score >= 80 and rank <= 40 :
    print ("you get A0.")

elif score >= 65 and rank <= 80 :
    print (" You get B+.")

elif score > 50 and rank <= 80 :
    print ("You get B0.")

elif score < 40 :
    print ("you get F.")

else :
    print ("you get C+/C0.")
    