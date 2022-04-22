from flask import Flask,render_template,request,redirect
import os


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/run", methods =['post','get'])
def run():
    if request.method == 'GET':
        return redirect("/")
    else:
        language = request.form.get("language")
        code = request.form.get("code")
        parament = request.form.get("parament")

        if language == 'py':
            f = open('/app/python/index.py', 'w+')
            f.write(code)
            f.close()
            f = open('/app/python/parament.txt', 'w+')
            f.write(parament)
            f.close()
            os.system("> /app/python/result.txt && python /app/python/index.py < /app/python/parament.txt > /app/python/result.txt 2>&1")
            f = open('/app/python/result.txt', 'r')
            result = f.read()
            f.close()
            return render_template("index.html",code=code,result=result,language=language,parament=parament)
        elif language == 'java':
            f = open('/app/java/index.java', 'w+')
            f.write(code)
            f.close()
            f = open('/app/java/parament.txt', 'w+')
            f.write(parament)
            f.close()
            os.system("> /app/java/result.txt && cd /app/java && javac index.java > result.txt 2>&1 && java Main < parament.txt > result.txt 2>&1 && cd /app/")
            f = open('/app/java/result.txt', 'r')
            result = f.read()
            f.close()
            return render_template("index.html",code=code,result=result,language=language,parament=parament)
        elif language == 'gcc':
            f = open('/app/gcc/index.cpp', 'w+')
            f.write(code)
            f.close()
            f = open('/app/gcc/parament.txt', 'w+')
            f.write(parament)
            f.close()
            os.system("> /app/gcc/result.txt && g++ /app/gcc/index.cpp -o /app/gcc/index > /app/gcc/result.txt 2>&1 && /app/gcc/index < /app/gcc/parament.txt > /app/gcc/result.txt 2>&1")
            f = open('/app/gcc/result.txt', 'r')
            result = f.read()
            f.close()
            return render_template("index.html",code=code,result=result,language=language,parament=parament)
        elif language == 'cs':
            f = open('/app/csc/index.cs', 'w+')
            f.write(code)
            f.close()
            f = open('/app/csc/parament.txt', 'w+')
            f.write(parament)
            f.close()
            os.system("> /app/csc/result.txt && mcs -out:/app/csc/index.exe /app/csc/index.cs > /app/csc/result.txt 2>&1 && mono /app/csc/index.exe > /app/csc/result.txt 2>&1")
            f = open('/app/csc/result.txt', 'r')
            result = f.read()
            f.close()
            return render_template("index.html",code=code,result=result,language=language,parament=parament)
        else:
            return redirect("/")


@app.route("/exercise")
def exercise():
    f = open('baitap.txt', 'r', encoding="utf-8")
    result = f.read()
    f.close()
    return render_template("exercise.html", result=result)
    
if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host="54.205.122.32", debug=True, port=80)
