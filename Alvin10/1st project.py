LDL = 1
HDL = 2
TRI = LDL + HDL
total = LDL + HDL + (TRI/5.0)
if (LDL < 100) and (HDL> 60) and (TRI<150) and (total<200):
    print ("OK")
elif (LDL>130) or (HDL<50) or (TRI> 200) or (total>240):
    print ("warning")
else:
    print ("borderline cholestrol problems!")