import pandas as pd
import tabula

pdf_path = "https://github.com/chezou/tabula-py/raw/master/tests/resources/data.pdf"

df = tabula.read_pdf("files/datasheet-cc-8800-1_removed.pdf", stream=True, pages="all")[
    0
]
df.rename(columns={"(m)": "boom_length", "(m).1": "super_lift_ballast"}, inplace=True)
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

df = df.loc[df["super_lift_ballast"] == 0]
print(df)

results = df.loc[df["boom_length"] == 108.0, ["16"]]
print(results)
