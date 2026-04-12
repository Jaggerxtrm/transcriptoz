#!/usr/bin/env python3
import argparse
import subprocess
import os
import torch
import sys
import json
from pathlib import Path
import logging
import locale
import codecs
import time
import threading
from importlib.metadata import version, PackageNotFoundError
import platform

# Configurazione encoding per Windows
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# Configurazione logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


def configure_logging(verbose: bool = False, debug: bool = False):
    """Configura dinamicamente il logging in base ai flag CLI"""
    # Rimuovi handler esistenti
    for h in logging.root.handlers[:]:
        logging.root.removeHandler(h)
    level = logging.DEBUG if debug else (logging.INFO if verbose else logging.WARNING)
    fmt = (
        '%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s'
        if debug
        else '%(asctime)s - %(levelname)s - %(message)s'
    )
    logging.basicConfig(
        level=level,
        format=fmt,
        handlers=[logging.StreamHandler(sys.stdout)],
    )
    logger.setLevel(level)
    logger.debug("Logging configurato", extra={"verbose": verbose, "debug": debug})

def get_package_version(package_name):
    """Get installed package version"""
    try:
        return version(package_name)
    except PackageNotFoundError:
        return None
def check_system_requirements():
    """Verifica tutti i requisiti di sistema"""
    requirements = {
        'cuda': False,
        'whisperx': False,
        'torch': False
    }
    
    print("\n\033[1;34m⚡ Verifica requisiti di sistema\033[0m")
    
    # Verifica CUDA
    try:
        if torch.cuda.is_available():
            cuda_version = torch.version.cuda
            requirements['cuda'] = True
            logger.info(f"\u2705 CUDA {cuda_version} disponibile - GPU: {torch.cuda.get_device_name(0)}")
        else:
            logger.warning("\u2757 CUDA non disponibile - Usando CPU (più lento)")
    except Exception as e:
        logger.error(f"\u274C Errore verifica CUDA: {str(e)}")
    
    # Verifica Torch
    try:
        torch_version = torch.__version__
        requirements['torch'] = True
        logger.info(f"\u2705 PyTorch {torch_version} installato")
    except Exception as e:
        logger.error(f"\u274C Errore PyTorch: {str(e)}")
    
    # Verifica WhisperX
    try:
        import whisperx
        requirements['whisperx'] = True
        logger.info("\u2705 WhisperX installato")
    except ImportError:
        logger.error("\u274C WhisperX non installato")
        print("\nInstalla WhisperX con:")
        print("pip install whisperx")
        return requirements
    
    return requirements

def setup_environment():
    """Configura l'ambiente per il corretto funzionamento"""
    # Imposta encoding UTF-8 per Windows
    if sys.platform == 'win32':
        os.system('chcp 65001')
        # Abilita TF32 per CUDA se disponibile
        if torch.cuda.is_available():
            torch.backends.cuda.matmul.allow_tf32 = True
            torch.backends.cudnn.allow_tf32 = True

def check_cuda():
    """Verifica se CUDA è disponibile e lo mostra"""
    if torch.cuda.is_available():
        logger.info(f"🚀 CUDA disponibile! Usando GPU: {torch.cuda.get_device_name(0)}")
        return True
    else:
        logger.info("⚠️ CUDA non disponibile, usando CPU")
        return False
def select_compute_type():
    """Guida l'utente nella selezione del tipo di computazione"""
    print("\n🔧 Seleziona il tipo di computazione:")
    print("  1) float32 - Più lento ma più compatibile")
    print("  2) float16 - Più veloce ma potrebbe non essere supportato")
    print("  3) int8 - Molto veloce ma meno preciso")
    
    while True:
        choice = input("\nSelezione (1-3) [default: 1]: ").strip() or '1'
        if choice == '1':
            return 'float32'
        elif choice == '2':
            return 'float16'
        elif choice == '3':
            return 'int8'
        print("❌ Selezione non valida. Riprova.")

def select_language():
    """Guida l'utente nella selezione della lingua"""
    languages = {
        '1': ('en', 'English'),
        '2': ('it', 'Italiano'),
        '3': ('fr', 'Français'),
        '4': ('de', 'Deutsch'),
        '5': ('es', 'Español'),
        '6': ('pt', 'Português'),
        '7': ('nl', 'Nederlands'),
        '8': ('ja', 'Japanese'),
        '9': ('zh', 'Chinese'),
        '10': ('other', 'Altra lingua (inserisci codice)')
    }
    
    print("\n🌍 Seleziona la lingua:")
    for key, (code, name) in languages.items():
        print(f"  {key}) {name}")
    
    while True:
        choice = input("\nSelezione (1-10) [default: 1]: ").strip() or '1'
        if choice in languages:
            if languages[choice][0] == 'other':
                custom_code = input("Inserisci il codice lingua (es. 'ru' per Russo): ").strip().lower()
                return custom_code
            return languages[choice][0]
        print("❌ Selezione non valida. Riprova.")

