#!/bin/bash
# Dashboard 자동 업로드 - 10분마다 반복

echo "🔄 자동 업로드 시작 (10분 간격)"
echo "Ctrl+C로 중지"
echo ""

count=0

while true; do
    count=$((count + 1))
    echo "=========================================="
    echo "[#$count] $(date '+%Y-%m-%d %H:%M:%S')"
    echo "=========================================="
    
    # 저장소 경로로 이동
    cd /d/jarvis-dashboard-web
    
    # 변경사항 확인
    if ! git diff --quiet dashboard_data.json; then
        echo "📤 변경사항 발견 - Git 업로드 시작..."
        
        # Git add
        git add dashboard_data.json
        
        # Git commit
        git commit -m "🤖 자동 업데이트 $(date '+%Y-%m-%d %H:%M:%S')"
        
        # Git push
        git push origin main
        
        if [ $? -eq 0 ]; then
            echo "✅ 업로드 성공!"
        else
            echo "❌ 업로드 실패!"
        fi
    else
        echo "ℹ️  변경사항 없음 - 업로드 생략"
    fi
    
    echo ""
    echo "⏰ 30초 대기 중..."
    echo ""
    
    sleep 30  # 30초마다
done
