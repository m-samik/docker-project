from flask import Flask , render_template , request
from twilio.rest import Client
import random
import os


app = Flask("myapp")

otp_value=0

def func_otp():
    otp = random.randint(200000,500000)
    return otp



numberd =[]
# export FLASK_ENV=development

@app.errorhandler(405)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error.html'), 405

@app.route('/web')
def web():
    return render_template('test.html')


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/get_phone', methods=['GET'])
def get_phone_no():
    try:
        global otp_value
        otp_value = func_otp()
        #otp_value.append(otp)
        num_data = request.args.get('phone')
        # account_sid = os.environ['account_sid']
        account_sid = "ACa116d11d5690adf1fd5b6b6e136f0040"
        auth_token = "0ce77a3b8d93870a074696916c0b123c"

        # auth_token = os.environ['auth_token']
        client = Client(account_sid, auth_token)
        numberd.append(num_data)
        message = client.messages \
                .create(
                        body=f"Hey OTP for DockerWeb Login is  : {otp_value} ",
                        from_='+16089274714',
                        to=f'+91{num_data}'
                    )
        if message.sid :
            success= "OTP Sent Sucessfully"
            return (success)

        else:
            failure ="Try ReSending the OTP"
            return render_template('login.html',failure=failure) 
    except:
        return "Try Again"

@app.route("/login" , methods=['POST'])
def login():
        if request.method == "POST":
        #Values getting from HTML Form 
            otp_f=request.form.get("otp")
            print(otp_f,type(otp_f))
            try:
                for j in numberd:
                    f_number= int(j)
                
                numberd.pop()
            except:
                value = "Enter Your Phone Number!!"
                return render_template("login.html",value=value)

            db =[{"name" : "Muhammad Sami Khanday" , "phone" : 8491881271} , {"name" : "Tabish" , "phone" : 9797859943}]
            for i in db:
                # print(i)
                if i['phone'] == f_number:
                    name = i['name']
            # print("otp is ",type(otp))
            # print("from form otp is" , type(otp_f))
            global otp_value
            if int(otp_f) == otp_value :
                print(type(otp_f))
                return render_template('index.html' , name=name)
            else:
                value = "Enter a Valid OTP"
                return render_template('login.html' , value=value)

if __name__ == "__main__":
    app.run(debug=True  , port=5002)