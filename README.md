# SW Town

웹프로그래밍 1분반 팀프로젝트

## 시작하기

```sh
git clone https://github.com/jye1225/sw-town.git
cd sw-town
```

`index.html`을 브라우저에서 열면 페이지 목록을 볼 수 있습니다.
패키지 설치나 빌드 과정은 없습니다.

### VS Code에서 실행

1. `sw-town` 폴더 자체를 VS Code에서 엽니다.
2. 권장 확장 프로그램인 **Live Server**를 설치합니다.
3. `index.html`을 우클릭하고 **Open with Live Server**를 선택합니다.
4. `http://127.0.0.1:5500`에서 확인합니다.

Live Server 없이 Python이 설치된 환경에서도 실행할 수 있습니다.

```sh
python -m http.server 5500 --bind 127.0.0.1
```

프로젝트 폴더에서 실행한 뒤 `http://127.0.0.1:5500`을 엽니다.
서버 종료는 터미널에서 `Ctrl+C`를 누릅니다.

## 폴더 구조

```text
sw-town/
├── index.html
├── login.html
├── signup.html
├── friend.html
├── friend-profile.html
├── friends.html
├── group.html
├── group-detail.html
├── mypage.html
├── profile-edit.html
├── calendar.html
├── css/
│   ├── reset.css
│   ├── common.css
│   ├── home.css
│   ├── auth.css
│   ├── friend.css
│   ├── group.css
│   ├── profile.css
│   └── calendar.css
├── js/                         # 추후 개발용, 현재 HTML에 연결하지 않음
│   ├── friend.js
│   └── calendar.js
├── images/
│   ├── logo/
│   ├── profile/
│   ├── group/
│   └── memory/
├── docs/
│   ├── planning.md
│   └── sitemap.md
├── .vscode/                    # 팀 공통 편집·Live Server 설정
├── .editorconfig
├── .gitattributes
├── .gitignore
└── README.md
```

빈 이미지 폴더는 `.gitkeep`으로 Git에 보관합니다.

## 작성 규칙

- 파일명은 소문자와 하이픈(`friend-profile.html`)을 사용합니다.
- UTF-8, LF 줄바꿈, 공백 2칸 들여쓰기를 사용합니다.
- 공통 스타일은 `css/common.css`, 화면별 스타일은 해당 전용 CSS에 작성합니다.
- CSS는 `reset.css` → `common.css` → 전용 CSS 순서로 연결합니다.
- 이미지와 페이지 경로는 상대 경로로 작성합니다.
- 중간 제출까지 `<script>`와 인라인 JavaScript를 추가하지 않습니다.

## 협업 시작

팀원은 저장소의 collaborator로 초대받아야 직접 push할 수 있습니다.
각자 담당 작업 브랜치에서 작업한 뒤 Pull Request로 `main`에 합칩니다.

```sh
git switch main
git pull --ff-only origin main
git switch -c feature/login-layout
# 담당 HTML과 CSS 수정 후
git add login.html css/auth.css
git commit -m "feat: 로그인 화면 마크업과 스타일 추가"
git push -u origin feature/login-layout
```

작업 브랜치명과 파일명은 담당 화면에 맞게 바꿉니다.

## 문서

- [기획 정리](docs/planning.md)
- [사이트맵 및 CSS 연결](docs/sitemap.md)
