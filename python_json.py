import json
import csv
from read_csv import read_csv

class result:
    def __init__(self, alias="", value=""):
        self.alias = alias
        self.value = value
        self.children = "default"

    def assign(self, child):
        self.children = child

class seed:
    def __init__(self, URL):
        self.URL = URL
        self.result = []

    def assign(self, res):
        self.result.append(res)



class makeJson():

    def handle_foreign(self):
        seeds=[]
        pp = read_csv()
        pp.read()
        field=pp.getField()
        url=pp.getUrl()
        rows=pp.getrows()

        for i in url:
            seed_obj=seed(i)
            seeds.append(seed_obj)

        for i in seeds:
            print(i)
            print(i.URL)

        # for i in rows:
        #     print(rows)

    def collect(self):
        s1=seed("www.a.com")

        r1 = result("r1.alias", "r1.value")
        # print(r1.alias)

        r2 = result("r2.alias", "r2.value")
        r3 = result("r3.alias", "r3.value")
        r4=result("r4.alias","r4.value")
        r2.assign(r1.__dict__)
        # print(r2.alias)
        r3.assign(r2.__dict__)
        s1.assign(r3.__dict__)
        s1.assign(r4.__dict__)
        with open('test.json', 'w') as f:
            json.dump(s1.__dict__, f)


jsonmake = makeJson()
jsonmake.collect()
jsonmake.handle_foreign()
