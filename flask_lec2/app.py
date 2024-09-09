from flask import Flask 


## Flask object 

## WSGI APPLICATION 
app= Flask(__name__)


# Decorator to define URLs 
@app.route('/')
# Binding function - function that will be called by default whenver the above URL is called 
def welcome():
    return 'Welcome to the flask API page'

@app.route('/members')
def members():
    return 'Members Welcome to the flask API page'

if __name__=='__main__':
    app.run(debug=True)