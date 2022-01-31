from flask import *
import requests
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def index():
    if request.method=='POST':
        city_name=request.form.get('city')
        r=requests.get('https://api.openweathermap.org/data/2.5/weather?q='+city_name+'&appid=7fc3d614db86362a6c107926b6b80951')
        json_object=r.json()
        temp=int(json_object['main']['temp'])
        pressure=int(json_object['main']['pressure'])
        humidity=int(json_object['main']['humidity'])
        temperature=int(temp-273.15)
        return render_template('home.html',temperature=temperature,pressure=pressure,humidity=humidity,city_name=city_name)
    else:
        return render_template('home.html')
if __name__=='__main__':
    app.run(debug=True)
