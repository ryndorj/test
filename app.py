from flask import Flask, send_from_directory
import os
from datetime import datetime

app = Flask(__name__, static_folder='/storage/emulated/0')

visitor_count = 0  # Зочлогчдын тоо хадгалах хувьсагч

@app.route('/')
def index():
    global visitor_count
    visitor_count += 1  # Шинэ зочин орж ирэхэд тоо нэмэгдэнэ

    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Серверийн цаг авах

    return f"""<!DOCTYPE html>
    <html>
    <head>
        <title>Chad Lou Web Site</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                transition: background 0.3s, color 0.3s;
                text-align: center;
                padding: 50px;
            }}
            .light {{
                background: #ffffff;
                color: #000000;
            }}
            .dark {{
                background: #121212;
                color: #ffffff;
            }}
            button {{
                margin: 10px;
                padding: 10px 20px;
                cursor: pointer;
            }}
            .info {{
                color: gray;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body class="light">
        <h1>Welcome to Chad Lou web site</h1>

        <!-- Дуу тоглуулагч -->
        <audio id="myAudio" controls>
            <source src="/B.mp3" type="audio/mpeg">
            Таны төхөөрөмж дуу тоглуулж чадсангүй.
        </audio>

        <!-- Dark/Light Mode товч -->
        <button onclick="toggleMode()">Гэрэл / Хар горим</button>

        <!-- Зочлогчдын тоо болон серверийн цаг -->
        <div class="info">
            <p>Visitors: {visitor_count}</p>
            <p>Server Time: {server_time}</p>
        </div>

        <script>
            function toggleMode() {{
                const body = document.body;
                if (body.classList.contains('light')) {{
                    body.classList.remove('light');
                    body.classList.add('dark');
                }} else {{
                    body.classList.remove('dark');
                    body.classList.add('light');
                }}
            }}
        </script>
    </body>
    </html>"""

@app.route('/B.mp3')
def serve_audio():
    return send_from_directory('/storage/emulated/0', 'B.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)from flask import Flask, send_from_directory
import os
from datetime import datetime

app = Flask(__name__, static_folder='/storage/emulated/0')

visitor_count = 0  # Зочлогчдын тоо хадгалах хувьсагч

@app.route('/')
def index():
    global visitor_count
    visitor_count += 1  # Шинэ зочин орж ирэхэд тоо нэмэгдэнэ

    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Серверийн цаг авах

    return f"""<!DOCTYPE html>
    <html>
    <head>
        <title>Chad Lou Web Site</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                transition: background 0.3s, color 0.3s;
                text-align: center;
                padding: 50px;
            }}
            .light {{
                background: #ffffff;
                color: #000000;
            }}
            .dark {{
                background: #121212;
                color: #ffffff;
            }}
            button {{
                margin: 10px;
                padding: 10px 20px;
                cursor: pointer;
            }}
            .info {{
                color: gray;
                margin-top: 20px;
            }}
        </style>
    </head>
    <body class="light">
        <h1>Welcome to Chad Lou web site</h1>

        <!-- Дуу тоглуулагч -->
        <audio id="myAudio" controls>
            <source src="/B.mp3" type="audio/mpeg">
            Таны төхөөрөмж дуу тоглуулж чадсангүй.
        </audio>

        <!-- Dark/Light Mode товч -->
        <button onclick="toggleMode()">Гэрэл / Хар горим</button>

        <!-- Зочлогчдын тоо болон серверийн цаг -->
        <div class="info">
            <p>Visitors: {visitor_count}</p>
            <p>Server Time: {server_time}</p>
        </div>

        <script>
            function toggleMode() {{
                const body = document.body;
                if (body.classList.contains('light')) {{
                    body.classList.remove('light');
                    body.classList.add('dark');
                }} else {{
                    body.classList.remove('dark');
                    body.classList.add('light');
                }}
            }}
        </script>
    </body>
    </html>"""

@app.route('/B.mp3')
def serve_audio():
    return send_from_directory('/storage/emulated/0', 'B.mp3')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
