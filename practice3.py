def string_test(string):
    upper_case=0
    lower_case=0
    for i in string:
        if i.isupper():
           upper_case+=1
        elif i.islower():
           lower_case+=1
        else:
           pass
    print("no of Upper case charachters:",upper_case) 
    print("no of Lower case charachters:",lower_case)   

string_test(input("Enter the sample string:"))