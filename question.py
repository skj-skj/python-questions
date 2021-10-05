# Ques 1) Filter Odd & Even Number from the Number List.
def ques1():
    nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
    odds = list(filter(lambda x:x%2!=0,nums))
    evens = list(filter(lambda x:x%2==0,nums))
    print(f"Numbrs: {nums}\nOdd Numbers: {odds}\nEven Numbers: {evens}")

# Ques 2) A List Contains Numbers & String, Filter Numbers & String in separate List.
def ques2():
    items = [1,2,3,"Numbers","String"]
    nums = []
    strings = []
    for n in items:
        try:
            n = int(n)
            nums.append(n)
        except:
            strings.append(n)

    print(f"Items: {items}\nNumbers: {nums}\nStrings: {strings}")

# Ques 3) Find Sum of all Odd Number till N.
def ques3():
    n = int(input("Enter n: "))
    sum = 0
    for i in range(1,n+1):
        if i%2!=0:
            sum+=i

    print(f"Total Odd Sum: {sum}")

# Ques 4) Find Sum of all Even Number till N.
def ques4():
    n = int(input("Enter n: "))
    sum = 0
    for i in range(1,n+1):
        if i%2==0:
            sum+=i

    print(f"Total Odd Sum: {sum}")

ques4()