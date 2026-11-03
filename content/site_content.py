"""Reviewed bilingual content. Regenerate the static site with scripts/build.py."""

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
 'subtitle': {'ko': '한 사람의 움직임을 따라, 영상에서 3D 모션 데이터까지.', 'en': 'From a person’s movement on screen to 3D motion data.'},
 'desc': {'ko': 'PHALP 인물 추적, 선수별 크롭, HMR 2.0 복원과 실제 SMPL 메쉬 재생을 연결한 연구 파이프라인입니다.',
          'en': 'A research pipeline connecting PHALP person tracking, player-specific crops, HMR 2.0 reconstruction, '
                'and replay of the resulting SMPL meshes.'},
 'role': {'ko': '파이프라인 전반 설계·구현 주도, 모델 연동·실험·결과 검수',
          'en': 'Led the overall pipeline design and implementation, including model integration, experiments, and output review'},
 'period': {'ko': '2026.07– · 연구 진행 중', 'en': 'Since Jul 2026 · Ongoing research'},
 'context': {'ko': 'AIV Lab / ETRI 연구과제', 'en': 'AIV Lab / ETRI research project'},
 'stack': 'Python / PyTorch / ViTDet-H / PHALP / HMR 2.0 / SMPL / MuJoCo',
 'repo': 'https://github.com/DKU-AIM/video-motion-pipeline',
 'caption': {'ko': '같은 6초의 선수 크롭 ↔ HMR 2.0 실제 출력 · 상세에서 단계별 시연',
             'en': 'The same six seconds: person crop ↔ actual HMR 2.0 output. Explore every stage in the case study.'},
 'sections': [{'id': 'problem',
               'label': {'ko': '목표와 역할', 'en': 'Goal & contribution'},
               'title': {'ko': '같은 사람의 영상·시간·모션을 하나의 단위로.',
                         'en': 'One data unit: the same person, time span, and motion.'},
               'paragraphs': [{'ko': '목표는 사람의 동작을 담은 영상과 3D 모션을 대응시켜, 후속 로봇 학습 연구에 활용할 데이터 단위를 만드는 것입니다. 그라운딩 모델의 행동 '
                                     '구간만 믿기보다, 인물 ID와 원본 시간축을 보존하고 각 단계의 결과를 대조하는 방식으로 설계를 발전시켰습니다.',
                               'en': 'The goal is to pair video of human actions with 3D motion as data units for '
                                     'future robot-learning research. I developed the design around preserving person '
                                     'IDs and source timestamps and reviewing each stage, rather than relying solely '
                                     'on action intervals predicted by grounding models.'}],
               'items': [({'ko': '직접 설계·구현', 'en': 'Design & implementation'},
                          {'ko': '파이프라인 전반의 설계와 구현을 주도했습니다. 모델별 GPU 실행 환경과 실행기를 구성하고, 그라운딩 비교에서 인물 추적·선수별 크롭·HMR 2.0 재추론·SMPL 메쉬 재생까지 연결했습니다. 각 단계의 입출력과 원본 시간·인물 ID를 정리해 결과를 대조할 수 있게 했습니다.',
                           'en': 'I led the overall pipeline design and implementation: GPU environments and model runners, grounding comparisons, person tracking, player-specific crops, HMR 2.0 re-inference, and SMPL mesh replay. I organized stage inputs and outputs around source timestamps and person IDs so that results could be compared across stages.'}),
                         ({'ko': '실험·품질 검수', 'en': 'Experiments & quality review'},
                          {'ko': '실험 대상·조건과 검수 기준을 정하고, 누락·새 ID 발생·타인 오연결을 구분했습니다. 문제가 생긴 사람과 시간 구간을 제외·보류하고 정상 구간은 보존하는 선별 기준을 정리했습니다. 사전학습 모델을 연동했으며, 구현·실행·문서화에는 AI 코딩 도구를 활용했습니다.',
                           'en': 'I defined experiment conditions and review criteria, distinguishing missing detections, newly assigned IDs, and associations with the wrong person. I established criteria to exclude or hold problematic person-time intervals while retaining unaffected segments. The pipeline integrates pretrained models; AI coding tools supported implementation, execution, and documentation.'})]},
              {'id': 'grounding',
               'label': {'ko': '설계를 바꾼 근거', 'en': 'Why the design changed'},
               'title': {'ko': 'FPS를 높여도, 놓치는 행동은 남았습니다.', 'en': 'Higher sampling rates still missed actions.'},
               'paragraphs': [{'ko': '7개 모델 × 5개 FPS × 2개 영상 × 3개 쿼리로 얻은 210개 응답을 비교했습니다. 모델별 출력 시각을 공통 형식으로 정리하고, '
                                     '지나치게 넓은 구간과 영상에 없는 행동을 원본에 대조했습니다. 210은 영상 수가 아니라 응답 수입니다.',
                               'en': 'I compared 210 responses: seven models × five FPS settings × two videos × three '
                                     'queries. After normalizing timestamps, I checked overly broad intervals and '
                                     'nonexistent actions against the footage. This is a response count, not a video '
                                     'count.'},
                              {'ko': '짧은 구간의 행동 판별을 앞에 연결해도 오탐과 누락이 함께 나타났습니다. 따라서 그라운딩 결과를 곧바로 정답으로 쓰지 않고, 인물 추적과 원본 '
                                     '시간축을 먼저 보존한 뒤 동작 설명을 연결하는 방향을 택했습니다.',
                               'en': 'Adding short-clip action classification still produced both false positives and '
                                     'misses. Rather than treating grounding outputs as labels, I prioritized person '
                                     'tracks and source timestamps before attaching action descriptions.'}]},
              {'id': 'pipeline',
               'label': {'ko': '파이프라인 설계', 'en': 'Pipeline design'},
               'title': {'ko': '추적용 추정과, 크롭 후 복원을 나눴습니다.',
                         'en': 'Tracking estimates and crop-based reconstruction serve different purposes.'},
               'paragraphs': [{'ko': '먼저 전체 화면에서 ViTDet-H가 사람을 찾고, HMR 2.0이 몸과 카메라 정보를 추정합니다. PHALP는 이 몸·위치·외형 정보를 프레임 '
                                     '사이에서 연결해 ID를 부여합니다. 따라서 HMR 2.0은 추적이 모두 끝난 뒤 처음 등장하는 모델이 아닙니다.',
                               'en': 'First, ViTDet-H detects people in full-frame footage, and HMR 2.0 estimates body '
                                     'and camera parameters. PHALP associates body, location, and appearance '
                                     'information across frames to assign identities. HMR 2.0 therefore also '
                                     'contributes to the tracking stage.'},
                              {'ko': '이후 검수한 선수와 시간 구간을 직접 고르고, 인물 박스에 각 변 10% 여백을 더해 크롭합니다. 선택한 선수 중심으로 복원을 다시 확인하기 '
                                     '위해 이 크롭에 HMR 2.0을 재실행했습니다. 원본 시각·ID·크롭 좌표를 함께 남겨 복원 결과를 원래 장면으로 되짚을 수 있게 했습니다.',
                               'en': 'I then manually select a reviewed player and time interval and crop the person '
                                     'box with 10% margins on each side. I rerun HMR 2.0 on those crops to inspect '
                                     'reconstruction around the selected player. Source times, IDs, and crop '
                                     'coordinates are retained so that outputs can be traced back to the original '
                                     'scene.'}],
               'items': [({'ko': '연결 기준', 'en': 'Alignment'},
                          {'ko': '시연의 모든 단계는 원본 15:35–15:41, 60 FPS·360프레임에 대응합니다.',
                           'en': 'Every demo stage maps to source time 15:35–15:41: 360 frames at 60 FPS.'}),
                         ({'ko': '저장 결과', 'en': 'Saved outputs'},
                          {'ko': 'SMPL 자세·체형·카메라 추정값, 프레임별 메쉬 정점·면과 관절 좌표. 월드 좌표계의 이동 경로는 별도 과제입니다.',
                           'en': 'SMPL pose, shape, camera estimates, mesh vertices and faces, and joint coordinates. '
                                 'Recovering motion in world coordinates is a separate task.'})]},
              {'id': 'experiments',
               'label': {'ko': '완료한 실험', 'en': 'Completed experiments'},
               'title': {'ko': '농구의 선수별 복원에서, 공연의 가림 검수까지.',
                         'en': 'From player-specific reconstruction to occlusion review.'},
               'paragraphs': [{'ko': '농구에서는 5개 클립의 96초·4,240프레임을 처리하고, 직접 선택한 선수 5명·6구간에 각 변 10% 여백을 둔 크롭과 HMR 2.0 '
                                     '재추론을 적용했습니다. 원래 FPS와 크롭의 픽셀 크기를 유지했습니다.',
                               'en': 'For basketball, I processed 96 seconds and 4,240 frames across five clips, then '
                                     'applied crops with 10% margins on each side and HMR 2.0 re-inference to six '
                                     'manually selected segments from five players. Original FPS and crop pixel '
                                     'dimensions were preserved.'},
                              {'ko': '대표 선수의 드리블 360프레임과 슛 244프레임에서는 저장된 SMPL 메쉬를 MuJoCo에 불러와 원본 배경 없이 재생했습니다. 위 플레이어의 '
                                     '‘3D 재생’은 이 드리블 결과입니다. 실제 추론 데이터를 확인하는 재생 시험으로, 로봇의 균형 제어나 동작 추종을 검증한 실험은 아닙니다.',
                               'en': 'For the featured player’s 360-frame dribble and 244-frame shot, the saved SMPL '
                                     'meshes were loaded into MuJoCo and replayed without the original background. The '
                                     'player above shows the dribble under “3D replay.” This playback checks the '
                                     'inferred data; it does not validate robot balance control or motion tracking.'},
                              {'ko': '후속 공연 실험은 약 30초씩 10개 구간입니다. 이동 범위를 포함하는 고정 그룹 ROI에서 검출·복원·ID 연결을 수행하고, 입력·메쉬 '
                                     'ID·비교 영상 총 30개와 수동 검수 기록을 정리했습니다.',
                               'en': 'The follow-up performance study used ten clips of about 30 seconds each. '
                                     'Detection, reconstruction, and identity association ran within fixed group ROIs '
                                     'covering movement, producing 30 input, mesh-ID, and comparison videos alongside '
                                     'manual review records.'}],
               'table': {'caption': {'ko': '각 실험에서 확보한 것', 'en': 'What each experiment established'},
                         'headers': [{'ko': '범위', 'en': 'Scope'},
                                     {'ko': '산출물', 'en': 'Output'},
                                     {'ko': '검증 수준', 'en': 'Validation scope'}],
                         'rows': [[{'ko': '그라운딩 210개 응답', 'en': '210 grounding responses'},
                                   {'ko': '공통 시간 형식·오탐/누락 비교', 'en': 'Normalized times and false-positive/miss review'},
                                   {'ko': '원본 장면 대조', 'en': 'Review against footage'}],
                                  [{'ko': '농구 선수별 6구간', 'en': '6 player-specific segments'},
                                   {'ko': '크롭·메쉬·SMPL 데이터', 'en': 'Crops, meshes, and SMPL data'},
                                   {'ko': '선택 구간의 수동 검수', 'en': 'Manual review of selected segments'}],
                                  [{'ko': '공연 10구간', 'en': '10 performance clips'},
                                   {'ko': 'ID 오류 유형·제외/보류 기준',
                                    'en': 'Identity-error categories and selection criteria'},
                                   {'ko': '표본 프레임+관측 로그', 'en': 'Sampled frames and observation logs'}]]},
               'note': {'ko': '처리량과 산출물 수는 정확도가 아닙니다. IDF1·HOTA·3D 정답 기반 정확도는 산출하지 않았습니다.',
                        'en': 'Processed frames and output counts are not accuracy measurements. IDF1, HOTA, and 3D '
                              'ground-truth accuracy were not evaluated.'}},
              {'id': 'review',
               'label': {'ko': '핵심 난제와 판단', 'en': 'Challenge & decisions'},
               'title': {'ko': '잠깐 사라진 사람과, 다른 사람에게 붙은 ID를 구분했습니다.',
                         'en': 'A temporary gap is different from an ID assigned to someone else.'},
               'paragraphs': [{'ko': '같은 공연 구간 M09에서 두 종류의 오류를 확인했습니다. ID5는 18프레임, 약 0.60초 누락된 뒤 같은 사람·같은 ID로 돌아왔습니다. '
                                     '이 경우 사람 전체를 버리는 대신 누락 시간만 제외할 수 있습니다.',
                               'en': 'In performance clip M09, ID5 disappeared for 18 frames, about 0.60 seconds, then '
                                     'returned on the same person with the same ID. This supports excluding the '
                                     'missing interval rather than discarding the person’s entire track.'},
                              {'ko': '다른 공연자는 프레임 819의 ID4에서 820의 ID28로 바뀌었습니다. 마지막 분리 표본인 프레임 899에서는 기존 ID4가 다른 공연자에게 '
                                     '붙었습니다. 새 ID가 생긴 시점과 잘못된 연결을 확인한 시점을 따로 기록하고, 관련 두 사람의 경계를 보류해 앞뒤 구간을 나누는 기준을 '
                                     '세웠습니다.',
                               'en': 'Another performer changed from ID4 at frame 819 to ID28 at frame 820. At the '
                                     'final separated sample, frame 899, the old ID4 was attached to a different '
                                     'performer. I recorded the new-ID event separately from the confirmed wrong '
                                     'association and defined a rule to withhold the uncertain boundary and split the '
                                     'affected tracks.'}],
               'note': {'ko': '가림 때문에 최초 오연결 프레임은 확정하지 않았습니다. 검수한 표본의 판단을 전 프레임 추적 정확도로 확대하지 않습니다.',
                        'en': 'Occlusion prevented identifying the first incorrect-association frame. Sampled review '
                              'findings are not a dense tracking-accuracy evaluation.'}},
              {'id': 'learning',
               'label': {'ko': '결과와 다음 단계', 'en': 'Outcome & next steps'},
               'title': {'ko': '다음 목표는, 검수한 모션에 행동 설명을 연결하는 것.',
                         'en': 'Next: connect reviewed motion to action descriptions.'},
               'paragraphs': [{'ko': '이번 연구에서 확보한 것은 실제 영상에 대응하는 사람별 크롭·3D 모션과, 사용할 구간을 판단하는 기준입니다. 추론이 끝났다는 사실만으로 학습에 '
                                     '적합한 데이터가 되지는 않았습니다. 인물·시간·모션의 대응을 유지하고 오류 구간을 따로 표시해야 결과를 다시 확인하고 선별할 수 있었습니다.',
                               'en': 'The work produced person-specific crops and 3D motion aligned with real footage, '
                                     'along with criteria for selecting usable segments. Finishing inference alone did '
                                     'not make the outputs suitable for learning. Preserving identity, time, and '
                                     'motion alignment—and marking faulty intervals—made the results reviewable.'},
                              {'ko': '이 기반 위에 자동 행동 분할과 캡셔닝, 품질 승인 단계를 연결할 계획입니다. 로봇에 적용하려면 별도로 관절 매핑과 리타게팅, 접촉·균형 제어, '
                                     '정책 학습을 검증해야 합니다. 현재의 메쉬 재생과 이 후속 목표를 구분해 연구를 이어가고 있습니다.',
                               'en': 'The next steps are automatic action segmentation, captioning, and quality '
                                     'approval. Robot applications will additionally require joint mapping, '
                                     'retargeting, contact and balance control, and policy-learning validation. These '
                                     'remain separate from the mesh playback demonstrated here.'}]}],
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
            {'ko': '추적·크롭·복원·메쉬 재생 및 구간 검수', 'en': 'Tracking, crops, reconstruction, mesh replay, and segment review'},
            False)],
 'cover': {'video': 'motion/cover.mp4', 'poster': 'motion/cover.jpg',
           'caption': {'ko': '같은 프레임의 원본 영상, PHALP 인물 추적, 실제 SMPL 메쉬 재생',
                       'en': 'Frame-aligned source footage, PHALP person tracking, and actual SMPL mesh replay'}},
 'card_facts': [({'ko': '데이터 연결', 'en': 'Data alignment'},
                 {'ko': '원본 시각·인물 ID·크롭 좌표·3D 모션을 프레임 단위로 연결',
                  'en': 'Source time, person ID, crop coordinates, and 3D motion aligned frame by frame'}, False),
                ({'ko': '검수 기준', 'en': 'Quality review'},
                 {'ko': '누락·ID 변경·오연결을 구분하고, 문제 구간의 제외·보류 기준 수립',
                  'en': 'Criteria for excluding or holding segments with gaps, ID changes, or incorrect associations'}, False)],
 'video': 'motion/compare.mp4',
 'poster': 'motion/compare.jpg',
 'showcase': {'title': {'ko': '먼저, 영상으로 살펴보세요.', 'en': 'See the pipeline in motion.'},
              'source': 'https://www.youtube.com/watch?v=kXuDZJ2TT3I&t=935s',
              'stages': [{'label': {'ko': '비교 보기', 'en': 'Compare'},
                          'title': {'ko': '선수 영상과 복원 결과를 나란히', 'en': 'Person crop and reconstruction, side by side'},
                          'description': {'ko': '왼쪽은 선택한 선수의 크롭, 오른쪽은 같은 프레임에 실제 HMR 2.0 메쉬를 겹친 결과입니다. 단계를 바꾸면 같은 시점이 '
                                                '유지됩니다.',
                                          'en': 'Left: the selected player’s crop. Right: the actual HMR 2.0 mesh '
                                                'overlaid on the same frame. Switching stages preserves the playback '
                                                'position.'},
                          'video': 'motion/compare.mp4',
                          'poster': 'motion/compare.jpg'},
                         {'label': {'ko': '입력', 'en': 'Input'},
                          'title': {'ko': '01. 공개 경기 영상에서 시작', 'en': '01. Start with game footage'},
                          'description': {'ko': 'FIBA U20 결승 영상의 15:35–15:41 구간입니다. 남색 21번 선수를 대상으로, 60 FPS의 같은 '
                                                '360프레임을 모든 단계에서 사용했습니다.',
                                          'en': 'A six-second excerpt from the FIBA U20 final, 15:35–15:41. Every '
                                                'stage uses the same 360 frames at 60 FPS, focusing on the player in '
                                                'navy jersey 21.'},
                          'video': 'motion/input.mp4',
                          'poster': 'motion/input.jpg'},
                         {'label': {'ko': '추적', 'en': 'Track'},
                          'title': {'ko': '02. 인물 박스와 ID를 연결', 'en': '02. Associate people across frames'},
                          'description': {'ko': 'ViTDet-H 검출과 HMR 2.0의 몸·외형 특징을 사용해 PHALP가 인물을 연결합니다. 이 시연의 대상은 ID '
                                                '9이며, 공 추적 결과는 포함하지 않습니다.',
                                          'en': 'PHALP associates people using ViTDet-H detections and HMR 2.0-based '
                                                'body and appearance features. The selected player is ID 9. This demo '
                                                'does not include ball tracking.'},
                          'video': 'motion/tracking.mp4',
                          'poster': 'motion/tracking.jpg'},
                         {'label': {'ko': '크롭', 'en': 'Crop'},
                          'title': {'ko': '03. 선수와 연속 구간을 선택', 'en': '03. Select a player and a continuous segment'},
                          'description': {'ko': '검수한 ID 9의 6초를 직접 선택했습니다. 매 프레임 선수 박스의 각 변에 10% 여백을 더하고, 원본 픽셀 크기를 유지한 '
                                                '채 고정 캔버스에 배치했습니다.',
                                          'en': 'I manually selected six reviewed seconds of ID 9. Each frame’s player '
                                                'box is expanded by 10% on every side and placed on a fixed-size '
                                                'canvas without resizing the source pixels.'},
                          'video': 'motion/crop.mp4',
                          'poster': 'motion/crop.jpg'},
                         {'label': {'ko': '메쉬', 'en': 'Mesh'},
                          'title': {'ko': '04. 선수 크롭에서 3D 몸을 다시 추정',
                                    'en': '04. Re-estimate the body from the person crop'},
                          'description': {'ko': '선수 크롭에 HMR 2.0을 다시 실행해 SMPL 자세·체형·카메라 값과 메쉬를 저장했습니다. 영상 위의 청록색 몸은 이 '
                                                '추론에서 나온 실제 출력입니다.',
                                          'en': 'HMR 2.0 runs again on the person crop to save SMPL pose, shape, '
                                                'camera parameters, and meshes. The cyan body overlaid on the footage '
                                                'is the actual inference output.'},
                          'video': 'motion/overlay.mp4',
                          'poster': 'motion/overlay.jpg'},
                         {'label': {'ko': '3D 재생', 'en': '3D replay'},
                          'title': {'ko': '05. 저장한 메쉬를 배경 없이 재생',
                                    'en': '05. Replay the saved mesh without the video background'},
                          'description': {'ko': '저장된 6,890개 정점의 SMPL 메쉬를 MuJoCo에서 재생했습니다. 루트를 고정한 기구학적 재생이며, 월드 이동 경로 '
                                                '복원·충돌·균형 제어·로봇 학습은 포함하지 않습니다.',
                                          'en': 'The saved SMPL mesh, with 6,890 vertices per frame, is replayed in '
                                                'MuJoCo. This is fixed-root kinematic playback, without recovered '
                                                'world translation, collisions, balance control, or robot learning.'},
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
              'scope': {'ko': '지금 연결한 범위는 영상에서 사람별 모션을 복원하고 검수하는 단계입니다. 자동 행동 분할·캡셔닝·품질 승인과 로봇 정책 학습은 후속 과제로 남아 있습니다.',
                        'en': 'This pipeline currently reconstructs and reviews person-specific motion from video. '
                              'Automatic action segmentation, captioning, quality approval, and robot policy learning '
                              'remain future work.'}}},
 {'slug': 'danzzan',
  'title': {'ko': '단짠', 'en': 'Danzzan'},
  'category': {'ko': 'Backend · 실제 서비스 운영', 'en': 'Backend · Live service'},
  'subtitle': {'ko': '6,000명 이상이 사용한 축제 서비스에서, 예매와 인증이 실패하는 순간까지 설계했습니다.',
               'en': 'For a festival service used by 6,000+ people, I designed ticketing and authentication with failure paths in '
                     'mind.'},
  'desc': {'ko': '총학생회·네이버와 협업한 대학 축제 서비스입니다. Redis·Lua로 예매 상태와 재고를 처리하고, 인증·번역·관리자 설정을 개선하며 봄·가을 축제 운영에 참여했습니다.',
           'en': 'A university festival service built in collaboration with the student council and NAVER. I worked on Redis/Lua '
                 'ticket allocation, authentication, translation, and admin settings, and participated in spring and autumn festival '
                 'operations.'},
  'role': {'ko': 'Redis·Lua 예매 처리, JWT 인증, 번역·실패 대응',
           'en': 'Redis/Lua ticketing, JWT authentication, translation and failure handling'},
  'period': '2025.12–2026.09',
  'context': {'ko': '대학 축제 웹 서비스 / 팀 프로젝트', 'en': 'University festival web service / Team project'},
  'stack': 'Spring Boot / Redis / Lua / MySQL / React / Docker',
  'repo': 'https://github.com/DKU-Dan-Zzan/Danzzan-BE',
  'images': ['danzzan-home.webp', 'danzzan-map.webp', 'danzzan-queue.webp'],
  'caption': {'ko': '팀 서비스 실제 화면 · 축제 홈, 부스 지도, 티켓 예매', 'en': 'Actual team-service screens · Festival home, booth map, and ticketing'},
  'sections': [{'id': 'problem',
                'label': {'ko': '배경과 역할', 'en': 'Context & my role'},
                'title': {'ko': '몰리는 요청과 계속 바뀌는 운영 조건을 함께 다뤘습니다.', 'en': 'Handling traffic bursts and changing operational needs.'},
                'paragraphs': [{'ko': '학생에게 흩어진 부스 정보, 공연 일정, 공지와 예매를 한곳에서 제공하고 운영진이 현장 상황을 반영할 수 있도록 만든 팀 서비스입니다. 한정된 티켓의 중복 발급을 막는 '
                                      '일과 예매·입장 상태를 사용자에게 정확히 보여주는 일이 핵심 과제였습니다.',
                                'en': 'The team brought booth information, performances, notices, and ticket reservations into one '
                                      'service while allowing organizers to respond to on-site needs. Key challenges were preventing '
                                      'duplicate ticket allocation and presenting reservation and entry states accurately.'},
                               {'ko': '저는 Redis 대기열과 Lua 발급 처리, JWT 로그인·회원가입, 번역 기능과 실패 대응을 맡았습니다. 6,000명 이상의 실사용자와 두 차례 축제 운영은 팀 공동 '
                                      '성과입니다. 봄에는 예매·입장 흐름을, 가을에는 다국어 사용성을 개선했습니다.',
                                'en': 'I owned Redis queueing and Lua ticket issuance, JWT login/signup, and translation with failure '
                                      'handling. More than 6,000 real users and two festival deployments are shared team outcomes. '
                                      'Spring focused on ticketing and entry; autumn added multilingual usability.'}]},
               {'id': 'ticketing',
                'label': {'ko': '동시 요청 처리', 'en': 'Concurrent requests'},
                'title': {'ko': '대기열을 상태 전이와 재고 정합성 문제로 풀었습니다.', 'en': 'Treating the queue as a state and inventory problem.'},
                'paragraphs': [{'ko': '대기·입장 준비·예매 가능·완료·만료 상태를 구분하고, Lua Script로 입장 자격·중복 신청·남은 재고 확인과 차감을 한 번에 처리했습니다. 이 원자성은 Redis '
                                      '내부의 작업에 해당하며 MySQL까지 포함하는 분산 트랜잭션을 뜻하지 않습니다.',
                                'en': 'I separated waiting, entry preparation, eligibility, completion, and expiry states. A Lua '
                                      'script checks entry eligibility, duplicate requests, and remaining inventory, then decrements '
                                      'stock atomically within Redis. This does not imply a distributed transaction covering MySQL.'},
                               {'ko': '단순히 성공 응답을 반환하는 것보다, 중간 단계에서 멈췄을 때 사용자가 어떤 상태인지 설명하는 데 집중했습니다. 빈 대기열, 비동기 예매 진행 중, 입장 만료와 예매 '
                                      '오픈 전 오류를 구분하도록 개선했습니다. Kafka·DB 비동기 처리에는 다른 팀원의 기여가 포함됩니다.',
                                'en': 'I focused on explaining the user’s state when processing stopped between steps, not just '
                                      'returning a success response. Improvements distinguished empty queues, pending asynchronous '
                                      'reservations, expired queue admission, and requests before opening time. Other teammates '
                                      'contributed to Kafka/database asynchronous processing.'}],
                'steps': [({'ko': '신청 자격 확인', 'en': 'Check eligibility'},
                           {'ko': '대기열·예매 시간·입장 유효성', 'en': 'Queue status, opening time, and entry validity'}),
                          ({'ko': 'Redis 원자 처리', 'en': 'Atomic Redis operation'},
                           {'ko': '중복 확인·재고 검사·차감', 'en': 'Duplicate check, inventory check, and decrement'}),
                          ({'ko': '상태·복구 안내', 'en': 'State & recovery'},
                           {'ko': '진행 중·완료·만료·실패를 구분', 'en': 'Distinguish pending, complete, expired, and failed'})]},
               {'id': 'recovery',
                'label': {'ko': '운영 개선', 'en': 'Operational improvements'},
                'title': {'ko': '실패한 뒤에도 다시 시도할 수 있는 서비스로.', 'en': 'Making failures recoverable.'},
                'paragraphs': [{'ko': '만료된 토큰이 로그인 요청에 붙으면 인증 필터에서 401이 발생해 다시 로그인할 수 없는 문제가 있었습니다. 로그인·토큰 재발급 등 공개 경로를 JWT 인증 필터의 검사 '
                                      '대상에서 제외해 인증 복구 흐름을 바로잡았습니다.',
                                'en': 'An expired token attached to a login request could trigger a 401 in the authentication filter '
                                      'and block the user from logging in again. I corrected the recovery path by bypassing the JWT '
                                      'authentication filter’s checks for public login and token-refresh endpoints.'},
                               {'ko': '번역 API 실패가 공지 등록 실패로 이어지지 않도록 예외를 처리했습니다. 콘텐츠 저장 시 번역을 보관하고, 영어가 없으면 한국어를 제공하며, 누락된 영문은 나중에 '
                                      '보충하는 흐름을 구현했습니다. 이미 작성된 번역은 보존합니다.',
                                'en': 'I handled translation API failures so they would not block notice creation. Translations are '
                                      'stored with content; missing English text falls back to Korean and can be backfilled later '
                                      'without overwriting existing translations.'},
                               {'ko': '예매 시간·수량·공연일을 관리자와 사용자 화면에 연결하고, 시작된 회차의 수정 제한과 티켓팅 ON/OFF 정책을 정리했습니다. 운영자가 직접 바꿀 수 있는 범위를 늘리는 '
                                      '방향으로 개선했습니다.',
                                'en': 'I connected ticket times, quantities, and performance dates across admin and user screens, and '
                                      'refined restrictions on editing open rounds and the ticketing on/off policy. The aim was to '
                                      'give organizers more control over routine changes.'}]},
               {'id': 'collaboration',
                'label': {'ko': '협업', 'en': 'Collaboration'},
                'title': {'ko': '총학생회·네이버와 이어지는 현장 입장 흐름.', 'en': 'An entry flow connected with the student council and NAVER.'},
                'paragraphs': [{'ko': '총학생회와 협업한 축제 운영에 네이버 Face Sign 연계 입장 흐름을 적용했습니다. 단짠은 티켓 예매, 제3자 제공 동의와 사전 등록 안내를 담당하고, 얼굴 정보 '
                                      '등록과 인증은 네이버가 처리합니다. 얼굴인식 모델 자체를 개발한 프로젝트는 아닙니다.',
                                'en': 'The festival service, built with the student council, supported an entry flow linked to NAVER '
                                      'Face Sign. Danzzan handled reservations, third-party data-sharing consent, and preregistration '
                                      'guidance; NAVER handled face registration and authentication. The project did not develop the '
                                      'face-recognition model.'},
                               {'ko': '예매 완료와 얼굴 등록 완료가 다른 단계임을 안내하고, 사용자 요구를 후속 다국어 기능에 반영했습니다. 대외 협업·행사 운영·프론트엔드·Kafka/DB 비동기 처리에는 '
                                      '팀원의 기여가 포함됩니다. 제 개인 기여는 예매·인증·번역의 백엔드 처리입니다.',
                                'en': 'The service explains that reservation completion and face registration are separate steps, and '
                                      'user needs informed later multilingual features. External coordination, event operations, '
                                      'frontend work, and Kafka/DB asynchronous processing include teammates’ contributions. My own '
                                      'contribution centers on ticketing, authentication, and translation in the backend.'}]},
               {'id': 'delivery',
                'label': {'ko': '일정과 협업', 'en': 'Delivery & teamwork'},
                'title': {'ko': '마감일만 공유하던 방식을, 진행 상황을 함께 보는 방식으로 바꿨습니다.', 'en': 'I made progress visible before the deadline.'},
                'paragraphs': [{'ko': '작업 지연이 반복될 때 Jira로 작업을 작게 나누고, 스프린트와 데일리 스크럼으로 진행 상황과 막힌 부분을 공유하도록 했습니다. 이후 티켓팅 일정이 앞당겨지자 남은 '
                                      '작업과 우선순위를 다시 정리했고, 팀은 변경된 기한 안에 개발을 마쳤습니다.',
                                'en': 'When work repeatedly slipped, I introduced smaller Jira tasks, sprints, and daily scrums to '
                                      'share progress and blockers. When the ticketing launch was subsequently brought forward, we '
                                      'revisited the remaining work and priorities, and the team completed development by the revised '
                                      'deadline.'}]},
               {'id': 'learning',
                'label': {'ko': '배운 점', 'en': 'What I learned'},
                'title': {'ko': '운영자가 쓰는 순간까지가 개발의 범위였습니다.', 'en': 'Development extends into day-to-day operations.'},
                'paragraphs': [{'ko': '요청을 빠르게 받는 것뿐 아니라 중간 단계에서 실패했을 때 사용자가 어디로 돌아갈지, 운영자가 무엇을 바꿀 수 있는지까지 정해야 했습니다. 예매 상태·인증 복구·번역 '
                                      '실패를 각각 다루면서 기능의 성공 경로와 복구 경로를 함께 설계하는 습관을 얻었습니다.',
                                'en': 'Accepting requests was only part of the work: I also had to define where users go after a '
                                      'failure and what operators can change. Working on ticket states, authentication recovery, and '
                                      'translation failures taught me to design success and recovery paths together.'},
                               {'ko': '프로젝트 활동 기간은 2025년 12월부터 2026년 9월까지입니다. 운영 당시 팀 성과와 개인 구현 범위를 구분해 기록했습니다.',
                                'en': 'My project involvement ran from December 2025 through September 2026. This case study '
                                      'distinguishes the service’s team outcomes from my implementation work.'}],
                'note': {'ko': '후속 테마 작업을 기존 축제 운영 성과나 이미 배포된 기능으로 합산하지 않습니다.',
                         'en': 'The follow-up theme work is not counted as a deployed feature or part of the earlier festival '
                               'operating results.'}}],
  'links': [({'ko': '백엔드 저장소', 'en': 'Backend repository'}, 'https://github.com/DKU-Dan-Zzan/Danzzan-BE'),
            ({'ko': '프론트엔드 저장소', 'en': 'Frontend repository'}, 'https://github.com/DKU-Dan-Zzan/Danzzan-FE'),
            ({'ko': '비동기 예매 상태 개선 커밋', 'en': 'Asynchronous reservation state fix'},
             'https://github.com/DKU-Dan-Zzan/Danzzan-BE/commit/11395c73ad285a7fae8553b6d8c59405f881c474')],
  'team': {'ko': '4인 팀 · 봄·가을축제 운영', 'en': '4-person team · Spring & autumn festivals'},
  'display_stack': 'Spring Boot / Redis / Lua / MySQL / Docker',
  'facts': [({'ko': '실사용자', 'en': 'Real users'}, {'ko': '6,000명 이상 · 팀 운영 성과', 'en': '6,000+ · Team operational outcome'}, True),
            ({'ko': '운영', 'en': 'Operations'}, {'ko': '2026 봄·가을축제 2회', 'en': 'Spring and autumn festivals, 2026'}, True),
            ({'ko': '협업', 'en': 'Collaboration'},
             {'ko': '총학생회 · NAVER Face Sign 연계 입장', 'en': 'Student council · NAVER Face Sign entry integration'},
             False)]},
 {'slug': 'soccer-analysis',
  'title': {'ko': '축구 드리블 동작 분석', 'en': 'Soccer dribbling analysis'},
  'category': {'ko': 'Computer vision · 연구', 'en': 'Computer vision · Research'},
  'subtitle': {'ko': '선수와 공의 움직임을 지표로 만들고, 계산에 쓰인 원본 장면까지 확인할 수 있게 했습니다.',
               'en': 'I turned player and ball motion into metrics that can be checked against the original footage.'},
  'desc': {'ko': '한 대의 카메라로 촬영한 드리블 영상에서 선수의 관절과 공을 추적합니다. 터치 주변의 헤드업·어깨 움직임과 전체 유효 프레임의 상체 각도를 계산하고, 원본 장면과 대조할 수 있는 연구용 보고서로 만듭니다.',
           'en': 'I track body landmarks and the ball in single-camera dribbling videos, measure head-up movement and shoulder motion '
                 'around touches and torso angle across all valid frames, and generate research reports that can be checked against '
                 'the source footage.'},
  'role': {'ko': '지표 설계, 터치 구간 실험, 분석 파이프라인 구현·검수', 'en': 'Metric design, touch-window experiments, pipeline development and review'},
  'period': {'ko': '2025.11– · 연구 진행 중', 'en': 'Since Nov 2025 · Ongoing research'},
  'context': 'AIV Lab',
  'stack': 'Python / MediaPipe / YOLO / SAM2 / NumPy / SciPy',
  'repo': 'https://github.com/jiwoo1105/soccer_motion_analysis',
  'video': 'soccer-ball-tracking.mp4',
  'poster': 'soccer-ball-poster.jpg',
  'caption': {'ko': '선수 관절 + 실제 공 검출 좌표와 궤적', 'en': 'Body landmarks + detected ball positions and trail'},
  'sections': [{'id': 'problem',
                'label': {'ko': '배경과 역할', 'en': 'Context & my role'},
                'title': {'ko': '관찰한 자세를, 다시 확인할 수 있는 측정값으로.', 'en': 'From visual observations to inspectable measurements.'},
                'paragraphs': [{'ko': '드리블 자세를 영상별로 비교하려면 무엇을, 어느 구간에서 측정했는지 설명할 수 있어야 합니다. 이 연구는 단안 영상의 관절과 공 궤적을 활용해 상체 움직임을 수치화하고, '
                                      '계산에 사용한 실제 장면을 함께 보여주는 분석 도구를 만드는 작업입니다.',
                                'en': 'Comparing dribbling technique requires a clear account of what was measured and over which '
                                      'frames. This project uses body landmarks and ball trajectories from monocular video to '
                                      'quantify upper-body movement and show the footage behind each measurement.'},
                               {'ko': '평가 의도와 지표 정의, 비교 실험 방향을 정하고 원본 장면 검수를 진행했습니다. AI 코딩 도구와 협업해 영상 입력부터 지표 계산, HTML·JSON 보고서 생성까지 '
                                      '분석 흐름을 구현하고 검증했습니다.',
                                'en': 'I defined the evaluation goals and metrics, directed comparative experiments, and reviewed the '
                                      'source footage. Working with AI coding tools, I developed and checked the pipeline from video '
                                      'input to metric calculation and HTML/JSON reporting.'}]},
               {'id': 'pipeline',
                'label': {'ko': '난제와 해결', 'en': 'Challenge & approach'},
                'title': {'ko': '배경 공을 따라가면, 자세를 평가할 시점도 달라집니다.',
                          'en': 'Tracking the wrong ball also changes when technique is measured.'},
                'paragraphs': [{'ko': '기본 경로는 MediaPipe Pose Heavy로 관절과 얼굴 지점을 포함한 신체 랜드마크 33개의 이미지 좌표와 추정 3D 좌표를 추출합니다. YOLOv8n으로 공의 '
                                      '초기 위치를 찾고 SAM2.1로 마스크를 추적한 뒤, 공의 수평 궤적과 발목 근접 조건으로 터치 후보를 계산합니다.',
                                'en': 'The default pipeline extracts 33 landmarks in image coordinates and estimated 3D coordinates '
                                      'with MediaPipe Pose Heavy. YOLOv8n initializes the ball location, SAM2.1 tracks its mask, and '
                                      'the horizontal trajectory and proximity to the ankles provide candidate touch events.'},
                               {'ko': 'SAM2가 선수가 다루는 공 대신 배경 공을 따라가는 사례를 확인했습니다. 발목과의 거리로 초기 대상을 고르고, 당시 실험에서는 250px 초과 상태가 5프레임 이어지면 '
                                      '재탐색하도록 했습니다. 이후 YOLO11s 발목 ROI 재검출과 같은 프레임을 대조해 실제 드리블 공을 가리키는지 검수했습니다.',
                                'en': 'I found cases where SAM2 followed a background ball instead of the player’s ball. I selected '
                                      'the initial target by ankle proximity and, in that experiment, triggered re-detection when the '
                                      'ball-to-ankle distance exceeded 250 pixels for five consecutive frames. I then compared the '
                                      'same frames with YOLO11s re-detection in an ankle-centered ROI to check that the target was '
                                      'the actual dribbling ball.'},
                               {'ko': '250px는 해당 입력 영상의 조건에 따른 기준입니다. 이 페이지의 영상은 별도 YOLO11 실험의 실제 검출값을 시각화한 것이며, 미검출 구간을 보간하거나 전체 추적 '
                                      '정확도 개선율로 표현하지 않았습니다.',
                                'en': 'The 250-pixel threshold depends on the input video conditions. This demo visualizes actual '
                                      'detections from the separate YOLO11 experiment, without interpolating missed detections or '
                                      'claiming a dataset-wide tracking improvement.'}]},
               {'id': 'metrics',
                'label': {'ko': '지표 설계', 'en': 'Metric design'},
                'title': {'ko': '터치 전후 16프레임에서 어깨 움직임을 집계합니다.', 'en': 'Measuring shoulder motion within 16 frames of each touch.'},
                'paragraphs': [{'ko': '어깨선의 3D 단위 방향을 평활화하고, 인접 프레임 사이 방향 변화에 FPS를 곱해 각속도를 구합니다. 현재는 공 터치 앞뒤 각각 16프레임에 포함된 유효한 인접 프레임 '
                                      '쌍에서 계산한 각속도를 평균합니다. 터치 구간끼리 겹치는 쌍은 한 번만 반영합니다.',
                                'en': 'I smooth the 3D unit vector along the shoulder line and multiply the angular change between '
                                      'adjacent frames by FPS to obtain angular speed. The current method averages the angular speeds '
                                      'computed from valid adjacent-frame pairs within 16 frames before and after each touch, '
                                      'counting overlapping pairs only once.'},
                               {'ko': '헤드업은 터치 주변의 어깨 중앙–눈 중앙 벡터가 수직축과 이루는 각도의 변화 범위를 측정합니다. 상체 지표는 무릎–엉덩이–어깨 각도를 전체 유효 프레임에서 평균합니다. '
                                      '항목별로 측정 대상과 시간 범위를 명시해 서로 다른 움직임을 혼동하지 않도록 했습니다.',
                                'en': 'The head-up metric measures the angular range of the shoulder-midpoint–eye-midpoint vector '
                                      'relative to the vertical axis around touches. The torso metric averages knee–hip–shoulder '
                                      'angles across all valid frames. Each metric states its measurement and time window '
                                      'explicitly.'}]},
               {'id': 'validation',
                'label': {'ko': '결과와 검증', 'en': 'Results & validation'},
                'title': {'ko': '계산이 맞는지와 평가가 타당한지를 나누어 봅니다.', 'en': 'Checking the calculation and the meaning of the score.'},
                'paragraphs': [{'ko': '3개 영상, 771프레임의 기존 추론 결과로 터치 ±16프레임 보고서를 재생성했고, 어깨 집계와 총점이 별도 계산과 1e−10 이내로 일치하는지 확인했습니다. 필수 '
                                      '항목을 계산할 수 없을 때는 총점을 N/A로 남깁니다.',
                                'en': 'Using saved inference outputs from three videos totaling 771 frames, I regenerated the '
                                      '±16-frame reports and checked that the shoulder aggregation and total score agreed with an '
                                      'independent calculation within 1e−10. The total is marked N/A when a required metric cannot be '
                                      'calculated.'},
                               {'ko': '후속 검증에서는 3개 영상을 각각 5회, 총 15회 원본부터 새로 분석했습니다. 저장 좌표를 재사용하지 않고 같은 CLI 기본 CPU 설정에서 관절 배열·공 궤적·터치 '
                                      '프레임·원시 지표·점수가 반복 간 정확히 일치하는지 확인했습니다. 기존 수동 검수 제외 구간은 적용하지 않았습니다.',
                                'en': 'In a follow-up, I reran each of three videos five times from the original input, for 15 fresh '
                                      'runs. Without reusing saved coordinates, body landmarks, ball tracks, touch frames, raw '
                                      'metrics, and scores matched exactly between repeats under the same default CLI CPU settings. '
                                      'Previous manually excluded intervals were not applied.'},
                               {'ko': '이 검증은 구현한 계산의 일관성을 확인한 것입니다. 전문가 등급은 항목별 정답 점수가 아니며, 독립적인 숙련도 평가 검증은 남아 있습니다. 가려짐, 단안 깊이 오차, '
                                      '터치 오검출이 측정에 미치는 영향을 계속 검토하고 있습니다.',
                                'en': 'This verifies computational consistency. The available expert grades are not ground-truth '
                                      'scores for each metric, and independent validation of skill assessment remains open. '
                                      'Occlusion, monocular depth errors, and false touch detections can still affect the '
                                      'measurements.'}],
                'note': {'ko': '2026.11.03 검토 · 반복 일치는 측정 정확도나 자동 숙련도 평가의 타당성을 입증하지 않습니다.',
                         'en': 'Reviewed 3 November 2026 · Repeatability does not establish measurement accuracy or the validity of '
                               'automated skill assessment.'}},
               {'id': 'learning',
                'label': {'ko': '배운 점', 'en': 'What I learned'},
                'title': {'ko': '공을 찾는 것과, 분석할 공을 고르는 것은 달랐습니다.',
                          'en': 'Detecting a ball and selecting the right ball are different tasks.'},
                'paragraphs': [{'ko': '대상을 잘못 고르면 터치 시점과 자세 지표까지 연쇄적으로 달라집니다. 그래서 최종 점수만 보기보다 공 선택 → 터치 후보 → 측정 구간을 원본 프레임에서 따로 확인하게 '
                                      '됐습니다. 계산의 재현성과 평가 지표의 타당성도 각각 검증해야 한다는 기준을 세웠습니다.',
                                'en': 'A wrong target propagates into touch timing and pose metrics. I learned to inspect target '
                                      'selection, candidate touches, and measurement windows separately against the source frames, '
                                      'rather than checking only the final score. Reproducible calculations and valid assessment '
                                      'metrics also require separate evidence.'}]}],
  'links': [({'ko': '분석 도구와 실행 안내', 'en': 'Analysis tool and usage'}, 'https://github.com/jiwoo1105/soccer_motion_analysis'),
            ({'ko': '터치 ±16프레임 반영 기록', 'en': 'Touch-window implementation'},
             'https://github.com/jiwoo1105/soccer_motion_analysis/commit/38e0ad5')],
  'team': {'ko': 'AIV Lab · 스포츠 동작 분석 연구', 'en': 'AIV Lab · Sports motion research'},
  'display_stack': 'Python / MediaPipe / YOLO / SAM2 / NumPy',
  'facts': [({'ko': '재실행 검증', 'en': 'Repeated runs'}, {'ko': '3개 영상 × 5회 · 총 15회', 'en': '3 videos × 5 runs · 15 runs total'}, True),
            ({'ko': '확인 범위', 'en': 'Verified scope'},
             {'ko': '같은 CPU 조건에서 좌표·지표·점수 일치', 'en': 'Matching coordinates, metrics, and scores under the same CPU settings'},
             False)]},
 {'slug': 'conquer-health',
  'title': 'Conquer Health',
  'category': {'ko': 'LLM 시스템 · 해커톤', 'en': 'LLM systems · Hackathon'},
  'subtitle': {'ko': 'MCP로 찾은 근거가 답변까지 이어지는지 확인하고, 실험의 작은 점수 차이도 다시 검증했습니다.',
               'en': 'I checked whether retrieved evidence reached the final answer, and re-examined small differences in '
                     'experimental scores.'},
  'desc': {'ko': '루닛 L2-preview의 추론 흐름을 개선한 의료 대화 프로젝트입니다. MCP 문서 조회·본문 전달, 출력 예산 실험과 답변 검수를 맡았으며, 팀은 직접 생성과 선택적 조회를 결합해 벤치마크상을 '
                 '받았습니다.',
           'en': 'A medical dialogue project improving inference around Lunit L2-preview. I worked on MCP document lookup, passing '
                 'retrieved text to generation, output-budget experiments, and response review. The team combined direct generation '
                 'with selective retrieval and won the benchmark award.'},
  'role': {'ko': 'MCP 문서 조회·본문 전달, 초기 안전 게이트, 출력 예산 실험',
           'en': 'MCP lookup and evidence delivery, initial safety gate, output-budget experiments'},
  'period': '2026.08.21–08.22',
  'context': {'ko': '루닛 의료 AI 해커톤 / AIM 팀 5인', 'en': 'Lunit medical AI hackathon / Team AIM, five members'},
  'stack': 'Python / FastAPI / MCP / L2-preview / HealthBench / Docker',
  'repo': 'https://github.com/Hackathon-AIM/health-conquer-submission',
  'visual': 'health',
  'caption': {'ko': '개인 구현·검수 흐름 도식 · 46.51점은 팀 최종 평가',
              'en': 'Diagram of my implementation and review flow · Score shown is the team’s final evaluation'},
  'award': {'ko': '루닛 · 벤치마크 1위 · AIM 팀 수상', 'en': 'Lunit · 1st in benchmark · Team AIM award'},
  'sections': [{'id': 'problem',
                'label': {'ko': '배경과 역할', 'en': 'Context & my role'},
                'title': {'ko': '문서를 찾는 것에서, 답변의 근거로 쓰이게 하는 것까지.', 'en': 'Making retrieved documents useful to the answer.'},
                'paragraphs': [{'ko': '제공된 L2-preview의 가중치를 바꾸지 않고 의료 질의응답을 개선하는 과제였습니다. 문서를 조회해도 필요한 본문이 생성 입력에 전달되지 않거나, 질문의 요구가 '
                                      '답변에서 누락되면 도구 호출의 성공만으로는 충분하지 않았습니다.',
                                'en': 'The task was to improve medical question answering without changing the provided L2-preview '
                                      'weights. A successful lookup was insufficient if the relevant document text did not reach '
                                      'generation or the answer missed part of the question.'},
                               {'ko': '저는 초기 MCP 검색·생성 연결과 약물 안전 게이트를 구현하고, 검색 본문이 모델 입력에 포함되는지와 답변이 질문의 요구·근거를 반영하는지를 나누어 검수했습니다. 이후 '
                                      '출력 예산 실험과 멀티턴 응답 지시 보강에도 참여했습니다. 팀의 최종 제출안과 개인 구현 범위는 커밋 단위로 구분했습니다.',
                                'en': 'I implemented the initial MCP retrieval/generation connection and medication safety gate, '
                                      'checking evidence delivery separately from whether the response addressed the question and '
                                      'used that evidence. I also worked on output-budget experiments and multi-turn response '
                                      'instructions. Individual contributions and the final team submission are distinguished by '
                                      'commit.'}]},
               {'id': 'implementation',
                'label': {'ko': '직접 구현한 부분', 'en': 'My implementation'},
                'title': {'ko': '검색 성공과, 근거를 사용하는 답변 사이의 빈틈을 확인했습니다.',
                          'en': 'I checked the gap between successful retrieval and an evidence-informed answer.'},
                'paragraphs': [{'ko': 'Python·FastAPI 기반 MCP 조회 흐름에서 문서를 찾는 단계와 본문을 생성 입력으로 넘기는 단계를 연결했습니다. 도구 반환만 확인하지 않고 검색 누락·중복, '
                                      '실제 전달 본문, 근거 없는 인용과 질문 요구의 누락을 나누어 살폈습니다.',
                                'en': 'I connected document lookup with delivery of the retrieved body text into generation through a '
                                      'Python/FastAPI MCP flow. Beyond checking tool returns, I examined missing or duplicate '
                                      'results, the text actually passed to the model, unsupported citations, and unanswered '
                                      'requirements.'}],
                'steps': [({'ko': '조회 연결', 'en': 'Connect retrieval'},
                           {'ko': 'MCP 문서 조회·초기 안전 게이트 구현', 'en': 'Implement MCP lookup and an initial safety gate'}),
                          ({'ko': '입력 확인', 'en': 'Inspect model input'},
                           {'ko': '검색 본문이 생성 입력에 포함되는지 검수', 'en': 'Check that retrieved text reaches generation'}),
                          ({'ko': '답변 확인', 'en': 'Review the response'},
                           {'ko': '질문의 요구·근거·응답 완결성 확인', 'en': 'Check requirements, evidence use, and completeness'})]},
               {'id': 'inference',
                'label': {'ko': '개인 실험', 'en': 'My experiment'},
                'title': {'ko': '출력 예산을 늘렸지만, 점수 개선이라고 단정하지 않았습니다.',
                          'en': 'A larger output budget did not establish a score improvement.'},
                'paragraphs': [{'ko': '출력 상한을 다시 확인하고, 제 후보 e6de327에서 서버 상한 설정을 2,048에서 32,768로 정정하면서 요청 출력 예산은 2,048에서 4,096토큰으로 '
                                      '늘렸습니다. 추론 중 잘림으로 재생성 경로에 들어가는 일을 줄이려는 실험이었습니다. 서버 상한과 실제 요청 예산은 서로 다른 설정입니다.',
                                'en': 'After rechecking the output limit, my candidate e6de327 corrected the configured server cap '
                                      'from 2,048 to 32,768 and raised the requested output budget from 2,048 to 4,096 tokens. The '
                                      'goal was to reduce truncation that triggered regeneration. The server cap and requested output '
                                      'budget are distinct settings.'},
                               {'ko': '장부상 이 후보는 49.59점으로, 기준선 반복 3회의 평균 49.18점과 0.41점 차이였습니다. 관측된 반복 변동 안에 있어 토큰 상향만의 개선 근거로 삼지 '
                                      '않았습니다. 점수와 함께 잘림, 폴백 발생, 지연을 확인할 필요가 있었습니다.',
                                'en': 'The ledger records 49.59 for this candidate, 0.41 points above the baseline’s three-run mean '
                                      'of 49.18. The difference lies within the observed run-to-run variation, so it does not '
                                      'establish a benefit from increasing the token budget alone. Truncation, fallback frequency, '
                                      'and latency also needed inspection.'}]},
               {'id': 'strategy',
                'label': {'ko': '팀의 선택과 범위', 'en': 'Team decisions & scope'},
                'title': {'ko': '도구를 항상 쓰기보다, 필요한 질문에 제한했습니다.', 'en': 'We reserved tools for questions that needed them.'},
                'paragraphs': [{'ko': '팀은 직접 생성의 기준선을 먼저 확인한 뒤, 한국어 약가·허가·성분·질병 코드처럼 정확한 조회가 필요한 질문에 MCP를 제한하는 방향을 검토했습니다. 조회 실패나 모호한 '
                                      '대상에는 직접 생성 경로를 유지하고, 긴 답변이 후처리에서 잘리지 않도록 개선했습니다.',
                                'en': 'After establishing a direct-generation baseline, the team explored selective MCP use for '
                                      'precise lookups such as Korean drug prices, approvals, ingredients, and disease codes. Direct '
                                      'generation remained the fallback for failed lookups or ambiguous targets, and post-processing '
                                      'was adjusted to preserve long answers.'},
                               {'ko': '이는 팀의 최종 제출 계열에 대한 설명입니다. 제 기여인 초기 연결·본문 전달·안전 게이트와 출력 예산 실험은 커밋으로 구분했습니다. 선택적 MCP의 실행 빈도나 최종 '
                                      '점수 기여도는 별도의 호출 로그 없이는 단정하지 않습니다.',
                                'en': 'This describes the team’s final submission family. My initial integration, evidence delivery, '
                                      'safety gate, and output-budget experiment are identified by their commits. Without separate '
                                      'call logs, I do not attribute a specific share of the final score to selective MCP.'}]},
               {'id': 'award',
                'label': {'ko': '결과와 수상', 'en': 'Results & award'},
                'title': {'ko': '벤치마크 1위. 팀 성과와 실험 점수는 구분합니다.',
                          'en': 'First in the benchmark—with experimental and final scores kept separate.'},
                'paragraphs': [{'ko': 'AIM 팀은 루닛 Conquer Health의 HealthBench 기반 최종 평가에서 14개 팀 중 1위로 벤치마크상을 받았습니다. 최종 3라운드 평균은 '
                                      '46.51점입니다. 이는 팀 공동 성과이며 MCP나 출력 예산 하나의 효과로 해석하지 않습니다.',
                                'en': 'Team AIM won the benchmark award, ranking first among 14 teams in the final HealthBench-based '
                                      'evaluation at Lunit Conquer Health. The three-round mean was 46.51. This is a shared team '
                                      'outcome, not an effect attributable solely to MCP or output budget.'}],
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
                'details': {'label': {'ko': '개발 대시보드 점수와 다른 이유', 'en': 'Why the development dashboard shows other scores'},
                            'paragraphs': [{'ko': '개발 장부의 54.37점과 마감 대시보드의 53.53점은 최종 3라운드 평가와 별도 기록입니다. 모델 서버 상태와 누적 변경이 함께 달라진 실험도 '
                                                  '있어, 서로 다른 기록을 단일 개선율로 계산하지 않았습니다. 상장은 수상 증빙이며 숫자 점수를 기재하지 않습니다.',
                                            'en': 'The development ledger’s 54.37 and the closing dashboard’s 53.53 are separate from '
                                                  'the three final rounds. Some development runs also differed in server state and '
                                                  'accumulated changes, so these records are not combined into one improvement rate. '
                                                  'The certificate documents the award, not numerical scores.'}]}},
               {'id': 'learning',
                'label': {'ko': '배운 점', 'en': 'What I learned'},
                'title': {'ko': '좋아 보이는 점수보다, 다시 확인할 수 있는 변화.', 'en': 'A change I can verify matters more than a promising score.'},
                'paragraphs': [{'ko': '같은 동작을 반복 평가해도 47.79–50.03으로 2.24점 차이가 났습니다. 제 출력 예산 후보의 기준선 평균 대비 +0.41점은 이 변동 안에 있어 개선이라고 '
                                      '단정하지 않았습니다. 잘림·재생성·지연과 답변 완결성을 함께 확인해야 한다는 기준을 세웠습니다.',
                                'en': 'Repeated evaluations of the same behavior ranged from 47.79 to 50.03—a 2.24-point spread. My '
                                      'output-budget candidate’s 0.41-point difference from the baseline mean fell within that '
                                      'variation, so I did not claim an improvement. I learned to examine truncation, retries, '
                                      'latency, and completeness alongside the score.'},
                               {'ko': '도구를 붙이는 것보다 중요한 것은 필요한 정보가 실제 답변까지 이어지는지, 그리고 변화가 반복해서 관측되는지였습니다. 이후 실험에서도 설정·관측·해석을 따로 남기고 '
                                      '있습니다.',
                                'en': 'What mattered was whether the information reached the answer and whether a change held up '
                                      'across evaluations. I now keep configuration, observations, and interpretation separate in '
                                      'experiment records.'}]}],
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
  'display_stack': 'Python / FastAPI / MCP / L2-preview / HealthBench',
  'facts': [({'ko': '최종 평가', 'en': 'Final evaluation'}, {'ko': '14개 팀 중 1위 · 벤치마크상', 'en': '1st of 14 teams · Benchmark award'}, True),
            ({'ko': '팀 평균', 'en': 'Team average'}, {'ko': '46.51점 · 최종 3라운드', 'en': '46.51 · Three final rounds'}, True),
            ({'ko': '개선 범위', 'en': 'Scope'},
             {'ko': '제공 모델의 응답 흐름 · 가중치 변경 없음', 'en': 'Response pipeline around the provided model · No weight changes'},
             False)]},
 {'slug': 'fish-detection',
  'title': {'ko': '넙치 증상 탐지 / Flatfish doctor', 'en': 'Flatfish doctor'},
  'category': {'ko': 'Computer vision · 애플리케이션', 'en': 'Computer vision · Application'},
  'subtitle': {'ko': '넙치 개체 탐지와 7종 외형 상태 분류를 앱으로 연결했습니다. 증상 분류의 최고 검증 Top-1은 87.68%입니다.',
               'en': 'I connected fish detection and seven-category appearance classification to an app. The symptom classifier '
                     'reached a peak validation Top-1 accuracy of 87.68%.'},
  'desc': {'ko': '넙치를 탐지한 뒤 개체별 크롭을 정상을 포함한 7개 외형 상태로 분류합니다. 데이터 전처리와 모델 학습부터 FastAPI 추론, Flutter 결과 화면까지 연결했습니다.',
           'en': 'A two-stage pipeline detects olive flounder and classifies individual crops into seven appearance categories, '
                 'including normal. I connected data preparation and model training to FastAPI inference and a Flutter results '
                 'interface.'},
  'role': {'ko': '데이터 전처리, 탐지·분류 학습, 추론 API·앱', 'en': 'Data preparation, detection/classification training, inference API and app'},
  'period': '2026.03–2026.06',
  'context': {'ko': '넙치 외형 증상 모니터링', 'en': 'Visual symptom monitoring for olive flounder'},
  'stack': 'YOLO / PyTorch / OpenCV / FastAPI / Flutter',
  'repo': 'https://github.com/jiwoo1105/fish-disease-detection',
  'images': ['fish-results.png'],
  'caption': {'ko': '개체별 증상 분류 결과 화면', 'en': 'Per-fish symptom classification results'},
  'sections': [{'id': 'problem',
                'label': {'ko': '배경과 역할', 'en': 'Context & my role'},
                'title': {'ko': '수조 전체의 배경보다, 개체의 상태에 집중합니다.', 'en': 'Focusing on each fish, not the tank background.'},
                'paragraphs': [{'ko': '수조 영상에는 물결과 조명 변화, 서로 겹치는 개체가 함께 들어옵니다. 전체 프레임에서 바로 증상을 판단하기보다 먼저 넙치의 위치를 찾고, 개체별 이미지를 잘라 증상을 '
                                      '분류하는 2단계 구조를 사용했습니다.',
                                'en': 'Tank footage includes ripples, lighting changes, and overlapping fish. Instead of classifying '
                                      'symptoms from the whole frame, the pipeline first locates fish and then classifies cropped '
                                      'images of each individual.'},
                               {'ko': '데이터 전처리, 탐지·분류 모델 학습, 좌표 변환과 추론 API, 결과 화면을 구현했습니다. 사용자가 분류 결과를 원본 개체 위치와 함께 확인하도록 연결하는 '
                                      '작업이었습니다.',
                                'en': 'I implemented data preparation, detection and classification training, coordinate conversion, '
                                      'the inference API, and the results interface, so users could relate a prediction back to the '
                                      'fish’s location in the original image.'}]},
               {'id': 'data',
                'label': {'ko': '데이터와 모델', 'en': 'Data and models'},
                'title': {'ko': '라벨을 크롭 데이터에 연결하고 클래스 편향을 줄였습니다.', 'en': 'Linking labels to crops and controlling class imbalance.'},
                'paragraphs': [{'ko': 'AI Hub 넙치 질병 데이터의 개체·증상 라벨을 매핑해 분류용 크롭을 만들었습니다. 매핑되지 않는 라벨은 제외하고, 특정 증상에 학습 샘플이 치우치지 않도록 학습 '
                                      '데이터에 클래스별 상한을 적용했습니다.',
                                'en': 'I mapped individual-fish and symptom labels from AI Hub’s flounder disease dataset to create '
                                      'classification crops. Unmapped labels were excluded, and per-class caps were applied to '
                                      'training samples to reduce class imbalance.'},
                               {'ko': '분류 대상은 정상·출혈·백점·반점/결절·체색변화·여윔·궤양의 7개 외형 상태입니다. 증상에서 질병·대응 안내로 이어지는 부분은 규칙 기반 매핑이며, 영상만으로 병원체를 '
                                      '확정하는 진단 모델과는 구분됩니다.',
                                'en': 'The seven visible states are normal, hemorrhage, white spots, spots/nodules, color change, '
                                      'emaciation, and ulcers. Rule-based mappings link symptom labels to disease information and '
                                      'suggested actions; the system does not identify the causative pathogen from video.'}]},
               {'id': 'validation',
                'label': {'ko': '검증', 'en': 'Validation'},
                'title': {'ko': '탐지와 분류의 성능을 따로 읽습니다.', 'en': 'Reading detection and classification results separately.'},
                'paragraphs': [{'ko': '저장된 검증 결과에서 증상 분류의 최고 Top-1 정확도는 87.68%, 개체 탐지 mAP50은 0.4455였습니다. 서로 다른 과제의 지표이므로 하나의 종합 정확도로 '
                                      '합치지 않습니다.',
                                'en': 'Saved validation results show a peak symptom-classification Top-1 accuracy of 87.68% and a '
                                      'fish-detection mAP50 of 0.4455. These measure different tasks and are not combined into a '
                                      'single system accuracy.'},
                               {'ko': '겹침과 탁한 수조 환경에서 탐지가 병목으로 남아 있습니다. 분류기가 올바르게 학습돼도 앞 단계에서 개체를 놓치면 결과를 만들 수 없으므로, 오탐·누락 데이터와 실제 환경 '
                                      '검증을 후속 과제로 보고 있습니다.',
                                'en': 'Detection remains a bottleneck with overlap and turbid water. Even a well-performing '
                                      'classifier cannot produce a result for a fish missed by the detector, so false detections, '
                                      'missed fish, and field validation remain priorities.'}],
                'image': 'fish-validation.jpg',
                'image_alt': {'ko': '분류 모델의 저장된 검증 배치 예측', 'en': 'Saved validation-batch predictions from the symptom classifier'},
                'stats': [('87.68%', {'ko': '분류 최고 검증 Top-1', 'en': 'Peak validation Top-1'}),
                          ('0.4455', {'ko': '개체 탐지 mAP50', 'en': 'Fish-detection mAP50'})]},
               {'id': 'application',
                'label': {'ko': '서비스 연결', 'en': 'Application'},
                'title': {'ko': '모델 결과를 사용자가 읽을 수 있는 화면으로.', 'en': 'Turning predictions into a readable interface.'},
                'paragraphs': [{'ko': '추론 결과를 개체 위치, 증상명과 신뢰도로 정리해 Flutter 앱에 표시했습니다. 서버 추론과 앱 화면을 연결하면서 원본·크롭·화면 사이 좌표 변환을 맞췄고, 결과 '
                                      '로그와 개체별 안내를 확인할 수 있도록 구성했습니다.',
                                'en': 'I organized inference outputs into fish locations, symptom labels, and confidence values for '
                                      'the Flutter app. Connecting inference to the interface required consistent coordinates across '
                                      'the source image, crops, and display, as well as readable result logs and per-fish '
                                      'information.'}],
                'note': {'ko': '저장된 데이터의 모델 검증과 앱 시연 범위입니다. 실제 양식장에서 질병 조기 발견 효과를 입증한 결과는 아닙니다.',
                         'en': 'The evidence covers dataset validation and an application demo, not demonstrated early-detection '
                               'outcomes at working fish farms.'}},
               {'id': 'learning',
                'label': {'ko': '배운 점', 'en': 'What I learned'},
                'title': {'ko': '데이터를 조정하는 단계와 성능을 확인하는 단계를 분리했습니다.',
                          'en': 'Training-data changes and validation serve different purposes.'},
                'paragraphs': [{'ko': '클래스별 샘플 수 조절은 학습 데이터에만 적용하고, 검증 데이터의 분포는 유지했습니다. 분류 정확도가 높아도 앞 단계의 탐지 누락을 해결하지는 못하므로 두 모델의 결과를 '
                                      '따로 봤습니다. 앱까지 연결하면서 모델 점수뿐 아니라 원본 개체와 결과 좌표가 맞는지도 확인해야 했습니다.',
                                'en': 'I capped class counts in the training set while leaving the validation distribution unchanged. '
                                      'A strong classifier cannot recover fish missed by the detector, so I examined the two models '
                                      'separately. Connecting inference to the app also required checking that result coordinates '
                                      'matched the original fish, beyond the model scores.'}]}],
  'links': [({'ko': '모델·앱 코드와 학습 결과', 'en': 'Model/app code and training results'},
             'https://github.com/jiwoo1105/fish-disease-detection'),
            ({'ko': '전체 시연 영상', 'en': 'Full demonstration'}, 'https://youtu.be/3LDmc6zdG0A')],
  'facts': [({'ko': '분류 검증', 'en': 'Classification validation'},
             {'ko': 'Top-1 87.68% · 7개 클래스', 'en': 'Top-1 87.68% · 7 classes'},
             True),
            ({'ko': '별도 탐지 지표', 'en': 'Separate detection metric'}, {'ko': 'mAP50 0.4455', 'en': 'mAP50 0.4455'}, False)]},
 {'slug': 'medguard',
  'title': 'MedGuard',
  'category': {'ko': '의료영상 · AI 보안 실험', 'en': 'Medical imaging · AI security experiments'},
  'subtitle': {'ko': '흉부 X-ray 분류기의 공격·방어를 비교했습니다. 기록된 DiffAttack 조건에서 Medical DiffPure는 Vanilla DiffPure보다 4.84%p 높은 정확도를 보였습니다.',
               'en': 'I compared attacks and defenses for a chest X-ray classifier. Under the recorded DiffAttack conditions, Medical '
                     'DiffPure exceeded Vanilla DiffPure accuracy by 4.84 percentage points.'},
  'desc': {'ko': '흉부 X-ray 분류기에 대한 FGSM·PGD·잠재공간 공격을 비교하고, FFT 분석과 의료 도메인 VAE를 결합한 정화 흐름을 실험했습니다.',
           'en': 'I compared FGSM, PGD, and latent-space attacks on a chest X-ray classifier and experimented with a purification '
                 'pipeline combining FFT analysis and a medical-domain VAE.'},
  'role': {'ko': '공격·방어 실험, 주파수 분석, 비교 시연', 'en': 'Attack/defense experiments, frequency analysis, comparison demo'},
  'period': '2026.02–2026.06',
  'context': {'ko': '의료영상 분류 강건성 실험', 'en': 'Robustness experiments for medical-image classification'},
  'stack': 'PyTorch / ResNet-50 / RoentGen VAE / FFT / Gradio',
  'repo': 'https://github.com/jiwoo1105/AISecurity',
  'video': 'medguard-demo.mp4',
  'poster': 'medguard-poster.jpg',
  'caption': {'ko': '공격 전후와 방어 결과를 비교하는 실제 시연', 'en': 'Demo comparing original, attacked, and purified inputs'},
  'sections': [{'id': 'problem',
                'label': {'ko': '배경과 역할', 'en': 'Context & my role'},
                'title': {'ko': '작은 입력 변화가 분류 결과를 바꾸는 경우.', 'en': 'When input perturbations change a prediction.'},
                'paragraphs': [{'ko': '흉부 X-ray의 폐렴 이진 분류기를 대상으로 입력에 대한 적대적 공격과 방어를 비교했습니다. 픽셀 공간 공격과 VAE 잠재공간 공격이 서로 다른 주파수 특성을 '
                                      '보이는지, 정화 과정이 분류 성능과 이미지 구조에 어떤 영향을 주는지 살폈습니다.',
                                'en': 'I compared adversarial attacks and defenses for a binary pneumonia classifier on chest X-rays. '
                                      'The experiments examined frequency differences between pixel-space and VAE latent-space '
                                      'attacks, and the effects of purification on classification and image structure.'},
                               {'ko': 'ResNet-50 분류기, FGSM·PGD 및 DiffAttack 계열 구현, FFT 시각화와 Gradio 비교 데모를 연결했습니다. AI 코딩 도구를 활용해 구현과 '
                                      '디버깅을 진행하며 실험 조건과 비교 결과를 정리했습니다.',
                                'en': 'I connected a ResNet-50 classifier, FGSM/PGD and a DiffAttack-style implementation, FFT '
                                      'visualizations, and a Gradio comparison demo. I used AI coding tools for implementation and '
                                      'debugging and organized the experimental conditions and results.'}]},
               {'id': 'approach',
                'label': {'ko': '접근', 'en': 'Approach'},
                'title': {'ko': '공격 특성과 정화 강도를 함께 비교했습니다.', 'en': 'Comparing perturbation patterns and purification strength.'},
                'paragraphs': [{'ko': 'FFT 분석으로 고주파 성분의 변화를 확인하고, RoentGen VAE를 이용한 정화와 정화 전 입력 이미지의 블렌딩을 실험했습니다. 공개 구현의 Medical '
                                      'DiffPure는 공격 유형에 따른 처리 강도와 폐 영역의 구조 일치도를 함께 고려하는 실험적 파이프라인입니다.',
                                'en': 'I used FFT analysis to inspect changes in high-frequency components and experimented with '
                                      'purification using the RoentGen VAE and blending the purified output with the input image. The '
                                      'repository’s Medical DiffPure is an experimental pipeline that considers attack-specific '
                                      'purification strength and structural consistency in lung regions.'},
                               {'ko': '주파수 변화가 작다는 사실만으로 정상 이미지와 특정 공격을 완벽히 구별할 수는 없습니다. 따라서 데모의 공격 분류 규칙을 일반적인 공격 탐지 보장으로 표현하지 않고, '
                                      '정해진 실험 조건의 비교로 다룹니다.',
                                'en': 'A small frequency change cannot reliably distinguish a clean image from every attack. I '
                                      'therefore treat the demo’s attack-classification rules as part of a controlled experiment, not '
                                      'as a general attack-detection guarantee.'}]},
               {'id': 'results',
                'label': {'ko': '실험 기록', 'en': 'Reported experiments'},
                'title': {'ko': '같은 설정에서 방어 방법을 비교합니다.', 'en': 'Comparing defenses within the reported setup.'},
                'paragraphs': [{'ko': '공개 저장소에는 Medical DiffPure의 공격하 정확도가 FGSM 58.31%, PGD 61.47%, DiffAttack 78.56%로 기록돼 있습니다. '
                                      'DiffAttack 조건의 Vanilla DiffPure 73.72%와 비교하면 4.84%p 차이입니다.',
                                'en': 'The public repository reports robust accuracy of 58.31% under FGSM, 61.47% under PGD, and '
                                      '78.56% under DiffAttack for Medical DiffPure. The DiffAttack result is 4.84 percentage points '
                                      'higher than the reported 73.72% for Vanilla DiffPure.'},
                               {'ko': '이 수치는 저장소에 기록된 설정의 비교 결과입니다. 모든 의료영상 모델이나 새로운 공격에 대한 우위를 뜻하지 않습니다. 적응형 공격, 다른 데이터 분포, 정화 후 병변 '
                                      '정보 보존은 추가 검증이 필요합니다.',
                                'en': 'These are results recorded for the repository’s experimental setup. They do not establish '
                                      'superiority across medical-image models or unseen attacks. Adaptive attacks, other data '
                                      'distributions, and preservation of diagnostic features after purification require further '
                                      'evaluation.'}],
                'stats': [('78.56%', {'ko': '기록된 DiffAttack 조건 정확도', 'en': 'Reported accuracy under DiffAttack'}),
                          ('+4.84 pp', {'ko': '같은 조건의 Vanilla DiffPure 대비', 'en': 'Over Vanilla DiffPure in that setup'})]},
               {'id': 'learning',
                'label': {'ko': '배운 점', 'en': 'What I learned'},
                'title': {'ko': '정화 후 정확도와 보존된 이미지 정보를 함께 봐야 했습니다.',
                          'en': 'Accuracy after purification is only part of the evidence.'},
                'paragraphs': [{'ko': '공격에 맞춘 정화가 분류 정확도를 높여도 원래 필요한 영상 정보까지 바꿀 수 있습니다. 그래서 공격 조건, 정화 강도, 이미지 구조를 함께 비교하는 관점을 배웠습니다. '
                                      '다음 검증에서는 같은 조건의 정확도뿐 아니라 병변 정보 보존과 새로운 공격에 대한 동작을 별도로 확인해야 합니다.',
                                'en': 'Purification tailored to an attack can improve classification while also changing useful image '
                                      'information. I learned to compare attack conditions, purification strength, and image '
                                      'structure together. Further validation must examine lesion preservation and behavior under new '
                                      'attacks alongside accuracy under matched conditions.'}]}],
  'links': [({'ko': '공격·방어 코드와 실험 기록', 'en': 'Attack/defense code and experiment records'},
             'https://github.com/jiwoo1105/AISecurity')],
  'facts': [({'ko': 'DiffAttack 비교', 'en': 'Under DiffAttack'},
             {'ko': 'Medical DiffPure 78.56% / 기본 DiffPure 73.72%', 'en': 'Medical DiffPure 78.56% / vanilla DiffPure 73.72%'},
             True),
            ({'ko': '검증 범위', 'en': 'Scope'}, {'ko': '실험 조건 내 방어 비교', 'en': 'Defense comparison under the tested conditions'}, False)]},
 {'slug': 'medai-agent',
  'title': 'MedAI Agent',
  'category': {'ko': 'LLM 워크플로우 · 프로토타입', 'en': 'LLM workflows · Prototype'},
  'subtitle': {'ko': '텍스트·음성·이미지 입력에서 약물 정보 조회와 8단계 LLM 처리를 거쳐 보고서를 보여주는 프로토타입을 구현했습니다.',
               'en': 'I built a prototype that takes text, voice, or image input through drug-information lookup and eight LLM stages '
                     'to a report.'},
  'desc': {'ko': '텍스트·음성·이미지 입력을 약물 정보 조회와 8단계 LLM 워크플로우에 연결한 프로토타입입니다. FastAPI와 React로 처리 단계와 분석 결과를 보여줍니다.',
           'en': 'A prototype connecting text, voice, and image inputs to medication-information retrieval and an eight-stage LLM '
                 'workflow. FastAPI and React expose the processing stages and resulting report.'},
  'role': {'ko': '입력·약물 조회·에이전트 흐름·결과 화면 연결', 'en': 'Input, medication lookup, agent orchestration, and results interface'},
  'period': {'ko': '2025 · 딥러닝 프로젝트', 'en': '2025 · Deep learning project'},
  'context': {'ko': '약물 정보 분석 프로토타입', 'en': 'Medication-information analysis prototype'},
  'stack': 'Python / FastAPI / GPT-4o / React / Vite',
  'repo': 'https://github.com/jiwoo1105/MedAI_Agent',
  'video': 'medai-demo.mp4',
  'poster': 'medai-poster.jpg',
  'caption': {'ko': '입력과 단계별 분석 결과의 실제 시연', 'en': 'Demo of input and staged analysis results'},
  'sections': [{'id': 'problem',
                'label': {'ko': '배경과 역할', 'en': 'Context & my role'},
                'title': {'ko': '입력 방식이 달라도 같은 분석 흐름으로.', 'en': 'One workflow for different input methods.'},
                'paragraphs': [{'ko': '사용자가 약물 정보를 텍스트로 적거나 음성·이미지로 제공했을 때, 약물명과 질문의 맥락을 정리하고 결과를 읽기 쉬운 보고서로 보여주는 프로토타입입니다. 입력 화면, 외부 '
                                      '약물 API, LLM 처리와 결과 UI를 하나의 흐름으로 연결했습니다.',
                                'en': 'This prototype organizes medication names and question context from text, voice, or image '
                                      'inputs and presents the output as a readable report. It connects the input interface, an '
                                      'external medication-information API, LLM processing, and the results UI.'}]},
               {'id': 'workflow',
                'label': {'ko': '워크플로우', 'en': 'Workflow'},
                'title': {'ko': '서로 다른 역할의 8단계를 연결했습니다.', 'en': 'Connecting eight stages with distinct roles.'},
                'paragraphs': [{'ko': '입력 이해 → 약물 인식 → 기본 지식 → 심화 분석 → 부작용 검토 → 근거 설명 → 개인화된 정보 정리 → 보고서 생성의 순서로 구성했습니다. 각 단계의 출력을 다음 '
                                      '단계로 넘기고 최종 요약, 주요 내용과 주의사항을 화면에 모읍니다.',
                                'en': 'The sequence covers input understanding, medication recognition, background knowledge, '
                                      'detailed analysis, side-effect review, evidence explanation, context-specific information, and '
                                      'report generation. Outputs pass between stages and are collected into a summary, key findings, '
                                      'and cautions.'},
                               {'ko': '여기서 8개 에이전트는 역할을 나눈 LLM 처리 단계입니다. 서로 독립적인 의료 전문가 8명이 검증했다는 의미가 아닙니다. 식약처 e약은요 API의 조회 정보와 LLM이 '
                                      '생성한 설명도 구분해 이해해야 합니다.',
                                'en': 'The eight agents are LLM processing stages assigned different roles; they are not eight '
                                      'independent medical experts. Information retrieved from the MFDS medication API must also be '
                                      'distinguished from explanations generated by the LLM.'}]},
               {'id': 'interface',
                'label': {'ko': '사용자 화면', 'en': 'Interface'},
                'title': {'ko': '기다리는 동안의 진행 상태와 결과를 함께 설계했습니다.', 'en': 'Designing both progress feedback and the final report.'},
                'paragraphs': [{'ko': 'React에서 텍스트·음성·이미지 입력을 제공하고, 처리 중에는 단계별 진행 상태를 보여줍니다. FastAPI 응답을 요약, 위험도 표시와 상세 설명으로 나눠 읽을 수 '
                                      '있게 구성했습니다. 여러 모델 호출이 이어지는 작업을 사용자에게 어떻게 전달할지 실험한 프로젝트입니다.',
                                'en': 'The React interface supports text, voice, and image input and displays progress through the '
                                      'processing stages. FastAPI responses are organized into a summary, a risk indicator, and '
                                      'detailed explanations. The project explores how to present a workflow that involves multiple '
                                      'model calls.'}]},
               {'id': 'limits',
                'label': {'ko': '검증 범위', 'en': 'Scope of validation'},
                'title': {'ko': '동작하는 프로토타입과 의료적 정확성은 별개의 과제입니다.', 'en': 'A working prototype is not clinical validation.'},
                'paragraphs': [{'ko': '공개 시연은 입력부터 결과 화면까지의 연결을 보여줍니다. 위험도 점수와 권장사항은 모델이 생성하는 참고 정보이며, 임상적으로 검증된 확률이나 처방 판단으로 해석할 수 '
                                      '없습니다.',
                                'en': 'The public demo shows the path from input to the results screen. Risk scores and '
                                      'recommendations are model-generated reference information, not clinically validated '
                                      'probabilities or prescribing decisions.'},
                               {'ko': '후속 과제는 약물명 인식 오류, 조회 근거 누락, 근거 없는 설명, 단계 간 오류 전파를 평가하는 것입니다. 에이전트 수를 늘리는 것보다 각 단계가 결과 품질에 '
                                      '기여하는지 측정할 필요가 있습니다.',
                                'en': 'Further evaluation should cover medication-name recognition errors, missing source '
                                      'information, unsupported explanations, and error propagation between stages. Each stage’s '
                                      'contribution to output quality needs to be measured.'}]},
               {'id': 'learning',
                'label': {'ko': '배운 점', 'en': 'What I learned'},
                'title': {'ko': '단계를 연결한 뒤에는, 각 단계의 필요성을 검증해야 합니다.',
                          'en': 'After connecting the stages, each stage needs to justify its role.'},
                'paragraphs': [{'ko': '입력·조회·생성·화면을 연결하는 과정에서 약물명 하나의 오류가 이후 설명과 보고서까지 전파될 수 있다는 점에 주목했습니다. 다음 단계는 처리 단계를 더 늘리는 것이 '
                                      '아니라, 조회한 사실과 생성한 설명을 추적하고 각 단계를 제외했을 때 품질이 어떻게 달라지는지 평가하는 것입니다.',
                                'en': 'Connecting input, lookup, generation, and display highlighted how a single drug-name error '
                                      'could propagate into later explanations and the report. The next step is to trace retrieved '
                                      'facts separately from generated explanations and evaluate how quality changes when each stage '
                                      'is removed, rather than simply adding more stages.'}]}],
  'links': [({'ko': '8단계 워크플로우와 시연 자료', 'en': 'Eight-stage workflow and demo'}, 'https://github.com/jiwoo1105/MedAI_Agent')],
  'facts': [({'ko': '구성', 'en': 'Workflow'}, {'ko': '8단계 LLM 워크플로우', 'en': 'Eight-stage LLM workflow'}, True),
            ({'ko': '현재 단계', 'en': 'Status'}, {'ko': '약물 정보 분석 프로토타입', 'en': 'Medication-information analysis prototype'}, False)]}]
