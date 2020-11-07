from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


client = MongoClient('mongodb://jungle:jungle@13.125.47.82', 27017)
db = client.dbjungle

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/loading', methods=['GET'])
def loading_memo():
    memo_list = list(db.memoVer2.find({},{'_id': 0}))
    return jsonify({'result': 'success', 'memo_list': memo_list})

@app.route('/posting', methods=['POST'])
def posting_memo():
    id_receive = request.form['id_give']
    title_receive = request.form['title_give']
    content_receive = request.form['content_give']
    db.memoVer2.insert_one({'id':id_receive, 'title':title_receive, 'content':content_receive})

    return jsonify({'result': 'success', 'msg':'저장완료'})

@app.route('/delete', methods=['POST'])
def delete_memo():
    id_receive = request.form['id_give']
    db.memoVer2.delete_one({'id':id_receive})

    return jsonify({'result': 'success', 'msg':'삭제완료'})

@app.route('/rewriting', methods=['POST'])
def rewriting_memo():
    id_receive = request.form['id_give']
    re_title_receive = request.form['re_title_give']
    re_content_receive = request.form['re_content_give']
    db.memoVer2.update_one({'id':id_receive},{'$set':{'title':re_title_receive, 'content':re_content_receive}})

    return jsonify({'result': 'success', 'msg':'수정완료'})

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)