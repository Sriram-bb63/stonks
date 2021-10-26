from flask import Flask, url_for, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            bp = float(request.form["bp"])
            bq = float(request.form["bq"])
            sp = float(request.form["sp"])
            sq = float(request.form["sq"])
        except:
            return render_template('error.html')
        if bp == sp and bq == sq:
            results = ["BREAK EVEN", "Break even", 0, 0 , "-", "-", "-", "-"]
            return render_template('result.html', results=results)
        elif bp <= 0 or bq <= 0 or sp <= 0 or sq <= 0:
            return render_template("error.html")
        else:
            tot_bp = bp * bq
            tot_sp = sp * sq
            total_result = tot_sp - tot_bp
            result = "Profit" if total_result > 0 else "Loss"
            result_title = result.upper()
            result_per_share = sp - bp
            result_percentage = (abs(total_result) / tot_bp) * 100
            result_percentage = float(f'{result_percentage:.2f}')
            rs1_val = sp / bp
            results = [result_title, result, float(f"{tot_bp:.2f}"), float(f"{tot_sp:.2f}"), float(f"{total_result:.2f}"), float(f"{result_per_share:.2f}"), float(f"{result_percentage:.2f}"), float(f"{rs1_val:.2f}")]
            return render_template('result.html', results=results)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)