"""Reviewed bilingual content. Regenerate the static site with scripts/build.py."""

# Verified against project chats, implementation and commits on 2026-11-03.
TECHNOLOGIES = [
 {'title': {'ko': '비전·3D 모션', 'en': 'Vision & 3D motion'},
  'tags': ['Python', 'PyTorch', 'OpenCV', 'PHALP', 'HMR 2.0 · SMPL', 'MediaPipe', 'YOLOv8 · SAM2', 'NumPy · SciPy'],
  'description': {'ko': '사전학습 모델을 연결해 인물·공을 추적하고, 3D 모션과 터치 구간 지표를 계산합니다.',
                  'en': 'I integrate pretrained models to track people and balls, reconstruct 3D motion, and compute touch-window metrics.'},
  'links': [('video-motion', {'ko': '로봇 데이터 파이프라인', 'en': 'Motion data pipeline'}), ('soccer-analysis', {'ko': '축구 드리블 분석', 'en': 'Dribbling analysis'})]},
 {'title': {'ko': 'LLM 응용·실험', 'en': 'LLM applications'},
  'tags': ['Python', 'FastAPI', 'MCP', 'Transformers'],
  'description': {'ko': 'MCP로 조회한 문서를 모델 입력에 전달하고, 출력 예산·응답 흐름을 실험합니다. 영상 모델의 입력과 결과도 같은 조건으로 비교합니다.',
                  'en': 'I pass documents retrieved through MCP into model inputs and test output budgets and response flows. I also compare video models under consistent conditions.'},
  'links': [('conquer-health', 'Conquer Health'), ('video-motion', {'ko': '영상 그라운딩 실험', 'en': 'Video grounding experiments'})]},
 {'title': {'ko': '서비스 개발', 'en': 'Service development'},
  'tags': ['Java · Spring Boot', 'Redis · Lua', 'Spring Security · JWT', 'MySQL · JPA', 'React · TypeScript'],
  'description': {'ko': '동시 예매와 인증 예외 처리를 구현하고, 관리자 설정·가입 화면을 연결합니다. 번역 실패 시 원문 제공과 후속 보정도 처리합니다.',
                  'en': 'I build concurrent ticketing and authentication error handling, connect admin settings and sign-up screens, and handle translation failures with source-text fallback and follow-up translation.'},
  'links': [('danzzan', {'ko': '단짠', 'en': 'Danzzan'})]}
]
COLLABORATION_TECH = ['Slack', 'Jira', 'Git · GitHub PR']

HOME = {'headline': {'ko': 'AI를 실제로 쓰이는<br>기능으로 만듭니다.', 'en': 'I build AI<br>people can use.'},
 'description': {'ko': '박지우의 AI / ML 포트폴리오. 컴퓨터 비전·3D 동작 분석, 의료 AI, 실제 서비스 개발 경험을 소개합니다.',
                 'en': 'Jiwoo Park’s AI/ML portfolio: computer vision, 3D motion analysis, medical AI, and real-world service '
                       'development.'},
 'about_title': {'ko': '동작하는 이유까지,<br>이해하며 만듭니다.', 'en': 'I build with an understanding<br>of how things work.'},
 'about': [{'ko': '컴퓨터 비전과 3D 동작 분석을 연구하는 AIV Lab 학부연구생 박지우입니다. 영상 속 움직임을 데이터로 해석하고, AI를 실제로 쓸 수 있는 기능으로 만드는 데 관심이 있습니다.',
            'en': 'I’m Jiwoo Park, an undergraduate researcher in the AIV Lab at Dankook University, working on computer vision and '
                  '3D motion analysis. I’m interested in turning movement in video into meaningful data and building AI features '
                  'people can use.'},
           {'ko': '코드가 왜 이렇게 동작하는지, 이 문제에 왜 이 설계가 필요한지 생각하며 개발합니다. 예상과 다른 결과가 나오면 입력 데이터와 처리 과정을 나눠 살펴보고, 실험과 로그로 원인을 확인합니다.',
            'en': 'As I build, I ask why the code behaves as it does and why a design fits the problem. When results differ from what '
                  'I expect, I examine the input data and each processing stage, using experiments and logs to investigate the '
                  'cause.'},
           {'ko': '컴퓨터 비전·의료 AI 연구와 축제 서비스 개발을 거치며, 연구에서는 결과의 근거를, 서비스에서는 사용자가 겪을 상황을 살피는 법을 배웠습니다. 선택한 방법을 설명할 수 있고, 팀과 함께 더 나은 답을 '
                  '찾아가는 AI 엔지니어가 되고자 합니다.',
            'en': 'Through computer vision and medical AI projects, as well as a festival service, I’ve learned to examine the '
                  'evidence behind research results and consider the situations users encounter. I aim to be an AI engineer who can '
                  'explain technical choices and work with a team to find better solutions.'}]}

SUMMARIES = {'soccer-analysis': {'ko': '선수와 공을 추적하고, 드리블 동작을 검수 가능한 지표로.',
                     'en': 'Tracking the player and ball to produce dribbling metrics that can be checked against the footage.'},
 'video-motion': {'ko': '영상의 움직임을 3D로 복원하고,<br>인물과 시간의 연결을 검수합니다.',
                  'en': 'Reconstructing 3D motion,<br>with checks on identity and timing.'},
 'danzzan': {'ko': '총학생회와 함께 운영한 대학 축제 서비스. 예매·인증·번역 백엔드를 담당했습니다.',
             'en': 'A university festival service operated with the student council. I built ticketing, authentication, and '
                   'translation features.'},
 'conquer-health': {'ko': '루닛 L2-preview의 의료 답변을 개선하며, MCP 근거 전달과 출력 예산을 실험했습니다.',
                    'en': 'I explored MCP evidence delivery and output budgets to improve medical responses from Lunit’s L2-preview.'},
 'fish-detection': {'ko': '넙치를 찾고, 개체별 외형 증상을 분류하는 앱.',
                    'en': 'An app that detects olive flounder and classifies each fish’s visible symptoms.'},
 'medguard': {'ko': '흉부 X-ray 모델의 적대적 공격과 방어를 비교한 실험.',
              'en': 'Experiments comparing adversarial attacks and defenses for a chest X-ray classifier.'},
 'medai-agent': {'ko': '약물 정보 조회와 8단계 LLM 분석을 연결한 프로토타입.',
                 'en': 'A prototype linking drug-information lookup with an eight-stage LLM workflow.'}}

FOCUS = {'soccer-analysis': {'ko': '평가 지표 설계 · 공 추적 검수', 'en': 'Metric design · Ball-tracking review'},
 'video-motion': {'ko': '파이프라인 전반 설계·구현 · 모델 연동·검수', 'en': 'Pipeline design and implementation · Model integration and review'},
 'danzzan': {'ko': 'Redis·Lua 예매 처리 · 인증·번역', 'en': 'Redis/Lua ticketing · Authentication and translation'},
 'conquer-health': {'ko': 'MCP 조회·본문 전달 · 출력 예산 실험', 'en': 'MCP evidence delivery · Output-budget experiments'}}

