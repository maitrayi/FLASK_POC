from flask import Flask,redirect,url_for

app=Flask(__name__)

@app.route('/')

def welcome():
    return 'Welcome to channel'

@app.route('/success/<int:score>')
def success(score):
    return 'the person has passed and score is  ' + str(score)
    ## return a html file 


@app.route('/fail/<int:score>')
def fail(score):
    return 'the person has Failed and score is  ' + str(score)

@app.route('/result/<int:marks>')
def result(marks):
    result=''
    if marks <50:
        result='fail'
    else :
        result='success'
    #return result 
    return redirect(url_for(result,score=marks))


if __name__ == '__main__':
    app.run(debug=True)
