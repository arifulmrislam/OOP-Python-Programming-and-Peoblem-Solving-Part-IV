# make a room tamp controller

living_room = 33
study_room = 28
outdoor_front = 35

if(living_room >= 35):
    print(f"{living_room} temp is lower than your expectation")
elif (study_room < outdoor_front):
    print(f"Hey!! your are good to go for study because the temp is lower than {outdoor_front}")
else:
    print("You should stay at home!")