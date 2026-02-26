#!/usr/bin/env python3
import argparse
import subprocess
import os
import torch
import sys

def check_cuda():
    """Verifica se CUDA è disponibile e lo mostra"""
    if torch.cuda.is_available():
        print(f"🚀 CUDA disponibile! Usando GPU: {torch.cuda.get_device_name(0)}")
        return True
    else:
        print("⚠️ CUDA non disponibile, usando CPU")
        return False

def select_model():
    """Guida l'utente nella selezione del modello"""
    models = {
        '1': ('tiny', 'Più veloce, meno accurato (~ 1GB RAM)'),
        '2': ('base', 'Veloce, accuratezza base (~ 1GB RAM)'),
        '3': ('small', 'Buon bilanciamento (~ 2GB RAM)'),
        '4': ('medium', 'Accurato (~ 5GB RAM) - CONSIGLIATO'),
        '5': ('large', 'Più accurato ma più lento (~ 10GB RAM)')
    }
    
    print("\n📊 Seleziona il modello Whisper:")
    for key, (model, desc) in models.items():
        print(f"  {key}) {model.capitalize()}: {desc}")
    
    while True:
        choice = input("\nSelezione (1-5) [default: 4]: ").strip() or '4'
        if choice in models:
            return models[choice][0]
        print("❌ Selezione non valida. Riprova.")

def select_format():
    """Guida l'utente nella selezione del formato"""
    formats = {
        '1': ('txt', 'Testo semplice'),
        '2': ('srt', 'Sottotitoli con timestamp'),
        '3': ('vtt', 'Web Video Text Tracks'),
        '4': ('json', 'JSON con timestamp e confidence'),
        '5': ('all', 'Tutti i formati')
    }
    
    print("\n📄 Seleziona il formato di output:")
    for key, (fmt, desc) in formats.items():
        print(f"  {key}) {fmt.upper()}: {desc}")
    
    while True:
        choice = input("\nSelezione (1-5) [default: 1]: ").strip() or '1'
        if choice in formats:
            return formats[choice][0]
        print("❌ Selezione non valida. Riprova.")

def select_file():
    """Guida l'utente nella selezione del file"""
    while True:
        file_path = input("\n📁 Inserisci il percorso del file audio/video: ").strip()
        if os.path.exists(file_path):
            return file_path
        print(f"❌ File non trovato: {file_path}")
        print("   Assicurati di inserire il percorso corretto.")

def select_output_dir():
    """Guida l'utente nella selezione della cartella output"""
    choice = input("\n📂 Vuoi specificare una cartella di output? (s/N): ").strip().lower()
    if choice == 's':
        while True:
            output_dir = input("Inserisci il percorso della cartella: ").strip()
            if output_dir:
                return output_dir
            print("❌ Percorso non valido.")
    return None

def confirm_choices(file_path, model, format, output_dir, use_gpu):
    """Mostra un riepilogo e chiede conferma"""
    print("\n" + "="*50)
    print("📋 RIEPILOGO CONFIGURAZIONE")
    print("="*50)
    print(f"File: {file_path}")
    print(f"Modello: {model}")
    print(f"Formato: {format}")
    print(f"Output: {output_dir if output_dir else 'Stessa cartella del file'}")
    print(f"GPU: {'Sì' if use_gpu else 'No (usando CPU)'}")
    print("="*50)
    
    choice = input("\nProcedere con questa configurazione? (S/n): ").strip().lower()
    return choice != 'n'

def transcribe_audio(input_file, model='medium', language='en', output_format='txt', output_dir=None, force_gpu=True):
    """Transcribe un file audio usando Whisper"""
    # Normalizza il percorso del file
    input_file = os.path.abspath(input_file)
    
    cmd = [
        'whisper',
        input_file,
        '--language', language,
        '--model', model,
        '--output_format', output_format,
        '--verbose', 'True'
    ]
    
    if force_gpu:
        cmd.extend(['--device', 'cuda'])
    else:
        cmd.extend(['--device', 'cpu'])
    
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        cmd.extend(['--output_dir', output_dir])
    
    print(f"\n🎙️ Avvio trascrizione...")
    print(f"Comando: {' '.join(cmd)}")
    
    try:
        # Mostra il comando completo per debugging
        print(f"\n📌 Eseguendo comando:")
        print(f"   {' '.join(cmd)}")
        
        # Esegui il comando catturando l'output
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        # Mostra l'output se presente
        if result.stdout:
            print(f"\n📝 Output: {result.stdout}")
        
        print(f"\n✅ Trascrizione completata!")
        if output_dir:
            print(f"File salvati in: {output_dir}")
            
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Errore durante la trascrizione:")
        print(f"   Codice errore: {e.returncode}")
        if e.stdout:
            print(f"   Output: {e.stdout}")
        if e.stderr:
            print(f"   Errore: {e.stderr}")
        print(f"\n💡 Suggerimenti:")
        print(f"   - Verifica che il file esista e sia accessibile")
        print(f"   - Prova con un modello più piccolo (es. tiny o base)")
        print(f"   - Assicurati che Whisper sia installato correttamente")
        print(f"   - Prova senza GPU aggiungendo '--cpu'")
        
    except Exception as e:
        print(f"\n❌ Errore inaspettato: {str(e)}")

def main():
    print("🎯 WHISPER TRANSCRIPTION TOOL")
    print("============================")
    
    # Controlla CUDA
    has_cuda = check_cuda()
    
    # Procedura guidata
    if len(sys.argv) > 1:
        # Se ci sono argomenti da linea di comando, usa quelli
        parser = argparse.ArgumentParser(description='Script per trascrizione con Whisper')
        parser.add_argument('input_file', help='File audio/video da trascrivere')
        parser.add_argument('--model', default='medium', 
                          choices=['tiny', 'base', 'small', 'medium', 'large'],
                          help='Modello da usare (default: medium)')
        parser.add_argument('--language', default='en', 
                          help='Lingua del file (default: en)')
        parser.add_argument('--format', default='txt',
                          choices=['txt', 'srt', 'vtt', 'json', 'all'],
                          help='Formato output (default: txt)')
        parser.add_argument('--output-dir', help='Cartella di output (opzionale)')
        parser.add_argument('--cpu', action='store_true', help='Forza uso CPU invece di GPU')
        
        args = parser.parse_args()
        file_path = args.input_file
        model = args.model
        format = args.format
        output_dir = args.output_dir
        use_gpu = has_cuda and not args.cpu
    else:
        # Procedura guidata interattiva
        model = select_model()
        format = select_format()
        file_path = select_file()
        output_dir = select_output_dir()
        use_gpu = has_cuda
        
        # Conferma
        if not confirm_choices(file_path, model, format, output_dir, use_gpu):
            print("❌ Operazione annullata.")
            return
    
    # Se l'utente vuole tutti i formati
    if format == 'all':
        formats = ['txt', 'srt', 'vtt', 'json']
        for fmt in formats:
            print(f"\n>>> Generando formato {fmt}")
            transcribe_audio(file_path, model, 'en', fmt, output_dir, use_gpu)
    else:
        transcribe_audio(file_path, model, 'en', format, output_dir, use_gpu)

if __name__ == '__main__':
    main()