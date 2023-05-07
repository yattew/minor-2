from flask import Flask
import pickle
import ranker

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))
# PATH = './docs/*.txt'
# ranker.setup_path(PATH)


@app.route("/query/<query>")
def query(query:str):
    context = " ".join(ranker.retrieve_doc(query))
    return model(question=query, context=context)


app.run(debug=True)