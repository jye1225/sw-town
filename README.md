# SM TOWN

> 눈송이들의 취향이 만나는 곳

웹프로그래밍 1분반 팀 프로젝트입니다.
취향이 맞는 친구와 소모임을 찾고, 함께한 만남을 기록하는 대학생 소셜 플랫폼을 HTML과 CSS로 만듭니다.

**🔗 사이트 바로가기: <https://jye1225.github.io/sw-town/index.html>**

## 주요 화면

| 화면 | 바로가기 | 담당 |
| --- | --- | --- |
| 홈 | [index.html](https://jye1225.github.io/sw-town/index.html) | 해인 |
| 로그인 · 회원가입 | [login.html](https://jye1225.github.io/sw-town/login.html) · [signup.html](https://jye1225.github.io/sw-town/signup.html) | 해인 |
| 친구 찾기 · 목록 · 프로필 | [friend.html](https://jye1225.github.io/sw-town/friend.html) · [friends.html](https://jye1225.github.io/sw-town/friends.html) · [friend-profile.html](https://jye1225.github.io/sw-town/friend-profile.html) | 효원 |
| 소모임 목록 · 상세 | [group.html](https://jye1225.github.io/sw-town/group.html) · [group-detail.html](https://jye1225.github.io/sw-town/group-detail.html) | 예은 |
| 만남 기록 캘린더 | [calendar.html](https://jye1225.github.io/sw-town/calendar.html) | 해인 |
| 마이페이지 · 프로필 수정 · 시간표 | [mypage.html](https://jye1225.github.io/sw-town/mypage.html) · [profile-edit.html](https://jye1225.github.io/sw-town/profile-edit.html) · [timetable.html](https://jye1225.github.io/sw-town/timetable.html) | 예은 · 효원 |

화면별 연결 관계와 CSS 파일은 [사이트맵](docs/sitemap.md)에 정리되어 있습니다.

## 로컬에서 실행하기

패키지 설치나 빌드 과정은 없습니다.

```sh
git clone https://github.com/jye1225/sw-town.git
cd sw-town
```

**VS Code + Live Server (권장)**

1. `sw-town` 폴더를 VS Code에서 엽니다.
2. 권장 확장 프로그램 **Live Server**를 설치합니다.
3. `index.html`을 우클릭하고 **Open with Live Server**를 선택합니다.
4. `http://127.0.0.1:5500`에서 확인합니다.

**Python 사용 시**

```sh
python -m http.server 5500 --bind 127.0.0.1
```

`http://127.0.0.1:5500`을 열고, 종료할 때는 터미널에서 `Ctrl+C`를 누릅니다.

## 폴더 구조

```text
sw-town/
├── index.html              # 홈
├── login.html              # 로그인
├── signup.html             # 회원가입
├── friend.html             # 친구 찾기
├── friends.html            # 내 친구 목록
├── friend-profile.html     # 친구 프로필
├── group.html              # 소모임 목록
├── group-detail.html       # 소모임 상세
├── calendar.html           # 만남 기록 캘린더
├── mypage.html             # 마이페이지
├── profile-edit.html       # 프로필 수정
├── timetable.html          # 내 주간 시간표
├── css/
│   ├── common.css          # 공통 변수, 헤더, 푸터, 버튼 등
│   ├── index.css           # 홈
│   ├── auth.css            # 로그인 · 회원가입
│   ├── friend.css          # 친구 화면 · 시간표
│   ├── group.css           # 소모임 화면
│   ├── profile.css         # 마이페이지 · 프로필 수정
│   └── calendar.css        # 캘린더
├── js/                     # 추후 개발용, 현재 HTML에 연결하지 않음
├── images/
│   ├── main/               # 홈 카드 사진
│   ├── group/              # 소모임 일러스트
│   ├── memory/             # 캘린더 만남 기록 사진
│   ├── profile/            # 프로필 이미지
│   └── logo/
├── docs/
│   ├── planning.md         # 기획
│   └── sitemap.md          # 사이트맵
├── .vscode/                # 팀 공통 편집 · Live Server 설정
├── .editorconfig
├── .gitattributes
└── .gitignore
```

빈 이미지 폴더는 `.gitkeep`으로 Git에 보관합니다.

## 작성 규칙

- 파일명은 소문자와 하이픈을 사용합니다. 예: `friend-profile.html`
- UTF-8, LF 줄바꿈, 공백 2칸 들여쓰기를 사용합니다.
- CSS는 `common.css` → 화면 전용 CSS 순서로 연결합니다.
- 색상, 여백 등 공통 값은 `common.css`의 CSS 변수(`--color-*` 등)를 사용합니다.
- 헤더와 네비게이션은 모든 화면에 같은 마크업을 복사해 사용하고, 현재 화면 메뉴에만 `is-active`와 `aria-current="page"`를 붙입니다.
- 이미지와 페이지 경로는 상대 경로로 작성합니다.

## 협업 방법

팀원은 저장소의 collaborator로 초대받아야 push할 수 있습니다.
담당 작업 브랜치에서 작업한 뒤 Pull Request로 `main`에 합칩니다.

```sh
git switch main
git pull --ff-only origin main
git switch -c feature/작업-이름
# 담당 HTML과 CSS 수정 후
git add 수정한-파일
git commit -m "feat: 작업 내용"
git push -u origin feature/작업-이름
```

push한 뒤 GitHub에서 **Compare & pull request**를 눌러 PR을 만듭니다.

## 문서

- [기획](docs/planning.md): 프로젝트 소개, 팀 구성, 디자인 규칙, 개발 범위
- [사이트맵](docs/sitemap.md): 화면 목록, 화면 간 이동, CSS 연결
