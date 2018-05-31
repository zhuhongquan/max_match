# max_match
简介：用正向最大匹配算法匹配中文分词，并给出了算法的P/R/F指标<br>

"segWords_集合法"和"segWords_拼接法"只在evel函数(评价模块)中算法不同，其余函数均一样。
"dev.ctb60.hwc.seg""test.ctb60.hwc.seg"两个文件是用来测试的数据（在测试时选用任意一个），文件里的每一行都是已经分好词的句子,词与词之间用一个空格隔开。<br>
下面介绍程序里的各个函数的用法：<br>
### 1.creat_dict(infile_name)<br>
infile_name为测试文件，例如"dev.ctb60.hwc.seg"，该函数将根据测试文件生成一个包含文件里所有分词的词典，每个词一行。<br>

### 2.creat_text(infile_name)<br>
infile_name为测试文件，例如"dev.ctb60.hwc.seg"，该函数将根据测试文件生成连续的文本，一句话一行，默认输出为文件"data.txt"。

### 3.SegWords(dict_name, data_name)<br>
dict_name为函数creat_dict生成的词典文件，默认文件名为"word.dict"；data_name为函数creat_text生成的连续文本。该函数将根据这两个文件用正向最大匹配算法匹配分词，结果输出为"data.out"。

### 4.eval(resultFile, answerFile)<br>
该函数功能是评价算法的"正确率/召回率/F值(P/R/F)"<br>
正确率(Precision) = 正确识别的词数/识别出的个体总数<br>
召回率(Recall) = 正确识别的个体总数/测试集中存在的个体总数<br>
F值 = 正确率\*召回率\*2/(正确率+召回率)<br>
resultFile为算法匹配得出的分词结果，即为上面的"data.out"；answerFile即为测试文件(作为标准答案)。
<br>

下面为"dev.ctb60.hwc.seg"数据的运行结果：<br>

![](https://github.com/zhuhongquan/max_match/raw/master/images/dev_result.png)  
