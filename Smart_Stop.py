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



