import csv
import json
import math
#from framework.tasks.standard.ScrapperTask import ScrapperTask

class Result:
    def __init__(self,alis,value="NA"):
        self.alis=alis
        self.value=value
        self.id=0
        self.pid=0
        self.children="NA"

    def assign(self, child):
        self.children = child

class Seed():
    def __init__(self,url,id):
        self.url=url
        self.result=[]
        self.id=id

class Output():
    def __init__(self):
        self.test="Output"
        self.seeds=[]


    def seedVal(self,seeds):
        self.seeds=seeds

class ScrapperTask():
    def getURLs(self):

        URLs=["a.com","b.com","c.com"]
        return URLs

    def getParentInfo(self):
        Info=[0,112,"Collector",0,113,"Title",113,114,"SubTitle",112,115,"Sub-Collector",114,116,"Sub-subTitle",0,117,"Free",116,118,"Sub-sub-subtile",0,119,"Collector1",0,120,"Collector2",0,121,"Collector3",0,122,"Collector4",122,123,"Collector4ko"]
        return Info

class makelistoflist():
    def makelist(self):
        scrapperObj=ScrapperTask()
        list_list=[]
        listit=[]
        children="NA"
        pre_list=scrapperObj.getParentInfo()
        len_pre_list=len(pre_list)
        for i in range(0,len_pre_list):
            if(i%3==0):
                if(pre_list[i]==0):
                    listit.append(pre_list[i])
                    listit.append(pre_list[i+1])
                    listit.append(pre_list[i+2])
                    a=self.check(pre_list,pre_list[i+1])
                    if(a):

        for j in range(0,len_pre_list):
            if(j%3==0):
                if(pre_list[j]!=0):


class makeJson():
    def collect(self):

        scrapperObj=ScrapperTask()
        seeds=[]
        resultsarray=[]
        parentInfo=scrapperObj.getParentInfo()
        Urlinfo=scrapperObj.getURLs()
        urlcount=len(Urlinfo)

        for i in range(0,urlcount):
            seedobj=Seed(Urlinfo[i],i)
            seeds.append(seedobj)

        for j in range(0, len(parentInfo)):
            if (j % 3 is 0):
                if (parentInfo[j] ==0):
                    print("A")
                    id = parentInfo[j + 1]
                    alias = parentInfo[j + 2]
                    print("..........")
                    print(alias)
                    print("..........")
                    result = Result(alias)
                    result.id = id
                    result.pid = 0
                    resultsarray.append(result.__dict__)
                else:


        # for k in range(0, len(parentInfo)):
        #     if (k % 3 == 0):
        #         if (parentInfo[k] == 0 ):
        #             pass
        #         else:
        #             id = parentInfo[k + 1]
        #             alias = parentInfo[k + 2]
        #             parentId = parentInfo[k]
        #             result = Result(alias)
        #             print("******************")
        #             print(parentId)
        #             print("******************")
        #             result.id = id
        #             result.pid = parentId
        #             for r in resultsarray:
        #                 # if (r.id == parentId):
        #                 #     r.assign(result)
        #                 print(r)

        for seedresult in seeds:
            seedresult.result=resultsarray
            print(seedresult.result)


        #seeds.append(seedobj.__dict__)
        # out=Output()
        # out.seedVal(seeds)
        # with open('test.json', 'w') as f:
        #     json.dump(out.__dict__, f)

mk=makeJson()
mk.collect()

# class csv_reader():
#     def csv_dict_URL_reader(self):
#         """
#         Read a CSV file using csv.DictReader
#         """
#
#         with open("test.csv") as f_obj:
#             print(".......................................")
#             reader = csv.DictReader(f_obj, delimiter='\t')
#             a=0
#             b1=0
#             for op in reader:
#                 a1=op["URL"]
#                 if(b1==a1):
#                     pass
#                 else:
#                     yield (a1)
#                 b1=a1
#
#                 a=a+1
#             print(a)
# #----------------------------------------------------------------------
#     def csv_dict_Field_reader(self):
#         """
#         Read a CSV file using csv.DictReader
#         """
#
#         with open("test.csv") as f_obj:
#             print(".......................................")
#             reader = csv.DictReader(f_obj, delimiter='\t')
#             a=0
#             b1=0
#             COUNT=0
#             for op in reader:
#                 a1=op["FIELD"]
#                 if(b1==a1):
#                     COUNT=COUNT+1
#                 else:
#                     yield (a1)
#                 b1=a1
#
#                 a=a+1
#             print(a,COUNT)
#
# csvreader=csv_reader()
# for i in csvreader.csv_dict_URL_reader():
#     print(i)
# for i in csvreader.csv_dict_Field_reader():
#     print(i)

