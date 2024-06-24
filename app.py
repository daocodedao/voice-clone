import spaces
import gradio as gr
import torch
from TTS.api import TTS
import os
import platform

os.environ["COQUI_TOS_AGREED"] = "1"

def getProxy():
    if platform.system() == "Linux":
        return "192.168.0.77:18808"
    else:
        return "127.0.0.1:10809"


os.environ['HTTP_PROXY'] = getProxy()
os.environ['HTTPS_PROXY'] = getProxy()


# device = "cuda"
device = "cuda" if torch.cuda.is_available() else "cpu"

# device = "cpu"

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

# @spaces.GPU(enable_queue=True)
def clone(text, audio):
    tts.tts_to_file(text=text, speaker_wav=audio, language="en", file_path="./output.wav")
    return "./output.wav"

demo = gr.Interface(fn=clone, 
                     inputs=[gr.Textbox(label='Text'),gr.Audio(type='filepath', label='Voice reference audio file')], 
                     outputs=gr.Audio(type='filepath'),
                     title='Voice Clone',
                     description="""
                     by [Tony Assi](https://www.tonyassi.com/)
                     
                     Please ❤️ this Space. I build custom AI apps for companies. <a href="mailto: tony.assi.media@gmail.com">Email me</a> for business inquiries.
                     """,
                     theme = gr.themes.Base(primary_hue="teal",secondary_hue="teal",neutral_hue="slate"),
                     examples=[["Hey! It's me Dorthy, from the Wizard of Oz. Type in whatever you'd like me to say.","./audio/Wizard-of-Oz-Dorthy.wav"],
                               ["It's me Vito Corleone, from the Godfather. Type in whatever you'd like me to say.","./audio/Godfather.wav"],
                               ["Hey, it's me Paris Hilton. Type in whatever you'd like me to say.","./audio/Paris-Hilton.mp3"],
                               ["Hey, it's me Megan Fox from Transformers. Type in whatever you'd like me to say.","./audio/Megan-Fox.mp3"],
                               ["Hey there, it's me Jeff Goldblum. Type in whatever you'd like me to say.","./audio/Jeff-Goldblum.mp3"],
                               ["Hey there, it's me Jeff Goldblum. Type in whatever you'd like me to say.","./audio/jasper.wav"],])
# demo.launch()

demo.launch(share=True, server_port=9651, ssl_verify=False, debug=True, show_error=True)