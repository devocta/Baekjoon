num = input()
res = 0
num_dict = {"A" : 10, "B" : 11, "C": 12, "D" : 13, "E": 14, "F" :15}
plc_val = 0
for i in range(len(num) -1, -1, -1):
    if num[i] in list(num_dict.keys()):
        for j in list(num_dict.keys()):
            if num[i] == j:
                res += num_dict.get(j) * 16 ** plc_val
                plc_val +=1
    else:
        res += int(num[i]) * 16 ** plc_val
        plc_val +=1
print(res)