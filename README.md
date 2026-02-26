# WhisperX Transcription Tool

Strumento per la trascrizione audio/video utilizzando WhisperX.

## ⚡ Caratteristiche Principali

- Riconoscimento automatico dei file audio/video nella cartella corrente
- Interfaccia CLI intuitiva e moderna
- Supporto per molteplici formati audio e video
- Trascrizione di alta qualità con WhisperX
- Supporto multilingua (90+ lingue)
- Ottimizzazione GPU con CUDA

## ⚙ Prerequisiti

1. Python 3.8 o superiore
2. CUDA (opzionale, ma raccomandato per prestazioni migliori)
3. PyTorch
4. WhisperX

## ⌂ Installazione

1. Clona o scarica questo repository
2. Apri PowerShell come amministratore
3. Naviga nella cartella del progetto
4. Esegui:

```powershell
# Installa le dipendenze
pip install -r requirements.txt

# Rendi lo script disponibile globalmente
$scriptPath = Join-Path $PWD "whisperx_global.py"
$envPath = [System.Environment]::GetEnvironmentVariable("PATH", "User")
[System.Environment]::SetEnvironmentVariable("PATH", "$envPath;$scriptPath", "User")
```

## ⎙ Utilizzo

Da qualsiasi cartella in PowerShell:

```powershell
python whisperx_global.py
```

Lo strumento ti guiderà attraverso:
1. Rilevamento automatico dei file audio/video nella cartella corrente
2. Selezione del modello (tiny → large-v3)
3. Tipo di computazione (float32, float16, int8)
4. Selezione della lingua
5. Formato di output (TXT, SRT, VTT, JSON, o tutti)
6. Selezione cartella output

## ⚡ Modelli Disponibili

- `tiny`: Più veloce, meno accurato (~ 1GB RAM)
- `base`: Veloce, accuratezza base (~ 1GB RAM)
- `small`: Buon bilanciamento (~ 2GB RAM)
- `medium`: Accurato (~ 5GB RAM) - CONSIGLIATO
- `large`: Più accurato ma più lento (~ 10GB RAM)
- `large-v2`: Più recente e accurato (~ 10GB RAM)
- `large-v3`: Ultimo modello, più accurato (~ 10GB RAM)

## ⚙ Tipi di Computazione

- `float32`: Più lento ma più compatibile
- `float16`: Più veloce ma potrebbe non essere supportato
- `int8`: Molto veloce ma meno preciso

## 🌐 Lingue Supportate

WhisperX supporta oltre 90 lingue. Ecco le principali con i loro codici:

### Lingue Principali
- Inglese: `en`
- Italiano: `it`
- Francese: `fr`
- Tedesco: `de`
- Spagnolo: `es`
- Portoghese: `pt`
- Olandese: `nl`
- Giapponese: `ja`
- Cinese: `zh`

### Altre Lingue Comuni
- Russo: `ru`
- Coreano: `ko`
- Hindi: `hi`
- Turco: `tr`
- Polacco: `pl`
- Svedese: `sv`
- Danese: `da`
- Norvegese: `no`
- Finlandese: `fi`
- Indonesiano: `id`
- Vietnamita: `vi`
- Tailandese: `th`
- Arabo: `ar`
- Ebraico: `he`

Per l'elenco completo delle lingue supportate, visita la [documentazione ufficiale di Whisper](https://github.com/openai/whisper/blob/main/whisper/tokenizer.py).

## ⚡ Funzionalità

- ⌖ Trascrizione audio/video
- ⎙ Multiple formati di output (TXT, SRT, VTT, JSON)
- ⚡ Supporto GPU (CUDA)
- ⌂ Rilevamento automatico file
- ⚙ Configurazione flessibile
- ✎ Allineamento preciso del testo

## ⚠ Risoluzione Problemi

Se incontri errori:

1. ⚙ Verifica che Python sia nel PATH di sistema
2. ✓ Controlla che tutte le dipendenze siano installate
3. ⚡ Se usi la GPU:
   - Verifica che CUDA sia installato correttamente
   - Prova a utilizzare lo strumento con CPU se persistono problemi
4. ⚠ Se hai problemi con float16, prova con float32

## ⌂ Formati Supportati

### Audio
- MP3 (.mp3)
- WAV (.wav)
- M4A (.m4a)
- FLAC (.flac)
- AAC (.aac)
- OGG (.ogg)
- WMA (.wma)

### Video
- MP4 (.mp4)
- AVI (.avi)
- MKV (.mkv)
- MOV (.mov) 