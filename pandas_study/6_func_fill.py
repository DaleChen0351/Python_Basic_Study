import pandas as pd

def add_2(x):
    return x+2

def each_item_loop(books):
    for i in books.index:
        books["Price"].at[i] = books["ListPrice"].at[i] * books["Discount"].at[i]

def serials_mul_serials(books):
    books["Price"] = books["ListPrice"] * books["Discount"] + 2


if __name__ == "__main__":
    # read xlsx with index_col = ID
    books = pd.read_excel("6.xlsx", index_col='ID')
    print(books.head())
    # each_item_loop(books)
    # serials_mul_serials(books)

        #apply_func
    books["ListPrice"] = books["ListPrice"].apply(add_2)

        # lambda_func 等效于add_2
    books["Discount"] = books["Discount"].apply(lambda x:x+0.2)

    print("==============")
    print(books)
