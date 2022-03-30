
import datetime as dt

mon = ["과학", "사회", "수학", "체육", "좌파", "컴구", "컴구", "DB1", "WEB1"]
tue = ["디자인", "디자인", "과학", "국어", "C언어", "C언어", "C언어", "WEB2", "프로젝트"]
wed = ["C언어", "C언어", "좌파", "수학", "전전기", "전전기", "자습", "DB2", "자습"]
thu = ["피컴", "피컴", "수학", "사회", "과학", "영어", "국어", "영어 회화", "자습"]
fri = ["사회", "개노잼 진로", "영어(정)", "성직", "CA", "CA", "집"]

a= dt.datetime.now()
b= a.weekday()
if a.weekday() == 0:
    print(mon)
elif b == 1:
    print(tue)
elif b == 2:
    print(wed)
elif b == 3:
    print(thu)
elif b == 4:
    print(fri)
else :
    print("버그 ㅋㅋ")

