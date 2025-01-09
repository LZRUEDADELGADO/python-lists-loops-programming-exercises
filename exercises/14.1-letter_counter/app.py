par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

for char in par.lower():
    if char.isalpha():  
        if char in counts:
            counts[char] += 1  
        else:
            counts[char] = 1  

print(counts)

