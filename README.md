# 🤖 Jarvis Trading Dashboard

실시간 트레이딩 대시보드 - 불멍 모드 🔥

## ✨ Features

- 🎨 실시간 워드 클라우드 (거래 시각화)
- 🔊 효과음 (상승: 굿/좋아, 하락: 억/윽)
- 💰 오늘/누적 손익 표시
- 📊 최근 거래 내역
- 🎁 빗썸 추천인 코드/링크
- 📱 반응형 (모바일 완벽 지원)

## 🚀 Quick Start

### 로컬 실행
```bash
# 브라우저에서 index.html 열기
open index.html
```

### Netlify 배포
```
1. https://app.netlify.com/drop 접속
2. 이 폴더를 드래그 앤 드롭
3. 완료! 즉시 URL 생성됨
```

### Vercel 배포
```bash
npm install -g vercel
vercel
```

## ⚙️ 커스터마이징

### 추천인 코드 변경
`index.html` 파일 열어서 수정:
```javascript
referralCode: 'JJCDWMIYMV'
referralLink: 'https://www.bithumb.com/react/JJCDWMIYMV'
```

### 효과음 변경
```javascript
const profitSounds = ['굿!', '좋아!', ...];  // 원하는 단어 추가
const lossSounds = ['억!', '윽!', ...];
```

## 📝 Note

현재는 시뮬레이션 모드로 작동합니다.
실제 봇 데이터와 연동하려면 DEPLOYMENT_GUIDE.md를 참고하세요.

## 🎉 Enjoy!

거래할수록 똑똑해지는 AI 트레이딩 봇과 함께
불멍하듯 대시보드를 즐기세요! 🔥

---

Powered by Jarvis ML Agent 🤖
