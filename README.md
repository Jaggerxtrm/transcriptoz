# WhisperX Transcription Tool

Strumento per la trascrizione audio/video utilizzando WhisperX con supporto YouTube.

## ⚡ Caratteristiche Principali

- 📺 **Download automatico da YouTube** - Supporta video, live, shorts
- 🎙️ Trascrizione di alta qualità con WhisperX
- 🌍 Supporto multilingua (90+ lingue)
- 📄 Multipli formati output (TXT, SRT, VTT, JSON)
- ⚡ **GPU CUDA supportata** - Windows, Linux, Mac
- 🧹 Cleanup automatico file temporanei

## ⚙ Prerequisiti

1. Python 3.9 - 3.12
2. yt-dlp (`pip install yt-dlp`)
3. WhisperX (`pip install whisperx`)

## ⌂ Installazione

### Linux / Mac (pyenv consigliato)

```bash
# Usa pyenv per Python 3.12
pyenv install 3.12.8
pyenv virtualenv 3.12.8 transcriptoz
pyenv local transcriptoz

# Installa dipendenze
pip install -r requirements.txt
```

### Windows (con CUDA)

```powershell
# 1. Installa Python 3.12 da python.org
# Assicurati di spuntare "Add Python to PATH"

# 2. Installa CUDA Toolkit (se hai GPU NVIDIA)
# Download: https://developer.nvidia.com/cuda-downloads
# Versione consigliata: CUDA 12.x

# 3. Verifica CUDA
nvidia-smi  # Dovrebbe mostrare la tua GPU

# 4. Crea ambiente virtuale
python -m venv transcriptoz
.\transcriptoz\Scripts\Activate.ps1

# 5. Installa PyTorch con CUDA
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121

# 6. Installa WhisperX
pip install whisperx yt-dlp
```

### Verifica Installazione

```bash
# Controlla dipendenze
python transcribe_youtube.py --check-deps

# Verifica CUDA (Windows/Linux)
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}'); print(f'GPU: {torch.cuda.get_device_name(0) if torch.cuda.is_available() else \"N/A\"}')"
```

## ⎙ Utilizzo Rapido

### Trascrivere video YouTube

```bash
# Trascrizione base (Italiano, modello tiny)
python transcribe_youtube.py "https://www.youtube.com/watch?v=VIDEO_ID"

# Con opzioni personalizzate
python transcribe_youtube.py "https://youtu.be/VIDEO_ID" \
  --model base \
  --language en \
  --output-format srt

# Live YouTube
python transcribe_youtube.py "https://www.youtube.com/live/LIVE_ID"

# Mantieni file audio dopo trascrizione
python transcribe_youtube.py "URL" --keep-audio
```

### Trascrivere file locale

```bash
# Usa lo script esistente
python whisperx_global.py
```

## ⚡ GPU CUDA (Windows)

**Sì, funziona su Windows con CUDA!** 🎉

### Requisiti GPU

| Componente | Requisito |
|------------|-----------|
| GPU | NVIDIA (GTX 1060 o superiore consigliato) |
| VRAM | 4GB+ (tiny/base), 8GB+ (medium), 12GB+ (large) |
| Driver | NVIDIA Driver 550+ |
| CUDA | 12.x (installato con PyTorch o separatamente) |

### Velocità Attesa

| Modello | CPU (i7) | GPU (RTX 3060) | GPU (RTX 4090) |
|---------|----------|----------------|----------------|
| tiny | 10x realtime | 0.5x realtime | 0.2x realtime |
| base | 8x realtime | 0.6x realtime | 0.3x realtime |
| medium | 4x realtime | 0.8x realtime | 0.4x realtime |
| large-v3 | 2x realtime | 1.5x realtime | 0.6x realtime |

*Realtime = tempo per trascrivere 1 minuto di audio*

### Windows PowerShell Example

```powershell
# Attiva ambiente
.\transcriptoz\Scripts\Activate.ps1

# Trascrivi con GPU
python transcribe_youtube.py "https://youtube.com/watch?v=VIDEO_ID" `
  --model medium `
  --language it `
  --device cuda `
  --compute-type float16
```

### Risoluzione Problemi CUDA (Windows)

```powershell
# Errore: CUDA not available
# Soluzione: Reinstalla PyTorch con CUDA
pip uninstall torch torchaudio
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121

# Errore: Out of memory
# Soluzione: Usa modello più piccolo o float16
python transcribe_youtube.py "URL" --model tiny --compute-type float16

# Errore: NVIDIA driver too old
# Soluzione: Aggiorna driver da GeForce Experience o nvidia.com
```

## ⚡ Modelli Disponibili

