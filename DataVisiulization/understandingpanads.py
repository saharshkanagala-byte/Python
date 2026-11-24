import pandas as pd
data = {"apples": [3,2,0,1], "oranges": [0,3,7,2]}
purchases = pd.DataFrame(data)
print(purchases)
purchases = pd.DataFrame(data, index = ['Saharsh', "Sara", "Arthur", "Jay"])
print(purchases)
print(purchases.loc["Saharsh"])
print(purchases.iloc[3])  
url = 'https://drive.google.com/file/d/1wpj5hPJdolr2hccnjdYo4XHX1j1c_AN5/view?usp=sharing'
fileid = url.split('/')[-2]
downloadurl = f'https://drive.google.com/uc?id={fileid}'
moviedf = pd.read_csv(downloadurl)
print(moviedf.head())
print(moviedf.tail())
print(moviedf.info())