# Park Jiwoo — AI / ML Portfolio

박지우의 컴퓨터 비전 연구와 서비스 개발 포트폴리오입니다.

**Website:** https://jiwoo1105.github.io/jiwoo-portfolio/

## 구성

- 흰색 캔버스, 사진 중심 인트로와 움직이는 이름
- 축구 드리블 분석, 영상 기반 3D 모션, Conquer Health, 단짠의 대표 카드
- 넙치 증상 탐지 상세 페이지와 추가 프로젝트 링크
- 실제 연구 출력 영상 3개, 장면 이동 버튼, 서비스 캡처와 팀 수상 증빙
- 모바일 메뉴, 모션 정지, reduced-motion 대응, 이메일 복사

별도의 빌드나 패키지 설치 없이 동작하는 HTML/CSS/JavaScript 사이트입니다.

## 수정과 배포

`index.html`에서 소개·프로젝트 순서를, `projects/*.html`에서 사례 설명을 수정합니다. 공통 디자인은 `assets/site.css`, 상호작용은 `assets/site.js`에 있습니다. 모든 내부 경로는 상대 경로여서 GitHub Pages 저장소 하위 경로에서 동작합니다.

`main`에 push하면 `.github/workflows/pages.yml`이 GitHub Pages로 배포합니다. 저장소 Settings → Pages → Source는 **GitHub Actions**입니다.

단순 로컬 확인:

```sh
python3 -m http.server 8765
```

영상의 특정 시점 이동까지 검증하려면 HTTP Range 요청을 지원하는 서버 또는 실제 GitHub Pages를 사용하세요. Python 기본 서버에서는 일부 브라우저의 영상 탐색이 제한될 수 있습니다.

## 내용과 미디어 출처

개인 기여는 박지우의 기존 포트폴리오, 본인의 공개 커밋과 프로젝트 검증 기록에 근거합니다. 공동 성과는 각 페이지에 팀 성과로 표시했습니다. 개인 지원서 원문, 대화 내역, 비공개 저장소 코드와 서버 접속 정보는 이 저장소에 포함하지 않습니다.

- [축구 드리블 분석](https://github.com/jiwoo1105/soccer_motion_analysis): 관절·터치 후보 출력 영상과 원본 프레임 검수. 2026-10-09 기준 어깨 평균 방향 변화 속도 방식의 해석과 한계를 반영했습니다. 예전 추적 영상의 수치는 현재 채점 성능 주장이 아닙니다.
- [영상 모션 파이프라인](https://github.com/DKU-AIM/video-motion-pipeline): CoMotion / Multi-HMR 2 인물 추적 비교, 스포츠 그라운딩의 실제 평가 입력과 3D 복원 예시. 그라운딩 시간 라벨은 검토용 초안이며 공식 정답이 아닙니다. 공개한 짧은 영상은 연구 내용을 설명하는 예시입니다. 입력 영상의 권리는 원저작자에게 있습니다.
- [Conquer Health](https://github.com/Hackathon-AIM/health-conquer-submission): 개인 MCP 구현 커밋, 성능 기록, 루닛 발급 AIM 팀 상장. 최종 46.51점과 순위는 팀 성과입니다. 특정 MCP 변경만의 인과적 개선으로 표시하지 않았습니다.
- [단짠](https://github.com/DKU-Dan-Zzan): 팀 실제 화면과 지우의 기존 자료. Redis/Lua·JWT·번역은 본인 기여, Kafka/DB 비동기 처리는 팀원 기여로 구분했습니다. 티켓팅 OFF 화면은 FE PR #121 / BE PR #75 로컬 검증 캡처입니다.
- [팀 공개 포트폴리오](https://juhee0223.github.io/juhee-portfolio/): 공동 서비스 화면과 운영·해커톤 최종 평가 수치의 보조 출처입니다.
- [넙치 증상 탐지](https://github.com/jiwoo1105/fish-disease-detection): 기존 포트폴리오의 실제 Flutter 앱과 저장된 모델 검증 이미지. 분류 Top-1 87.68%와 탐지 mAP50 0.4455를 다른 과제의 지표로 구분했습니다.

## 사진과 디자인

메인 사진은 사용자가 제공한 5568×4872 원본을 3600px / 1600px 웹용으로 최적화한 것입니다. 별도로 만든 AI 보정 시안보다 원본의 실제 디테일이 높아 사이트에는 원본 계열을 사용했습니다. 인물과 배경을 새로 생성하지 않았습니다.

디자인 방향은 [Dennis Snellenberg](https://dennissnellenberg.com/)의 큰 사진·타이포그래피·여백·움직임과 사용자가 지정한 흰색 배경, 사각형 프로젝트 구성을 참고했습니다. 해당 사이트의 소스 코드나 인물 사진은 사용하지 않았습니다.

폰트: [Pretendard](https://github.com/orioncactus/pretendard), SIL Open Font License. 라이선스는 `assets/Pretendard-LICENSE.txt`에 포함했습니다.
