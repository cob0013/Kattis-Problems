import math	
line = list(map(float, input().split()))
h = line[0]
ang = line[1]
print(math.ceil((h  / (math.sin(math.radians(ang))))))