from flask import Flask, render_template
app = Flask(__name__)

## Setiap URL memiliki nama fungsi yang sama,
## Alama-alamat pada route('/'), dll. harus tidak boleh sama.

@app.route('/')
def home():
   return render_template('index.html')

    
if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)