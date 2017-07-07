from flask import Flask,request,jsonify
import time
app=Flask(__name__)
tasks ={
    "1":{
        
        'title': u'Request ',
        'description': '', 
        'status': '',
        'time_remain' :0
    },
    "2":{
        'title': u'Server',
        'description': '', 
        'status': '',
        'time_remain':0
    }
}
@app.route('/')

def index():
    return "Hello world"
    
@app.route('/api/request', methods=['GET'])
def request_conn():
    """
    Get api for running the server for requested time.
    :return: {"status":"ok"} on successful completion of time
    
    """
    time_out = int(request.args.get('timeout'))
    connid=(request.args.get('connid'))
    try :
        tasks[connid]['status']="running"
        for i in range(time_out,0,-1):
            time.sleep(1)
            tasks[connid]['time_remain']=i
            if(tasks[connid]['status']=="killed"):
                return jsonify({'status':tasks[connid]['status']})
        tasks[connid]['status']="ok"        
        return jsonify({'status':tasks[connid]['status']})
            
    except :
        return jsonify({'status':'connid not found'})
        
@app.route('/api/serverstatus')
def server_stats():
    """
    Get api for server status
    :return : running request with their time left for completion 
    """
    stat={}
    for k, v in tasks.items():
        if v['status']=="running":
            stat[k]=v['time_remain']
    return jsonify(stat)
    
@app.route('/api/kill',methods=['PUT'])
def kill():
    """
    PUT api for ending a request with the provided connid
    :return : {"status":"ok"} if the request was running else invalid connid
    """
    conn=str(request.json.get('connid'))
    status_kill=""
    try:
        if(tasks[conn]['status']=="running"):
            tasks[conn]['status']="killed"
            status_kill="ok"
        else:
            status_kill="Invalid connection id :"+conn      
    except:
        status_kill="Invalid connection id :"+conn
        
    return jsonify({"status":status_kill})
        

if __name__=="__main__":
    app.run(debug=True,threaded=True)
    
