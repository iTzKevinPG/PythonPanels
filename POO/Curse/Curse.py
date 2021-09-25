class Curse :
    
    #Default Parameters
    code: int
    nameCurse: str
    schedule: str
    creditsCurse: int 
    
    #Instance Parameters
    teacher: str
    studentsCurse = []
    activities = []
        
    #Contructor
    def __init__(self, code: int, nameCurse: str, schedule: str, creditsCurse: int):
        
        self.code = code
        self.nameCurse = nameCurse
        self.schedule = schedule
        self.creditsCurse = creditsCurse
    
    #Methods
    def assignTeacher(self, teacherName: str):
        
        self.teacher = teacherName
        print("Se asigno el docente " + self.teacher)
        pass
    
    def enrollStudent(self, studentName: str, studentId: int):               
        
        self.studentsCurse.append({'studentName': studentName, 'studentId': studentId})
        print("Se matriculo el estudiante " + studentName + " con la identificacion", studentId)
        pass
    
    def deEnrollStudent(self, studentId: int):
        
        for i in range(len(self.studentsCurse)):
            
            if self.studentsCurse[i]['studentId'] == studentId:
                
                print("Se elimino el estudiante " + str(self.studentsCurse[i]['studentName']))
                del self.studentsCurse[i]                
                break
        
        pass
    
    def addActivity(self, activityName: str, activityDesc: str):               
        
        self.activities.append({'activityName': activityName, 'activityDesc': activityDesc})
        print("Se agrego la actividad " + activityName)
        pass
    
    def showActivities(self):
        
        for i in range(len(self.activities)):
            
            print(str(i+1) + ". " + self.activities[i]['activityName'] + ":")
            print("   " + self.activities[i]['activityDesc'])
        
        pass
    
    def showStudents(self):
        
        for i in range(len(self.studentsCurse)):
            
            print(str(i+1) + ". " + self.studentsCurse[i]['studentName'] + " con identificador " + str(self.studentsCurse[i]['studentId']))
        
        pass
    
    def showTeacher(self):
        
        print("El docente del curso " + self.nameCurse + " es " + self.teacher)
        
        pass