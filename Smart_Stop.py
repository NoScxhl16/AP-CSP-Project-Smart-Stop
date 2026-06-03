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
