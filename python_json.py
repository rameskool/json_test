import json
import csv


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
        self.children = "default"

    def assign(self, res):
        self.result=[]
        self.result.append(res)



class makeJson():
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
        #s1.assign(r4.__dict__)
        with open('test.json', 'w') as f:
            json.dump(s1.__dict__, f)


jsonmake = makeJson()
jsonmake.collect()
