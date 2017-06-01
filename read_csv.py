import csv



class read_csv:

    def __init__(self):
        self.arr_url=[]
        self.arr_field=[]
        self.url_result={}
        self.rows=[]

    def read(self):
        a=[]
        row=[]
        rows=[]
        with open("output_scrapper_task_.tsv") as f:
            reader = csv.reader(f)
            for row in reader:
                a.append(row)
        total=(len(a))
        for i in range(1,total):
            b=str(a[i])
            b2=b.split(r"\t")[0]
            field=b.split(r"\t")[1]
            index=b.split(r"\t")[2]
            level=b.split(r"\t")[3]
            b6=b.split(r"\t")[4]
            value=b6.replace("']","")
            url=b2.replace("['" or '["',"")
            url = url.replace('["', "")

            if url in self.arr_url:
                pass
            else:
                self.arr_url.append(url)
            if field in self.arr_field:
                pass
            else:
                self.arr_field.append(field)






    def getUrl(self):
        return self.arr_url

    def getField(self):
        return self.arr_field

    def getrows(self):
        return  None

