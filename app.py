from flask import Flask 
app = Flask(__name__) 

@app.route('/')
def hello(): 
   return "Hello from Docker! (EL BOUHAMDI AMINE) Updated 18-05-2025" 

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=5000) 