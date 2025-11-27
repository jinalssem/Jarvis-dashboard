#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 자동 업로드 스크립트
dashboard_data.json을 GitHub에 자동으로 푸시
"""

import os
import subprocess
import shutil
from datetime import datetime
from pathlib import Path

# ===== 설정 =====
DASHBOARD_DATA_SOURCE = 'D:/ML_Agentl/jarvis-dashboard/dashboard_data.json'
DASHBOARD_DATA_DEST = 'dashboard_data.json'
GIT_USER_NAME = 'Jarvis Bot'
GIT_USER_EMAIL = 'bot@jarvis.com'
# ==============

def log(message):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] {message}")

def check_git_repo():
    if not os.path.exists('.git'):
        log("❌ Error: Not a git repository!")
        return False
    return True

def copy_data_file():
    try:
        source = Path(DASHBOARD_DATA_SOURCE)
        dest = Path(DASHBOARD_DATA_DEST)
        
        if not source.exists():
            log(f"⏳ Source file not found: {source}")
            log("   Waiting for trading bot to create data...")
            return False
        
        shutil.copy2(source, dest)
        log(f"✅ Copied: {source} → {dest}")
        return True
        
    except Exception as e:
        log(f"❌ Error copying file: {e}")
        return False

def git_push():
    try:
        subprocess.run(['git', 'config', 'user.name', GIT_USER_NAME], check=True)
        subprocess.run(['git', 'config', 'user.email', GIT_USER_EMAIL], check=True)
        
        subprocess.run(['git', 'add', DASHBOARD_DATA_DEST], check=True)
        
        result = subprocess.run(['git', 'status', '--porcelain'], 
                              capture_output=True, text=True, check=True)
        
        if not result.stdout.strip():
            log("ℹ️  No changes to commit")
            return True
        
        commit_msg = f"Update trading data - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        subprocess.run(['git', 'commit', '-m', commit_msg], check=True)
        log(f"✅ Committed: {commit_msg}")
        
        subprocess.run(['git', 'push'], capture_output=True, text=True, check=True)
        log("✅ Successfully pushed to GitHub!")
        
        return True
        
    except subprocess.CalledProcessError as e:
        log(f"❌ Git error: {e}")
        return False
    except Exception as e:
        log(f"❌ Unexpected error: {e}")
        return False

def main():
    log("=" * 60)
    log("🚀 GitHub Auto Upload - Starting...")
    log("=" * 60)
    
    if not check_git_repo():
        return
    
    if not copy_data_file():
        log("⏭️  Skipping upload - no data file")
        return
    
    if git_push():
        log("=" * 60)
        log("🎉 Upload completed successfully!")
        log("=" * 60)
    else:
        log("=" * 60)
        log("❌ Upload failed")
        log("=" * 60)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log("\n⏹️  Interrupted by user")
    except Exception as e:
        log(f"❌ Fatal error: {e}")
