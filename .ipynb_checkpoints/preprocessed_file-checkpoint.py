import pandas as pd

# Data class for ETL process
class Data:
    def __init__(self, path_books, path_cust):
        self.path_books = path_books
        self.path_cust = path_cust
        self._prepared = False  # Flag to indicate if data is prepared
        self._top_books = None
        self._custrew = None

    @property
    def prepared(self):
        return self._prepared

    def prepare_data(self):
        self._top_books = pd.read_csv(self.path_books)
        self._custrew = pd.read_csv(self.path_cust)
        
        if "Rank" in self._top_books.columns and "Sno" in self._custrew.columns:
            self._top_books.set_index("Rank", inplace=True)
            self._custrew.drop("Sno", axis=1, inplace=True)
            self._prepared = True

    @property
    def top_books(self):
        if not self.prepared:
            self.prepare_data()
        return self._top_books

    @property
    def custrew(self):
        if not self.prepared:
            self.prepare_data()
        return self._custrew
    
    def added_features(self):
        """
        this method adds features to top_books and custrew datas
        ı runned this codes in strdata_analysis.ipynb file then ı write codes to this method from that file
        """
        
        # object type columns content applied str.lower method
        # first loop is for top books
        if not self.prepared:
            self.prepare_data()
                    
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