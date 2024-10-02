from flask import Flask
import socket
import os
import platform

app = Flask(__name__)

@app.route('/')
def index():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    os_info = os.uname()
    platform_info = platform.platform()
    return f'''
    <h1>System Information</h1>
    <p><strong>Hostname:</strong> {hostname}</p>
    <p><strong>IP Address:</strong> {ip_address}</p>
    <p><strong>OS Info:</strong> {os_info}</p>
    <p><strong>Platform Info:</strong> {platform_info}</p>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)