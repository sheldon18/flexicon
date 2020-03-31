import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

#flask app
app = Flask(__name__)

#mongo variables
app.config["MONDO_DBNAME"] = os.environ.get('MONGO_DBNAME')
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')

#PyMongo Instance
mongo = PyMongo(app)


@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template("index.html", 
    words = mongo.db.words.find())
    
@app.route('/add_word')
def add_word():
    return render_template('addword.html',
    partofspeech=mongo.db.partofspeech.find())
    
@app.route('/insert_word', methods=['POST'])
def insert_word():
    words = mongo.db.words
    words.insert_one(request.form.to_dict())
    return redirect(url_for('home_page'))
    
@app.route('/edit_word/<word_id>')
def edit_word(word_id):
    the_word = mongo.db.words.find_one({"_id": ObjectId(word_id)})
    all_partofspeech = mongo.db.partofspeech.find()
    return render_template('editword.html', word=the_word, partofspeech=all_partofspeech)
    
@app.route('/update_word/<word_id>', methods=["POST"])
def update_word(word_id):
    words = mongo.db.words
    words.update( {'_id': ObjectId(word_id)},
    {
        'word_name':request.form.get('word_name'),
        'part_of_speech':request.form.get('part_of_speech'),
        'word_definition':request.form.get('word_definition'),
        'pronunciation':request.form.get('pronunciation'),
        'sentence_use':request.form.get('sentence_use'),
        'submitter_name':request.form.get('submitter_name')
    })
    return redirect(url_for('home_page'))

@app.route('/delete_word/<word_id>')
def delete_word(word_id):
    mongo.db.words.remove({'_id': ObjectId(word_id)})
    return redirect(url_for('home_page'))

    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
        
      