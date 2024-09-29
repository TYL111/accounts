import tkinter as tk
import accounting as ac

root = tk.Tk() 
root.geometry('400x500+500+200') 
root.title('Account')
root.resizable(False,True)
root.minsize(width=None,height=500)

class fun_select:
    def __init__(self, master):
        self.root = master
        self.page = tk.Frame(self.root) 
        self.page.pack()
        self.btm_add = tk.Button(self.page,text = 'Add',command=self.addPage)
        self.btm_add.pack()
        self.btm_search = tk.Button(self.page,text = 'Search',command=self.searchPage)
        self.btm_search.pack()
        self.btm_delete = tk.Button(self.page,text= 'Delete',command=self.deletePage)
        self.btm_delete.pack()

    def addPage(self):
        self.page.destroy()
        add_page(self.root)
    def searchPage(self):
        self.page.destroy()
        search_page(self.root)
    def deletePage(self):
        self.page.destroy()
        delete_page(self.root)

class add_page:
    def __init__(self, master):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()

        self.dateLabel = tk.Label(self.page,text='DATE (yyyy-mm-dd)')
        self.dateLabel.pack()
        self.dateEntry = tk.Entry(self.page)
        self.dateEntry.config(fg="black",bg='white')
        self.dateEntry.pack()

        self.itemLabel = tk.Label(self.page,text='ITEM')
        self.itemLabel.pack()
        self.itemEntry = tk.Entry(self.page)
        self.itemEntry.config(fg="black",bg='white')
        self.itemEntry.pack()

        self.categoryLabel = tk.Label(self.page,text='CATEGORY')
        self.categoryLabel.pack()
        self.categoryEntry = tk.Entry(self.page)
        self.categoryEntry.config(fg="black",bg='white')
        self.categoryEntry.pack()

        self.costLabel = tk.Label(self.page,text='COST')
        self.costLabel.pack()
        self.costEntry = tk.Entry(self.page)
        self.costEntry.config(fg="black",bg='white')
        self.costEntry.pack()

        self.addConfirm = tk.Button(self.page,text='Confirm',command=self.addNewRecored)
        self.addConfirm.pack()

        self.backToHome = tk.Button(self.page,text='back',command=self.back)
        self.backToHome.pack()
    
    def addNewRecored(self):
        date = self.dateEntry.get()
        item = self.itemEntry.get()
        category = self.categoryEntry.get()
        cost = self.costEntry.get()
        ac.fun(ac.file()).input_new_accounting(date,item,cost,category)
    
    def back(self):
        self.page.destroy()
        fun_select(self.root)

class delete_page:
    def __init__(self, master):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()

        self.targetDateLabel = tk.Label(self.page,text='Date (yyyy-mm-dd)')
        self.targetDateLabel.pack()
        self.targetDateEntry = tk.Entry(self.page,bg='white',fg='black')
        self.targetDateEntry.pack()
        
        self.targetItemLabel = tk.Label(self.page,text='Item')
        self.targetItemLabel.pack()
        self.targetItemEntry = tk.Entry(self.page,bg='white',fg='black')
        self.targetItemEntry.pack()

        self.confirm = tk.Button(self.page,text='Confirm',command=self.delete)
        self.confirm.pack()

        self.backToHome = tk.Button(self.page,text='back',command=self.back)
        self.backToHome.pack()

    def delete(self):
        date = self.targetDateEntry.get()
        item = self.targetItemEntry.get()
        ac.fun(ac.file()).delete_record(date,item)
    
    def back(self):
        self.page.destroy()
        fun_select(self.root)

class search_page:
    def __init__(self, master):
        self.root = master
        self.page = tk.Frame(self.root)
        self.page.pack()
        self.type = tk.Label(self.page,text='Search Type')
        self.type.pack()
        self.byDate = tk.Button(self.page,text='Date',command=self.searchByDate_input)
        self.byDate.pack()
        self.byCategory = tk.Button(self.page,text='Category',command=self.searchByCategory_input)
        self.byCategory.pack()
        self.all = tk.Button(self.page,text='All',command=self.searchAll)
        self.all.pack()
        self.backToHome = tk.Button(self.page,text='back',command=self.back)
        self.backToHome.pack()

    def back(self):
        self.page.destroy()
        fun_select(self.root)

    def searchByDate_input(self):
        self.page.destroy()
        self.searchpage = tk.Frame(self.root)
        self.searchpage.pack()
        self.typelabel = tk.Label(self.searchpage,text='DATE (yyyy-mm-dd)')
        self.typelabel.pack()
        self.date = tk.Entry(self.searchpage,background="white",fg="black")
        self.date.pack()
        self.search = tk.Button(self.searchpage,text='Search',command=self.searchByDate)
        self.search.pack()
        self.backToHome = tk.Button(self.searchpage,text='back',command=self.input_back)
        self.backToHome.pack()
        self.result = tk.Label(self.searchpage, text="")
        self.result.pack()
        self.sum = tk.Label(self.searchpage, text='')
        self.sum.pack()

    def searchByDate(self):
        date = self.date.get()
        result, total = ac.fun(ac.file()).search_by_date(date)
        self.result.config(text=result)
        self.sum.config(text=f'Total: {total}')

    def searchByCategory_input(self):
        self.page.destroy()
        self.searchpage = tk.Frame(self.root)
        self.searchpage.pack()
        self.typelabel = tk.Label(self.searchpage,text='Category')
        self.typelabel.pack()
        self.category = tk.Entry(self.searchpage,background="white",fg="black")
        self.category.pack()
        self.search = tk.Button(self.searchpage,text='Search',command=self.searchByCategory)
        self.search.pack()
        self.backToHome = tk.Button(self.searchpage,text='back',command=self.input_back)
        self.backToHome.pack()
        self.result = tk.Label(self.searchpage, text="")
        self.result.pack()
        self.sum = tk.Label(self.searchpage, text='')
        self.sum.pack()

    def searchByCategory(self):
        category = self.category.get()
        result, total = ac.fun(ac.file()).search_by_category(category)
        self.result.config(text=result)
        self.sum.config(text=f'Total: {total}')

    def searchAll(self):
        self.page.destroy()
        self.searchpage = tk.Frame(self.root)
        self.searchpage.pack()
        result , total = ac.fun(ac.file()).search_all()
        self.result = tk.Label(self.searchpage, text=result)
        self.result.pack()
        self.sum = tk.Label(self.searchpage, text=f'Total:{total}')
        self.sum.pack()
        self.backToHome = tk.Button(self.searchpage,text='back',command=self.input_back)
        self.backToHome.pack()


    def input_back(self):
        self.searchpage.destroy()
        fun_select(self.root)

fun_select(root)
root.mainloop()
