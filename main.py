from datetime import time

import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import random
import os
import webbrowser
import time
from fastapi.responses import JSONResponse
import json
from static.audio_func import func2, time_of_prev_sentence, silence_times, initialize_arrays_script

# from static.audio_func import time_of_prev_sentence

app = FastAPI()

static_dir = "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


# global length_prev_sentence, pos_prev_sentence


def multiple(num):
    return num * 2


@app.get('/ron1', response_class=HTMLResponse)
async def ron11():
    current_dir = os.getcwd()
    file_path1 = "static/bdika.html"
    with open(file_path1, "r") as f:
        file_path1 = f.read()
    val = 5.7
    return file_path1


@app.get('/12')
async def root():
    return {'example': 'This is an example', 'data': 8}


_pos = 0


@app.get('/ron', response_class=HTMLResponse)
async def ron1():
    num1 = 0
    current_dir = os.getcwd()
    audio_file_path = "static/Most dog owners have.mp3"
    current_dir = os.getcwd()
    file_path = "static/web.html"
    with open(file_path, "r") as f:
        file_path = f.read()
    stam = 5.7

    def jump_to_second(seconds, pause_time):
        return 89

    def get_2(num):
        return 2 * num

    _pos_prev_sentence = -2
    _length_prev_sentence = -2

    def get_pos_prev_sentence(audio, audio2, pos):
        print("DFDFD")
        # globals()._pos = 5
        if pos < 0:
            return 6
        else:
            globals().pos_prev_sentence, globals().length_prev_sentence = time_of_prev_sentence(audio, audio2, pos)
            return JSONResponse(content={"pos_prev_sentence": _pos_prev_sentence})

    def func():
        # global _pos
        # _pos = 5
        return 2

    def get_length_prev_sentence(audio, audio2, pos):
        if _length_prev_sentence == -1:
            globals().pos_prev_sentence, globals().length_prev_sentence = time_of_prev_sentence(audio, audio2, pos)
        return JSONResponse(content={"length_prev_sentence": _length_prev_sentence})

    return f"""
            <!DOCTYPE html>
                <html>
                        <span id="result"></span>
                        <span id="result1"></span>
                          
                        <body>
                            <h1>Audio Example</h1>
                            <a id="dynamicLink" href="#" target="_blank">
                                <button>Go to Site</button>
                            </a>
                            <script>
                                    func();
                                    document.getElementById("result").innerHTML = {_pos};
                                    document.write({_pos});
                                    //{{num1}} = 23;
                            </script>
                            <script>
                                document.write({_pos});

                            </script>

                            <script>
                                    
                                    //var resultElement = document.getElementById("result");
                                    //var resultValue = {get_2(3)};
                                    var resultValue;
                                    var resultValue1; 
                                    //resultElement.innerHTML = resultValue;
                                    
                                    //document.write(resultValue);
                                </script>
                            <audio id="audio" controls>
                                <source src="static/Most dog owners have.mp3" type="audio/mp3">
                                Your browser does not support the audio element.
                            </audio>
                            <audio id="audio2" controls>
                                <source src="static/He Most dog owners have.mp3" type="audio/mp3">
                                Your browser does not support the audio element.
                            </audio>

                            <button onclick="jump_to_second(5,4)">I'm dont realized</button>

                            <script>
                                var vall = jump_to_second(7,8);
                            </script>
                            <script>
                                var resultElement = document.getElementById("result");
                                var audio = document.getElementById("audio");
                                var audio2 = document.getElementById("audio2");
                                var pos=-1;
                                var pos_prev_sentence = get_pos_prev_sentence(audio, audio2, pos);
                                document.write(1022);
                                resultElement.innerHTML = 123;
                                var length_prev_sentence = get_length_prev_sentence(audio, audio2, pos);
                                console.log(pos_prev_sentence);
                                console.log(pos_length_sentence);
                                
                            </script>

                            <script>
                                    {num1=}  23;
                                    document.write(232);
                            </script>

                        </body>
                </html>

            """


k1 = 0


