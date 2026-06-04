# Sets the background color and how fast the simulation updates.
app.background ='lightCyan'
app.stepsPerSecond = 30

# Lists to keep track of the amount of students, the wait time, and the buses.
app.students=[]
app.studentWaitTimes=[]
app.buses=[]

# Main starting values for the simulation
app.weather = 'Clear'
app.simulationRunning=False
app.totalWaitTime=0
app.waitGoal=30
app.busCapacity=4
app.totalStudentsAdded=0
app.studentsPickedUp=0
app.stepCounter=0

# The drawing of the title and subtitle
Label('Smart Stop',200,20,size=26,bold=True)
Label('Bus Pickup Simulator',200,43,size=13)

# The drawing for the bus stop area
Rect(20,75,360,135,fill='lightGray',border='black')
Rect(35,100,95,70,fill='white',border='black')
Polygon(30,100,82,65,135,100,fill='darkSlateGray')
Label('BUS STOP',82,128,size=11,bold=True)
Label('Waiting Area',250,95,size=12,bold=True)

# Section for drawing the road and yellow lines
Rect(0,220,400,55,fill='dimGray')
Line(0,247,400,247,fill='yellow',lineWidth=3,dashes=True)
Label('Pickup Road',200,290,size=12, bold=True)

# Creates the risk meter that shows how unsafe the waiting conditions are.
Rect(135,180,130,15,fill='white',border='black')
riskBar=Rect(135,180,1,15,fill='green')
Label('Risk Meter',200,173,size=10)

# Creates the buttons on the bottom for the main controls
addStudentButton=Rect(10,310,85,28,fill='white',border='black')
addBusButton=Rect(105,310,85,28,fill='white',border='black')
weatherButton=Rect(200,310,85,28,fill='white',border='black')
goalButton=Rect(295,310,85,28,fill='white',border='black')

startButton=Rect(70,350,110,30,fill='lightGreen',border='black')
resetButton=Rect(220,350,110,30, fill='fireBrick',border='black')

# Creates the text on each button for what it does
Label('+ Students',52,324,size=10,bold=True)
Label('+ Bus',147,324,size=10,bold=True)
Label('Weather',242,324,size=10,bold=True)
Label('Wait Goal',337,324,size=10,bold=True)
Label('Start/Pause',125,365,size=10,bold=True)
Label('Reset',275,365,size=11,bold=True)

# Creates labels that display live information about the simulation.
studentLabel=Label('Students: 0',55,395,size=10)
busLabel=Label('Buses: 0',135,395,size=10)
weatherLabel=Label('Weather: Clear',230,395,size=10)
riskLabel=Label('Risk: Low',335,395,size=10,fill='green')

timeLabel=Label('Time: 0/30 sec',75,58,size=11)
pickedUpLabel=Label('Picked Up: 0',180,58,size=11)
efficiencyLabel=Label('Efficiency: 0%',295,58,size=11)

adviceLabel=Label('Add students and buses, then press Start.',200,200,size=10)

