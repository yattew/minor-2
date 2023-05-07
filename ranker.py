import glob
import math
from rank_bm25 import BM25Okapi



def create_corpus(file_names):
    corpus = []
    #punctuations = '''!()-[]{};:'"\,\n<>./?@#$%^&*_~'''
    for file_name in file_names:
        try:
            with open(file_name, 'r') as f_obj:
                text = f_obj.read()
            text = text.replace('\n', ' ')
            final_text = text
            #for char in text:
                #if char not in punctuations:
                    #final_text = final_text + char
            list_text = final_text.split(" ")
            corpus.append(list_text)
        except:
            pass
    return corpus


# globals
PATH = './docs/*.txt'
FILE_NAMES=glob.glob(PATH)
CORPUS = create_corpus(FILE_NAMES)
BM25 = BM25Okapi(CORPUS)

def setup_path(path):
    PATH = path

def retrieve_doc(query):
    tokenized_query = query.split(' ')
    doc_scores = BM25.get_scores(tokenized_query)
    return CORPUS[list(doc_scores).index(max(doc_scores))]

# print(retrieve_doc("potential market manipulation"))
