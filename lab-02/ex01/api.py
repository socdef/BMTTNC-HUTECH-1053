from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)  # Sửa lỗi cú pháp ở đây

# Khởi tạo đối tượng CaesarCipher
caesar_cipher = CaesarCipher()

# API để mã hóa
@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

# API để giải mã
@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Hàm main chạy server Flask
if __name__ == "__main__":  # Sửa _name_ => __name__
    app.run(host="0.0.0.0", port=5000, debug=True)  # Sửa port-5000 => port=5000
