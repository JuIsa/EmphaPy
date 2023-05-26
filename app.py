from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key= 'asd'
@app.route('/')
def index():
    return render_template('index.html',message = 'Enter Text')

@app.route('/emp',methods=['POST','GET'])
def greet():
    words = str(request.form['text_input'])
    words = words.split()
    result = ''
    for word in words:
        result+=emphasize(word)+' '
    return render_template('index.html',message = result)

def emphasize(word):
    lens = [10,6,4,2]
    places = [4,2,1,0]
    for l in range(len(lens)):
        if len(word)>=lens[l]:
            return '<b class="light">'+word.replace(word[places[l]],word[places[l]]+'</b>')
    return '<b class="light">'+word+'</b>'
    # if len(word)>=10:
    #     return '<b class="light">'+word.replace(word[4],word[4]+'</b>')
    # elif len(word)>=6:
    #     return '<b class="light">'+word.replace(word[3],word[3]+'</b>')
    # elif len(word)>=4:
    #     return '<b class="light">'+word.replace(word[2],word[2]+'</b>')
    # elif len(word)>2:
    #     return '<b class="light">'+word.replace(word[1],word[1]+'</b>')
    # else:
    #     return '<b class="light">'+word+'</b>'