@app.get('/ron2/{pos: float}', response_class=HTMLResponse)
async def ron2(pos: float):
    kk = pos

    def func(t):
        global k1
        k1 = 5
        return 2

    return f"""
            <!DOCTYPE html>
                <html>
                        <span id="result"></span>

                        <body>
                            <h1>Audio Example</h1>
                            
                            <a id="dynamicLink" href="#" target="_blank">
                                <button>Go to Site</button>
                            </a>
                           
                            
                            <script>
                                    var dynamicValue = 56;
                                    var linkElement = document.getElementById('dynamicLink');
                                    linkElement.href = "http://127.0.0.1:8002/ron2/" + dynamicValue;  
                                    
                                    
                                    var k2 = 5;
                                    document.write({kk});                                                                                                    
                            </script>
                                                        
                            
                            
                        </body>
                </html>

            """


@app.get('/ron3/{poss: float}', response_class=HTMLResponse)
async def ron3(poss: float):
    kk = poss
    i = 1
    current_dir = os.getcwd()

    def func(t):
        global k1
        k1 = 5
        return 2

    file_path = "static/bdika.html"
    with open(file_path, "r") as f:
        file_path = f.read()
    arr1 = [3, 6, 9]
    # return file_path
    return """
            <!DOCTYPE html>
                <html>
                <body>
                    <head>
                    <title>Audio Silence Detection</title>
                </head>
            
                            <audio id="audio" controls>
                                            <source src="static/Most dog owners have.mp3" type="audio/mp3">
                                            Your browser does not support the audio element.
                            </audio>
                            <audio id="audio2" controls>
                                            <source src="static/He Most dog owners have.mp3" type="audio/mp3">
                                            Your browser does not support the audio element.
                            </audio>
                    
                            <span id="title">Audio Silence Detection</span>
                            <button onclick="jumpToSecond(5,4)">I'm dont realized</button>
                    
                            <script>
                            let x = [1, 8, 15, 21, 31, 41, 51];
                            let y = [5, 12, 19, 29, 39, 49, 59];
                            
                            var audio = document.getElementById("audio");
                            var audio2 = document.getElementById("audio2");
                            
                            var pos1;
                            var pos_prev_sentence=5;
                            var length_prev_sentence=5;
                            
                            function jumpToSecond(seconds, pause_time) {
                                pos1 = audio.currentTime;
                                let j;
                                for(j=1; j<7; j++){
                                    if(pos1 > y[j] && pos1 < y[j+1]){
                                        break;  
                                        }
                                }
                                length_prev_sentence = y[j+1] - y[j];
                                audio.pause();
                                audio2.play();
                                audio2.currentTime = y[j];
                                document.getElementById("title").innerHTML = 489;
                                setTimeout(function() {
                                    audio2.pause();
                                    audio.play();
                                    audio.currentTime = pos1;
                                }, length_prev_sentence * 1000);
                            }



                            </script>
                    </body>
                </html>
                
            """


kl = "904"





