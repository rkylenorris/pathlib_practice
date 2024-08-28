import pathlib as pl
import sqlite3
import pandas as pd

# get current work directory path/name, check if eq what expected
cwd = pl.Path.cwd()
expectedDir = 'pathlib_practice'
if cwd.name == expectedDir:
    print('correct directory')
else:
    print(f'incorrect directory, is "{cwd.name}", should be "{expectedDir}"')


# iterate over directory contents
for file in cwd.iterdir():
    print(file.name)


data_path = pl.Path(cwd / "data")
data_files = data_path.glob("*.csv")

permits_path = pl.Path(data_path / "Building_Permits.csv")
permits_df = pd.read_csv(permits_path)
permits_columns = permits_df.columns
print(permits_columns[22], permits_columns[32])

# for f in data_files:
#     print(f)

db_path = data_path / 'database.sqlite'
# print(db_path)
# conn = sqlite3.connect(db_path)
#
# csv_dfs = []
#
# for f in data_files:
#     print(f)
#     csv_dfs.append(pd.read_csv(f))
#
# print(len(csv_dfs))
#
# for table in csv_dfs:
#     print(table.head())
#     table.to_sql(f.stem, conn, if_exists='replace', index=False)

# conn.commit()
#
# permits_df = pd.read_sql("SELECT * FROM Building_Permits LIMIT 100", conn)
# col_24_df = pd.read_sql("SELECT * FROM Cost_of_Living_Index_by_Country_2024 LIMIT 100", conn)
# print(permits_df.head(), col_24_df.head())
# conn.close()
