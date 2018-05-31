def creat_dict(infile_name):
    infile = open(infile_name, "r", encoding="utf-8")
    outfile = open("word.dict", "w", encoding="utf-8")
    s = infile.readline()
    word_list = []
    while s != '':
        temp_list = s.split()
        word_list.extend(temp_list)
        s = infile.readline()
    for i in word_list:
        outfile.writelines(i+'\n')
    infile.close()
    outfile.close()

def creat_text(infile_name):
    infile = open(infile_name, "r", encoding="utf-8")
    outfile = open("data.txt", "a", encoding="utf-8")
    s = infile.readline()
    while s != '':
        temp_list = s.split()
        for i in temp_list:
            outfile.write(i)
        outfile.write("\n")
        s = infile.readline()
    infile.close()
    outfile.close()

def SegWords(dict_name, data_name):
    word_dict=set()
    result = []
    # 读取字典文件
    with open(dict_name,"r",encoding="utf-8") as dictfile:
        for word in dictfile.readlines():
            word=word.strip()  # 去掉换行符
            word_dict.add(word)
    # 读取目标分词文件
    with open(data_name,"r", encoding="utf-8") as datafile:
        for line in datafile.readlines():
            line=line.strip()  # 去掉换行符
            i=0
            res=[]
            # 逐行读取每行进行分词操作，结果放到res中
            while i<len(line):
                for j in range(10):
                    temp = 10-j+i
                    s=line[i:temp]
                    if s in word_dict:
                        res.append(s)
                        i=temp
                        break
                    # 如果只剩一个字则直接分词
                    if j==9:
                        res.append(line[i])
                        i=i+1
                        break
            result.append(res)
    # 将结果输出到文件
    with open("data.out","a", encoding="utf-8") as resultFile:
        for row in result:
            for word in row:
                resultFile.write(word+" ")
            resultFile.write("\n")
    return result

def eval(resultFile,answerFile):
    count_right = 0  # 正确识别的个体总数
    count_split = 0  # 识别出的个体总数
    count_ans = 0  # 测试集中存在的个体总数
    list1 = []  # 用于存放算法得出的结果
    list2 = []  # 用于存放词典中的结果
    with open(resultFile, "r", encoding="utf-8") as resultFile:
        for s1 in resultFile.readlines():
            temp_list1=s1.split()
            count_split += len(temp_list1)
            list1.append(temp_list1)
    with open(answerFile, "r", encoding="utf-8") as answerFile:
        for s2 in answerFile.readlines():
            temp_list2=s2.split()
            count_ans+=len(temp_list2)
            list2.append(temp_list2)

    # print(len(list1))
    # print(len(list2))
    '''
    for i in range(len(list2)):
        set_i = set(list2[i])
        for j in list1[i]:
            if j in set_i:
                count_right += 1
    '''

    # outfile = open("dev拼接法正确匹配到的分词.txt", "a", encoding="utf-8")
    for i in range(len(list2)):
        j = 0
        k = 0

        while j < len(list1[i]) or k < len(list2[i]):
            s1 = list1[i][j]
            s2 = list2[i][k]
            while s1 == s2:
                count_right += 1
                # outfile.write(s1+"\n")
                j += 1
                k += 1
                if j >= len(list1[i]) or k >= len(list2[i]):
                    break
                s1 = list1[i][j]
                s2 = list2[i][k]
            while s1!=s2:
                if len(s2) < len(s1):
                    k = k + 1
                    s2 = s2 + list2[i][k]
                if len(s2) > len(s1):
                    j = j + 1
                    s1 = s1 + list1[i][j]
            j += 1
            k += 1
    # outfile.close()

    print("正确识别的个体总数：", count_right)
    print("识别出的个体总数：", count_split)
    print("测试集中存在的个体总数：", count_ans)

    pre = count_right / count_split
    rec = count_right / count_ans
    F = 2 * pre * rec / (pre + rec)
    print('正确率 = %d' % count_right, '/', '%d' % count_split, '=', '%0.6f' % (pre * 100), '%')
    print('召回率 = %d' % count_right, '/', '%d' % count_ans, '=', '%0.6f' % (rec * 100), '%')
    print('F值 = %.6f' % (F * 100), '%')


def main():
    creat_dict("train.ctb60.hwc.seg")
    creat_text("dev.ctb60.hwc.seg")
    SegWords("word.dict", "data.txt")  # 根据词典和语料进行分词
    eval("data.out", "dev.ctb60.hwc.seg")
main()