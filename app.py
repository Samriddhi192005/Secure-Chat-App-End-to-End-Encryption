from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
from encryption_utils import decrypt_message, encrypt_message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")

# Chat history for reference (not encrypted)
chat_history = []

@socketio.on('send_message')
def handle_send_message(data):
    encrypted_msg = data['message']
    sender = data['sender']

    # Decrypt the incoming message
    decrypted_msg = decrypt_message(encrypted_msg)

    print(f"{sender}: {decrypted_msg}")
    chat_history.append(f"{sender}: {decrypted_msg}")

    # Send encrypted message back to clients
    re_encrypted = encrypt_message(decrypted_msg)
    emit('receive_message', {'sender': sender, 'message': re_encrypted}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000)
