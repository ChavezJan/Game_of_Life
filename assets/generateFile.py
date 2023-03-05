"""
    Name: Jorge Alejandro Chavez Nuñez
    ID: 0199414
"""
"""
    Write the new text without Space's
"""
import time
def fileWrite(text) -> None:
    file = open("Report.txt","a")
    text +="\n"
    file.write(text)
    file.close()

"""
    Generate Report
"""
def generateReportToW(fps,patterns)-> None:
    total =0
    for i in patterns:
        total += i
    if(total == 0):
        total +=1
    # time.sleep(2)
    text = "|Iteration: " + str(fps+1) +" |\n"
    text += "−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−----"+"\n"
    text += "|               | Count |  Percent |"+"\n"
    text += "|−−−−−−−−−− + −−−− + −−−− + −−−−−−−−−−|"+"\n"
    text += "|Block         |   "+str(patterns[0])+"   |    "+(str(round((patterns[0]*100)/total,2)))+"    |"+"\n"
    text += "|Beehive       |   "+str(patterns[1])+"   |    "+(str(round((patterns[1]*100)/total,2)))+"    |"+"\n"
    text += "|Loaf          |   "+str(patterns[2])+"   |    "+(str(round((patterns[2]*100)/total,2)))+"    |"+"\n"
    text += "|Boat          |   "+str(patterns[3])+"   |    "+(str(round((patterns[3]*100)/total,2)))+"    |"+"\n"
    text += "|Tub           |   "+str(patterns[4])+"   |    "+(str(round((patterns[4]*100)/total,2)))+"    |"+"\n"
    text += "|Blinker       |   "+str(patterns[5])+"   |    "+(str(round((patterns[5]*100)/total,2)))+"    |"+"\n"
    text += "|Toad          |   "+str(patterns[6])+"   |    "+(str(round((patterns[6]*100)/total,2)))+"    |"+"\n"
    text += "|Beacon        |   "+str(patterns[7])+"   |    "+(str(round((patterns[7]*100)/total,2)))+"    |"+"\n"
    text += "|Glider        |   "+str(patterns[8])+"   |    "+(str(round((patterns[8]*100)/total,2)))+"    |"+"\n"
    text += "|LG sp ship    |   "+str(patterns[9])+"   |    "+(str(round((patterns[9]*100)/total,2)))+"    |"+"\n"
    text += "|−−−−−−−−−− + −−−− + −−−− + −−−−−−−−−−|"+"\n"
    text += "|Total | "+str(total)+" | |"+"\n"
    text += "−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−"+"\n"
    fileWrite(str(text))




    