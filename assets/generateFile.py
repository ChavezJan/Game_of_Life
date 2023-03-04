"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
"""
    Write the new text without Space's
"""
def fileWrite(text) -> None:
    file = open("Report.txt","a")
    text +="\n"
    file.write(text)
    file.close()

"""
    Generate Report
"""
def generateReportToW(fps,patterns)-> None:
    total =1
    for i in patterns:
        total += i

    text = "|Iteration: " + str(fps+1) +" |\n"
    text += "−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−----"+"\n"
    text += "|               | Count |  Percent |"+"\n"
    text += "|−−−−−−−−−− + −−−− + −−−− + −−−−−−−−−−|"+"\n"
    text += "|Block         |   "+str(patterns[0])+"   |    "+(str((patterns[0]*100)/total))+"    |"+"\n"
    text += "|Beehive       |   "+str(patterns[1])+"   |    "+(str((patterns[1]*100)/total))+"    |"+"\n"
    text += "|Loaf          |   "+str(patterns[2])+"   |    "+(str((patterns[2]*100)/total))+"    |"+"\n"
    text += "|Boat          |   "+str(patterns[3])+"   |    "+(str((patterns[3]*100)/total))+"    |"+"\n"
    text += "|Tub           |   "+str(patterns[4])+"   |    "+(str((patterns[4]*100)/total))+"    |"+"\n"
    text += "|Blinker       |   "+str(patterns[5])+"   |    "+(str((patterns[5]*100)/total))+"    |"+"\n"
    text += "|Toad          |   "+str(patterns[6])+"   |    "+(str((patterns[6]*100)/total))+"    |"+"\n"
    text += "|Beacon        |   "+str(patterns[7])+"   |    "+(str((patterns[7]*100)/total))+"    |"+"\n"
    text += "|Glider        |   "+str(patterns[8])+"   |    "+(str((patterns[8]*100)/total))+"    |"+"\n"
    text += "|LG sp ship    |   "+str(patterns[9])+"   |    "+(str((patterns[9]*100)/total))+"    |"+"\n"
    text += "|−−−−−−−−−− + −−−− + −−−− + −−−−−−−−−−|"+"\n"
    text += "|Total | "+str(total)+" | |"+"\n"
    text += "−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−"+"\n"
    fileWrite(str(text))




    