def select_model():
    """Guida l'utente nella selezione del modello"""
    models = {
        '1': ('tiny', 'Più veloce, meno accurato (~ 1GB RAM)'),
        '2': ('base', 'Veloce, accuratezza base (~ 1GB RAM)'),
        '3': ('small', 'Buon bilanciamento (~ 2GB RAM)'),
        '4': ('medium', 'Accurato (~ 5GB RAM) - CONSIGLIATO'),
        '5': ('large', 'Più accurato ma più lento (~ 10GB RAM)'),
        '6': ('large-v2', 'Più recente e accurato (~ 10GB RAM)'),
        '7': ('large-v3', 'Ultimo modello, più accurato (~ 10GB RAM)')
    }
    
    print("\n📊 Seleziona il modello WhisperX:")
    for key, (model, desc) in models.items():
        print(f"  {key}) {model.capitalize()}: {desc}")
    
    while True:
        choice = input("\nSelezione (1-7) [default: 4]: ").strip() or '4'
        if choice in models:
            return models[choice][0]
        print("❌ Selezione non valida. Riprova.")

def select_features():
    """Guida l'utente nella selezione delle funzionalità"""
    print("\n\033[1;33m⚙ Seleziona le funzionalità\033[0m")
    
    features = {
        'output_format': 'all',
        'compute_type': select_compute_type(),
        'language': select_language()
    }
    
    # Formato output
    formats = {
        '1': 'txt',
        '2': 'srt',
        '3': 'vtt',
        '4': 'json',
        '5': 'all'
    }
    
    print("\n\033[1;36m⎙ Formato output:\033[0m")
    print("  1) TXT - Solo testo")
    print("  2) SRT - Sottotitoli")
    print("  3) VTT - Web Video Text")
    print("  4) JSON - Con timestamp")
    print("  5) ALL - Tutti i formati")
    
    while True:
        choice = input("\nSelezione (1-5) [default: 5]: ").strip() or '5'
        if choice in formats:
            features['output_format'] = formats[choice]
            break
        print("\u274C Selezione non valida. Riprova.")
    
    return features

def get_audio_files():
    """Trova tutti i file audio nella cartella corrente"""
    audio_extensions = ('.mp3', '.wav', '.m4a', '.flac', '.aac', '.ogg', '.wma', '.mp4', '.avi', '.mkv', '.mov')
    audio_files = []
    
    for file in os.listdir('.'):
        if file.lower().endswith(audio_extensions):
            audio_files.append(file)
    
    return audio_files

def select_file():
    """Guida l'utente nella selezione del file"""
    audio_files = get_audio_files()
    
    if audio_files:
        print("\n\033[1;35m⌂ File audio/video trovati nella cartella corrente:\033[0m")
        for idx, file in enumerate(audio_files, 1):
            print(f"  {idx}) {file}")
        print(f"  {len(audio_files) + 1}) Specifica un altro file")
        
        while True:
            choice = input(f"\nSelezione (1-{len(audio_files) + 1}): ").strip()
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(audio_files):
                    return os.path.abspath(audio_files[choice - 1])
                elif choice == len(audio_files) + 1:
                    break
            print("\u274C Selezione non valida. Riprova.")
    
    while True:
        file_path = input("\n\033[1;35m⌂ Inserisci il percorso del file audio/video:\033[0m ").strip()
        file_path = os.path.abspath(file_path)
        if os.path.exists(file_path):
            return file_path
        print(f"\u274C File non trovato: {file_path}")
        print("   Assicurati di inserire il percorso corretto.")

def select_output_dir():
    """Guida l'utente nella selezione della cartella output"""
    choice = input("\n📂 Vuoi specificare una cartella di output? (s/N): ").strip().lower()
    if choice == 's':
        while True:
            output_dir = input("Inserisci il percorso della cartella: ").strip()
            output_dir = os.path.abspath(output_dir)
            os.makedirs(output_dir, exist_ok=True)
            return output_dir
    return None

def confirm_choices(file_path, model, features, output_dir, use_gpu):
    """Mostra un riepilogo e chiede conferma"""
    print("\n" + "="*50)
    print("\033[1;32m☰ RIEPILOGO CONFIGURAZIONE\033[0m")
    print("="*50)
    print(f"File: {file_path}")
    print(f"Modello: {model}")
    print(f"Formato: {features['output_format']}")
    print(f"Tipo computazione: {features['compute_type']}")
    print(f"Output: {output_dir if output_dir else 'Stessa cartella del file'}")
    print(f"GPU: {'Sì' if use_gpu else 'No (usando CPU)'}")
    print("="*50)
    
    choice = input("\nProcedere con questa configurazione? (S/n): ").strip().lower()
    return choice != 'n'