@app.get('/{poss:float}', response_class=HTMLResponse)
async def ron4(poss: float, sleep=3):

    en_start = [0] * 8
    time_p = 3

    def func1():
        ron4()

    # if poss != 0 and arr_end_en != 0:
    #     time_p, sleep = time_of_prev_sentence(file_en, file_he, poss)
    # else:
    #     arr_start_en, arr_end_en = silence_times(file_en, 0.8)
    #     arr_start_he, arr_end_he = silence_times(file_he, 0.5)
    return f"""
            <!DOCTYPE html>
            <html>
            <body>
            <button onclick="jumpToSecond()">I'm dont realized</button>
            <audio id="audio" controls>
                                            <source src="static/Most dog owners have.mp3" type="audio/mp3">
                                            Your browser does not support the audio element.
                            </audio>
                            <audio id="audio2" controls>
                                            <source src="static/He Most dog owners have.mp3" type="audio/mp3">
                                            Your browser does not support the audio element.
                            </audio>
                <span id="check"> err</span>

                <script>
                    let arr_start_en = [3.0100226757369613, 6.084172335600907, 13.650249433106575, 19.070340136054423, 25.041632653061225, 37.66448979591837, 45.82344671201814, 53.21532879818594, 60.83909297052154, 71.96367346938776, 78.30453514739229, 86.89673469387755, 96.80789115646259, 104.2772335600907, 108.8804081632653,115.25351473922902, 124.35863945578231, 129.3443083900227, 135.99859410430838, 141.50371882086168, 146.52507936507936, 169.59260770975058, 175.8338321995465, 186.93814058956917, 195.8401814058957,203.35487528344672, 210.45192743764173];
                    let arr_end_en = [3.6370068027210882, 6.728344671201814, 14.622902494331067, 20.06172335600907, 26.029750566893423, 38.64875283446712, 46.81451247165533, 54.25224489795919, 61.8259410430839, 72.95809523809524, 79.3015873015873, 87.89777777777778, 97.7687074829932, 105.25319727891157, 109.87913832199547, 116.23170068027211, 125.34031746031746, 130.33337868480726, 136.98285714285714, 142.50462585034015, 147.50725623582767, 170.55342403628117, 176.81755102040816, 187.94834467120182, 196.8269387755102, 204.30965986394557, 211.4415419501134];
                    let arr_start_he = [3.9937414965986395, 8.485895691609977, 16.504172335600906, 21.960544217687076, 29.45764172335601, 44.08095238095238, 53.66553287981859, 61.63678004535147, 70.5481179138322, 84.7312925170068, 91.53120181405896, 100.1463492063492, 112.35736961451248, 120.90430839002268, 126.7231746031746, 133.46448979591835, 145.6385941043084, 152.32598639455782, 160.07410430839002, 166.86526077097506, 172.76145124716552, 194.24244897959184, 197.54054421768708, 205.54344671201815, 218.0434013605442, 227.28403628117914, 237.0326984126984, 247.5978231292517];
                    let arr_end_he = [5.12421768707483, 9.486485260770975, 17.55546485260771, 22.998412698412697, 30.477913832199548, 45.11446712018141, 54.690657596371885, 62.67501133786848, 71.57741496598639, 85.75727891156463, 92.60544217687075, 101.15374149659864, 113.41795918367347, 122.00054421768708, 127.72589569160998, 134.4980045351474, 146.7560544217687, 153.3568253968254, 161.1663492063492, 167.85691609977323, 173.8231746031746, 195.2634013605442, 198.55301587301588, 206.56798185941042, 219.12852607709752, 228.33628117913833, 238.040589569161, 248.63922902494332];
                    var audio = document.getElementById("audio");
                    var audio2 = document.getElementById("audio2");           
                    
                        function jumpToSecond() {{
                                var j;
                                var pos2 = audio.currentTime;
                                audio.pause();
                        for(j=0; j<arr_end_en.length-1; j++)
                            if(pos2 < arr_end_en[j+1])
                                break;    
                        audio2.play();
                        audio2.currentTime = arr_end_he[j];
                        var time_sleep = arr_end_he[j+1]-arr_end_he[j];
                        setTimeout(function() {{
                                    audio2.pause();
                                    audio.play();
                                    audio.currentTime = pos2;
                                }}, time_sleep * 1000);
                        }}
                </script>
            </body>
            </html>
            """

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="18.117.70.224", port=8002)


file_en = "static/Most dog owners have.mp3"
file_he = "static/He Most dog owners have.mp3"


@app.get('/', response_class=HTMLResponse)
async def ron5(sleep=3):
    en_start = [0] * 8
    time_p = 3

    def func1():
        ron4()

    return f"""
            <!DOCTYPE html>
            <html>
            <body>
            <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }

        #container {
            text-align: center;
            padding: 20px;
        }

        button {
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
        }

        audio {
            width: 100%;
            max-width: 300px;
        }
    </style>
            <button onclick="jumpToSecond()">I'm dont realized</button>
            <audio id="audio" controls>
                                            <source src="{file_en}" type="audio/mp3">
                                            Your browser does not support the audio element.
                            </audio>
                            <audio id="audio2" controls>
                                            <source src="{file_he}" type="audio/mp3">
                                            Your browser does not support the audio element.
                            </audio>
                <span id="check"> err</span>

                <script>
                    {initialize_arrays_script("arr_start_en", "arr_end_en", "arr_start_he", "arr_end_he", file_en, file_he)} 
                    var audio = document.getElementById("audio");
                    var audio2 = document.getElementById("audio2");           

                        function jumpToSecond() {{
                                var j;
                                var pos2 = audio.currentTime;
                                audio.pause();
                        for(j=0; j<arr_end_en.length-1; j++)
                            if(pos2 < arr_end_en[j+1])
                                break;    
                        audio2.play();
                        audio2.currentTime = arr_end_he[j];
                        var time_sleep = arr_end_he[j+1]-arr_end_he[j];
                        setTimeout(function() {{
                                    audio2.pause();
                                    audio.play();
                                    audio.currentTime = pos2;
                                }}, time_sleep * 1000);
                        }}
                </script>
            </body>
            </html>
            """
