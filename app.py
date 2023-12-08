from flask import Flask, render_template, request, send_from_directory
import os
import qrcode

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    url = request.form.get('url')

    features = qrcode.QRCode(version=1, box_size=15, border=2)
    features.add_data(url)
    features.make(fit=True)

    if not os.path.exists('static'):
        os.makedirs('static')

    generate_image = features.make_image(fill_color="black", back_color="white")
    image_path = 'static/image.png'
    generate_image.save(image_path)

    return render_template('result.html', image_path=image_path)

@app.route('/static/<filename>')
def static_file(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    app.run(debug=True)
