from flask import Flask, request, jsonify
from flask_cors import CORS
from db import create_table
import models
from datetime import datetime, date


app = Flask(__name__)
CORS(app)



@app.route('/api/v1/news', methods=['GET'])
def get_news():
    result = models.get_news()
    
    data = {
            
            'status': 200,
            'data': result
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp


@app.route('/api/v1/news/<news_id>', methods=['GET'])
def get_news_by_id(news_id):
    try:
        result = models.get_news_by_id(news_id)
        data = {
                
                'status': 200,
                'data': result
            
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
                
                'status': 404,
                'message': "Data Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp
        
    
@app.route('/api/v1/news', methods=['POST'])
def insert_news():
    
    title = request.form['title']
    content = request.form['content']
    datetime = request.form['datetime']
    flag = request.form['flag']
    result = models.insert_news(title, content, datetime, flag)
    
    data = {
        
            'status': 201,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 201
    
    return resp


@app.route('/api/v1/news/<news_id>', methods=['PUT'])
def update_news(news_id):
    
    news_id = request.form['news_id']
    title = request.form['title']
    content = request.form['content']
    datetime = request.form['datetime']
    flag = request.form['flag']
    result = models.update_news( news_id, title, content, datetime, flag)
  
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp

@app.route('/api/v1/news/<news_id>', methods=['PATCH'])
def flag_news(news_id):
    
    news_id = request.form['news_id']
    flag = request.form['flag']
    result = models.flag_news(news_id, flag)
  
    data = {
        
            'status': 200,
            'message': 'Success!'
        
        }
    
    resp = jsonify(data)
    resp.status_code = 200
    
    return resp


@app.route('/api/v1/news/<news_id>', methods=['DELETE'])
def delete_news(news_id):
    try :
        result = models.delete_news(news_id)
        
        data = {
                
                'status': 200,
                'message': "Success!"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        
        return resp
    
    except:
        data = {
                
                'status': 404,
                'message': "Data Not Found"
            
            }
        
        resp = jsonify(data)
        resp.status_code = 404
        
        return resp

if __name__ == "__main__":
    #create_table_users()
    #print(get_data())
    app.run(port=5000)