# Arranges students into rows inside the waiting area so they remain visible and organized.
def arrangeStudents():
    for i in range(len(app.students)):
        app.students[i].centerX=160+(i%10)*18
        app.students[i].centerY=115+(i//10)*18
    
# Adds new students, starts their wait time at zero, and prevents the waiting area from passing 30 students.        
def addStudents(amount):
    for i in range(amount):
        if len(app.students)<30:
            student=Circle(160,115,6,fill='navy')
            app.students.append(student)
            app.studentWaitTimes.append(0)
            app.totalStudentsAdded+=1
        else: 
            adviceLabel.value='Waiting area is full. Add a bus first.'    
        
    arrangeStudents()

# Creates a bus with a chosen capacity and speed, then places it off screen before it drives in.    
def createBus(capacity,speed):
    bus = Group(
        Rect(-80,230,65,30,fill='gold',border='black'),
        Rect(-70,237,14,9,fill='skyBlue',border='black'),
        Rect(-48,237,14,9,fill='skyBlue',border='black'),
        Circle(-67,260,5,fill='black'),
        Circle(-30,260,5,fill='black'),
        Label('BUS',-48,253,size=8,bold=True)
    )
        
    bus.capacity=capacity
    bus.speed=speed
    bus.pickedUp=False
    bus.centerX=-80-len(app.buses)*90
    app.buses.append(bus)
    
# Changes the weather each time the button is clicked and updates the background to match it.    
def changeWeather():
    if app.weather=='Clear':
        app.weather='Rain'
        app.background='lightSteelBlue'
        
    elif app.weather=='Rain':
        app.weather='Snow'
        app.background='aliceBlue'
        
    elif app.weather=='Snow':
        app.weather='Hot'
        app.background='moccasin'
        
    elif app.weather=='Hot':
        app.weather='Cold'
        app.background='lavender'
        
    elif app.weather=='Cold':
        app.weather='Clear'
        app.background='lightCyan'
        
# Changes the wait goal between 30 45, and 60 seconds so the user can adjust the simulation.
def changeWaitGoal():
    if app.waitGoal==30:
        app.waitGoal=45
    elif app.waitGoal==45:
        app.waitGoal=60
    else:
        app.waitGoal=30
        
# Finds the longest wait time so the risk meter can react to the student waiting the longest.        
def findOldestWait():
    oldest=0
    
    for wait in app.studentWaitTimes:
        if wait>oldest:
            oldest=wait
            
    return oldest
    
# Calculates one risk score using weather, wait time, crowd size, bus count, and pickup efficiency.        
def calculateRisk(weatherType,waitSeconds,studentTotal,busTotal,efficiency):
    riskScore=0
    overGoalCount=0
    
    for wait in app.studentWaitTimes:
        if wait>app.waitGoal:
            overGoalCount+=1
            
    if weatherType=='Clear':
        if overGoalCount>=5 and busTotal<=1:
            riskScore+=15
        else:
            riskScore+=5
        
    elif weatherType=='Rain':
        if overGoalCount>=1:
            riskScore+=5
        elif studentTotal>=20:
            riskScore+=20
        elif studentTotal>=10:
            riskScore+=15
        
        else:
            riskScore+=12
  
    elif weatherType=='Snow':
        if overGoalCount>=1:
            riskScore+=20
        elif studentTotal>=15:
            riskScore+=40
        elif studentTotal>=10:
             riskScore+=35
        
        else:
            riskScore+=60
            
    elif weatherType=='Hot' or weatherType=='Cold':
        if overGoalCount>=1:
            riskScore+=5
        elif studentTotal>=25:
            riskScore+=20
        elif studentTotal>=15:
             riskScore+=15
        
        else:
            riskScore+=15        
                
            
    if busTotal==0 and studentTotal>=15:
        riskScore+=10
    elif busTotal==1 and studentTotal>20:
        riskScore+=7
    elif busTotal>=3:
        riskScore-=5
                
    if efficiency < 30 and app.totalStudentsAdded > 15:
        riskScore+=5
    elif efficiency > 70:
        riskScore-=5
        
    if overGoalCount>=10:
        riskScore+=15
    elif overGoalCount>=5:
        riskScore+=8
    
        
    if riskScore<0:
        riskScore=0
                
    return riskScore

# Finds the percent of all students who have been picked up.        
def findEfficiency():
    if app.totalStudentsAdded==0:
        return 0
        
    return int((app.studentsPickedUp / app.totalStudentsAdded)*100)

def pickedupStudents(bus):
    for i in range(bus.capacity):
        if len(app.students)>0:
            app.students[0].visible=False
            app.students.pop(0)
            app.studentWaitTimes.pop(0)
            app.studentsPickedUp+=1
            
    arrangeStudents()

def updateBuses():
    for bus in app.buses:
        bus.centerX +=bus.speed
        
        if bus.centerX>185 and bus.centerX < 215 and bus.pickedUp==False:
            pickedupStudents(bus)
            bus.pickedUp=True
            
        if bus.centerX>480:
            bus.centerX=-80
            bus.pickedUp=False

# Adds one second to each student's wait time.
def updateWaitTimes():
    for i in range (len(app.studentWaitTimes)):
        app.studentWaitTimes[i]+=1
        
# Updates all text labels, the risk bar, and the advice message on the screen.        
def updateLabels():
    oldestWait=findOldestWait()
    efficiency=findEfficiency()
    
    riskScore=calculateRisk(app.weather,app.totalWaitTime,len(app.students),
                            len(app.buses),efficiency)
                            
    studentLabel.value='Students: ' + str(len(app.students))
    busLabel.value='Buses: '+str(len(app.buses))
    weatherLabel.value='Weather: ' + app.weather
    timeLabel.value='Time: ' + str(app.totalWaitTime) + ' / ' + str(app.waitGoal) + ' sec'
    pickedUpLabel.value='Picked Up: ' + str(app.studentsPickedUp)
    efficiencyLabel.value='Efficiency: ' + str(efficiency) + '%'
    
    barWidth=riskScore*2
    
    if barWidth<1:
        barWidth=1
    if barWidth>130:
        barWidth=130
    
    riskBar.width=barWidth
    
    if riskScore<15:
        riskLabel.value='Risk: Low'
        riskLabel.fill='green'
        riskBar.fill='green'
        adviceLabel.value='Conditions are safe right now.'
    elif riskScore<35:
        riskLabel.value='Risk: Medium'
        riskLabel.fill='orange'
        riskBar.fill='orange'
        adviceLabel.value='Some students are starting to wait too long. Add more buses.'
    elif riskScore<55:
        riskLabel.value='Risk: High'
        riskLabel.fill='red'
        riskBar.fill='red'
        adviceLabel.value='Add buses to lower the crowd and wait time.'
    else:
        riskLabel.value='Risk: Critical'
        riskLabel.fill='darkRed'
        riskBar.fill='darkRed'
        adviceLabel.value='Unsafe waiting conditions. More buses are needed.'
