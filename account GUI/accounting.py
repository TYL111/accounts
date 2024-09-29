import json

#檔案位置

class file:
    def __init__(self,file_address = "./record.json"):
        self.file_address = file_address
        self.account_record = []
    #新增紀錄
    def add_record(self,date,item,cost,category):
        record = {
            "date":f"{date}",
            "item":f"{item}",
            "cost":f"{cost}",
            "category":f"{category}"
        }
        self.account_record.append(record)

    #寫入json
    def save_to_json(self,index):
        with open(self.file_address,"w") as f:
            json.dump(index,f,indent=4)

    #讀取json
    def load_record(self):
        try:
            with open(self.file_address,"r") as f:
                self.account_record = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            self.account_record = []

class fun():
    def __init__(self,file_manager):
        self.file_manager = file_manager

    #輸入新資料
    def input_new_accounting(self,date,item,cost,category):
        if not date or not item or not cost or not category:
            print("error:input error")
        else:
            self.file_manager.load_record()
            self.file_manager.add_record(date,item,cost,category)
            self.file_manager.save_to_json(self.file_manager.account_record)

      

    #搜尋功能
    def search_by_date(self,date):
        sum = 0
        result = "{:20}{:20}{:20}{:20}\n".format("DATE","ITEM","CATEGORY","COST")
        self.file_manager.load_record()
        for x in self.file_manager.account_record:
            if date in x["date"]:
                result +="{:20}{:20}{:20}{:20}\n".format(x["date"],x["item"],x["category"],"$"+x["cost"])
                sum += int(x["cost"])
        return result,sum
    
    def search_by_category(self,category):
        sum = 0
        result = "{:20}{:20}{:20}{:20}\n".format("DATE","ITEM","CATEGORY","COST")
        self.file_manager.load_record()
        for x in self.file_manager.account_record:
            if x["category"] == category:
                result +="{:20}{:20}{:20}{:20}\n".format(x["date"],x["item"],x["category"],"$"+x["cost"])
                sum += int(x["cost"])
        return result,sum
    
    def search_all(self):
        sum = 0
        result = "{:20}{:20}{:20}{:20}\n".format("DATE","ITEM","CATEGORY","COST")
        self.file_manager.load_record()
        for x in self.file_manager.account_record:
            result +="{:20}{:20}{:20}{:20}\n".format(x["date"],x["item"],x["category"],"$"+x["cost"])
            sum += int(x["cost"])
        return result,sum


    #刪除功能
    def delete_record(self,target_date,target_item):
        new_record = []
        self.file_manager.load_record()
        if not target_date or not target_item:
            print("error:missing input")
        new_record = [record for record in self.file_manager.account_record if not (record["date"] == target_date and record["item"] == target_item)]
        if len(new_record) == len(self.file_manager.account_record):
            print("error:not found")
            return
        else:
            self.file_manager.account_record = new_record
            self.file_manager.save_to_json(self.file_manager.account_record)

