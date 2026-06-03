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
