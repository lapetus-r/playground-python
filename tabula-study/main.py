import tabula

pdf_path = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"

dfs = tabula.read_pdf("files/datasheet-cc-8800-1_removed.pdf", stream=True, pages="all")
# read_pdf returns list of DataFrames
print(len(dfs))
print(len(dfs[0]))

for index, table in enumerate(dfs):
    print(f"\nData Index: {index}")
    print(type(table))
    print(table)
