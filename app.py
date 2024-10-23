from flask import Flask, render_template, request

app = Flask(__name__)

def binary_conversion(text):
    binary_result = ''
    for huruf in text:
        if huruf.isdigit():
            biner = bin(int(huruf))[2:]
            biner = biner.zfill(8)
        else:
            integer = ord(huruf)
            biner = bin(integer)[2:]
            biner = biner.zfill(8)
        binary_result += biner + ' '
    return binary_result.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_text = request.form['input_text']
        binary_output = binary_conversion(input_text)
        return render_template('index.html', binary_output=binary_output)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
