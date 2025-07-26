import socketio
from encryption_utils import encrypt_message, decrypt_message

sio = socketio.Client()

# Prompt user for name
name = input("Enter your name: ")

@sio.on('connect')
def on_connect():
    print("Connected to server!\n")

@sio.on('receive_message')
def on_message(data):
    sender = data['sender']
    encrypted_msg = data['message']
    decrypted_msg = decrypt_message(encrypted_msg)

    if sender != name:
        print(f"\n{sender}: {decrypted_msg}")

def send_messages():
    while True:
        msg = input()
        encrypted = encrypt_message(msg)
        sio.emit('send_message', {'sender': name, 'message': encrypted})

if __name__ == '__main__':
    try:
        sio.connect('http://localhost:5000')
        send_messages()
    except KeyboardInterrupt:
        print("\nDisconnected from chat.")
        sio.disconnect()
