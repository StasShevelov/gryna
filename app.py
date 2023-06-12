import parser1
from flask import Flask, render_template, request
import you


from rembg import remove as rm
from PIL import Image
from gpytranslate import SyncTranslator


#...
t = SyncTranslator()
app = Flask(__name__)

ch = []
def think(m):


    response = you.Completion.create(
        prompt=t.translate(m, targetlang="en").text,
        chat=ch)

    

    ch.append({"question": t.translate(m, targetlang="en").text, "answer": response["response"]})
    res = t.translate(response["response"], targetlang="ru").text.replace("YouBot", "Гриня")
    res = res.replace("You.com", "СенсонЭйАй")
  
    return res




@app.route('/')
def index():
    
    
    
    return render_template('index.html')

@app.route('/google', methods=['GET'])
def google():
    
        
    search = request.args.get('search')  # запрос к данным формы
    res = parser1.search(search)
    
    if res == "":
        return render_template('index.html')
    else:

        return render_template('index.html', answer= think(search), results = res)
    


@app.route('/chat')
def chat():
      
    return render_template("chat.html")



ans = []
@app.route('/answer', methods=['POST'])
def answer():
    
    m = request.form['message']
    ans.append(f"""<div class="message user-message">
      <div class="avatar"></div>
      <div class="content">
        {m}
        <div class="timestamp">12:05 PM</div>
      </div>
    </div>
    <div class="message bot-message">
      <div class="content">
        {think(m)}
        <div class="timestamp">12:10 PM</div>
      </div>
    </div>""")
    print(ans)
    return render_template('chat.html', otvet = "".join(ans) )




def remove_str(v1):
    v1= v1.replace(" ", "SPACE")
    v2 = ''.join(filter(str.isalnum, v1))
    return v2.replace("SPACE", " ")
    




@app.route('/removebg')
def removebg():
    return render_template("removeBg.html")

@app.route('/removebgres', methods=['POST'])
def removebgres():
    f = request.files['file']
    output_path = 'static\img\output.png'
    inp = Image.open(f)
    output = rm(inp)
    output.save(output_path)
    return  render_template("removeBg.html")

if __name__ == '__main__':
    app.run()
