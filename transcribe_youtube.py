#!/usr/bin/env python3
"""
YouTube Transcription Pipeline
Download audio from YouTube and transcribe with WhisperX
"""

import argparse
import subprocess
import os
import sys
import time
from pathlib import Path

def check_dependencies():
    """Check if required tools are installed"""
    missing = []
    
    # Check yt-dlp
    try:
        subprocess.run(['yt-dlp', '--version'], capture_output=True, check=True)
        print("✅ yt-dlp installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        missing.append('yt-dlp (pip install yt-dlp)')
    
    # Check whisperx
    try:
        subprocess.run([sys.executable, '-m', 'whisperx', '--version'], 
                      capture_output=True, check=True)
        print("✅ whisperx installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        missing.append('whisperx (pip install whisperx)')
    
    if missing:
        print("\n❌ Missing dependencies:")
        for dep in missing:
            print(f"   - {dep}")
        sys.exit(1)
    
    print("\n✅ All dependencies available\n")
    sys.exit(0)

def download_audio(youtube_url, output_dir='.', audio_format='mp3', quality='best'):
    """Download audio from YouTube using yt-dlp"""
    print(f"\n📥 Downloading audio from: {youtube_url}")
    
    output_template = os.path.join(output_dir, '%(title)s.%(ext)s')
    
    cmd = [
        'yt-dlp',
        '-x',  # Extract audio
        '--audio-format', audio_format,
        '--audio-quality', quality,
        '-o', output_template,
        '--no-playlist',  # Single video only
        youtube_url
    ]
    
    print(f"Command: {' '.join(cmd)}")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        # Find the downloaded file
        for file in os.listdir(output_dir):
            if file.endswith(f'.{audio_format}') and os.path.getmtime(os.path.join(output_dir, file)) > time.time() - 60:
                return os.path.join(output_dir, file)
        
        # Fallback: find most recent audio file
        audio_files = [f for f in os.listdir(output_dir) if f.endswith(f'.{audio_format}')]
        if audio_files:
            return os.path.join(output_dir, max(audio_files, key=lambda x: os.path.getmtime(os.path.join(output_dir, x))))
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Download failed: {e}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        sys.exit(1)

def transcribe_audio(audio_file, model='tiny', language='it', compute_type='float32', 
                    device='cpu', output_dir='transcripts', output_format='txt'):
    """Transcribe audio file using WhisperX"""
    print(f"\n🎙️ Transcribing: {audio_file}")
    print(f"Model: {model} | Language: {language} | Device: {device}")
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    
    cmd = [
        sys.executable, '-m', 'whisperx',
        audio_file,
        '--model', model,
        '--language', language,
        '--compute_type', compute_type,
        '--device', device,
        '--output_dir', output_dir,
        '--output_format', output_format
    ]
    
    print(f"Command: {' '.join(cmd)}")
    print("\n⏳ This may take a while (especially on CPU)...\n")
    
    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        if result.stdout:
            print(result.stdout)
            
        # Find output file
        base_name = os.path.splitext(os.path.basename(audio_file))[0]
        output_file = os.path.join(output_dir, f"{base_name}.{output_format}")
        
        return output_file
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Transcription failed: {e}")
        if e.stderr:
            print(f"Error: {e.stderr}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(
        description='Download YouTube video and transcribe with WhisperX',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://www.youtube.com/watch?v=abc123
  %(prog)s https://youtu.be/abc123 --model base --language en
  %(prog)s https://youtube.com/live/abc123 --output-format srt
  %(prog)s --check-deps
        """
    )
    
    parser.add_argument('url', nargs='?', help='YouTube video URL')
    parser.add_argument('--model', default='tiny',
                       choices=['tiny', 'base', 'small', 'medium', 'large', 'large-v2', 'large-v3'],
                       help='Whisper model (default: tiny)')
    parser.add_argument('--language', default='it', help='Audio language (default: it)')
    parser.add_argument('--compute-type', default='float32',
                       choices=['float32', 'float16', 'int8'],
                       help='Compute type (default: float32)')
    parser.add_argument('--device', default='cpu',
                       choices=['cpu', 'cuda'],
                       help='Device to use (default: cpu)')
    parser.add_argument('--output-dir', default='transcripts',
                       help='Output directory (default: transcripts)')
    parser.add_argument('--output-format', default='txt',
                       choices=['txt', 'srt', 'vtt', 'json'],
                       help='Output format (default: txt)')
    parser.add_argument('--audio-format', default='mp3',
                       choices=['mp3', 'wav', 'm4a'],
                       help='Audio format for download (default: mp3)')
    parser.add_argument('--quality', default='128K',
                       help='Audio quality (default: 128K)')
    parser.add_argument('--keep-audio', action='store_true',
                       help='Keep downloaded audio file after transcription')
    parser.add_argument('--check-deps', action='store_true',
                       help='Only check dependencies and exit')
    
    args = parser.parse_args()
    
    # Check dependencies
    if args.check_deps or not args.url:
        check_dependencies()
    
    # Download audio
    audio_file = download_audio(
        args.url,
        output_dir='.',
        audio_format=args.audio_format,
        quality=args.quality
    )
    
    print(f"\n✅ Downloaded: {audio_file}")
    
    # Transcribe
    output_file = transcribe_audio(
        audio_file,
        model=args.model,
        language=args.language,
        compute_type=args.compute_type,
        device=args.device,
        output_dir=args.output_dir,
        output_format=args.output_format
    )
    
    print(f"\n✅ Transcription complete!")
    print(f"📄 Output: {output_file}")
    
    # Show preview
    if os.path.exists(output_file):
        print("\n📝 Preview (first 500 chars):")
        print("-" * 50)
        with open(output_file, 'r', encoding='utf-8') as f:
            print(f.read()[:500])
        print("-" * 50)
    
    # Cleanup
    if not args.keep_audio:
        print(f"\n🗑️ Cleaning up audio file: {audio_file}")
        os.remove(audio_file)

if __name__ == '__main__':
    main()
