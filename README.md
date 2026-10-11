# Park Jiwoo — AI / ML Portfolio

박지우의 컴퓨터 비전 연구와 서비스 개발 포트폴리오입니다.

**Website:** https://jiwoo1105.github.io/jiwoo-portfolio/

## 구성

- 흰색 본문, 첫 화면을 채우는 사진과 크기를 줄인 움직이는 이름
- 대표 4개: 축구 드리블 분석, 로봇학습데이터 구축 파이프라인, 단짠, Conquer Health
- Other projects: 넙치 증상 탐지, MedGuard, MedAI Agent의 실제 대표 화면·영상
- 넙치 증상 탐지 상세 페이지와 추가 프로젝트 링크
- 실제 모델 출력 영상과 서비스 시연, 팀 수상 증빙
- 화면에 보이는 미리보기만 무음 반복 재생. 개별 재생·정지와 전체 애니메이션 정지, 백그라운드 탭·화면 이탈 시 정지
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
- [로봇학습데이터 구축 파이프라인](https://github.com/DKU-AIM/video-motion-pipeline): 그라운딩·추적·복원 실행과 검수 기록. 공개 시연은 ETRI 제공 농구 영상을 쓰지 않고, [Molmo 공개 농구 데모](https://storage.googleapis.com/oe-training-public/demo_videos/arena_basketball.mp4)의 첫 8초에 CoMotion을 새로 실행해 만들었습니다. 12.5fps, 100프레임, 무음. 모델 출력 자세·체형·이동 파라미터를 프레임별 SMPL 인체 메쉬(6,890 정점)로 복원한 시각화이며 실제 로봇 전이나 자세 정확도 평가 결과가 아닙니다. 입력 영상의 권리는 원저작자에게 있습니다.
- [Conquer Health](https://github.com/Hackathon-AIM/health-conquer-submission): 개인 MCP 구현 커밋, 성능 기록, 루닛 발급 AIM 팀 상장. 최종 46.51점과 순위는 팀 성과입니다. 특정 MCP 변경만의 인과적 개선으로 표시하지 않았습니다.
- [단짠](https://github.com/DKU-Dan-Zzan): 팀 실제 화면과 지우의 기존 자료. Redis/Lua·JWT·번역은 본인 기여, Kafka/DB 비동기 처리는 팀원 기여로 구분했습니다. 티켓팅 OFF 화면은 FE PR #121 / BE PR #75 로컬 검증 캡처입니다.
- [팀 공개 포트폴리오](https://juhee0223.github.io/juhee-portfolio/): 공동 서비스 화면과 운영·해커톤 최종 평가 수치의 보조 출처입니다.
- [넙치 증상 탐지](https://github.com/jiwoo1105/fish-disease-detection): 기존 포트폴리오의 실제 Flutter 앱과 저장된 모델 검증 이미지. 분류 Top-1 87.68%와 탐지 mAP50 0.4455를 다른 과제의 지표로 구분했습니다.

## 사진과 디자인

메인 사진은 사용자가 제공한 5568×4872 원본을 3600px / 1600px 웹용으로 최적화한 것입니다. 별도로 만든 AI 보정 시안보다 원본의 실제 디테일이 높아 사이트에는 원본 계열을 사용했습니다. 인물과 배경을 새로 생성하지 않았습니다.

디자인 방향은 [Dennis Snellenberg](https://dennissnellenberg.com/)의 큰 사진·타이포그래피·여백·움직임과 사용자가 지정한 흰색 배경, 사각형 프로젝트 구성을 참고했습니다. 해당 사이트의 소스 코드나 인물 사진은 사용하지 않았습니다.

폰트: [Pretendard](https://github.com/orioncactus/pretendard), SIL Open Font License. 라이선스는 `assets/Pretendard-LICENSE.txt`에 포함했습니다.

2026-10-09 프로젝트 구성 수정: [Kaixin Chai의 프로젝트 목록](https://cckaixin.github.io/myWebsite/)에서 영상과 설명을 나란히 읽는 구조를 참고했습니다. MedGuard 시연은 본인의 공개 AISecurity 저장소 `assets/demo.mp4`, MedAI 시연은 공개 MedAI_Agent 저장소 `demo/시현영상.mov`의 10–28초를 무음 H.264로 변환한 클립입니다.

2026-10-11 수정: 단짠을 대표 프로젝트로 승격했습니다. 실사용자 6,000명 이상·티켓팅 동시접속 약 4,000명은 운영자 박지우가 제공한 운영 규모이며 부하 테스트의 가상 사용자 수와 구분합니다. 기존 가입자 집계 6,063명 및 PPT의 동접 약 4,500명과 별개로 최신 사용자 확인에 맞춰 보수적으로 표기했습니다. 총학생회 협업과 네이버 Face Sign 연계는 기존 포트폴리오와 서비스 역할 구분 기록에 근거합니다.

축구 시연은 기준1 영상 239프레임과 기존 YOLO11s 발목 ROI 추론 캐시를 프레임별로 연결했습니다. 기존 후보 선택 함수의 실제 검출값만 공 박스와 16프레임 궤적으로 표시하며, 미검출 프레임에는 보간하지 않습니다. 자세 평가 방식을 새로 바꾼 작업은 아닙니다.

자격 및 교육: SQLD 취득일은 기존 박지우 포트폴리오의 2025.06.27 기록, AWS 교육명과 수료일은 본인 수료증 2개를 확인했습니다. AWS 항목은 교육 수료이며 AWS Certification 자격증으로 표시하지 않습니다. Conquer Health의 벤치마크 1위는 최종 평가 순위, 정식 상장 명칭은 벤치마크상이며 AIM 팀 공동 성과입니다.
