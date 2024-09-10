from flask import Flask,redirect,url_for, render_template,request
app=Flask(__name__)

@app.route('/')
def welcom():
    return render_template('index.html')
    #return "Welcome to my Page"

@app.route('/Success/<int>:marks')
def Success(marks):
    return "Congratulations you have passed with score " + str(marks )

@app.route('/fail/<int>:marks')
def fail(marks):
    return "You have Failed with score " + str(marks )

@app.route('/result/<int>:marks')
def result(marks):

    result=''
    if marks>=40:
        result='Success'
    else : 
        result='fail'
    return redirect(url_for(result,marks))
    
@app.route('/Submit', methods=['POST','GET'])
def Submit():
    total_score = 0
    if request.method=='POST':
        science=float(request.form['Science'])
        math=float(request.form['Maths'])
        dat_science=float(request.form['DataScience'])
        total_score = int((science+math+dat_science)/3)
    resu=""
    if int(total_score)>=50:
        resu="Success"
    else:
        resu="fail"
   
    return redirect(url_for(resu, marks = total_score))

if __name__=='__main__':
    app.run(debug=True)