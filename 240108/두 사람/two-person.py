s = input().split()
age_first = int(s[0])
sex_first = s[1]

a = input().split()
age_second = int(a[0])
sex_second = a[1]

if (age_first>=19 and sex_first =="M") or (age_second>=19 and sex_second=="M"):
    print(1)
else:
    print(0)