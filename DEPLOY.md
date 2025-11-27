# 🚀 배포 가이드 - 3분 안에 완료!

## 📦 준비된 파일들

폴더 안에 다음 파일들이 있습니다:
```
jarvis-dashboard/
├── index.html       # 메인 대시보드
├── README.md        # 설명서
└── netlify.toml     # Netlify 설정
```

---

## 🎯 배포 방법 (선택하세요!)

### 방법 1️⃣: Netlify Drop (가장 쉬움! ⭐⭐⭐⭐⭐)

**1단계: 사이트 접속**
```
https://app.netlify.com/drop
```

**2단계: 폴더 드래그**
```
jarvis-dashboard 폴더 전체를
브라우저 창에 드래그 앤 드롭!
```

**완료!** 
```
✅ 즉시 배포 완료!
🌐 URL: https://random-name-123.netlify.app

→ 이 URL을 북마크하거나 공유하세요!
```

**소요 시간: 30초** ⚡

---

### 방법 2️⃣: Vercel (빠르고 전문적! ⭐⭐⭐⭐)

**1단계: Vercel CLI 설치**
```bash
npm install -g vercel
```

**2단계: 배포**
```bash
cd jarvis-dashboard
vercel
```

**3단계: 질문에 답변**
```
? Set up and deploy? Y
? Which scope? (본인 계정)
? Link to existing project? N
? Project name? jarvis-dashboard
? Directory? ./
? Override settings? N
```

**완료!**
```
✅ 배포 완료!
🌐 URL: https://jarvis-dashboard.vercel.app
```

**소요 시간: 2분** ⚡

---

### 방법 3️⃣: GitHub Pages (영구 무료! ⭐⭐⭐⭐)

**1단계: GitHub 저장소 생성**
```
https://github.com/new
Repository name: jarvis-dashboard
Public
Create repository
```

**2단계: 파일 업로드**
```bash
cd jarvis-dashboard
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/jarvis-dashboard.git
git push -u origin main
```

**3단계: GitHub Pages 활성화**
```
Settings → Pages
Source: Deploy from a branch
Branch: main / (root)
Save
```

**완료!**
```
✅ 배포 완료!
🌐 URL: https://YOUR_USERNAME.github.io/jarvis-dashboard/
```

**소요 시간: 3분** ⚡

---

## ⚙️ 배포 전 커스터마이징 (선택사항)

### 추천인 코드 변경

`index.html` 파일을 텍스트 에디터로 열고:

```javascript
// 이 부분을 찾아서 수정
let state = {
    // ...
    referralCode: 'ABC123XYZ',  // ← 여기에 실제 코드 입력
    referralLink: 'https://www.bithumb.com/react/member/join/ABC123XYZ'  // ← 여기도 수정
};
```

저장 후 배포하세요!

---

## 📱 배포 후 확인사항

### ✅ 체크리스트

- [ ] 브라우저에서 URL 접속
- [ ] 워드 클라우드 움직이는지 확인
- [ ] 효과음 작동하는지 확인 (상승/하락)
- [ ] 손익 표시되는지 확인
- [ ] 추천인 코드 복사 버튼 테스트
- [ ] 추천인 링크 복사 버튼 테스트
- [ ] 모바일에서 접속 테스트

### 📱 모바일 테스트

```
1. 스마트폰 브라우저에서 URL 접속
2. 화면이 잘 보이는지 확인
3. 홈 화면에 추가 (선택사항)
4. 언제든지 확인 가능!
```

---

## 🎨 미리보기

배포하면 이런 화면이 나타납니다:

```
┌───────────────────────────────────────┐
│  🤖 Jarvis Trading Bot                │
│  실시간 거래 대시보드 - 불멍 모드 🔥  │
├───────────────────────────────────────┤
│                                       │
│    [워드 클라우드 - 움직이는 단어들]  │
│  BTC 매수! 굿! ETH 상승! 좋아!        │
│     XRP 하락 억! DOGE 악!             │
│                                       │
├───────────────────────────────────────┤
│ 💰 오늘 손익: +125,430원 (+2.3%)     │
│ 📈 누적 손익: +1,234,567원 (+15.2%)  │
├───────────────────────────────────────┤
│ 📊 최근 거래                          │
│ 14:32:15  BTC  매수  +12,345원       │
├───────────────────────────────────────┤
│ 🎁 빗썸 친구 초대                     │
│ 추천인 코드: ABC123XYZ  [복사]       │
│ [🔗 초대 링크 복사]                   │
└───────────────────────────────────────┘
```

---

## 🔧 문제 해결

### Q: Netlify Drop에서 에러가 나요
**A:** 폴더 전체를 드래그하세요 (index.html 파일만이 아니라!)

### Q: URL이 이상한 이름이에요
**A:** Netlify 대시보드에서 Site settings → Change site name

### Q: 효과음이 안 나와요
**A:** 브라우저 설정 → 사이트 권한 → 음성 합성 허용

### Q: 모바일에서 레이아웃이 깨져요
**A:** 인터넷 연결 확인 (Tailwind CDN 로드 필요)

---

## 🎉 완료!

이제 다음을 즐기세요:

- ✅ 언제 어디서나 접속
- ✅ 친구들에게 자랑
- ✅ 불멍하듯 감상
- ✅ 모바일에서도 확인
- ✅ 추천인 링크 공유

---

## 📞 추가 도움말

더 자세한 정보가 필요하면:
- Netlify 문서: https://docs.netlify.com
- Vercel 문서: https://vercel.com/docs
- GitHub Pages: https://pages.github.com

---

**축하합니다!** 🎊
당신만의 트레이딩 대시보드가 온라인에 올라갑니다!

이제 불멍을 시작하세요! 🔥