PROJECTS = [{'slug': 'video-motion',
  'title': {'ko': '로봇학습데이터 구축 파이프라인', 'en': 'A data pipeline for robot learning'},
  'category': {'ko': 'Video understanding · 연구', 'en': 'Video understanding · Research'},
  'subtitle': {'ko': '영상 속 움직임을, 출처와 품질을 확인할 수 있는 학습 데이터로.',
               'en': 'Turning motion in video into learning data with traceable sources and reviewable quality.'},
  'desc': {'ko': '인물 추적·크롭·3D 모션을 원본 시간과 ID로 연결하고, 캡셔닝과 로봇 추종까지 단계별로 검토한 연구 파이프라인입니다.',
           'en': 'A research pipeline aligning person tracks, crops and 3D motion by source time and identity, '
                 'with separate captioning and robot-tracking pilots.'},
  'role': {'ko': '파이프라인 전반 설계·구현 주도, 모델 연동·실험·결과 검수',
           'en': 'Led the overall pipeline design and implementation, including model integration, experiments, '
                 'and output review'},
  'period': {'ko': '2026.07– · 연구 진행 중', 'en': 'Since Jul 2026 · Ongoing research'},
  'context': {'ko': 'AIV Lab / ETRI 연구과제', 'en': 'AIV Lab / ETRI research project'},
  'affiliation': {'logo': 'brands/etri.svg',
                  'alt': 'ETRI 한국전자통신연구원',
                  'label': {'ko': '연구과제', 'en': 'Research project'},
                  'kind': 'etri'},
  'stack': 'Python / PyTorch / ViTDet-H / PHALP / HMR 2.0 / SMPL / MuJoCo',
  'repo': 'https://github.com/DKU-AIM/video-motion-pipeline',
  'caption': {'ko': '같은 6초의 선수 크롭 ↔ HMR 2.0 실제 출력 · 상세에서 단계별 시연',
              'en': 'The same six seconds: person crop ↔ actual HMR 2.0 output. Explore every stage in the case '
                    'study.'},
  'sections': [{'id': 'problem',
                'label': {'ko': '01 · 문제 정의', 'en': '01 · The problem'},
                'title': {'ko': '모델의 출력을 모으는 것만으로는 학습 데이터가 되지 않았습니다.',
                          'en': 'Model outputs alone were not a usable dataset.'},
                'paragraphs': [{'ko': '영상에서 행동 구간을 찾고 3D 모션과 설명을 묶으려면, 모든 결과가 같은 사람의 같은 순간을 가리켜야 합니다. 구간을 잘못 찾거나 '
                                      'ID가 바뀌면 그럴듯한 메쉬와 설명도 서로 다른 장면을 나타낼 수 있었습니다.',
                                'en': 'To pair action intervals with 3D motion and descriptions, every output '
                                      'must refer to the same person at the same moment. An incorrect interval or '
                                      'identity switch can pair plausible meshes and captions with the wrong '
                                      'scene.'},
                               {'ko': '저는 ETRI 연구과제에서 파이프라인 전반의 설계·구현을 주도했습니다. 먼저 7개 모델·5개 FPS·2개 영상·3개 쿼리의 210개 '
                                      '응답을 비교했습니다. FPS를 높여도 행동 누락과 넓은 구간 예측이 남아, 그라운딩 출력을 곧바로 정답으로 삼지 않는 방향으로 설계를 '
                                      '바꿨습니다.',
                                'en': 'I led the pipeline design and implementation within an ETRI research '
                                      'project. I first compared 210 responses across seven models, five FPS '
                                      'settings, two videos and three queries. Missed actions and overly broad '
                                      'intervals persisted at higher sampling rates, so I changed the design to '
                                      'avoid treating grounding outputs as labels.'}],
                'visual': {'caption': {'ko': '설계의 중심: 같은 사람 · 같은 시간',
                                       'en': 'Design principle: one person, one timeline'},
                           'flow': [({'ko': '원본 영상·시각', 'en': 'Source video & time'},
                                     {'ko': '모든 출력이 돌아갈 기준', 'en': 'The reference for every output'}),
                                    ({'ko': '인물 ID·선택 구간', 'en': 'Person ID & selected interval'},
                                     {'ko': '누락·ID 변경을 검수', 'en': 'Review gaps and identity changes'}),
                                    ({'ko': '크롭·3D 모션·설명', 'en': 'Crop, 3D motion & caption'},
                                     {'ko': '같은 구간의 결과를 대조', 'en': 'Compare outputs from the same interval'})]},
                'outcome': {'ko': '인물 ID와 원본 시간축을 먼저 보존하고, 각 단계의 결과를 대조할 수 있는 연결 구조를 만들었습니다.',
                            'en': 'The pipeline preserves person IDs and source times before linking outputs, '
                                  'making each stage traceable to the input.'},
                'insight': {'ko': '파이프라인의 핵심을 모델 수가 아니라 데이터 간 대응 관계로 정의했습니다. 이후 단계가 앞 단계의 오류를 숨기지 않도록 원본과 중간 결과를 '
                                  '함께 남겼습니다.',
                            'en': 'I began defining the pipeline by the alignment between its data, rather than '
                                  'the number of models. Keeping source footage and intermediate outputs made '
                                  'upstream errors visible.'}},
               {'id': 'pipeline',
                'label': {'ko': '02 · 데이터 연결', 'en': '02 · Connecting the data'},
                'title': {'ko': '크롭과 메쉬를 원본의 인물·프레임에 묶었습니다.',
                          'en': 'Linking each crop and mesh to its source person and frame.'},
                'paragraphs': [{'ko': '전체 화면의 ViTDet-H 검출과 HMR 2.0 추정을 PHALP가 연결해 인물 ID를 만듭니다. 저는 검수한 선수와 연속 구간을 '
                                      '선택하고, 박스 각 변에 10% 여백을 둔 크롭에 HMR 2.0을 다시 실행했습니다.',
                                'en': 'PHALP associates full-frame ViTDet-H detections and HMR 2.0 estimates into '
                                      'person tracks. I selected reviewed players and continuous intervals, added '
                                      'a 10% margin on each box edge, and reran HMR 2.0 on the crops.'},
                               {'ko': '원본 시각·프레임 번호·ID·크롭 좌표를 SMPL 결과와 함께 저장했습니다. 각 단계의 프레임 수와 FPS도 확인해, 이상한 메쉬를 '
                                      '발견하면 입력 구간까지 되짚을 수 있게 했습니다. 별도 공연 검수에서는 일시 누락과 타인에게 붙은 ID를 구분해 제외·보류 기준을 '
                                      '정리했습니다.',
                                'en': 'I stored source times, frame numbers, IDs and crop coordinates with the '
                                      'SMPL outputs, checking frame counts and FPS across stages. This made '
                                      'unusual meshes traceable to their inputs. In a separate performance-video '
                                      'review, I distinguished temporary gaps from wrong-person associations and '
                                      'defined exclusion and hold criteria.'}],
                'visual': {'video': 'evidence/motion-aligned.mp4',
                           'poster': 'motion/compare.jpg',
                           'caption': {'ko': '같은 선수의 RGB · HMR 메쉬 · MuJoCo 재생, 동일한 6초. 공개 FIBA 영상의 실제 출력입니다.',
                                       'en': 'RGB, HMR mesh and MuJoCo replay of the same player and six seconds. '
                                             'Actual outputs from public FIBA footage.'},
                           'wide': True},
                'outcome': {'ko': '선택한 선수 5명의 6구간에서 크롭·SMPL 파라미터·메쉬를 연결했습니다. 영상은 저장된 메쉬의 고정 루트 재생이며, 로봇의 균형 제어 '
                                  '시연과 구분합니다.',
                            'en': 'Crops, SMPL parameters and meshes are linked across six selected intervals '
                                  'from five players. This video replays saved meshes with a fixed root; it does '
                                  'not demonstrate robot balance control.'}},
               {'id': 'captioning',
                'label': {'ko': '03 · 행동 설명 검수', 'en': '03 · Reviewing descriptions'},
                'title': {'ko': '문장이 자연스러워도, 공을 가진 선수는 틀릴 수 있었습니다.',
                          'en': 'A fluent caption could still give the ball to the wrong player.'},
                'paragraphs': [{'ko': '검수한 모션에 행동 설명을 붙이기 위해 같은 6개 RGB 크롭을 4 FPS로 입력하고 Qwen·InternVL의 프롬프트 세 조건을 '
                                      '비교했습니다. 입력 프레임과 모델 버전을 고정하고 실제 요청·응답 36개를 보존했습니다.',
                                'en': 'To attach action descriptions to reviewed motion, I compared three prompt '
                                      'conditions for Qwen and InternVL using the same six RGB crops at 4 FPS. I '
                                      'kept input frames and model versions fixed and retained all 36 requests '
                                      'and responses.'},
                               {'ko': '행동을 명시적으로 질문해도 공이 없는 선수의 드리블을 설명하거나, 드리블 후반의 공 릴리스를 놓쳤습니다. 프롬프트를 바꾼 뒤 문장이 '
                                      '풍부해진 것과 행동을 더 정확하게 설명한 것을 따로 판단했습니다.',
                                'en': 'Even explicit action prompts could describe an off-ball player as '
                                      'dribbling or omit the late ball release. I evaluated richer wording '
                                      'separately from more accurate action descriptions.'}],
                'visual': {'images': [('evidence/motion-release.jpg',
                                       {'ko': '후반 릴리스 구간의 실제 검수 이미지. 응답 문장을 원본 장면과 대조했습니다.',
                                        'en': 'Actual review frames around the late release, used to check '
                                              'descriptions against the footage.'})]},
                'outcome': {'ko': '캡셔닝 비교는 완료했지만 자동 행동 정답의 품질은 확보하지 못했습니다. 최종 프롬프트 선택을 최고 정확도 달성으로 해석하지 않았습니다.',
                            'en': 'The comparison is complete, but reliable automatic action labels remain '
                                  'unresolved. Selecting a final prompt did not establish that it was the most '
                                  'accurate.'},
                'insight': {'ko': '생성 성공을 데이터 품질 승인과 분리했습니다. 학습 데이터에는 “설명 있음”보다 “누구의 어떤 행동을 실제로 설명하는가”를 확인하는 절차가 '
                                  '필요했습니다.',
                            'en': 'I separated successful generation from quality approval. For learning data, '
                                  'the relevant check is whose action a caption actually describes, not simply '
                                  'whether a caption exists.'}},
               {'id': 'simulation',
                'label': {'ko': '04 · 로봇 적용의 경계', 'en': '04 · Testing physical feasibility'},
                'title': {'ko': '메쉬는 재생됐지만, 전신을 따라가던 로봇은 넘어졌습니다.',
                          'en': 'The mesh replayed; the robot fell while tracking the full-body motion.'},
                'paragraphs': [{'ko': '저장된 SMPL을 GMR로 G1의 29관절에 매핑한 뒤 물리 시뮬레이션에서 추종을 시험했습니다. 초기 자세·속도·발 접촉을 확인하고, '
                                      '시작 시각 변경·초기 속도 제거·접촉 보정과 PPO 추가 학습을 비교했습니다.',
                                'en': 'I mapped the saved SMPL motion to G1’s 29 joints with GMR and tested '
                                      'tracking in physics simulation. I examined initial pose, velocity and foot '
                                      'contact, then compared start-time changes, removal of initial velocity, '
                                      'contact correction and additional PPO training.'},
                               {'ko': '접촉 보정 후 2,000회 학습한 전신 과제도 평가 10회 모두 실패했습니다. 원인을 좁히기 위해 하체·허리를 서 있는 목표로 바꾼 '
                                      '팔 중심 과제를 따로 평가했고, 같은 짧은 모션의 초기 교란 시험에서는 10회 모두 통과했습니다.',
                                'en': 'Full-body tracking still failed in all ten evaluations after contact '
                                      'correction and 2,000 training iterations. To narrow the failure, I tested '
                                      'an arm-focused task with standing targets for the lower body and waist. '
                                      'That restricted task passed all ten initial-perturbation trials on the '
                                      'same short motion.'}],
                'visual': {'video': 'evidence/g1-fullbody.mp4',
                           'poster': 'evidence/g1-fullbody.jpg',
                           'caption': {'ko': 'RGB · 보정 목표 · 실제 물리 실행의 비교. 전신 추종 실패를 보여주는 실험 영상입니다.',
                                       'en': 'RGB, corrected target and actual physics rollout. This experiment '
                                             'shows the full-body tracking failure.'},
                           'wide': True},
                'outcome': {'ko': '관절 변환과 정책 학습·평가는 실행했습니다. 팔 중심 과제의 제한적 통과와 미해결인 전신 추종을 구분했으며, 공 상호작용과 실제 로봇 배포는 '
                                  '수행하지 않았습니다.',
                            'en': 'Joint conversion, policy training and evaluation were executed. The restricted '
                                  'arm-tracking result is separate from the unresolved full-body task; ball '
                                  'interaction and deployment to a physical robot were not tested.'},
                'insight': {'ko': '영상에서 복원한 동작이 로봇이 실행할 수 있는 동작은 아니었습니다. 데이터 형식·기구학 재생·물리 추종을 나눠 검증하고, 실패할 때 과제를 '
                                  '좁혀 원인을 분리하는 기준을 얻었습니다.',
                            'en': 'Reconstructed motion was not automatically executable motion. I learned to '
                                  'validate data format, kinematic replay and physical tracking separately, and '
                                  'to isolate failures with a narrower task.'}},
               {'id': 'learning',
                'label': {'ko': '05 · 남은 과제', 'en': '05 · What remains'},
                'title': {'ko': '각 단계의 성공 기준을 나눈 파이프라인으로.',
                          'en': 'A pipeline with explicit checks at each stage.'},
                'paragraphs': [{'ko': '이 연구에서 만든 것은 모델 실행을 연결한 코드뿐 아니라, 원본으로 돌아가 오류를 확인하고 사용할 구간을 판단하는 구조입니다. '
                                      '구현·실험·검수와 문서화에는 AI 코딩 도구를 활용했고, 사전학습 모델의 자체 개발이나 파인튜닝 성과로 소개하지 않습니다.',
                                'en': 'The work produced both integrated model runners and a structure for '
                                      'tracing errors to the source and deciding which intervals to retain. AI '
                                      'coding tools supported implementation, experiments, review and '
                                      'documentation; the work does not claim new pretrained models or '
                                      'fine-tuning.'},
                               {'ko': '다음 과제는 ID·행동 설명·모션 품질을 함께 승인하는 절차와 전신 추종 안정화입니다. 현재는 선택 구간의 데이터 구축과 독립 '
                                      '파일럿까지 수행한 연구이며, 전체 영상에서 로봇 학습까지 자동으로 완주하는 시스템은 아닙니다.',
                                'en': 'The remaining work is joint quality approval for identity, captions and '
                                      'motion, plus stable full-body tracking. The current research covers '
                                      'selected-interval data construction and independent pilots, not an '
                                      'automatic end-to-end system from arbitrary video to robot learning.'}]}],
  'links': [({'ko': '팀 공개 파이프라인·모델 실행 안내', 'en': 'Team pipeline and model setup'},
             'https://github.com/DKU-AIM/video-motion-pipeline'),
            ({'ko': '개인 그라운딩 실행기·파서', 'en': 'My grounding runners and parsers'},
             'https://github.com/jiwoo1105/video-grounding'),
            ('PHALP', 'https://github.com/brjathu/PHALP'),
            ('HMR 2.0', 'https://github.com/shubham-goel/4D-Humans'),
            ('MuJoCo', 'https://github.com/google-deepmind/mujoco'),
            ('SMPL · Loper et al. (2015)', 'https://smpl.is.tue.mpg.de/'),
            ({'ko': '시연 원본 · FIBA Basketball', 'en': 'Demo source · FIBA Basketball'},
             'https://www.youtube.com/watch?v=kXuDZJ2TT3I&t=935s')],
  'team': {'ko': 'AIV Lab · 영상 이해·3D 모션 연구', 'en': 'AIV Lab · Video understanding & 3D motion'},
  'display_stack': 'Python / PyTorch / PHALP / HMR 2.0 / SMPL',
  'facts': [({'ko': '복원 실험', 'en': 'Reconstruction study'},
             {'ko': '4,240프레임 · 선수별 6구간', 'en': '4,240 frames · 6 player-specific segments'},
             True),
            ({'ko': '설계의 출발점', 'en': 'Design research'},
             {'ko': '7개 모델 · 그라운딩 210개 응답 비교', 'en': '7 models · 210 grounding responses compared'},
             True),
            ({'ko': '현재 단계', 'en': 'Status'},
             {'ko': '데이터 구축·캡셔닝 비교·로봇 추종 파일럿',
              'en': 'Data construction, caption comparisons and robot-tracking pilots'},
             False)],
  'cover': {'video': 'motion/cover.mp4',
            'poster': 'motion/cover.jpg',
            'caption': {'ko': '같은 프레임의 원본 영상, PHALP 인물 추적, 실제 SMPL 메쉬 재생',
                        'en': 'Frame-aligned source footage, PHALP person tracking, and actual SMPL mesh replay'}},
  'card_facts': [({'ko': '데이터 연결', 'en': 'Data alignment'},
                  {'ko': '원본 시각·인물 ID·크롭 좌표·3D 모션을 프레임 단위로 연결',
                   'en': 'Source time, person ID, crop coordinates, and 3D motion aligned frame by frame'},
                  False),
                 ({'ko': '검수 기준', 'en': 'Quality review'},
                  {'ko': '누락·ID 변경·오연결을 구분하고, 문제 구간의 제외·보류 기준 수립',
                   'en': 'Criteria for excluding or holding segments with gaps, ID changes, or incorrect '
                         'associations'},
                  False)],
  'video': 'motion/compare.mp4',
  'poster': 'motion/compare.jpg',
  'showcase': {'title': {'ko': '먼저, 영상으로 살펴보세요.', 'en': 'See the pipeline in motion.'},
               'source': 'https://www.youtube.com/watch?v=kXuDZJ2TT3I&t=935s',
               'stages': [{'label': {'ko': '비교 보기', 'en': 'Compare'},
                           'title': {'ko': '선수 영상과 복원 결과를 나란히',
                                     'en': 'Person crop and reconstruction, side by side'},
                           'description': {'ko': '왼쪽은 선택한 선수의 크롭, 오른쪽은 같은 프레임에 실제 HMR 2.0 메쉬를 겹친 결과입니다. 단계를 바꾸면 '
                                                 '같은 시점이 유지됩니다.',
                                           'en': 'Left: the selected player’s crop. Right: the actual HMR 2.0 '
                                                 'mesh overlaid on the same frame. Switching stages preserves the '
                                                 'playback position.'},
                           'video': 'motion/compare.mp4',
                           'poster': 'motion/compare.jpg'},
                          {'label': {'ko': '입력', 'en': 'Input'},
                           'title': {'ko': '01. 공개 경기 영상에서 시작', 'en': '01. Start with game footage'},
                           'description': {'ko': 'FIBA U20 결승 영상의 15:35–15:41 구간입니다. 남색 21번 선수를 대상으로, 60 FPS의 같은 '
                                                 '360프레임을 모든 단계에서 사용했습니다.',
                                           'en': 'A six-second excerpt from the FIBA U20 final, 15:35–15:41. '
                                                 'Every stage uses the same 360 frames at 60 FPS, focusing on the '
                                                 'player in navy jersey 21.'},
                           'video': 'motion/input.mp4',
                           'poster': 'motion/input.jpg'},
                          {'label': {'ko': '추적', 'en': 'Track'},
                           'title': {'ko': '02. 인물 박스와 ID를 연결', 'en': '02. Associate people across frames'},
                           'description': {'ko': 'ViTDet-H 검출과 HMR 2.0의 몸·외형 특징을 사용해 PHALP가 인물을 연결합니다. 이 시연의 대상은 '
                                                 'ID 9이며, 공 추적 결과는 포함하지 않습니다.',
                                           'en': 'PHALP associates people using ViTDet-H detections and HMR '
                                                 '2.0-based body and appearance features. The selected player is '
                                                 'ID 9. This demo does not include ball tracking.'},
                           'video': 'motion/tracking.mp4',
                           'poster': 'motion/tracking.jpg'},
                          {'label': {'ko': '크롭', 'en': 'Crop'},
                           'title': {'ko': '03. 선수와 연속 구간을 선택',
                                     'en': '03. Select a player and a continuous segment'},
                           'description': {'ko': '검수한 ID 9의 6초를 직접 선택했습니다. 매 프레임 선수 박스의 각 변에 10% 여백을 더하고, 원본 픽셀 '
                                                 '크기를 유지한 채 고정 캔버스에 배치했습니다.',
                                           'en': 'I manually selected six reviewed seconds of ID 9. Each frame’s '
                                                 'player box is expanded by 10% on every side and placed on a '
                                                 'fixed-size canvas without resizing the source pixels.'},
                           'video': 'motion/crop.mp4',
                           'poster': 'motion/crop.jpg'},
                          {'label': {'ko': '메쉬', 'en': 'Mesh'},
                           'title': {'ko': '04. 선수 크롭에서 3D 몸을 다시 추정',
                                     'en': '04. Re-estimate the body from the person crop'},
                           'description': {'ko': '선수 크롭에 HMR 2.0을 다시 실행해 SMPL 자세·체형·카메라 값과 메쉬를 저장했습니다. 영상 위의 청록색 '
                                                 '몸은 이 추론에서 나온 실제 출력입니다.',
                                           'en': 'HMR 2.0 runs again on the person crop to save SMPL pose, shape, '
                                                 'camera parameters, and meshes. The cyan body overlaid on the '
                                                 'footage is the actual inference output.'},
                           'video': 'motion/overlay.mp4',
                           'poster': 'motion/overlay.jpg'},
                          {'label': {'ko': '3D 재생', 'en': '3D replay'},
                           'title': {'ko': '05. 저장한 메쉬를 배경 없이 재생',
                                     'en': '05. Replay the saved mesh without the video background'},
                           'description': {'ko': '저장된 6,890개 정점의 SMPL 메쉬를 MuJoCo에서 재생했습니다. 루트를 고정한 기구학적 재생이며, 월드 '
                                                 '이동 경로 복원·충돌·균형 제어·로봇 학습은 포함하지 않습니다.',
                                           'en': 'The saved SMPL mesh, with 6,890 vertices per frame, is replayed '
                                                 'in MuJoCo. This is fixed-root kinematic playback, without '
                                                 'recovered world translation, collisions, balance control, or '
                                                 'robot learning.'},
                           'video': 'motion/replay.mp4',
                           'poster': 'motion/replay.jpg'}],
               'pipeline': [({'ko': '원본 영상', 'en': 'Source video'},
                             {'ko': '원본 시각과 FPS 보존', 'en': 'Preserve source time and FPS'}),
                            ({'ko': '인물 추적', 'en': 'Person tracking'},
                             {'ko': 'ViTDet-H · HMR 2.0 특징 → PHALP ID 연결',
                              'en': 'ViTDet-H + HMR 2.0 features → PHALP association'}),
                            ({'ko': '선수별 크롭', 'en': 'Person crops'},
                             {'ko': '대상·구간 수동 선택 · 박스 각 변 10% 여백',
                              'en': 'Manual person/segment selection · 10% margins per side'}),
                            ({'ko': '3D 모션 복원', 'en': '3D reconstruction'},
                             {'ko': '크롭에 HMR 2.0 재실행 → SMPL 저장', 'en': 'Rerun HMR 2.0 on crops → save SMPL'}),
                            ({'ko': '메쉬 재생·검수', 'en': 'Replay & review'},
                             {'ko': '저장한 정점을 MuJoCo에서 재생 · 영상과 대조',
                              'en': 'Replay saved vertices in MuJoCo · review against footage'})],
               'scope': {'ko': '위 영상은 저장된 SMPL 메쉬의 고정 루트 재생입니다. 캡셔닝 비교와 G1 물리 추종 파일럿은 아래에 별도로 소개하며, 전신 추종과 전체 '
                               '자동화는 아직 미해결입니다.',
                         'en': 'The video above replays saved SMPL meshes with a fixed root. Captioning '
                               'comparisons and G1 physics pilots are presented separately below; full-body '
                               'tracking and end-to-end automation remain unresolved.'}}},
 {'slug': 'danzzan',
  'title': {'ko': '단짠', 'en': 'Danzzan'},
  'category': {'ko': 'Backend · 실제 서비스 운영', 'en': 'Backend · Live service'},
  'subtitle': {'ko': '학생의 예매부터 현장 입장까지, 상태와 실패 경로를 설계했습니다.',
               'en': 'Designing states and recovery paths from ticket requests to on-site entry.'},
  'desc': {'ko': '총학생회·NAVER Face Sign 연계 축제 서비스입니다. Redis·Lua 예매, JWT 인증 복구와 다국어 처리의 문제 정의·구현·검증을 소개합니다.',
           'en': 'A festival service connected to the student council and NAVER Face Sign. Case studies cover '
                 'Redis/Lua ticketing, JWT recovery and multilingual content handling.'},
  'role': {'ko': '대규모 티켓팅 백엔드, 로그인·회원가입, 다국어 지원',
           'en': 'High-traffic ticketing backend, sign-in and registration, multilingual support'},
  'role_items': [({'ko': '대규모 티켓팅', 'en': 'High-traffic ticketing'},
                  {'ko': 'Redis·Lua 기반 동시 예매 처리', 'en': 'Concurrent reservation handling with Redis and Lua'}),
                 ({'ko': '로그인·회원가입', 'en': 'Sign-in & registration'},
                  {'ko': 'JWT 재발급·예외 처리, 가입 입력·검증·저장',
                   'en': 'JWT refresh and error handling; sign-up validation and persistence'}),
                 ({'ko': '다국어 지원', 'en': 'Multilingual support'},
                  {'ko': '번역 처리·실패 대응', 'en': 'Translation and failure handling'})],
  'affiliation': {'logo': 'brands/danzzan-npay.jpg',
                  'alt': 'DANZZAN × Npay',
                  'label': {'ko': 'Face Sign 연계 입장', 'en': 'Face Sign entry integration'},
                  'kind': 'collab'},
  'field_video': {'video': 'danzzan/face-sign-entry.mp4',
                  'poster': 'danzzan/face-sign-entry.jpg',
                  'title': {'ko': 'Face Sign으로 입장하는 순간', 'en': 'Face Sign entry in action'},
                  'description': {'ko': '현장 인증부터 축제 입장까지 담은 약 10초의 영상입니다.',
                                  'en': 'A 10-second excerpt showing Face Sign verification and festival entry.'}},
  'period': '2025.12–2026.09',
  'context': {'ko': '대학 축제 웹 서비스 / 팀 프로젝트', 'en': 'University festival web service / Team project'},
  'stack': 'Spring Boot / Redis / Lua / MySQL / React / Docker',
  'repo': 'https://github.com/DKU-Dan-Zzan/Danzzan-BE',
  'images': ['danzzan-home.webp', 'danzzan-map.webp', 'danzzan-queue.webp'],
  'caption': {'ko': '팀 서비스 실제 화면 · 축제 홈, 부스 지도, 티켓 예매',
              'en': 'Actual team-service screens · Festival home, booth map, and ticketing'},
  'sections': [{'id': 'problem',
                'label': {'ko': '01 · 문제 정의', 'en': '01 · The problem'},
                'title': {'ko': '축제의 정해진 시간에, 제한된 티켓과 바뀌는 정보를 전달해야 했습니다.',
                          'en': 'A fixed opening time, limited tickets and information that kept changing.'},
                'paragraphs': [{'ko': '단짠은 총학생회와 함께 운영한 대학 축제 서비스입니다. 학생은 부스·공연·공지를 확인하고 예매하며, 운영진은 계속 바뀌는 정보를 '
                                      '전달해야 했습니다. 저는 예매·인증·번역 백엔드를 중심으로 사용자 상태와 실패 이후의 동작을 설계했습니다.',
                                'en': 'Danzzan is a university festival service operated with the student '
                                      'council. Students browse booths, performances and notices and reserve '
                                      'tickets, while organizers publish changing information. My focus was '
                                      'ticketing, authentication and translation backend logic, including user '
                                      'states and failure handling.'},
                               {'ko': '활동 기간은 2025.12–2026.09이며 6,000명 이상이 사용한 운영 성과는 4인 팀의 결과입니다. 아래에서는 봄 예매 준비, '
                                      '가을 다국어 기능, 축제 종료 후 개선을 구분합니다.',
                                'en': 'The project ran from December 2025 to September 2026. Serving over 6,000 '
                                      'users was the four-person team’s operating result. The cases below '
                                      'distinguish spring ticketing preparation, autumn localization and later '
                                      'improvements.'}],
                'visual': {'images': [('danzzan-home.webp', {'ko': '봄 축제 홈', 'en': 'Spring festival home'}),
                                      ('danzzan-map.webp', {'ko': '부스 위치 안내', 'en': 'Booth map'})],
                           'phones': True}},
               {'id': 'ticketing',
                'label': {'ko': '02 · 동시 예매 설계', 'en': '02 · Concurrent ticketing'},
                'title': {'ko': '재고를 차감하기 전에, “지금 예매할 수 있는 사람”을 정의했습니다.',
                          'en': 'Before decrementing inventory, I defined who was allowed to book.'},
                'paragraphs': [{'ko': '대기열에 들어온 사람과 예매할 차례가 된 사람은 다릅니다. 중복 확인과 재고 차감을 각각 실행하면 요청 사이에 다른 요청이 끼어들 수 '
                                      '있어, 예매 자격과 재고 처리를 함께 설계해야 했습니다.',
                                'en': 'Joining the queue is different from being eligible to book. Separate '
                                      'duplicate checks and inventory updates can be interleaved with other '
                                      'requests, so eligibility and inventory needed to be handled together.'},
                               {'ko': '기존 슬롯 방식을 WAITING → READY → ACTIVE → DONE / EXPIRED 상태로 바꿨습니다. Lua에서 '
                                      'ACTIVE 상태·유효 시간·중복 신청·잔여 재고를 확인하고 차감과 신청 표시를 묶었습니다. 실패 시 보상 스크립트도 구성했습니다.',
                                'en': 'I replaced the slot-based approach with WAITING → READY → ACTIVE → DONE / '
                                      'EXPIRED states. Lua checks ACTIVE status, validity time, duplicate '
                                      'requests and inventory before applying the decrement and reservation '
                                      'marker together. I also added compensation scripts.'}],
                'visual': {'images': [('danzzan-queue.webp',
                                       {'ko': '대기 순번을 보여주는 실제 서비스 화면',
                                        'en': 'Actual service screen showing queue position'}),
                                      ('danzzan-ticketing.png',
                                       {'ko': '회차별 예매 화면', 'en': 'Ticket selection by performance'})],
                           'phones': True},
                'outcome': {'ko': '예매 자격 검사와 재고 차감·신청 표시를 하나의 Lua 실행으로 묶었습니다. 팀 부하실험에서는 4,000 VU로 2,000장을 발급했고 중복 '
                                  '사용자 0건, HTTP 실패율 0.30%를 기록했습니다. 이 수치는 팀 시스템의 테스트 결과이며 실제 운영 동접과는 별도입니다.',
                            'en': 'Eligibility checks, inventory decrement and the reservation marker were '
                                  'combined in one Lua execution. The team load test issued 2,000 tickets at '
                                  '4,000 VU, with zero duplicate users and a 0.30% HTTP failure rate. These are '
                                  'test results for the team system, separate from live concurrency.'},
                'insight': {'ko': '동시성을 설계할 때 재고 차감뿐 아니라 예매 자격·유효 시간·실패 이후의 상태까지 함께 다뤄야 한다는 기준을 얻었습니다. Redis 안에서의 '
                                  '원자적 처리와 Kafka·MySQL로 이어지는 저장 경로는 각각의 실패 조건을 살펴야 했습니다.',
                            'en': 'I learned to design concurrency around eligibility, validity time and '
                                  'post-failure state as well as inventory. Atomic operations inside Redis and '
                                  'the persistence path through Kafka and MySQL required separate consideration '
                                  'of failure conditions.'},
                'evidence': [({'ko': '개인 구현 커밋', 'en': 'My implementation'},
                              'https://github.com/DKU-Dan-Zzan/Danzzan-BE/commit/f68eeb5'),
                             ({'ko': '팀 부하실험 조건·결과', 'en': 'Team load-test conditions and results'},
                              'https://github.com/DKU-Dan-Zzan/Danzzan-BE/blob/main/docs/load-test-report.md')]},
               {'id': 'translation',
                'label': {'ko': '03 · 외부 API와 운영', 'en': '03 · External APIs & operations'},
                'title': {'ko': '번역이 실패해도 공지는 올라가고, 운영진의 수정은 남아야 했습니다.',
                          'en': 'Translation failures should not block notices or overwrite human edits.'},
                'paragraphs': [{'ko': '가을 축제의 영어 지원은 버튼 번역만으로 끝나지 않았습니다. 운영진이 추가하는 공지·부스·공연 정보도 다뤄야 했기에, 조회할 때마다 '
                                      '번역하는 대신 등록·수정 시 번역을 DB에 저장하고 관리자에게 수정 경로를 제공했습니다.',
                                'en': 'Autumn localization had to cover new notices, booths and performances, not '
                                      'just interface labels. I translated content on creation or update and '
                                      'stored it in the database, allowing organizers to review and edit the '
                                      'English text.'},
                               {'ko': '번역 API 예외가 핵심 업무인 공지 저장을 막지 않도록 분리했습니다. 영문이 없으면 한국어를 제공하고 누락된 값만 후속 '
                                      '보정했습니다. 콘텐츠 수정에서는 원문 변경 여부와 이번 요청의 수동 영문을 필드별로 판단하도록 규칙을 순수 함수로 분리했습니다.',
                                'en': 'I isolated translation exceptions so that notices could still be saved. '
                                      'Missing English falls back to Korean and can be filled later. For content '
                                      'edits, I extracted field-level rules into a pure function to handle source '
                                      'changes and prioritize English explicitly entered in the current '
                                      'request.'}],
                'visual': {'images': [('evidence/danzzan-admin-english.png',
                                       {'ko': '개발 PR의 관리자 영문 입력 화면',
                                        'en': 'English editing fields captured for the development PR'}),
                                      ('danzzan-en.png',
                                       {'ko': '사용자가 보는 영어 공지 목록', 'en': 'English notices shown to users'})],
                           'wide': True},
                'outcome': {'ko': '공지 저장을 번역 API 성공 여부와 분리하고, 원문 대체·누락 보정·수동 입력의 우선순위를 정리했습니다. 8월 리팩터링에서는 필드 규칙의 '
                                  '조건 조합 15개를 테스트해 실패 대응과 수정 규칙을 확인했습니다.',
                            'en': 'Notice persistence was decoupled from translation API success, with explicit '
                                  'rules for source-text fallback, filling missing values and manual input. The '
                                  'August refactor tested 15 field-rule combinations to check failure handling '
                                  'and edit precedence.'},
                'insight': {'ko': '외부 API를 붙일 때는 호출 성공보다 먼저, 실패해도 유지해야 하는 업무와 자동 처리·사람의 수정 간 우선순위를 정해야 했습니다.',
                            'en': 'Integrating an external API required deciding which core work must survive a '
                                  'failure and how automation should interact with human edits.'},
                'evidence': [({'ko': '번역 실패 대응', 'en': 'Translation failure handling'},
                              'https://github.com/DKU-Dan-Zzan/Danzzan-BE/commit/49e969e'),
                             ({'ko': '필드별 결정 규칙·테스트', 'en': 'Field rules and tests'},
                              'https://github.com/DKU-Dan-Zzan/Danzzan-BE/commit/dd19772')]},
               {'id': 'recovery',
                'label': {'ko': '04 · 인증 복구', 'en': '04 · Authentication recovery'},
                'title': {'ko': '다시 로그인하려는 요청이 인증 필터에서 막혔습니다.',
                          'en': 'The authentication filter blocked the request intended to restore access.'},
                'paragraphs': [{'ko': '프론트가 만료된 Access Token을 로그인 요청에도 붙이면 컨트롤러에 도달하기 전에 401이 발생했습니다. 요청을 필터부터 '
                                      '추적해, 로그인·재발급 등 공개 경로에서도 기존 토큰을 검사하는 것이 원인임을 확인했습니다.',
                                'en': 'When the client attached an expired access token to a login request, the '
                                      'request received a 401 before reaching the controller. Tracing it through '
                                      'the filter showed that public login and refresh routes were validating the '
                                      'old token.'},
                               {'ko': '로그인·재발급·가입 인증 등 공개 경로를 필터 검사에서 제외하고, 보호된 리소스의 인증과 접근을 복구하는 요청의 경계를 분리했습니다. '
                                      '기존 인증이 만료돼도 사용자가 다시 인증할 수 있는 경로를 확보하는 것이 핵심이었습니다.',
                                'en': 'I excluded public login, refresh and registration-verification routes from '
                                      'the token filter, separating access to protected resources from requests '
                                      'that restore access. The key was keeping reauthentication reachable after '
                                      'an existing token expired.'}],
                'visual': {'caption': {'ko': '만료 토큰의 요청 경로', 'en': 'Request path with an expired token'},
                           'flow': [({'ko': '증상: 로그인도 401', 'en': 'Symptom: login returns 401'},
                                     {'ko': '컨트롤러에 도달하기 전 차단', 'en': 'Blocked before the controller'}),
                                    ({'ko': '원인: 공개 경로의 토큰 검사', 'en': 'Cause: token checks on public routes'},
                                     {'ko': '인증 복구 요청과 보호 요청의 경계 확인',
                                      'en': 'Identify recovery routes versus protected routes'}),
                                    ({'ko': '수정: 공개 경로 건너뛰기', 'en': 'Fix: bypass the filter on public routes'},
                                     {'ko': '로그인·재발급 흐름을 분리',
                                      'en': 'Separate login and refresh from protected requests'})]},
                'outcome': {'ko': '만료 토큰이 공개 로그인·재발급 경로를 선차단하던 원인을 제거했습니다. 공개 경로의 토큰 필터 제외를 2026.04.06 수정에 '
                                  '반영했습니다.',
                            'en': 'The April 6 fix removed the filter behavior that rejected public login and '
                                  'refresh requests because of an expired token.'},
                'evidence': [({'ko': 'JWT 필터 수정', 'en': 'JWT filter fix'},
                              'https://github.com/DKU-Dan-Zzan/Danzzan-BE/commit/b4916f7')]},
               {'id': 'collaboration',
                'label': {'ko': '05 · 현장으로 연결', 'en': '05 · Connecting to on-site entry'},
                'title': {'ko': '예매 이후의 입장 절차까지 연결한 팀 서비스.',
                          'en': 'A team service that connected reservations to entry.'},
                'paragraphs': [{'ko': '총학생회 운영과 NAVER Face Sign 입장에 맞춰 예매·제3자 제공 동의·사전 등록 안내를 연결했습니다. 단짠의 티켓 상태와 '
                                      '네이버의 얼굴 등록 상태는 별도 절차이며, 얼굴 정보 등록·인증은 네이버가 처리합니다.',
                                'en': 'The service connected reservations, third-party data-sharing consent and '
                                      'preregistration guidance to student-council operations and NAVER Face Sign '
                                      'entry. Ticket status and face enrollment are separate procedures; NAVER '
                                      'handles facial data and authentication.'},
                               {'ko': '제 기여는 예매·인증·번역 처리와 관련 화면 연동입니다. 대외 협의, 현장 운영, 프론트엔드와 비동기 저장에는 팀원들의 기여가 '
                                      '있습니다. 영상은 팀 서비스가 현장에서 쓰인 맥락을 보여줍니다.',
                                'en': 'My contributions cover ticketing, authentication, translation and related '
                                      'interface integration. Other members contributed external coordination, '
                                      'operations, frontend work and asynchronous persistence. The footage shows '
                                      'the team service in its operating context.'}],
                'visual': {'video': 'danzzan/face-sign-entry.mp4',
                           'poster': 'danzzan/face-sign-entry.jpg',
                           'caption': {'ko': '사용자 제공 현장 영상 · 약 10초 · 무음. NAVER Face Sign 연계 입장.',
                                       'en': 'User-provided on-site footage · Approximately 10 seconds · No '
                                             'audio. Entry linked to NAVER Face Sign.'},
                           'wide': True}},
               {'id': 'learning',
                'label': {'ko': '06 · 배운 점', 'en': '06 · What I learned'},
                'title': {'ko': '정상 경로뿐 아니라, 실패해도 이어지는 흐름을 설계합니다.',
                          'en': 'Designing the path forward when a step fails.'},
                'paragraphs': [{'ko': '예매에서는 자격·재고·상태를 함께 다뤘고, 번역에서는 공지 저장과 외부 API 실패를 분리했으며, 인증에서는 복구 경로가 차단되지 '
                                      '않게 했습니다. 기능을 추가할 때 “중간에서 멈추면 사용자와 데이터가 어떤 상태로 남는가”를 먼저 살피는 기준을 얻었습니다.',
                                'en': 'Ticketing required eligibility, inventory and states to be designed '
                                      'together; translation required notice persistence to survive API failure; '
                                      'authentication required an accessible recovery path. I learned to ask what '
                                      'state the user and data would be left in if a step stopped midway.'},
                               {'ko': '축제 종료 후에는 관리자 회차 설정·수정 잠금·티켓팅 ON/OFF와 예매 오류 응답을 개선했습니다. 운영에서 얻은 이해를 바탕으로 '
                                      '다음 운영을 준비하는 후속 개발로 이어갔습니다.',
                                'en': 'After the festivals, I improved session settings, edit locks, ticketing '
                                      'ON/OFF controls and error responses, using what I had learned from the '
                                      'service to prepare for future operations.'}]}],
  'links': [({'ko': '백엔드 저장소', 'en': 'Backend repository'}, 'https://github.com/DKU-Dan-Zzan/Danzzan-BE'),
            ({'ko': '프론트엔드 저장소', 'en': 'Frontend repository'}, 'https://github.com/DKU-Dan-Zzan/Danzzan-FE'),
            ({'ko': '축제 후 예매 상태 개선', 'en': 'Post-festival reservation state fix'},
             'https://github.com/DKU-Dan-Zzan/Danzzan-BE/commit/11395c73ad285a7fae8553b6d8c59405f881c474')],
  'team': {'ko': '4인 팀 · 봄·가을축제 운영', 'en': '4-person team · Spring & autumn festivals'},
  'display_stack': 'Spring Boot / Redis / Lua / MySQL / Docker',
  'facts': [({'ko': '실사용자', 'en': 'Real users'},
             {'ko': '6,000명 이상 · 팀 운영 성과', 'en': '6,000+ · Team operational outcome'},
             True),
            ({'ko': '운영', 'en': 'Operations'},
             {'ko': '2026 봄·가을축제 2회', 'en': 'Spring and autumn festivals, 2026'},
             True),
            ({'ko': '협업', 'en': 'Collaboration'},
             {'ko': '총학생회 협업 & NAVER Face Sign 연계 입장',
              'en': 'Student council collaboration & NAVER Face Sign entry integration'},
             False)]},
 {'slug': 'soccer-analysis',
  'title': {'ko': '축구 드리블 동작 분석', 'en': 'Soccer dribbling analysis'},
  'category': {'ko': 'Computer vision · 연구', 'en': 'Computer vision · Research'},
  'subtitle': {'ko': '좋은 드리블을 평가한다는 목표를, 설명 가능한 측정 기준으로 옮겼습니다.',
               'en': 'Translating the goal of evaluating dribbling into explicit, inspectable measurements.'},
  'desc': {'ko': '한 대의 카메라로 촬영한 드리블 영상에서 선수의 관절과 공을 추적합니다. 터치 주변의 헤드업·어깨 움직임과 전체 유효 프레임의 상체 각도를 계산하고, 원본 장면과 대조할 '
                 '수 있는 연구용 보고서로 만듭니다.',
           'en': 'I track body landmarks and the ball in single-camera dribbling videos, measure head-up movement '
                 'and shoulder motion around touches and torso angle across all valid frames, and generate '
                 'research reports that can be checked against the source footage.'},
  'role': {'ko': '지표 설계, 터치 구간 실험, 분석 파이프라인 구현·검수',
           'en': 'Metric design, touch-window experiments, pipeline development and review'},
  'period': {'ko': '2025.11–2026.06 · 완료', 'en': 'Nov 2025–Jun 2026 · Completed'},
  'context': 'AIV Lab',
  'stack': 'Python / MediaPipe / YOLO / SAM2 / NumPy / SciPy',
  'repo': 'https://github.com/jiwoo1105/soccer_motion_analysis',
  'video': 'soccer-ball-tracking.mp4',
  'poster': 'soccer-ball-poster.jpg',
  'caption': {'ko': '별도 YOLO11 ROI 실험 · 선수 관절·공 검출 좌표',
              'en': 'Separate YOLO11 ROI experiment · Body landmarks and detected ball positions'},
  'sections': [{'id': 'problem',
                'label': {'ko': '01 · 문제 정의', 'en': '01 · The problem'},
                'title': {'ko': '“많이 움직였다”는 수치가 “잘했다”는 평가는 아니었습니다.',
                          'en': 'More movement did not necessarily mean better dribbling.'},
                'paragraphs': [{'ko': '단안 영상에서 자세를 추정하는 것보다 어려운 문제는 무엇을 측정해야 평가 의도를 설명할 수 있는지 정하는 일이었습니다. 어깨의 최대 '
                                      '방향 차이는 낮은 등급 영상에서도 크게 나왔고, 점수 가중치나 상한을 바꿔도 원시값의 순서가 바뀌지는 않았습니다.',
                                'en': 'Beyond estimating pose from a monocular video, the harder question was '
                                      'what measurement could represent the evaluation intent. Maximum '
                                      'shoulder-direction differences were also large in lower-rated videos. '
                                      'Changing score weights or caps did not change the ordering of the raw '
                                      'measurements.'},
                               {'ko': '저는 교수님 피드백을 계산 정의로 구체화하고 원본·관절·공 궤적·지표를 함께 볼 수 있는 분석 흐름을 구현했습니다. 프로젝트는 '
                                      '2026.06 완료했고, 이 페이지의 9~11월 비교·재실행 자료는 종료 후 연구 검토입니다.',
                                'en': 'I translated faculty feedback into calculation definitions and built an '
                                      'analysis flow that exposes source footage, joints, ball trajectories and '
                                      'metrics together. The project concluded in June 2026; the '
                                      'September–November comparisons and reruns shown here are subsequent '
                                      'research reviews.'}],
                'visual': {'images': [('evidence/soccer-windows.png',
                                       {'ko': '2026.10 후속 검토: 터치 윈도우를 넓혀도 최대각과 등급의 관계가 일관되지 않았습니다.',
                                        'en': 'October 2026 follow-up: wider touch windows did not produce a '
                                              'consistent relationship between maximum angle and rating.'})],
                           'wide': True}},
               {'id': 'metrics',
                'label': {'ko': '02 · 측정 기준 재정의', 'en': '02 · Redefining the measurement'},
                'title': {'ko': '움직임의 크기와 속도를 나누고, 평가할 시간 구간을 맞췄습니다.',
                          'en': 'Separating movement magnitude from speed, then defining when to measure.'},
                'paragraphs': [{'ko': '최대각 후보와 인접 프레임의 평균 방향 변화 속도를 분리해 비교했습니다. 터치 앞뒤 ±6·10·16·20·24·30프레임을 검토한 '
                                      '뒤, 교수님의 평가 의도에 맞춰 기존 프레임별 속도를 유지하면서 터치 주변 값만 평균하도록 정리했습니다.',
                                'en': 'I compared maximum-angle candidates separately from average directional '
                                      'angular speed and examined ±6, 10, 16, 20, 24 and 30-frame windows. '
                                      'Following faculty feedback, I retained the framewise speed calculation but '
                                      'averaged only the values around touches.'},
                               {'ko': '최종 ±16은 헤드업과 시간 범위를 맞춘 선택입니다. 겹치는 프레임 쌍은 한 번만 집계하고, 결측을 건너뛰어 멀리 떨어진 두 프레임을 '
                                      '연결하지 않았습니다. 필요한 항목이 없으면 총점을 N/A로 남겼습니다.',
                                'en': 'The final ±16 window aligns the interval with the head-up metric. '
                                      'Overlapping frame pairs are counted once, missing intervals are not '
                                      'bridged, and an unavailable required metric leaves the total score as '
                                      'N/A.'}],
                'visual': {'images': [('evidence/soccer-selection.png',
                                       {'ko': '실제 장면과 속도 파형을 함께 본 ±10 실험 예시. 최종 ±16 결과와 구분합니다.',
                                        'en': 'An actual ±10-frame experiment linking footage to the speed '
                                              'waveform. This is not the final ±16 result.'})],
                           'wide': True},
                'outcome': {'ko': '측정 대상·시간 범위·결측 처리 규칙을 명시했습니다. 등급 구분 성능의 일관된 개선이나 최적 윈도우를 찾았다는 결과는 얻지 못했습니다.',
                            'en': 'The measurement, interval and missing-data rules became explicit. The '
                                  'comparisons did not establish consistent improvement in rating separation or '
                                  'an optimal window.'},
                'insight': {'ko': '전체 전문가 등급을 특정 관절 지표의 정답으로 취급하지 않게 됐습니다. 원하는 점수에 맞추기 전에, 그 숫자가 어떤 동작을 측정하는지부터 '
                                  '설명해야 했습니다.',
                            'en': 'I stopped treating an overall expert rating as ground truth for one joint '
                                  'metric. Before fitting a score, I needed to explain the movement the '
                                  'underlying number actually measured.'}},
               {'id': 'pipeline',
                'label': {'ko': '03 · 입력 오류 추적', 'en': '03 · Tracing input errors'},
                'title': {'ko': '공 하나를 잘못 고르면, 평가할 순간도 달라집니다.',
                          'en': 'Choosing the wrong ball also changes the moments being evaluated.'},
                'paragraphs': [{'ko': '기본 경로는 MediaPipe의 관절 추정과 YOLOv8n 초기 검출·SAM2.1 추적을 연결합니다. 배경 공이 초기 대상으로 '
                                      '선택되면 터치 후보와 자세를 집계하는 시간까지 영향을 받아, 공 좌표를 원본 위에 겹쳐 확인했습니다.',
                                'en': 'The default path combines MediaPipe pose estimates with YOLOv8n '
                                      'initialization and SAM2.1 tracking. Selecting a background ball affects '
                                      'touch candidates and measurement windows, so I overlaid the tracked '
                                      'coordinates on the source footage.'},
                               {'ko': '발목 근접 선택·재탐색과 별도 YOLO11 발목 ROI 재검출을 비교했습니다. 근접 조건을 만족하는 배경 공도 있어 완전한 해결에는 '
                                      '이르지 못했습니다. 최종 점수만으로는 드러나지 않는 오류를 입력 단계에서 확인할 수 있도록 결과를 남겼습니다.',
                                'en': 'I reviewed ankle-proximity selection, reacquisition and a separate YOLO11 '
                                      'ankle-ROI redetection experiment. A background ball could still satisfy '
                                      'the proximity criterion, so the problem was not fully resolved. The '
                                      'outputs make input-level failures visible even when a final score alone '
                                      'would hide them.'}],
                'visual': {'video': 'soccer-ball-tracking.mp4',
                           'poster': 'soccer-ball-poster.jpg',
                           'caption': {'ko': '별도 YOLO11 ROI 실험의 실제 공 검출. 기본 YOLOv8·SAM2 경로의 성능 증거와 구분합니다.',
                                       'en': 'Actual ball detections from the separate YOLO11 ROI experiment, not '
                                             'a performance demonstration of the default YOLOv8/SAM2 path.'}},
                'insight': {'ko': '검출 결과가 존재하는지, 올바른 대상을 고른 것인지, 그 결과로 계산한 지표가 타당한지는 각각 다른 질문이었습니다. 검수를 이 세 단계로 '
                                  '나누게 됐습니다.',
                            'en': 'A detection existing, the correct object being selected, and the resulting '
                                  'metric being valid are three different questions. I learned to review them '
                                  'separately.'}},
               {'id': 'validation',
                'label': {'ko': '04 · 후속 검증', 'en': '04 · Follow-up validation'},
                'title': {'ko': '같은 결과가 반복돼도, 같은 오류가 반복될 수 있습니다.',
                          'en': 'A repeatable result can also be a repeatable error.'},
                'paragraphs': [{'ko': '종료 후 논문 리뷰에 대응해 3개 영상을 각각 5회, 같은 CLI·CPU 조건에서 원본부터 다시 분석했습니다. 관절 배열·공 '
                                      '궤적·터치 프레임·원시 지표·점수는 반복 간 일치했습니다. 저장 결과 771프레임의 재집계도 별도 계산과 1e−10 이내로 '
                                      '맞았습니다.',
                                'en': 'For a later paper review, I reprocessed three source videos five times '
                                      'each with the same CLI and CPU settings. Joint arrays, ball trajectories, '
                                      'touch frames, raw metrics and scores matched across repeats. Separately, '
                                      'recomputing 771 saved frames agreed with an independent calculation within '
                                      '1e−10.'},
                               {'ko': '그러나 11월 검토에서는 잘못된 초기 공 선택도 확인됐습니다. 반복 일치와 측정 정확성을 분리하고, 원본 장면에서 대상이 맞는지 '
                                      '확인해야 한다는 한계를 함께 기록했습니다.',
                                'en': 'The November review also identified incorrect initial ball selection. I '
                                      'therefore recorded repeatability separately from measurement accuracy and '
                                      'kept source-level object checks as a necessary validation step.'}],
                'visual': {'images': [('evidence/soccer-initial-ball.jpg',
                                       {'ko': '2026.11 후속 검토: 초기 프롬프트가 실제 드리블 공과 다른 곳을 가리킨 사례.',
                                        'en': 'November 2026 follow-up: the initial prompt points away from the '
                                              'ball actually being dribbled.'})]}},
               {'id': 'learning',
                'label': {'ko': '05 · 배운 점', 'en': '05 · What I learned'},
                'title': {'ko': '숫자를 조정하기 전에, 문제의 정의를 다시 봅니다.',
                          'en': 'Revisiting the definition before adjusting the number.'},
                'paragraphs': [{'ko': '가중치 조정에 앞서 측정 대상·시간 범위·입력 품질을 분리했습니다. 이 과정을 통해 결과가 기대와 다를 때 마지막 점수만 만지는 '
                                      '대신, 정의 → 입력 → 계산 → 해석 순서로 원인을 좁히는 방법을 익혔습니다.',
                                'en': 'I separated the measurement, its time interval and input quality before '
                                      'adjusting weights. When results differed from expectations, I learned to '
                                      'investigate definition → input → calculation → interpretation instead of '
                                      'changing the final score alone.'}]}],
  'links': [({'ko': '분석 도구와 실행 안내', 'en': 'Analysis tool and usage'},
             'https://github.com/jiwoo1105/soccer_motion_analysis'),
            ({'ko': '터치 ±16프레임 반영 기록', 'en': 'Touch-window implementation'},
             'https://github.com/jiwoo1105/soccer_motion_analysis/commit/38e0ad5')],
  'team': {'ko': 'AIV Lab · 스포츠 동작 분석 연구', 'en': 'AIV Lab · Sports motion research'},
  'display_stack': 'Python / MediaPipe / YOLO / SAM2 / NumPy',
  'facts': [({'ko': '종료 후 재검증', 'en': 'Post-project validation'},
             {'ko': '2026.10 · 3개 영상 × 5회', 'en': 'Oct 2026 · 3 videos × 5 runs'},
             True),
            ({'ko': '확인 범위', 'en': 'Verified scope'},
             {'ko': '같은 CPU 조건에서 좌표·지표·점수 일치',
              'en': 'Matching coordinates, metrics, and scores under the same CPU settings'},
             False)]},
 {'slug': 'conquer-health',
  'title': 'Conquer Health',
  'category': {'ko': 'LLM 시스템 · 해커톤', 'en': 'LLM systems · Hackathon'},
  'subtitle': {'ko': '가중치를 바꿀 수 없는 의료 모델에서, 근거 전달과 답변 완결성을 개선하는 실험.',
               'en': 'Improving evidence delivery and answer completeness around a medical model with fixed '
                     'weights.'},
  'desc': {'ko': '루닛 L2-preview의 추론 흐름을 개선한 의료 대화 프로젝트입니다. MCP 문서 조회·본문 전달, 출력 예산 실험과 답변 검수를 맡았으며, 팀은 직접 생성과 선택적 '
                 '조회를 결합해 벤치마크상을 받았습니다.',
           'en': 'A medical dialogue project improving inference around Lunit L2-preview. I worked on MCP '
                 'document lookup, passing retrieved text to generation, output-budget experiments, and response '
                 'review. The team combined direct generation with selective retrieval and won the benchmark '
                 'award.'},
  'role': {'ko': 'MCP 문서 조회·본문 전달, 초기 안전 게이트, 출력 예산 실험',
           'en': 'MCP lookup and evidence delivery, initial safety gate, output-budget experiments'},
  'period': '2026.08.21–08.22',
  'context': {'ko': '루닛 의료 AI 해커톤 / AIM 팀 5인', 'en': 'Lunit medical AI hackathon / Team AIM, five members'},
  'stack': 'Python / FastAPI / MCP / L2-preview / Docker',
  'repo': 'https://github.com/Hackathon-AIM/health-conquer-submission',
  'visual': 'health',
  'caption': {'ko': '개인 구현·검수 흐름 도식 · 46.51점은 팀 최종 평가',
              'en': 'Diagram of my implementation and review flow · Score shown is the team’s final evaluation'},
  'award': {'ko': '루닛 · 벤치마크 1위 · AIM 팀 수상', 'en': 'Lunit · 1st in benchmark · Team AIM award'},
  'sections': [{'id': 'problem',
                'label': {'ko': '01 · 문제 정의', 'en': '01 · The problem'},
                'title': {'ko': '의료 답변의 품질을, 모델 바깥의 처리 과정에서 개선해야 했습니다.',
                          'en': 'Improving medical answers through the system around a fixed model.'},
                'paragraphs': [{'ko': '루닛이 제공한 L2-preview의 가중치를 바꾸지 않고 의료 질의응답을 개선하는 해커톤이었습니다. 검색 도구를 더 붙이거나 출력량을 '
                                      '늘리는 것만으로는 질문의 요구를 빠짐없이 다루고 근거를 사용하는 답변을 보장할 수 없었습니다.',
                                'en': 'The hackathon asked us to improve medical question answering without '
                                      'changing Lunit’s L2-preview weights. Adding retrieval tools or a larger '
                                      'output budget did not by itself ensure that answers addressed the question '
                                      'completely and used the evidence.'},
                               {'ko': '저는 초기 MCP 검색·본문 전달·약물 안전 게이트를 구현하고 출력 예산과 멀티턴 지시를 실험했습니다. 먼저 조회 → 모델 입력 → '
                                      '생성 → 후처리로 흐름을 나눠, 정보가 어디서 빠지는지 확인했습니다.',
                                'en': 'I implemented the initial MCP lookup, evidence delivery and medication '
                                      'safety gate, and experimented with output budgets and multi-turn '
                                      'instructions. I separated lookup, model input, generation and '
                                      'post-processing to inspect where information could be lost.'}],
                'visual': {'caption': {'ko': '확인한 경계', 'en': 'Boundaries I inspected'},
                           'flow': [({'ko': '조회 결과', 'en': 'Retrieved content'},
                                     {'ko': '관련 문서가 반환되는가', 'en': 'Does retrieval return relevant material?'}),
                                    ({'ko': '생성 입력', 'en': 'Generation input'},
                                     {'ko': '문서 본문이 실제 입력에 포함되는가',
                                      'en': 'Does the document body reach the model?'}),
                                    ({'ko': '최종 답변', 'en': 'Final answer'},
                                     {'ko': '요구사항·근거·응답 끝부분이 남는가',
                                      'en': 'Are requirements, evidence and the answer ending preserved?'})]}},
               {'id': 'implementation',
                'label': {'ko': '02 · 근거 전달 설계', 'en': '02 · Evidence delivery'},
                'title': {'ko': '도구 호출의 성공과, 근거를 쓴 답변의 성공을 나눴습니다.',
                          'en': 'A successful tool call was not the same as an evidence-based answer.'},
                'paragraphs': [{'ko': 'MCP 모델이 문서 목록만 본 뒤 검색을 끝내거나, 근거를 수집하고도 빈 선택 결과를 반환하는 경로를 확인했습니다. 목록 탐색만으로 '
                                      '종료하면 본문 조회를 한 번 더 유도하고, 수집된 근거가 있는데 최종 선택이 비면 수집분으로 복구하도록 검색·생성 연결을 '
                                      '보완했습니다.',
                                'en': 'The retrieval model could stop after listing documents or return an empty '
                                      'final selection despite having collected evidence. I added a prompt to '
                                      'fetch the document body when it stopped at exploration, and a recovery '
                                      'path that uses the collected evidence when the final selection is empty.'},
                               {'ko': '팀은 직접 생성 기준선을 확인한 뒤 한국어 약가·허가·성분·질병 코드처럼 조회가 필요한 질문에 도구 사용을 제한하는 방향을 '
                                      '검토했습니다. 초기 연결과 본문 전달은 제 기여이며, 최종 선택적 조회·긴 답변 보존은 팀 제출안의 개선입니다.',
                                'en': 'After establishing a direct-generation baseline, the team explored '
                                      'limiting tools to questions needing lookup, such as Korean pricing, '
                                      'approvals, ingredients and disease codes. My contribution was the initial '
                                      'integration and evidence delivery; selective lookup and preserving long '
                                      'answers belong to the team submission.'}],
                'visual': {'caption': {'ko': '개인 구현 → 팀 제출 전략', 'en': 'My integration → team submission strategy'},
                           'flow': [({'ko': '목록만 보고 종료', 'en': 'Stops after listing documents'},
                                     {'ko': '본문 조회를 한 번 더 유도', 'en': 'Prompt once more for the document body'}),
                                    ({'ko': '수집했지만 빈 선택', 'en': 'Evidence collected, selection empty'},
                                     {'ko': '수집한 근거로 복구하고 미확보 항목도 전달',
                                      'en': 'Recover collected evidence and retain missing-evidence notes'}),
                                    ({'ko': '생성에 근거 전달', 'en': 'Pass evidence to generation'},
                                     {'ko': '존재하지 않는 인용 ID는 제외',
                                      'en': 'Discard citation IDs absent from the retrieved store'})]},
                'insight': {'ko': '도구 사용 횟수보다 필요한 정보가 최종 답변까지 살아 있는지가 중요했습니다. 기능을 추가한 위치뿐 아니라 정보가 사라지는 경계까지 확인하게 '
                                  '됐습니다.',
                            'en': 'What mattered was whether needed information survived into the final answer, '
                                  'not how many tools were used. I learned to inspect the boundaries where '
                                  'information could disappear.'}},
               {'id': 'inference',
                'label': {'ko': '03 · 실험 판단', 'en': '03 · Judging an experiment'},
                'title': {'ko': '점수는 올랐지만, 개선이라고 결론 내리지 않았습니다.',
                          'en': 'The score was higher; the evidence was not enough to call it an improvement.'},
                'paragraphs': [{'ko': '답변 잘림과 재생성 경로를 줄이려는 후보 e6de327에서 서버 상한을 2,048→32,768로 정정하고, 실제 요청 출력 예산은 '
                                      '2,048→4,096토큰으로 늘렸습니다. 서버가 허용하는 상한과 요청이 사용하는 예산을 구분해 설정을 확인했습니다.',
                                'en': 'To investigate truncated answers and regeneration, candidate e6de327 '
                                      'corrected the server cap from 2,048 to 32,768 while raising the requested '
                                      'output budget from 2,048 to 4,096 tokens. I checked these as distinct '
                                      'settings.'},
                               {'ko': '후보는 49.59점, 기준선 3회 평균은 49.18점이었습니다. 차이는 +0.41점이지만 기준선 반복은 47.79–50.03, '
                                      '2.24점 폭으로 달랐습니다. 이 결과만으로 토큰 상향의 개선 효과를 주장하지 않았습니다.',
                                'en': 'The candidate scored 49.59 against a three-run baseline mean of 49.18. The '
                                      '+0.41 difference was within the observed baseline spread of 47.79–50.03, '
                                      'or 2.24 points. This was insufficient evidence to attribute an improvement '
                                      'to the larger token budget.'}],
                'visual': {'images': [('evidence/health-experiment.svg',
                                       {'ko': '개발 실험 장부를 재구성한 비교. 기준선 관측 범위와 후보 점수를 같은 축에 표시했습니다.',
                                        'en': 'Comparison reconstructed from the development ledger: observed '
                                              'baseline range and candidate score on the same scale.'})],
                           'wide': True},
                'outcome': {'ko': '수치와 설정을 남기고, 잘림·폴백·지연·답변 완결성을 함께 확인해야 한다는 평가 기준을 정리했습니다. 최종 대회 점수와 이 개발 실험은 '
                                  '별개입니다.',
                            'en': 'I retained the settings and scores and identified truncation, fallback, '
                                  'latency and completeness as additional checks. This development experiment is '
                                  'separate from the final competition evaluation.'},
                'insight': {'ko': '가장 높은 한 번의 점수를 고르는 대신, 기준선 변동 안에서 설명 가능한 변화인지 먼저 확인했습니다. 변경 내용과 관측 결과, 그 결과로 '
                                  '내릴 수 있는 결론을 따로 기록하는 습관을 얻었습니다.',
                            'en': 'Instead of selecting the highest single score, I first considered whether the '
                                  'change could be distinguished from baseline variation. I learned to record the '
                                  'change, observation and supported conclusion separately.'}},
               {'id': 'award',
                'label': {'ko': '04 · 팀의 최종 결과', 'en': '04 · The final team result'},
                'title': {'ko': '벤치마크 1위. 팀 성과와 실험 점수는 구분합니다.',
                          'en': 'First in the benchmark—with experimental and final scores kept separate.'},
                'paragraphs': [{'ko': 'AIM 팀은 루닛 Conquer Health의 HealthBench 기반 최종 평가에서 14개 팀 중 1위로 벤치마크상을 받았습니다. '
                                      '최종 3라운드 평균은 46.51점입니다. 이는 팀 공동 성과이며 MCP나 출력 예산 하나의 효과로 해석하지 않습니다.',
                                'en': 'Team AIM won the benchmark award, ranking first among 14 teams in the '
                                      'final HealthBench-based evaluation at Lunit Conquer Health. The '
                                      'three-round mean was 46.51. This is a shared team outcome, not an effect '
                                      'attributable solely to MCP or output budget.'}],
                'table': {'caption': {'ko': '팀 공개 최종 평가 기록', 'en': 'Team-reported final evaluation'},
                          'headers': [{'ko': '평가', 'en': 'Evaluation'}, {'ko': '점수', 'en': 'Score'}],
                          'rows': [['Round 1', '46.17'],
                                   ['Round 2', '45.55'],
                                   ['Round 3', '47.82'],
                                   [{'ko': '평균', 'en': 'Mean'}, '46.51']]},
                'image': 'conquer-award.png',
                'image_alt': {'ko': 'AIM 팀 Conquer Health 벤치마크 상장 · 2026.08.22',
                              'en': 'Team AIM’s Conquer Health benchmark award · 22 August 2026'},
                'image_class': 'award-figure',
                'details': {'label': {'ko': '개발 대시보드 점수와 다른 이유',
                                      'en': 'Why the development dashboard shows other scores'},
                            'paragraphs': [{'ko': '개발 장부의 54.37점과 마감 대시보드의 53.53점은 최종 3라운드 평가와 별도 기록입니다. 모델 서버 '
                                                  '상태와 누적 변경이 함께 달라진 실험도 있어, 서로 다른 기록을 단일 개선율로 계산하지 않았습니다. 상장은 수상 '
                                                  '증빙이며 숫자 점수를 기재하지 않습니다.',
                                            'en': 'The development ledger’s 54.37 and the closing dashboard’s '
                                                  '53.53 are separate from the three final rounds. Some '
                                                  'development runs also differed in server state and accumulated '
                                                  'changes, so these records are not combined into one '
                                                  'improvement rate. The certificate documents the award, not '
                                                  'numerical scores.'}]}},
               {'id': 'learning',
                'label': {'ko': '05 · 배운 점', 'en': '05 · What I learned'},
                'title': {'ko': 'AI 시스템의 개선도, 원인과 결과를 설명할 수 있어야 합니다.',
                          'en': 'An AI system improvement needs an explainable link between cause and result.'},
                'paragraphs': [{'ko': 'MCP를 연결했다는 사실이나 더 긴 답변을 생성했다는 사실만으로 품질 개선을 설명할 수 없었습니다. 제어할 수 있는 설정을 나누고, '
                                      '실제 입력과 응답을 확인하며, 반복 변동과 팀 변경을 구분하는 실험 태도를 배웠습니다.',
                                'en': 'Connecting MCP or generating longer answers did not alone explain an '
                                      'improvement. I learned to separate controllable settings, inspect actual '
                                      'inputs and responses, and distinguish run-to-run variation from the '
                                      'effects of team changes.'}]}],
  'links': [({'ko': '팀 저장소와 실행 구조', 'en': 'Team repository and architecture'},
             'https://github.com/Hackathon-AIM/health-conquer-submission'),
            ({'ko': '개인 구현: MCP 연결·안전 게이트', 'en': 'My implementation: MCP integration and safety gate'},
             'https://github.com/Hackathon-AIM/health-conquer-submission/commit/75a96193672ebe55bfbbaa42a382c9681794bb41'),
            ({'ko': '개인 실험: 출력 예산 조정', 'en': 'My experiment: output budget'},
             'https://github.com/Hackathon-AIM/health-conquer-submission/commit/e6de32700de51aeb320172b1dd87ad52721305f5'),
            ({'ko': '실험 장부 대조와 점수 해석', 'en': 'Ledger review and score interpretation'},
             'https://github.com/Hackathon-AIM/health-conquer-submission/blob/main/docs/experiment-retrospective.md'),
            ({'ko': '팀의 최종 평가 기록', 'en': 'Team-reported final evaluation'},
             'https://juhee0223.github.io/juhee-portfolio/projects/conquer-health.html')],
  'team': {'ko': '5인 팀 · 루닛 의료 AI 해커톤', 'en': '5-person team · Lunit medical AI hackathon'},
  'display_stack': 'Python / FastAPI / MCP / L2-preview',
  'facts': [({'ko': '최종 평가', 'en': 'Final evaluation'},
             {'ko': '14개 팀 중 1위 · 벤치마크상', 'en': '1st of 14 teams · Benchmark award'},
             True),
            ({'ko': '팀 평균', 'en': 'Team average'},
             {'ko': '46.51점 · 최종 3라운드', 'en': '46.51 · Three final rounds'},
             True),
            ({'ko': '개선 범위', 'en': 'Scope'},
             {'ko': '제공 모델의 응답 흐름 · 가중치 변경 없음',
              'en': 'Response pipeline around the provided model · No weight changes'},
             False)]},
 {'slug': 'fish-detection',
  'title': {'ko': '넙치 증상 탐지 / Flatfish doctor', 'en': 'Flatfish doctor'},
  'category': {'ko': 'Computer vision · 애플리케이션', 'en': 'Computer vision · Application'},
  'subtitle': {'ko': '넙치 개체 탐지와 7종 외형 상태 분류를 앱으로 연결했습니다. 증상 분류의 최고 검증 Top-1은 87.68%입니다.',
               'en': 'I connected fish detection and seven-category appearance classification to an app. The '
                     'symptom classifier reached a peak validation Top-1 accuracy of 87.68%.'},
  'desc': {'ko': '넙치를 탐지한 뒤 개체별 크롭을 정상을 포함한 7개 외형 상태로 분류합니다. 데이터 전처리와 모델 학습부터 FastAPI 추론, Flutter 결과 화면까지 연결했습니다.',
           'en': 'A two-stage pipeline detects olive flounder and classifies individual crops into seven '
                 'appearance categories, including normal. I connected data preparation and model training to '
                 'FastAPI inference and a Flutter results interface.'},
  'role': {'ko': '데이터 전처리, 탐지·분류 학습, 추론 API·앱',
           'en': 'Data preparation, detection/classification training, inference API and app'},
  'period': '2026.03–2026.06',
  'context': {'ko': '넙치 외형 증상 모니터링', 'en': 'Visual symptom monitoring for olive flounder'},
  'stack': 'YOLO / PyTorch / OpenCV / FastAPI / Flutter',
  'repo': 'https://github.com/jiwoo1105/fish-disease-detection',
  'images': ['fish-results.png'],
  'caption': {'ko': '개체별 증상 분류 결과 화면', 'en': 'Per-fish symptom classification results'},
  'sections': [{'id': 'problem',
                'label': {'ko': '01 · 문제 정의', 'en': '01 · The problem'},
                'title': {'ko': '수조의 이미지에서, 개체별로 확인할 수 있는 결과까지.',
                          'en': 'From a tank image to a result tied to each fish.'},
                'paragraphs': [{'ko': '물결·조명·겹친 개체가 섞인 전체 프레임에서는 어느 물고기의 증상인지 연결하기 어렵습니다. 저는 개체 탐지 → 크롭 → 7종 외형 '
                                      '상태 분류로 작업을 나누고, 결과를 원본 위치로 돌려주는 앱까지 연결했습니다.',
                                'en': 'Ripples, lighting and overlapping fish make it difficult to associate '
                                      'symptoms with an individual in a full-frame image. I separated detection, '
                                      'cropping and seven-class visual-symptom classification, then connected '
                                      'predictions back to their positions in the app.'},
                               {'ko': '담당 범위는 라벨 전처리, 탐지·분류 학습, 추론 API와 좌표 변환, Flutter 결과 화면입니다. 질병명·대응 안내는 증상에 '
                                      '따른 규칙 매핑이며 영상만으로 병원체를 확진하는 모델은 아닙니다.',
                                'en': 'My work covered label preprocessing, detection and classification '
                                      'training, the inference API, coordinate conversion and Flutter results UI. '
                                      'Disease and response guidance uses symptom-based rules, not image-based '
                                      'confirmation of a pathogen.'}],
                'visual': {'images': [('evidence/fish-monitoring.png',
                                       {'ko': '다중 수조 모니터링 시연 화면', 'en': 'Multi-tank monitoring demo'}),
                                      ('fish-results.png',
                                       {'ko': '원본 개체에 표시한 증상 예측',
                                        'en': 'Symptom predictions overlaid on the source fish'})],
                           'phones': True},
                'note': {'ko': '앱 시연 입력에는 AI 생성 영상이 포함됩니다. 실제 양식장 실증이나 질병 조기 발견 효과의 근거로 사용하지 않습니다.',
                         'en': 'Demo inputs include AI-generated footage. They do not demonstrate field '
                               'validation or early-detection outcomes at a working farm.'}},
               {'id': 'data',
                'label': {'ko': '02 · 데이터와 병목', 'en': '02 · Data & bottlenecks'},
                'title': {'ko': '분류 정확도가 높아도, 찾지 못한 개체는 평가할 수 없었습니다.',
                          'en': 'A strong classifier cannot evaluate a fish the detector missed.'},
                'paragraphs': [{'ko': 'AI Hub의 개체·증상 라벨을 크롭에 연결하고 매핑되지 않는 라벨은 제외했습니다. 학습에는 클래스별 상한을 적용해 쏠림을 줄이되, '
                                      '평가 분포가 바뀌지 않도록 검증 데이터는 유지했습니다.',
                                'en': 'I mapped AI Hub object and symptom annotations to crops and excluded '
                                      'unmapped labels. Class caps were applied only to training data, leaving '
                                      'the validation distribution unchanged.'},
                               {'ko': '분류의 최고 검증 Top-1은 87.68%였지만 탐지 mAP50은 0.4455였습니다. 두 지표를 종합 정확도처럼 합치지 않고, '
                                      '겹침·탁한 수조에서 개체를 놓치는 앞 단계가 결과를 제한한다는 점을 따로 봤습니다.',
                                'en': 'Peak validation Top-1 classification accuracy was 87.68%, while detection '
                                      'mAP50 was 0.4455. I kept the metrics separate and identified missed fish '
                                      'in overlapping or turbid scenes as an upstream bottleneck.'}],
                'visual': {'images': [('fish-validation.jpg',
                                       {'ko': '분류기의 저장된 검증 배치 예측. 전체 앱의 정확도와는 다른 평가입니다.',
                                        'en': 'Saved classifier validation-batch predictions. This evaluates a '
                                              'different task from end-to-end application accuracy.'})]},
                'insight': {'ko': '잘 나온 모델 점수만으로 파이프라인을 평가하지 않게 됐습니다. 앞 단계의 누락이 뒤 단계에 전달할 입력 자체를 없애는지 먼저 확인해야 '
                                  '했습니다.',
                            'en': 'I learned not to judge a pipeline by its strongest model score. An upstream '
                                  'miss can remove the input that a later stage needs.'}},
               {'id': 'application',
                'label': {'ko': '03 · 결과를 화면으로', 'en': '03 · Making results inspectable'},
                'title': {'ko': '예측값과 화면의 물고기가 같은 개체를 가리키도록.',
                          'en': 'Making sure a prediction and its overlay refer to the same fish.'},
                'paragraphs': [{'ko': '모델 좌표를 원본 이미지와 앱 화면으로 변환하고, 위치·증상·신뢰도를 함께 전달했습니다. 사용자가 개체별 결과와 수조별 기록을 확인할 '
                                      '수 있도록 FastAPI 응답을 Flutter 화면에 연결했습니다.',
                                'en': 'I converted model coordinates to source-image and app-display coordinates '
                                      'and passed position, symptom and confidence together. FastAPI responses '
                                      'were connected to Flutter so users could inspect individual predictions '
                                      'and detection history by tank.'}],
                'visual': {'images': [('evidence/fish-history.png',
                                       {'ko': '실제 앱의 수조별 탐지 결과 기록. 안내 문구는 규칙 기반 출력입니다.',
                                        'en': 'Actual detection-result history by tank. Guidance text is '
                                              'rule-based.'})],
                           'phones': True}},
               {'id': 'learning',
                'label': {'ko': '04 · 배운 점', 'en': '04 · What I learned'},
                'title': {'ko': '전처리부터 사용자 화면까지, 같은 대상을 보존합니다.',
                          'en': 'Preserving the same object from preprocessing to the interface.'},
                'paragraphs': [{'ko': '라벨의 의미, 탐지된 개체, 크롭 분류와 표시 좌표가 연결되어야 결과를 설명할 수 있었습니다. 학습 데이터 조정과 검증을 분리하고, '
                                      '단계별 병목과 최종 화면의 대응을 함께 확인하는 기준을 얻었습니다.',
                                'en': 'Explaining a result required the label meaning, detected object, crop '
                                      'classification and display coordinates to stay aligned. I learned to '
                                      'separate training-data changes from validation and inspect both '
                                      'stage-level bottlenecks and final overlays.'}]}],
  'links': [({'ko': '모델·앱 코드와 학습 결과', 'en': 'Model/app code and training results'},
             'https://github.com/jiwoo1105/fish-disease-detection'),
            ({'ko': '전체 시연 영상', 'en': 'Full demonstration'}, 'https://youtu.be/3LDmc6zdG0A')],
  'facts': [({'ko': '분류 검증', 'en': 'Classification validation'},
             {'ko': 'Top-1 87.68% · 7개 클래스', 'en': 'Top-1 87.68% · 7 classes'},
             True),
            ({'ko': '별도 탐지 지표', 'en': 'Separate detection metric'},
             {'ko': 'mAP50 0.4455', 'en': 'mAP50 0.4455'},
             False)]},
 {'slug': 'medguard',
  'title': 'MedGuard',
  'category': {'ko': '의료영상 · AI 보안 실험', 'en': 'Medical imaging · AI security experiments'},
  'subtitle': {'ko': '흉부 X-ray 분류기의 공격·방어를 비교했습니다. 기록된 DiffAttack 조건에서 Medical DiffPure는 Vanilla DiffPure보다 '
                     '4.84%p 높은 정확도를 보였습니다.',
               'en': 'I compared attacks and defenses for a chest X-ray classifier. Under the recorded DiffAttack '
                     'conditions, Medical DiffPure exceeded Vanilla DiffPure accuracy by 4.84 percentage points.'},
  'desc': {'ko': '흉부 X-ray 분류기에 대한 FGSM·PGD·잠재공간 공격을 비교하고, FFT 분석과 의료 도메인 VAE를 결합한 정화 흐름을 실험했습니다.',
           'en': 'I compared FGSM, PGD, and latent-space attacks on a chest X-ray classifier and experimented '
                 'with a purification pipeline combining FFT analysis and a medical-domain VAE.'},
  'role': {'ko': '공격·방어 실험, 주파수 분석, 비교 시연',
           'en': 'Attack/defense experiments, frequency analysis, comparison demo'},
  'period': '2026.02–2026.06',
  'context': {'ko': '의료영상 분류 강건성 실험', 'en': 'Robustness experiments for medical-image classification'},
  'stack': 'PyTorch / ResNet-50 / RoentGen VAE / FFT / Gradio',
  'repo': 'https://github.com/jiwoo1105/AISecurity',
  'video': 'medguard-demo.mp4',
  'poster': 'medguard-poster.jpg',
  'caption': {'ko': '공격 전후와 방어 결과를 비교하는 실제 시연', 'en': 'Demo comparing original, attacked, and purified inputs'},
  'sections': [{'id': 'problem',
                'label': {'ko': '01 · 문제 정의', 'en': '01 · The problem'},
                'title': {'ko': '공격을 지우는 과정에서, 분류에 필요한 정보도 사라질 수 있습니다.',
                          'en': 'Removing an attack can also remove information needed for classification.'},
                'paragraphs': [{'ko': '흉부 X-ray 분류기에 대한 공격 방어는 노이즈를 많이 제거하는 문제로만 볼 수 없었습니다. 입력을 바꾸는 정화가 분류 결과와 원래 '
                                      '영상 구조에 함께 영향을 주기 때문입니다. 저는 ResNet-50 폐렴 분류기와 FGSM·PGD·DiffAttack 계열 공격, '
                                      'FFT 분석과 정화 비교를 연결했습니다.',
                                'en': 'Defending a chest X-ray classifier was not simply a matter of removing '
                                      'more noise. Purification changes both the classification input and its '
                                      'structure. I connected a ResNet-50 pneumonia classifier, FGSM, PGD and '
                                      'DiffAttack-style attacks, FFT analysis and purification comparisons.'}],
                'visual': {'images': [('evidence/medguard-attacks.jpg',
                                       {'ko': '실제 Gradio 시연: 같은 입력에 대한 공격별 이미지와 예측 비교.',
                                        'en': 'Actual Gradio demo comparing attacked images and predictions for '
                                              'the same input.'})]}},
               {'id': 'approach',
                'label': {'ko': '02 · 대응 설계', 'en': '02 · The approach'},
                'title': {'ko': '공격 유형과 정화 강도를 함께 비교했습니다.',
                          'en': 'Comparing attack characteristics and purification strength together.'},
                'paragraphs': [{'ko': 'FFT로 주파수 변화를 살피고, RoentGen VAE 정화와 입력 이미지의 블렌딩을 조절했습니다. 강한 정화를 일률적으로 '
                                      '적용하기보다 공격 조건별 결과와 폐 영역 구조의 일치도를 함께 검토하는 실험 경로를 구성했습니다.',
                                'en': 'I inspected frequency changes with FFT and varied RoentGen VAE '
                                      'purification and blending with the input. The experimental path considers '
                                      'attack conditions and lung-region structure alongside the purification '
                                      'result.'},
                               {'ko': '주파수 변화가 작다고 해서 정상 이미지와 잠재공간 공격을 확실히 구분할 수는 없습니다. 따라서 데모의 분기 규칙은 실험용 휴리스틱이며 '
                                      '일반적인 공격 탐지 보장으로 해석하지 않았습니다.',
                                'en': 'Small frequency changes do not reliably distinguish a clean image from a '
                                      'latent-space attack. The demo’s routing rule is therefore an experimental '
                                      'heuristic, not a guarantee of attack detection.'}],
                'visual': {'video': 'medguard-demo.mp4',
                           'poster': 'evidence/medguard-defense.jpg',
                           'caption': {'ko': '공격과 방어 결과를 비교하는 실제 시연. 개별 예시는 전체 평가 통계를 대신하지 않습니다.',
                                       'en': 'Actual attack/defense comparison demo. Individual examples do not '
                                             'replace aggregate evaluation results.'}},
                'insight': {'ko': '방어 후 분류 점수와 이미지 보존을 같은 것으로 보지 않게 됐습니다. 더 강한 변환이 필요한 정보까지 바꾸는지 함께 확인해야 했습니다.',
                            'en': 'I learned to distinguish post-defense classification scores from image '
                                  'preservation, checking whether stronger transformations also changed useful '
                                  'information.'}},
               {'id': 'results',
                'label': {'ko': '03 · 확인한 결과', 'en': '03 · Results'},
                'title': {'ko': '비교 조건을 고정하고, 결과의 범위를 남겼습니다.',
                          'en': 'Reporting the result together with its comparison conditions.'},
                'paragraphs': [{'ko': '공개 저장소의 동일 DiffAttack 조건에서 Medical DiffPure는 78.56%, Vanilla DiffPure는 '
                                      '73.72%로 4.84%p 차이를 기록했습니다. Medical DiffPure의 FGSM·PGD 조건 정확도는 각각 58.31%, '
                                      '61.47%였습니다.',
                                'en': 'Under the repository’s DiffAttack setup, Medical DiffPure achieved 78.56% '
                                      'accuracy versus 73.72% for Vanilla DiffPure, a 4.84 percentage-point '
                                      'difference. Medical DiffPure recorded 58.31% and 61.47% under FGSM and '
                                      'PGD, respectively.'},
                               {'ko': '이 결과는 저장소에 기록된 설정의 비교입니다. 새로운 공격·다른 분포·정화 후 병변 보존까지 검증한 결과는 아니며, 실제 임상 적용 '
                                      '효과와도 구분합니다.',
                                'en': 'These are comparisons under the recorded settings. They do not validate '
                                      'unseen attacks, other distributions, preservation of pathology after '
                                      'purification or clinical outcomes.'}],
                'visual': {'images': [('evidence/medguard-defense.jpg',
                                       {'ko': '실제 방어 비교 화면. 정량 수치는 별도의 저장소 평가 기록을 사용했습니다.',
                                        'en': 'Actual defense-comparison screen. Quantitative figures come from '
                                              'the separate repository evaluation.'})]}},
               {'id': 'learning',
                'label': {'ko': '04 · 배운 점', 'en': '04 · What I learned'},
                'title': {'ko': '방어의 목표를, 정확도 회복과 정보 보존으로 나눴습니다.',
                          'en': 'Separating accuracy recovery from information preservation.'},
                'paragraphs': [{'ko': '공격 조건을 명시하고 같은 조건의 비교를 남기는 것이 결과 해석에 중요했습니다. 새로운 방어를 평가할 때도 평균 점수뿐 아니라 어떤 '
                                      '입력을 바꿨고 무엇이 보존됐는지 확인해야 한다는 기준을 얻었습니다.',
                                'en': 'Stating the attack conditions and preserving comparable results was '
                                      'essential to interpretation. I learned to evaluate a defense by what it '
                                      'changes and preserves as well as by its average score.'}]}],
  'links': [({'ko': '공격·방어 코드와 실험 기록', 'en': 'Attack/defense code and experiment records'},
             'https://github.com/jiwoo1105/AISecurity')],
  'facts': [({'ko': 'DiffAttack 비교', 'en': 'Under DiffAttack'},
             {'ko': 'Medical DiffPure 78.56% / 기본 DiffPure 73.72%',
              'en': 'Medical DiffPure 78.56% / vanilla DiffPure 73.72%'},
             True),
            ({'ko': '검증 범위', 'en': 'Scope'},
             {'ko': '실험 조건 내 방어 비교', 'en': 'Defense comparison under the tested conditions'},
             False)]},
 {'slug': 'medai-agent',
  'title': 'MedAI Agent',
  'category': {'ko': 'LLM 워크플로우 · 프로토타입', 'en': 'LLM workflows · Prototype'},
  'subtitle': {'ko': '텍스트·음성·이미지 입력에서 약물 정보 조회와 8단계 LLM 처리를 거쳐 보고서를 보여주는 프로토타입을 구현했습니다.',
               'en': 'I built a prototype that takes text, voice, or image input through drug-information lookup '
                     'and eight LLM stages to a report.'},
  'desc': {'ko': '텍스트·음성·이미지 입력을 약물 정보 조회와 8단계 LLM 워크플로우에 연결한 프로토타입입니다. FastAPI와 React로 처리 단계와 분석 결과를 보여줍니다.',
           'en': 'A prototype connecting text, voice, and image inputs to medication-information retrieval and an '
                 'eight-stage LLM workflow. FastAPI and React expose the processing stages and resulting report.'},
  'role': {'ko': '입력·약물 조회·에이전트 흐름·결과 화면 연결',
           'en': 'Input, medication lookup, agent orchestration, and results interface'},
  'period': {'ko': '2025 · 딥러닝 프로젝트', 'en': '2025 · Deep learning project'},
  'context': {'ko': '약물 정보 분석 프로토타입', 'en': 'Medication-information analysis prototype'},
  'stack': 'Python / FastAPI / GPT-4o / React / Vite',
  'repo': 'https://github.com/jiwoo1105/MedAI_Agent',
  'video': 'evidence/medai-result.mp4',
  'poster': 'evidence/medai-result.jpg',
  'caption': {'ko': '원본 시연 00:30–01:20 발췌 · 처리 진행과 결과 화면',
              'en': 'Original demo excerpt, 00:30–01:20 · Processing and results'},
  'sections': [{'id': 'problem',
                'label': {'ko': '01 · 문제 정의', 'en': '01 · The problem'},
                'title': {'ko': '자유로운 입력을, 이어서 처리할 수 있는 정보로 바꾸기.',
                          'en': 'Turning free-form input into information the next stage can use.'},
                'paragraphs': [{'ko': '텍스트·음성·이미지로 들어온 약물 정보를 같은 흐름에서 처리하고, 사용자가 읽을 수 있는 보고서로 전달하는 프로토타입입니다. 저는 '
                                      '입력 화면, 약물 정보 API, 역할을 나눈 LLM 처리와 결과 UI를 연결했습니다.',
                                'en': 'This prototype handles medication information supplied as text, voice or '
                                      'images through a shared workflow and presents a readable report. I '
                                      'connected input interfaces, a medication-information API, role-specific '
                                      'LLM processing and the results UI.'}],
                'visual': {'images': [('evidence/medai-input.jpg',
                                       {'ko': '실제 시연의 입력 화면. 텍스트·음성·이미지 입력을 제공합니다.',
                                        'en': 'Input screen from the actual demo, supporting text, voice and '
                                              'image input.'})]}},
               {'id': 'workflow',
                'label': {'ko': '02 · 처리 흐름', 'en': '02 · Processing flow'},
                'title': {'ko': '입력 이해부터 보고서까지, 단계별 결과를 이어 붙였습니다.',
                          'en': 'Connecting stage outputs from input understanding to the report.'},
                'paragraphs': [{'ko': '입력 이해·약물 인식·기본 지식·심화 분석·부작용 검토·근거 설명·개인화 정보·보고서 생성의 8단계를 구성했습니다. 앞 단계의 출력을 '
                                      '다음 단계에 전달하고, FastAPI 응답을 React의 요약과 상세 화면으로 연결했습니다.',
                                'en': 'The eight stages cover input understanding, medication recognition, '
                                      'background knowledge, detailed analysis, side-effect review, evidence '
                                      'explanation, contextual information and report generation. Outputs pass '
                                      'between stages, and FastAPI responses feed React summary and detail '
                                      'views.'},
                               {'ko': '여덟 단계는 역할을 나눈 LLM 호출이며 독립된 의료 전문가의 검증은 아닙니다. 식약처 e약은요 API에서 조회한 사실과 모델이 '
                                      '생성한 설명을 구분해 해석해야 합니다.',
                                'en': 'These stages are LLM calls assigned different roles, not independent '
                                      'medical experts. Facts retrieved from the MFDS medication API must be '
                                      'distinguished from model-generated explanations.'}],
                'visual': {'video': 'evidence/medai-result.mp4',
                           'poster': 'evidence/medai-result.jpg',
                           'caption': {'ko': '원본 시연에서 발췌한 처리·결과 화면. 긴 시연의 해당 구간을 담았습니다.',
                                       'en': 'Processing and result screens excerpted from the original '
                                             'demonstration.'}},
                'outcome': {'ko': '입력부터 조회·생성·보고서 표시까지 연결한 프로토타입과 시연을 확보했습니다. 위험도·권장사항의 의료적 정확도는 검증하지 않았습니다.',
                            'en': 'The prototype and demo connect input, lookup, generation and report display. '
                                  'Medical accuracy of the risk indicators and recommendations was not '
                                  'validated.'}},
               {'id': 'interface',
                'label': {'ko': '03 · 사용자에게 전달', 'en': '03 · Communicating the workflow'},
                'title': {'ko': '여러 호출의 결과를, 읽을 수 있는 하나의 화면으로.',
                          'en': 'Presenting a multi-call workflow in a readable result screen.'},
                'paragraphs': [{'ko': '처리 중에는 진행 상태를 보여주고, 최종 결과는 요약·주요 내용·주의사항과 상세 설명으로 나눴습니다. 생성된 내용을 그대로 길게 '
                                      '나열하기보다 사용자가 현재 단계와 결과를 구분해 볼 수 있도록 구성했습니다.',
                                'en': 'The interface shows progress during processing and organizes the result '
                                      'into a summary, key points, cautions and detail. This helps users '
                                      'distinguish the workflow state from its output rather than reading an '
                                      'undifferentiated block of generated text.'}],
                'visual': {'images': [('evidence/medai-result.jpg',
                                       {'ko': '실제 결과 UI. 표시된 위험도는 모델 출력이며 임상적으로 검증된 확률이 아닙니다.',
                                        'en': 'Actual results UI. The displayed risk indicator is model output, '
                                              'not a clinically validated probability.'})]}},
               {'id': 'learning',
                'label': {'ko': '04 · 배운 점과 과제', 'en': '04 · Learning & remaining work'},
                'title': {'ko': '연결한 단계 수보다, 정보가 어떻게 전달되는지가 중요했습니다.',
                          'en': 'The flow of information mattered more than the number of stages.'},
                'paragraphs': [{'ko': '약물명이나 앞 단계의 해석이 후속 설명의 입력이 되는 구조를 만들며, 오류가 어디에서 생겼는지 확인할 수 있어야 한다는 점을 '
                                      '배웠습니다. 현재 성과는 실행 가능한 연결과 UI이며, 단계별 제거 실험이나 의료적 정확도 검증까지 완료한 프로젝트는 아닙니다.',
                                'en': 'Building a system where drug names and early interpretations become later '
                                      'inputs highlighted the need to locate errors in the flow. The demonstrated '
                                      'result is the integration and UI; stage-ablation studies and '
                                      'medical-accuracy validation remain uncompleted.'},
                               {'ko': '다음 검증에서는 조회한 사실과 생성한 설명을 추적하고, 특정 단계를 제거했을 때 품질과 지연이 어떻게 달라지는지 확인하려 합니다. 이 '
                                      '계획을 이미 입증한 품질 개선 성과와 구분합니다.',
                                'en': 'Further evaluation should trace retrieved facts and generated explanations '
                                      'and measure how removing stages changes quality and latency. This is a '
                                      'validation plan, not a claimed quality improvement.'}]}],
  'links': [({'ko': '8단계 워크플로우와 시연 자료', 'en': 'Eight-stage workflow and demo'},
             'https://github.com/jiwoo1105/MedAI_Agent')],
  'facts': [({'ko': '구성', 'en': 'Workflow'}, {'ko': '8단계 LLM 워크플로우', 'en': 'Eight-stage LLM workflow'}, True),
            ({'ko': '현재 단계', 'en': 'Status'},
             {'ko': '약물 정보 분석 프로토타입', 'en': 'Medication-information analysis prototype'},
             False)]}]
