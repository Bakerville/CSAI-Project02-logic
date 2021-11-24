def sortedClause(clause):
    return sorted(clause, key = lambda x: x[1])
def read_file(filename):
    file = open(filename, 'r')
    index = 0
    alpha = []
    KB = []
    for line in file:
        if(index==0):
            clause = line.strip().split(" OR ")
            for i in range(len(clause)):
                if(clause[i][0]!='-'):
                    clause[i] = " " + clause[i]
            alpha = clause
        elif(index==1):
            count = int(line)
        else:
            clause = line.strip().split(" OR ")
            for i in range(len(clause)):
                if(clause[i][0]!='-'):
                    clause[i] = " " + clause[i]
            KB.append(sortedClause(clause))
        index+=1
    return KB,alpha
def Combinable(clause_1, clause_2):
    count = 0
    word = ""
    for i in clause_1:
        for j in clause_2:
            if(i[1]==j[1]):
                if(i[0]!=j[0]):
                    count+=1
                    word = i[1]
    if(count!=1):
        return -1
    return word
def negativeClause(clause):
    neg = []
    for i in clause:
        if(i[0]==" "):
            neg.append(["-"+i[1]])
        elif(i[0]=="-"):
            neg.append([" " + i[1]])
    return neg
def PL_resolve(clause_1, clause_2):
    new = []
    word = Combinable(clause_1,clause_2)
    if word!=-1:
        new = clause_1 + clause_2
        new = sortedClause(new)

        for i in new.copy():
            if(word in i):
                new.remove(i)
        return list(dict.fromkeys(new))
    return -1
def PL_resolution(KB, alpha):
    steps = []
    clauses = KB.copy()
    clauses.extend(negativeClause(alpha))
    while True:
        new = []
        for i in range(0,len(clauses)-1):
            for j in range(i+1,len(clauses)):
                resolvents = PL_resolve(clauses[i], clauses[j])
                if resolvents == []:
                    new.append("{}")
                    steps.append(new)
                    return True, steps
                if(resolvents not in clauses and resolvents!=-1):
                    new.append(resolvents)
        if(new!=[]):
            steps.append(new)
        else:
            return False, steps
        clauses.extend(new)
def changedClause(clause):
    if clause =="{}":
        return clause
    for i in range(len(clause)):
        if clause[i][0]==" ":
            clause[i] = clause[i][1]
    return " OR ".join(clause)
def write_file(filename, steps,result):
    f = open(filename, "w")
    for i in steps:
        f.write(str(len(i)))
        f.write("\n")
        for j in i:
            f.write(changedClause(j))
            f.write("\n")
    if(result==True):
        f.write("Yes")
    else:
        f.write("No")
    f.close()
if __name__ == '__main__':
    KB, alpha = read_file("input_0.txt")
    result, steps = PL_resolution(KB, alpha)
    write_file("output_0.txt", steps, result)
    KB,alpha = read_file("input_1.txt")
    result, steps = PL_resolution(KB,alpha)
    write_file("output_1.txt",steps,result)
    KB, alpha = read_file("input_2.txt")
    result, steps = PL_resolution(KB, alpha)
    write_file("output_2.txt", steps, result)
    KB, alpha = read_file("input_3.txt")
    result, steps = PL_resolution(KB, alpha)
    write_file("output_3.txt", steps, result)
    KB, alpha = read_file("input_4.txt")
    result, steps = PL_resolution(KB, alpha)
    write_file("output_4.txt", steps, result)
    filename = input("Nhap duong dan moi: ")
    if(filename==""):
        exit()
    else:
        result_file = filename[:-4] +"_result.txt"
        KB, alpha = read_file(filename)
        result, steps = PL_resolution(KB, alpha)
        write_file(result_file, steps, result)