def transcribe_with_whisperx(input_file, model, features, output_dir=None, use_gpu=True, verbose=False, debug=False):
    """Transcribe un file audio usando WhisperX con streaming output e timing"""
    start_time = time.time()
    # Configura l'ambiente prima della trascrizione
    setup_environment()

    # Verifica versioni installate
    torch_version = get_package_version('torch')

    cmd = [
        sys.executable,
        '-u',  # unbuffered per streaming
        '-m', 'whisperx',
        input_file,
        '--model', model,
        '--language', features['language'],
        '--compute_type', features['compute_type']
    ]

    # Nota: non aggiungiamo flag '--verbose' al comando whisperx per evitare incompatibilità

    if not use_gpu:
        cmd.extend(['--device', 'cpu'])
    else:
        if torch.cuda.is_available():
            cmd.extend(['--device', 'cuda'])
            logger.info(f"\u2705 Usando GPU: {torch.cuda.get_device_name(0)}")
        else:
            logger.warning("\u2757 GPU non disponibile, usando CPU")
            cmd.extend(['--device', 'cpu'])

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        cmd.extend(['--output_dir', output_dir])

    # Formato output
    if features['output_format'] != 'all':
        cmd.extend(['--output_format', features['output_format']])

    logger.info(f"\n\033[1;36m⚡ Avvio trascrizione con WhisperX...\033[0m")
    logger.debug(f"⌘ Comando: {' '.join(cmd)}")

    try:
        # Ambiente subprocess
        my_env = os.environ.copy()
        my_env['PYTHONIOENCODING'] = 'utf-8'
        my_env['PYTHONUNBUFFERED'] = '1'
        # Disabilita warning per versioni troppo verbose, lasciabili in debug
        if not debug:
            my_env['PYTHONWARNINGS'] = 'ignore::UserWarning,ignore::FutureWarning'

        # Esegui processo con streaming STDOUT/STDERR
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding='utf-8',
            env=my_env
        )

        # Stream in tempo reale
        for line in iter(process.stdout.readline, ''):
            line = line.rstrip()
            if not line:
                continue
            # Normalizza output di progresso
            if 'it/s' in line or '%' in line or 'ETA' in line:
                logger.info(f"⏳ {line}")
            else:
                logger.info(line)
        process.stdout.close()
        returncode = process.wait()
        duration = time.time() - start_time

        if returncode == 0:
            logger.info(f"\n\u2705 Trascrizione completata in {duration:.1f}s")
            if output_dir:
                logger.info(f"File salvati in: {output_dir}")
        else:
            raise subprocess.CalledProcessError(returncode, cmd)

    except subprocess.CalledProcessError as e:
        logger.error(f"\n\u274C Errore durante la trascrizione (code {e.returncode}):")
        logger.debug(f"Comando fallito: {' '.join(cmd)}")
        print(f"\n\u2139 Suggerimenti:")
        print(f"   - Verifica che WhisperX sia installato: pip install whisperx")
        print(f"   - Prova con un modello più piccolo")
        print(f"   - Se hai problemi con float16, usa float32")
        print(f"   - Prova senza GPU aggiungendo '--device cpu'")

    except Exception as e:
        logger.error(f"\n\u274C Errore inaspettato: {str(e)}")
        logger.debug("Eccezione", exc_info=True)

def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="WhisperX Transcription Tool")
    parser.add_argument('--verbose', action='store_true', help='Abilita output dettagliato')
    parser.add_argument('--debug', action='store_true', help='Abilita output di debug molto verboso')
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    configure_logging(verbose=args.verbose or args.debug, debug=args.debug)

    logo = """
    ██╗    ██╗██╗  ██╗██╗███████╗██████╗ ███████╗██████╗ ██╗  ██╗
    ██║    ██║██║  ██║██║██╔════╝██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
    ██║ █╗ ██║███████║██║███████╗██████╔╝█████╗  ██████╔╝ ╚███╔╝ 
    ██║███╗██║██╔══██║██║╚════██║██╔═══╝ ██╔══╝  ██╔══██╗ ██╔██╗ 
    ╚███╔███╔╝██║  ██║██║███████║██║     ███████╗██║  ██║██╔╝ ██╗
     ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝╚══════╝╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
    """
    print("\033[36m" + logo + "\033[0m")  # Cyan color for the logo
    print("\n\033[1;32m⌖ WHISPERX TRANSCRIPTION TOOL\033[0m")
    print("============================")

    # Verifica requisiti iniziale
    t0 = time.time()
    requirements = check_system_requirements()
    logger.info(f"⏱ Requisiti verificati in {time.time() - t0:.2f}s")

    # Verifica requisiti minimi
    if not requirements['whisperx'] or not requirements['torch']:
        logger.error("\n\u274C Requisiti minimi non soddisfatti. Installare le dipendenze mancanti.")
        return

    print("\n\033[1;33m⚡ Configurazione Trascrizione\033[0m")
    print("============================")

    # Procedura guidata
    model = select_model()
    features = select_features()

    file_path = select_file()
    output_dir = select_output_dir()
    use_gpu = requirements['cuda']

    # Conferma
    if not confirm_choices(file_path, model, features, output_dir, use_gpu):
        logger.info("\u274C Operazione annullata.")
        return

    # Esegui trascrizione
    transcribe_with_whisperx(file_path, model, features, output_dir, use_gpu, verbose=args.verbose, debug=args.debug)

if __name__ == '__main__':
    main() 