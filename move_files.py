import os
from tqdm import tqdm
article_path = "./archive/Article/"
dest_path = "./docs/"
if not os.path.exists(dest_path):
    os.mkdir(dest_path)
articles = os.listdir(article_path)
count = 0
for i in tqdm(range(len(articles))):
    article = articles[i]
    for file in os.listdir(article_path+article):
        if file.split(".")[0].endswith("Text"):
            os.rename(article_path + article + "/" + file, dest_path + "doc"+f"{count}"+".txt")
            count+=1