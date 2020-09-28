from flask import Flask, request, render_template
app=Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
@app.route('/',methods=["POST","GET"])
def home():
    if request.method =="POST":
        import path
        x1 =float(request.form["x1"])
        x2 =float(request.form["x2"])
        x3 =float(request.form["x3"])
        x4 =float(request.form["x4"])
        x5 =float(request.form["x5"])
        x6 =float(request.form["x6"])
        data=[x1,x2,x3,x4,x5,x6]
        result = path.pathes(data)
        return result
    else:
        return render_template('index.html')
if __name__ == '__main__':
    app.run(port=app.config["PORT"],debug=app.config["DEBUG"])
