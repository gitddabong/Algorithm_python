n = int(input())
x = 1
y = 1

plan = list(input().split())

for i in range(len(plan)):
    signal = plan[i]

    if signal == "L":
        if x < n:
            x -= 1
        
    if signal == "R":
        if x > 0:
            x += 1

    if signal == "U":
        if y > 1:
            y -= 1
    
    if signal == "D":
        if y < n:
            y += 1
            
print(y, x)