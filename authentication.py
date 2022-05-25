import pyrebase

firebaseConfig = {
    # //yout config code
    apiKey: "AIzaSyBpJ19yUGGEBHShU3DUBknVI0zsMDa5HFQ",
    authDomain: "authentication-of-users-app.firebaseapp.com",
    databaseURL: "https://authentication-of-users-app-default-rtdb.firebaseio.com",
    projectId: "authentication-of-users-app",
    storageBucket: "authentication-of-users-app.appspot.com",
    messagingSenderId: "516976118680",
    appId: "1:516976118680:web:edaafcb483a3320a2139ed",
    measurementId: "G-TF17VRKR37"
  };
firebase=firebase.initialize_app(firebaseConfig)
auth=firebase.auth(email)
email='test@gmail.com'
password='123456'
user=auth.create_user_with_email_and_password(email,password)
auth.send_password_reset_email(email)