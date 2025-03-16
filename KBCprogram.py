print("KBC")
ques=[1,2,3,4,5,6,7]
ans=[1,2,3,4,5,6,7]
ques[0]="1)what is the capital of India?\na.delhi\nb.haryana\nc.karnataka\nd.kashmir\nanswer:"
ques[1]="2)what is 30+29?\na.55\nb.59\nc.67\nd.78\nanswer:"
ques[2]="3)when does the leap year comes?\na.every 3year\nb.every 2years\nc.every 16years\nd.every 4 years\nanswer:"
ques[3]="4)colour blue and yellow gives____\na.burgundy\nb.green\nc.white\nd.orange\nanswer:"
ques[4]="5)how many bones are there in a human body?\na.206\nb.308\nc.196\nd.247\nanswer:"
ques[5]="6)how many states are there in India?\na.33\nb.28\nc.45.\nd.16\nanswer:"
ques[6]="7)how many seas are there on earth?\na.23\nb.over30\nc.over50\nd.70\nanswer:"
ans[0]="a"
ans[1]="b"
ans[2]="d"
ans[3]="b"
ans[4]="a"
ans[5]="b"
ans[6]="c"
print("Let's start")
for q in ques[6]:
 q1=input(ques[0])
 if q1==ans[0]:
    print("correct ans, you won 100pts")
    q1=100
 else:
    print("wrong ans")
    q1=0
    print("The total points earned:", q1 )
    break

 q2=input(ques[1])
 if q2==ans[1]:
    print("correct ans, you won 100pts")
    q2=100
 else:
    print("wrong ans")
    q2=0
    print("The total points earned:", q1 + q2 )
    break
 q3=input(ques[2])
 if q3==ans[2]:
    print("correct ans, you won 100pts")
    q3=100
 else:
    print("wrong ans")
    q3=0
    print("The total points earned:", q1 + q2 + q3 )
    break
 q4=input(ques[3])
 if q4==ans[3]:
    print("correct ans, you won 100pts")
    q4=100
 else:
    print("wrong ans")
    q4=0
    print("The total points earned:", q1 + q2 + q3 + q4 )
    break
 q5=input(ques[4])
 if q5==ans[4]:
    print("correct ans, you won 100pts")
    q5=100
 else:
    print("wrong ans")
    q5=0
    print("The total points earned:", q1 + q2 + q3 + q4 + q5 )
    break
 q6=input(ques[5])
 if q6==ans[5]:
    print("correct ans, you won 100pts")
    q6=100
 else:
    print("wrong ans")
    q6=0
    print("The total points earned:", q1 + q2 + q3 + q4 + q5 + q6 )
    break
 q7=input(ques[6])
 if q7==ans[6]:
    print("correct ans, you won 100pts")
    q7=100
 else:
    print("wrong ans")
    q7=0
    print("The total points earned:", q1 + q2 + q3 + q4 + q5 + q6 + q7)
 break
print("THANK YOU FOR PLAYING")


