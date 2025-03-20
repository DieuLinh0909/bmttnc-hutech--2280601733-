from flask import Flask, render_template, request
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.playfair import PlayFairCipher
from cipher.railfence import RailFenceCipher 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/railfence")
def railfence():
    return render_template('railfence.html')  

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, key)
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKey']
    Vigenere = VigenereCipher()
    encrypted_text = Vigenere.vigenere_encrypt(text, key)  # Đã sửa tên phương thức
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    Vigenere = VigenereCipher()
    decrypted_text = Vigenere.vigenere_encrypt(text, key)  # Đã sửa tên phương thức
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"



@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText'].strip()  # Xóa khoảng trắng ở đầu và cuối
    key = request.form['inputKey'].strip()  # Chìa khóa cho Playfair
    playfair = PlayFairCipher()  # Sử dụng lớp PlayFairCipher
    playfair_matrix = playfair.create_playfair_matrix(key)  # Tạo ma trận Playfair từ chìa khóa
    encrypted_text = playfair.playfair_encrypt(text, playfair_matrix)  # Gọi phương thức mã hóa của Playfair
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText'].strip()  # Xóa khoảng trắng ở đầu và cuối
    key = request.form['inputKey'].strip()  # Chìa khóa cho Playfair
    playfair = PlayFairCipher()  # Sử dụng lớp PlayFairCipher
    playfair_matrix = playfair.create_playfair_matrix(key)  # Tạo ma trận Playfair từ chìa khóa
    decrypted_text = playfair.playfair_decrypt(text, playfair_matrix)  # Gọi phương thức giải mã của Playfair
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText'].strip()  
    key = int(request.form['inputKey'])  
    railfence = RailFenceCipher()  
    encrypted_text = railfence.rail_fence_encrypt(text, key)  
    return f"text: {text}<br/>key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText'].strip()  
    key = int(request.form['inputKey'])  
    railfence = RailFenceCipher()  
    decrypted_text = railfence.rail_fence_decrypt(text, key)  
    return f"text: {text}<br/>key: {key}<br/>decrypted text: {decrypted_text}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)