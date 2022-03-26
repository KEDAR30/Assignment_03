def fun (str):
    upper=0
    lower=0
    for i in str :
        if i.isupper():
            upper +=1
        elif i.islower():
            lower +=1

    print('no. of upper case characters:',upper)
    print('no. of lower case characters:',lower)

s= str(input("Enter any string :"))
fun(s)
