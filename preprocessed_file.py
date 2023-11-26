import pandas as pd

# Data class for ETL process
class Data:
    def __init__(self,path_books,path_cust):
        self.top_books = pd.read_csv(path_books)
        self.custrew = pd.read_csv(path_cust)
        
    def preprared_data(self):
        if "Rank" in self.top_books.columns and "Sno" in self.custrew.columns:
            self.top_books.set_index("Rank",inplace=True)
            self.custrew.drop("Sno",axis=1,inplace=True)
            return self.top_books,self.custrew
        else:
            return self.top_books,self.custrew

    def added_features(self):
        """
        this method adds features to top_books and custrew datas
        ı runned this codes in strdata_analysis.ipynb file then ı write codes to this method from that file
        """
        
        # object type columns content applied str.lower method
        # first loop is for top books
        for col in self.top_books.select_dtypes(include=[object]).columns:
            self.top_books[col] = self.top_books[col].str.lower()

        # second loop is for custrew
        for col in self.custrew.select_dtypes(include=[object]).columns:
            self.custrew[col] = self.custrew[col].str.lower()

        # added features to top_books
        self.top_books[['first_name', 'last_name']] = self.top_books['author'].str.split(" ", n=1, expand=True)

        arr = list()
        for i in range(1,len(self.top_books)+1):
            arr.append(len(self.top_books['genre'].str.split(" ")[i]))
        self.top_books["count genre"] = arr

        self.top_books[["link","book","dp","id","ref","slug"]] = [i for i in self.top_books.url.str.split("/")]

        # added features to custrew
        arr = list()
        for ii in range(len(self.custrew)):
            arr.append(len([i.split(" ") for i in self.custrew["review title"]][ii]))
        self.custrew["title length"] = arr
        return self.top_books,self.custrew