| Modello | RAM | VRAM | Velocità | Accuratezza | Uso Consigliato |
|---------|-----|------|----------|-------------|-----------------|
| `tiny` | ~1GB | ~1GB | ⚡⚡⚡ | ⭐⭐ | Test, CPU-only |
| `base` | ~1GB | ~1GB | ⚡⚡ | ⭐⭐⭐ | Uso generale |
| `small` | ~2GB | ~2GB | ⚡ | ⭐⭐⭐⭐ | Bilanciato |
| `medium` | ~5GB | ~4GB | 🐌 | ⭐⭐⭐⭐⭐ | Produzione |
| `large-v3` | ~10GB | ~8GB | 🐌🐌 | ⭐⭐⭐⭐⭐+ | Massima qualità |

## 🌐 Lingue Supportate

Codici lingua principali:
- `it` - Italiano
- `en` - English
- `fr` - Français
- `de` - Deutsch
- `es` - Español
- `pt` - Português
- `ja` - Japanese
- `zh` - Chinese
- `ru` - Russian
- `ko` - Korean

[Lista completa](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py)

## ⚙ Opzioni Complete

```bash
python transcribe_youtube.py "URL" \
  --model tiny \              # Modello Whisper
  --language it \             # Lingua audio
  --compute-type float32 \    # float32|float16|int8
  --device cpu \              # cpu|cuda
  --output-dir transcripts \  # Cartella output
  --output-format txt \       # txt|srt|vtt|json
  --audio-format mp3 \        # mp3|wav|m4a
  --quality 128K \            # Qualità audio
  --keep-audio                # Mantieni file audio
```

## 📁 Struttura Progetto

```
transcriptoz/
├── transcribe_youtube.py   # Pipeline YouTube → Trascrizione
├── whisperx_global.py      # Interfaccia CLI per file locali
├── whisper.py              # Wrapper Whisper base
├── requirements.txt        # Dipendenze Python
└── transcripts/            # Output trascrizioni
```

## ⚠ Risoluzione Problemi

### Errori di download YouTube
```bash
# Aggiorna yt-dlp
pip install -U yt-dlp

# Prova con proxy se bloccato
yt-dlp --proxy "http://proxy:port" "URL"
```

### Errori di trascrizione
```bash
# Verifica dipendenze
python transcribe_youtube.py --check-deps

# Prova modello più piccolo
python transcribe_youtube.py "URL" --model tiny

# Usa CPU se GPU dà errori
python transcribe_youtube.py "URL" --device cpu
```

### Python version error
```bash
# WhisperX richiede Python 3.9-3.12
pyenv install 3.12.8
pyenv virtualenv 3.12.8 transcriptoz
pyenv local transcriptoz
```

### CUDA non rilevato (Windows)
```powershell
# Verifica installazione CUDA
python -c "import torch; print(torch.cuda.is_available())"

# Se False, reinstalla PyTorch CUDA
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
```

## 📊 Formati Output

| Formato | Uso | Timestamp |
|---------|-----|-----------|
| `txt` | Testo semplice | ❌ |
| `srt` | Sottotitoli video | ✅ |
| `vtt` | Web video text | ✅ |
| `json` | Dati strutturati | ✅ |

## ⚡ Esempi

### Trascrizione meeting (Italiano)
```bash
python transcribe_youtube.py "https://youtube.com/live/MEETING_ID" \
  --model base \
  --language it \
  --output-format srt
```

### Trascrizione conferenza (Inglese, alta qualità, GPU)
```bash
python transcribe_youtube.py "https://youtu.be/CONFERENCE_ID" \
  --model medium \
  --language en \
  --device cuda \
  --compute-type float16 \
  --output-format json \
  --keep-audio
```

### Batch processing (script)
```bash
#!/bin/bash
for url in $(cat video_urls.txt); do
  python transcribe_youtube.py "$url" --model tiny
done
```

### Windows PowerShell Batch
```powershell
Get-Content video_urls.txt | ForEach-Object {
  python transcribe_youtube.py $_ --model base --device cuda
}
```

## 🔧 Configurazione Windows Completa

```powershell
# 1. Crea cartella progetto
mkdir C:\transcriptoz
cd C:\transcriptoz

# 2. Crea ambiente virtuale
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 3. Installa PyTorch con CUDA 12.1
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121

# 4. Installa WhisperX e yt-dlp
pip install whisperx yt-dlp

# 5. Verifica CUDA
python -c "import torch; print(f'CUDA: {torch.cuda.is_available()}')"

# 6. Trascrivi primo video
python transcribe_youtube.py "https://youtube.com/watch?v=VIDEO_ID" --device cuda
```

## 📝 License

MIT License - Uso libero per progetti personali e commerciali.

## 🤝 Support

Per problemi o domande:
1. Controlla i prerequisiti (Python 3.9-3.12)
2. Verifica CUDA: `python -c "import torch; print(torch.cuda.is_available())"`
3. Aggiorna le dipendenze: `pip install -U whisperx yt-dlp`
