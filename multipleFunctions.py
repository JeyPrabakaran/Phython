class multipleFunctions():


    def percentage():
        Subject1=int(input('Enter Subject1 Mark: '))
        Subject2=int(input('Enter Subject2 Mark: '))
        Subject3=int(input('Enter Subject3 Mark: '))
        Subject4=int(input('Enter Subject4 Mark: '))
        Subject5=int(input('Enter Subject5 Mark: '))
        Total=(Subject1+Subject2+Subject3+Subject4+Subject5)
        Percentage=Total/5
        print('\n','Subject1=',Subject1,'\n','Subject2=',Subject2,'\n','Subject3=',Subject3,'\n','Subject4=',
        Subject4,'\n','Subject5=',Subject5)
        print('\n','Total=',Total,'\n','Percentage=',Percentage)                 


 
        
    def oddEven():
        number=int(input('Enter a Number'))
        if(number%2==0):
            print(number,'is even number')
        else:
            print(number,'is odd number')  
            
    def Eligible():
        gender=str(input('Enter Gender: '))
        Age=int(input('Enter Age: '))
        print('\n','Your Gender: ',gender,'\n','Your Age: ',Age,'\n')
        if(gender=='Male'):
            if(Age>=21):
                message='Eligible'
            else:
                message='Not Eligible'
        elif(gender=='Female'):
            if(Age>=18):
                message='Eligible'        
            else:
                message='Not Eligible'
        return message


    def BMI():
        BMI=int(input("Enter the BMI Index:"))
        if(BMI<=18.5):
            print("Underweight")
        elif(BMI<=24.9):
            print("Normal")
        elif(BMI<=29.9):
            print("Overweight")
        else:
            print("Very Overweight")
#Triangle area & perimeter    
    def areatriangle(Height,Breadth):
        print('Area Formula:(Height*Breadth/2)')
        areaTriangle=(Height*Breadth/2)
        print('Area of Triangle: ',areaTriangle)
        
             
    def perimetertriangle(Height1,Height2,Breadth2):
        print('Perimeter formula:Height1+Height2+Breadth')
        perimeter=Height1+Height2+Breadth2
        print('Perimeter of Triangle: ',perimeter)
         
#Height=int(input('Enter the Triangle Height: '))
#Breadth=int(input('Enter the Breadth of Triangle: '))
#Height1=int(input('Enter the Triangle Height1: '))
#Height2=int(input('Enter the Triangle Height2: '))
#Breadth2=int(input('Enter the Breadth of Triangle: '))            
             
                


 


