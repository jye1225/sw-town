# SM TOWN 사이트맵

## 화면 목록

| 화면 | HTML | CSS | 담당 |
| --- | --- | --- | --- |
| 홈 | `index.html` | `common.css` · `index.css` | 해인 |
| 로그인 | `login.html` | `common.css` · `auth.css` | 해인 |
| 회원가입 | `signup.html` | `common.css` · `auth.css` | 해인 |
| 친구 찾기 | `friend.html` | `common.css` · `friend.css` | 효원 |
| 내 친구 목록 | `friends.html` | `common.css` · `friend.css` | 효원 |
| 친구 프로필 | `friend-profile.html` | `common.css` · `profile.css` · `friend.css` | 효원 |
| 소모임 목록 | `group.html` | `common.css` · `group.css` | 예은 |
| 소모임 상세 | `group-detail.html` | `common.css` · `group.css` | 예은 |
| 만남 기록 캘린더 | `calendar.html` | `common.css` · `calendar.css` | 해인 |
| 마이페이지 | `mypage.html` | `common.css` · `profile.css` | 예은 |
| 프로필 수정 | `profile-edit.html` | `common.css` · `profile.css` | 예은 |
| 친구와 공강 맞추기 | `timetable.html` | `common.css` · `friend.css` | 효원 |

## 화면 구조

```text
홈 (index.html)
├── 친구 찾기 (friend.html)
│   ├── 내 친구 목록 (friends.html)
│   │   └── 친구 프로필 (friend-profile.html)
│   └── 친구 프로필 (friend-profile.html)
├── 소모임 목록 (group.html)
│   └── 소모임 상세 (group-detail.html#모임-id)
├── 만남 기록 캘린더 (calendar.html)
├── 마이페이지 (mypage.html)
│   ├── 프로필 수정 (profile-edit.html)
│   ├── 내 친구 목록 (friends.html)
│   ├── 만남 기록 캘린더 (calendar.html)
│   └── 참여 중인 소모임 (group-detail.html#모임-id)
└── 로그인 (login.html) ⇄ 회원가입 (signup.html)
```

## 공통 네비게이션

로그인 · 회원가입을 제외한 모든 화면의 헤더에 같은 메뉴가 있습니다.

| 메뉴 | 이동 화면 |
| --- | --- |
| 로고 `SM TOWN.` | `index.html` |
| HOME | `index.html` |
| FRIEND | `friend.html` |
| GROUP | `group.html` |
| CALENDAR | `calendar.html` |
| MY PAGE | `mypage.html` |
| 프로필 버튼 | `login.html` |

로그인 · 회원가입 화면의 헤더에는 홈으로 가는 로고만 있습니다.

## 화면 이동 흐름

| 시작 화면 | 동작 | 이동 화면 |
| --- | --- | --- |
| 홈 | 친구 찾기 카드 | `friend.html` |
| 홈 | 소모임 찾기 카드 | `group.html` |
| 홈 | 회원가입하기 링크 | `signup.html` |
| 로그인 | 로그인 버튼 | `mypage.html` (실제 인증 없음) |
| 회원가입 | 회원가입 버튼 | 가입 완료 화면(`signup.html#signup-complete`) → 프로필 수정 또는 `index.html` (실제 가입 없음) |
| 친구 찾기 | 하트 버튼 | `friend-profile.html` |
| 내 친구 목록 | 친구 카드 | `friend-profile.html` |
| 소모임 목록 | 모임 카드 | `group-detail.html#baseball` 등 모임별 주소 |
| 마이페이지 | 프로필 수정 버튼 | `profile-edit.html` |

소모임 상세는 한 페이지에 모든 모임이 들어 있습니다.
주소 뒤의 `#baseball`, `#reading`, `#cafe`, `#exhibition`, `#photo`, `#walk`에 따라 해당 모임만 보여 줍니다.

## HTML/CSS로 전환하는 상세 화면

- 친구 프로필: `#flower`, `#star`, `#moon`, `#spring`
- 공강 비교: `#with-flower`, `#with-star`, `#with-moon`, `#with-spring`
- 캘린더: `#month-09`, `#month-10`, `#month-11` 및 `#record-1010` 등 날짜별 기록
- 프로필 입력 확인: `profile-edit.html#profile-review`
