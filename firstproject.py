##'''a=2;
##print(type(a));
##a=3.2;
##print(type(a));
##b='sri';
##print(str(a)+b'''

a = float(input('Add an operand'));
b = float(input("Add another operand"));
c = input('''Choose an operator''');
print(a,b,c);
if(c=='+'):
    print('Addition:',a+b);

elif(c=='-'):
    print('Subtraction:',a-b);

elif(c=='*'):
    print('Multiplication:',a*b);

elif(c=='/'):
    try:
        print('Division:',a/b);
    except Exception as e:
        print(e);

elif(c=='%'):
    print('Modulus:',a%b);

else:
    print('Please enter valid operator');
    
