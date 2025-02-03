from flask import Flask, render_template, request, send_file
import os
from pydub import AudioSegment
import librosa
import numpy as np

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('Acc.html')

@app.route('/processar', methods=['POST'])
def processar():
    arquivo = request.files['audio']
    caminho_original = os.path.join(UPLOAD_FOLDER, 'original.wav')
    arquivo.save(caminho_original)

    # Gerar acompanhamento (exemplo simplificado)
    y, sr = librosa.load(caminho_original, sr=22050)
    acompanhamento = np.random.uniform(-0.1, 0.1, len(y))  # Exemplo: ruído branco
    caminho_acompanhamento = os.path.join(UPLOAD_FOLDER, 'acompanhamento.wav')
    librosa.output.write_wav(caminho_acompanhamento, acompanhamento, sr)

    # Mixar áudio original com acompanhamento
    audio_original = AudioSegment.from_wav(caminho_original)
    audio_acompanhamento = AudioSegment.from_wav(caminho_acompanhamento)
    audio_mixado = audio_original.overlay(audio_acompanhamento)
    caminho_mixado = os.path.join(UPLOAD_FOLDER, 'mixado.wav')
    audio_mixado.export(caminho_mixado, format="wav")

    return {
        "original": caminho_original,
        "acompanhamento": caminho_acompanhamento,
        "mixado": caminho_mixado
    }

@app.route('/baixar/<tipo>')
def baixar(tipo):
    caminho = os.path.join(UPLOAD_FOLDER, f'{tipo}.wav')
    return send_file(caminho, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
