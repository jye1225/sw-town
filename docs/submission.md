# 16팀 SM TOWN 제출 준비

GitHub Pages용 파일명은 유지하고, 제출용 폴더에서만 이름과 연결 경로를 변환합니다.

- HTML: `16_SMTOWN_index.html`, `16_SMTOWN_friend-profile.html` 등
- 이미지: `16_find-friend.jpg`, `16_snow-avatar.jpg` 등. 원본을 실제 JPEG로 변환하며 확장자만 바꾸지 않습니다.
- 포함: 연결된 HTML/CSS, JPEG 이미지, 수행계획서 PDF. 로컬 폰트 원본 바이트와 출처는 CSS 안에 포함해 오프라인에서도 표시합니다.
- 제외: `.git`, `.vscode`, 개발 문서, 스크립트 폴더, 미사용 CSS, `.gitkeep`
- 압축 해제 후 시작 파일: `16_SMTOWN_index.html`

## 패키지 다시 만들기

Python 3, Node.js와 이미지 변환용 `sharp`를 사용하는 개발 도구입니다. 웹사이트 실행에는 설치가 필요 없습니다.
기존 sharp 설치를 사용하는 경우 `SHARP_MODULE` 환경 변수에 해당 모듈의 절대 경로를 지정할 수 있습니다.

```sh
python scripts/prepare-submission.py --team-number 16 --team-name SMTOWN --plan-pdf output/pdf/16_SMTOWN_수행계획서_초안.pdf
```

결과는 Git에서 제외된 `output/submission/`에 만들어집니다. 기존 결과는 덮어쓰지 않습니다.

## 현재 구현 범위

- 로그인·회원가입도 JavaScript 없이 HTML 폼 이동과 CSS :target(가입 완료 화면)으로 동작합니다.
- 친구 카드 선택, 친구별 프로필, 공강 비교, 9~11월 캘린더의 월/날짜 전환은 HTML/CSS로 동작합니다.
- 소모임 참여는 접을 수 있는 안내로 제공하며 신청 기록을 저장하지 않습니다.
- 프로필 입력 확인은 현재 입력 화면을 유지하는 안내입니다. 서버 저장과 사진 미리보기 기능은 포함하지 않습니다.
- 수행계획서 PDF는 현재 저장소 기획과 알려진 담당 정보를 정리한 초안입니다. 수업에서 별도 양식을 요구하면 그 양식에 맞춰 제출합니다.
