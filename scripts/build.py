#!/usr/bin/env python3
"""Build both static locales with the Python standard library only."""
from pathlib import Path
import html
import importlib.util

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('site_content', ROOT / 'content/site_content.py')
content = importlib.util.module_from_spec(spec)
spec.loader.exec_module(content)
BASE = 'https://jiwoo1105.github.io/jiwoo-portfolio/'
PROJECTS = content.PROJECTS

def esc(value):
    return html.escape(str(value), quote=True)

def render(lang, slug=None):
    def t(value):
        return value[lang] if isinstance(value, dict) else value
    def L(ko, en):
        return ko if lang == 'ko' else en
    project = next((p for p in PROJECTS if p['slug'] == slug), None)
    local_path = f'projects/{slug}.html' if slug else 'index.html'
    path = ('en/' if lang == 'en' else '') + local_path
    asset = ('../../' if slug else '../') + 'assets/' if lang == 'en' else ('../assets/' if slug else 'assets/')
    home = '../' if slug else './'
    alternate = ('../../' if slug else '../') + local_path if lang == 'en' else ('../en/' if slug else 'en/') + local_path
    title = t(project['title']) + ' — Park Jiwoo' if project else 'Park Jiwoo — AI / ML Developer'
    description = t(project['desc']) if project else t(content.HOME['description'])
    links = ''.join(f'<a href="{home}#{id}">{label}</a>' for id,label in [('work',L('프로젝트','Work')),('about',L('소개','About')),('contact',L('연락','Contact'))])
    theme_label=L('다크 모드로 전환','Switch to dark mode')
    language_links = (f'<span lang="ko" aria-current="page">KO</span><a data-language-link href="{alternate}" lang="en" hreflang="en" aria-label="View this page in English">EN</a>' if lang=='ko' else f'<a data-language-link href="{alternate}" lang="ko" hreflang="ko" aria-label="이 페이지를 한국어로 보기">KO</a><span lang="en" aria-current="page">EN</span>')
    companion_script = f'<script type="module" src="{asset}companion-loader.js"></script>' if not project else ''
    showcase_script = f'<script src="{asset}motion-showcase.js" defer></script>' if project and project.get('showcase') else ''
    head = f'''<!doctype html>
<html lang="{lang}" data-theme="light"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#ffffff">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:image" content="{BASE}assets/hero.jpg">
<link rel="canonical" href="{BASE}{path}"><link rel="alternate" hreflang="ko" href="{BASE}{local_path}"><link rel="alternate" hreflang="en" href="{BASE}en/{local_path}">
<script src="{asset}preferences.js"></script><link rel="icon" href="{asset}favicon.svg" type="image/svg+xml"><link rel="preload" as="font" href="{asset}pretendard.woff2" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{asset}site.css"><link rel="stylesheet" href="{asset}refresh.css"><link rel="stylesheet" href="{asset}portfolio.css"><script src="{asset}site.js" defer></script>{companion_script}{showcase_script}</head>
<body class="{'project-page' if slug else 'home'}"><a class="skip-link" href="#main">{L('본문으로 바로가기','Skip to content')}</a>
<header class="site-header {'hero-header' if not slug else ''}"><a class="brand" href="{home}" aria-label="{L('박지우 홈','Park Jiwoo home')}"><span class="brand-symbol">©</span><span>Park Jiwoo</span></a>
<div class="header-controls"><nav class="desktop-nav" aria-label="{L('주요 메뉴','Main navigation')}">{links}</nav><div class="language-switch" aria-label="{L('언어','Language')}">{language_links}</div><button class="theme-toggle" type="button" data-theme-toggle aria-pressed="false" aria-label="{theme_label}" title="{theme_label}"><span class="theme-symbol" aria-hidden="true">◐</span><span class="theme-label">{L('다크','Dark')}</span></button><button class="menu-trigger" type="button" aria-controls="menu-dialog" aria-haspopup="dialog"><span class="menu-dot"></span>{L('메뉴','Menu')}</button></div></header>
<dialog id="menu-dialog" class="menu-dialog" aria-labelledby="menu-title"><div class="menu-top"><span id="menu-title">{L('메뉴','Navigation')}</span><button class="menu-close" aria-label="{L('메뉴 닫기','Close menu')}" type="button">{L('닫기','Close')} <span aria-hidden="true">×</span></button></div><nav aria-label="{L('모바일 메뉴','Mobile navigation')}">{links}</nav><a class="menu-email" href="mailto:psskej00@gmail.com">psskej00@gmail.com</a></dialog><main id="main">'''

    def external(label, url):
        return f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{t(label)} <span aria-hidden="true">↗</span></a>'

    def stats(items, cls='case-results'):
        return f'<dl class="{cls}">' + ''.join(f'<div><dt>{t(label)}</dt><dd>{t(value)}</dd></div>' for value,label in items) + '</dl>'

    def health():
        steps=[L('의료 질문','Medical query'),L('필요한 근거 조회','Evidence lookup'),L('본문을 생성 입력에 전달','Pass evidence to the model'),L('답변의 근거·완결성 검수','Review evidence use & completeness')]
        return f'<div class="health-story"><div class="visual-label">Conquer Health / AIM</div><p class="visual-title">{L("근거 조회부터,<br>완결된 답변까지.","From evidence retrieval<br>to a complete answer.")}</p><ol class="evidence-flow">'+''.join(f'<li><span>{i:02d}</span>{step}</li>' for i,step in enumerate(steps,1))+f'</ol><div class="visual-result"><strong>46.51</strong><span>{L("팀 최종 3라운드 평균<br>HealthBench 벤치마크 1위","Team final three-round average<br>1st in the HealthBench benchmark")}</span></div></div>'

    def tracking():
        return f'''<div class="tracking-story"><div class="visual-label">Motion data / Identity review</div><p class="visual-title">{L('같은 사람의 움직임을,<br>끝까지 연결하기.','Keeping motion connected<br>to the same person.')}</p><div class="track-case"><div class="track-case-heading"><span>01 / {L('누락 후 같은 ID 복귀','Same ID after a gap')}</span><strong>ID 5</strong></div><div class="track-rail"><span>ID 5</span><i class="track-gap">18 frames</i><span>ID 5</span></div><p>{L('약 0.60초의 공백만 제외 후보','Exclude only the ~0.60-second gap')}</p></div><div class="track-case"><div class="track-case-heading"><span>02 / {L('새 ID와 타인 오연결','New ID & wrong association')}</span><strong>ID 4 → 28</strong></div><div class="track-rail track-rail-switch"><span>ID 4</span><i>f819 → f820</i><span>ID 28</span></div><p>{L('f899: 기존 ID 4가 다른 사람에게 연결됨','f899: the old ID 4 is on a different person')}</p></div><div class="tracking-footer"><span>M09 · PHALP / HMR 2.0</span><span>{L('검수 기록 도식','Review-record diagram')}</span></div></div>'''

    def media(p, detail=False):
        caption=t(p['caption'])
        if p.get('video'):
            video_id='preview-'+p['slug']
            video=p['video']
            if detail: video=p.get('detail_video',video)
            attrs='controls preload="metadata"' if detail else 'data-preview controls muted loop preload="none"'
            result=f'<video id="{video_id}" class="project-preview-video" {attrs} playsinline poster="{asset}{p["poster"]}" aria-label="{esc(caption)}"><source src="{asset}{video}" type="video/mp4"><a href="{asset}{video}">{L("시연 영상 보기","Open demo video")}</a></video>'
            if not detail: result+=f'<button class="preview-toggle" type="button" data-preview-toggle aria-controls="{video_id}" aria-label="{esc(caption)} {L("재생","Play")}"><span aria-hidden="true">▶</span><span class="preview-button-label">{L("재생","Play")}</span></button>'
        elif p.get('visual')=='health': result=health()
        elif p.get('visual')=='tracking': result=tracking()
        else: result=''.join(f'<img src="{asset}{img}" alt="{esc(caption)} {i+1}" loading="lazy">' for i,img in enumerate(p['images']))
        if detail:
            cls='case-demo '+('health-demo' if p.get('visual') in ('health','tracking') else 'phones-demo' if len(p.get('images',[]))>=2 else 'image-demo' if p.get('images') else '')
            return f'<figure class="{cls}"><div>{result}</div><figcaption>{caption}</figcaption></figure>'
        cls='health-preview' if p.get('visual') in ('health','tracking') else 'still-preview danzzan-still' if len(p.get('images',[]))>=2 else 'still-preview fish-preview' if p.get('images') else 'mesh-preview'
        return f'<figure class="project-visual"><div class="preview-media {cls}">{result}</div><figcaption>{caption}</figcaption></figure>'

    def facts(p, compact=False):
        rows=[(L('직접 담당','My contribution'),p['role'],False)]
        rows+=p.get('facts',[])
        if compact: rows=rows[:2]
        result='<dl class="project-facts">'
        for label,value,emphasis in rows:
            result+=f'<div><dt>{t(label)}</dt><dd class="{"fact-highlight" if emphasis else ""}">{t(value)}</dd></div>'
        if not compact: result+=f'<div><dt>{L("사용 기술","Technologies")}</dt><dd class="tech-list">'+''.join(f'<span>{esc(tag.strip())}</span>' for tag in p.get('display_stack',p['stack']).split('/'))+'</dd></div>'
        return result+'</dl>'

    def showcase(p):
        demo=p['showcase']; stages=demo['stages']; first=stages[0]
        result=f'<section id="demo" class="motion-showcase section-wrap" data-motion-showcase aria-labelledby="demo-heading"><div class="motion-heading"><div><span class="eyebrow">VIDEO → MOTION DATA</span><h2 id="demo-heading">{t(demo["title"])}</h2></div><p>{L("같은 선수 · 같은 6초 · 실제 모델 출력","One player · The same 6 seconds · Actual model outputs")}</p></div>'
        result+=f'<div class="motion-stages" role="group" aria-label="{L("시연 단계 선택","Choose a demo stage")}" hidden>'
        for i,s in enumerate(stages):
            result+=f'<button type="button" aria-pressed="{str(i==0).lower()}" aria-controls="motion-player" data-stage data-src="{asset}{s["video"]}" data-poster="{asset}{s["poster"]}" data-title="{esc(t(s["title"]))}" data-description="{esc(t(s["description"]))}"><span>{"↔" if i==0 else f"{i:02d}"}</span>{t(s["label"])}</button>'
        result+=f'</div><div class="motion-player-frame"><video id="motion-player" controls playsinline loop muted preload="metadata" poster="{asset}{first["poster"]}" aria-labelledby="motion-stage-title" aria-describedby="motion-stage-description"><source src="{asset}{first["video"]}" type="video/mp4"><a href="{asset}{first["video"]}">{L("영상 파일 열기","Open video file")}</a></video></div>'
        result+=f'<div class="motion-caption"><div aria-live="polite" aria-atomic="true"><h3 id="motion-stage-title">{t(first["title"])}</h3><p id="motion-stage-description">{t(first["description"])}</p></div><label class="motion-speed" hidden>{L("재생 속도","Playback speed")}<select data-playback-speed aria-label="{L("영상 재생 속도","Video playback speed")}"><option value="0.5">0.5×</option><option value="1" selected>1×</option><option value="2">2×</option></select></label></div><p class="motion-error" role="status" hidden></p>'
        result+='<noscript><div class="motion-fallback">'+''.join(f'<a href="{asset}{s["video"]}">{t(s["label"])}</a>' for s in stages)+'</div></noscript>'
        result+=f'<p class="motion-source">{L("영상 출처","Footage")}: {external("FIBA Basketball · Slovenia v France, U20 EuroBasket 2024", demo["source"])} <span>15:35–15:41 · 60 FPS · ID 9 / #21</span></p>'
        result+=f'<div class="motion-pipeline"><div class="motion-pipeline-heading"><h3>{L("영상이 데이터가 되는 과정","From video to motion data")}</h3><span>{L("단계를 눌러 결과 확인","Select a stage above to inspect its output")}</span></div><ol>'
        for title,desc in demo['pipeline']:
            result+=f'<li><strong>{t(title)}</strong><span>{t(desc)}</span></li>'
        result+=f'</ol><p class="motion-scope">{t(demo["scope"])}</p></div></section>'
        return result

    def card(p, featured=True):
        url=f'projects/{p["slug"]}.html'
        result=f'<article id="{p["slug"]}" class="project-card {"project-card-featured" if featured else "project-card-small"}">{media(p)}<div class="project-card-copy"><div class="project-card-meta"><span>{t(p.get("team",p["category"]))}</span><span>{t(p["period"])}</span></div><h3><a href="{url}">{t(p["title"])}<span aria-hidden="true">↗</span></a></h3><p class="project-summary">{t(content.SUMMARIES[p["slug"]])}</p>'
        result+=facts(p,compact=not featured)
        result+=f'<div class="project-card-links"><a href="{url}">{L("프로젝트 읽기","Read the case study")} <span aria-hidden="true">→</span></a>{external("GitHub",p["repo"])}</div></div></article>'
        return result

    if not project:
        body=f'''<section class="hero" aria-labelledby="hero-title"><img class="hero-photo" src="{asset}hero.jpg" srcset="{asset}hero-mobile.jpg 1600w, {asset}hero.jpg 3600w" sizes="100vw" alt="{L('산과 호수 위에서 패러글라이딩을 즐기는 박지우','Jiwoo paragliding above mountains and a lake')}" width="3600" height="3150" fetchpriority="high"><div class="hero-introduction"><p class="hero-identity">{L('박지우','Jiwoo Park')} <span>AI / ML Developer</span></p><h1 id="hero-title">{t(content.HOME['headline'])}</h1></div><div class="hero-bottom"><a class="hero-scroll" href="#about">{L('아래로 둘러보기','Take a look around')} <span aria-hidden="true">↓</span></a><button class="motion-toggle" data-motion-toggle aria-pressed="false" type="button"><span class="motion-symbol" aria-hidden="true">Ⅱ</span><span class="motion-label">{L('움직임 멈추기','Pause motion')}</span></button></div></section>
<section class="about section-wrap" id="about" aria-labelledby="about-title"><div class="companion" data-companion><div class="companion-stage"><img class="companion-placeholder" src="{asset}companion-fallback.svg" alt="{L('컴퓨터 앞에서 작업하는 작은 강아지','A little dog working at a computer')}" width="600" height="450" loading="lazy"><canvas aria-hidden="true"></canvas><span class="companion-bubble" data-companion-status role="status"></span></div><div class="companion-caption"><span>{L('작은 작업실에서.','At the little desk.')}</span><button type="button" data-companion-greet hidden>{L('인사하기','Say hello')} <span aria-hidden="true">✳</span></button></div></div><div class="about-copy"><span class="eyebrow">{L('안녕하세요, 박지우입니다.','A little about Jiwoo.')}</span><h2 id="about-title">{t(content.HOME['about_title'])}</h2>''' + ''.join(f'<p>{t(p)}</p>' for p in content.HOME['about']) + f'''<a class="about-work-link" href="#work">{L('제가 만든 것들','See what I’ve built')} <span aria-hidden="true">↘</span></a></div></section>
<section class="work section-wrap" id="work" aria-labelledby="work-title"><div class="section-heading work-heading"><div><h2 id="work-title">Selected work</h2><p>{L('직접 만들고, 실험하고, 운영했습니다.','Built, tested, and put to work.')}</p></div><button class="work-motion-toggle" type="button" data-motion-toggle aria-pressed="false"><span class="motion-symbol" aria-hidden="true">Ⅱ</span><span class="motion-label">{L('애니메이션 멈추기','Pause motion')}</span></button></div><div class="featured-work">''' + ''.join(card(p) for p in PROJECTS[:4]) + f'''</div><div class="other-work"><div class="section-heading other-work-heading"><div><h2>{L('다른 프로젝트','Other projects')}</h2><p>{L('호기심이 이어진 곳들.','Where curiosity led next.')}</p></div></div><div class="other-project-grid">''' + ''.join(card(p,False) for p in PROJECTS[4:]) + f'''</div></div><a class="text-link github-work" href="https://github.com/jiwoo1105" target="_blank" rel="noopener noreferrer">{L('GitHub에서 더 보기','Explore more on GitHub')} ↗</a></section>
<section class="credentials section-wrap" id="credentials" aria-labelledby="credentials-title"><div class="section-heading credentials-heading"><div><h2 id="credentials-title">{L('자격 및 교육','Credentials & training')}</h2><p>{L('자격 취득과 교육 수료 이력.','Professional qualification and completed courses.')}</p></div></div><div class="credential-list">'''
        rows=[('2025-06-27','SQLD · '+L('SQL 개발자','SQL Developer'),L('한국데이터산업진흥원 · 국가공인 자격 취득','Korea Data Agency · Nationally accredited qualification'),None),('2026-07-22','Generative AI Essentials on AWS',L('Amazon Web Services · 교육 수료','Amazon Web Services · Course completed'),'aws-generative-ai.pdf'),('2026-07-23','Agentic AI Foundations',L('Amazon Web Services · 교육 수료','Amazon Web Services · Course completed'),'aws-agentic-ai.pdf')]
        for date,name,issuer,pdf in rows:
            action=f'<a href="{asset}{pdf}" target="_blank" rel="noopener noreferrer" aria-label="{esc(name)} {L("수료증 PDF 새 탭에서 보기","certificate PDF, opens in a new tab")}">{L("수료증","Certificate")} ↗</a>' if pdf else f'<span class="credential-kind">{L("자격","Qualification")}</span>'
            body+=f'<article class="credential-row"><time datetime="{date}">{date.replace("-",".")}</time><div><h3>{name}</h3><p>{issuer}</p></div>{action}</article>'
        body+=f'''</div></section><section class="contact section-wrap" id="contact" aria-labelledby="contact-title"><div class="contact-top"><span class="eyebrow">{L('함께 풀어볼 문제가 있나요?','Have a problem we could work on together?')}</span><span class="contact-name">Park Jiwoo</span></div><div class="contact-heading"><h2 id="contact-title">Let’s talk<span class="blue-period">.</span></h2><a class="circle-link contact-circle magnetic" href="mailto:psskej00@gmail.com" aria-label="{L('박지우에게 이메일 보내기','Email Jiwoo')}" ><span aria-hidden="true">↗</span></a></div><div class="contact-actions"><a class="outline-link" href="mailto:psskej00@gmail.com">psskej00@gmail.com ↗</a><a class="outline-link" href="https://github.com/jiwoo1105" target="_blank" rel="noopener noreferrer">GitHub ↗</a><button class="copy-email" type="button" data-copy-email="psskej00@gmail.com">{L('이메일 복사','Copy email')}</button><span class="copy-status sr-only" role="status"></span></div></section>'''
    else:
        p=project
        demo_link=f'<a href="#demo">{L("영상으로 보기","Watch the demo")} ↓</a>' if p.get('showcase') else ''
        body=f'<section class="case-header section-wrap"><a href="{home}#work" class="back-link">← {L("모든 프로젝트","All projects")}</a><div class="case-heading-meta"><span>{t(p["category"])}</span><span>{t(p["period"])}</span></div><h1 class="case-title editorial-title">{t(p["title"])}</h1><p class="case-subtitle">{t(p["subtitle"])}</p><div class="case-hero-links">{demo_link}{external(L("프로젝트 코드","Project code"),p["repo"])}<a href="#problem">{L("나의 기여 살펴보기","Explore my contribution")} ↓</a></div></section>'
        if p.get('showcase'):
            body+=showcase(p)
            body+=f'<div class="motion-facts section-wrap"><div class="case-summary-panel"><h2>{L("실험 범위와 나의 역할","Scope & my contribution")}</h2><p>{t(p["context"])}</p>'+facts(p)+'</div></div>'
        else:
            body+='<div class="case-at-a-glance section-wrap"><div>'+media(p,True)+f'</div><div class="case-summary-panel"><h2>{L("프로젝트 한눈에 보기","At a glance")}</h2><p>{t(p["context"])}</p>'+facts(p)+'</div></div>'
        body+=f'<div class="case-layout section-wrap"><nav class="case-nav" aria-label="{L("프로젝트 목차","Case study sections")}"><span>{L("이 프로젝트의 이야기","In this case study")}</span>'+''.join(f'<a href="#{s["id"]}">{t(s["label"])}</a>' for s in p['sections'])+f'<a href="#sources">{L("코드와 근거","Code & evidence")}</a></nav><div class="case-content">'
        for s in p['sections']:
            body+=f'<section class="case-block" id="{s["id"]}"><h2>{t(s["label"])}</h2><div class="case-text"><h3>{t(s["title"])}</h3>'
            body+=''.join(f'<p>{t(text)}</p>' for text in s['paragraphs'])
            if s.get('steps'):
                body+='<ol class="process-flow">'+''.join(f'<li><strong>{t(title)}</strong><p>{t(description)}</p></li>' for title,description in s['steps'])+'</ol>'
            if s.get('items'):
                body+='<dl class="contribution-list">'+''.join(f'<div><dt>{t(label)}</dt><dd>{t(value)}</dd></div>' for label,value in s['items'])+'</dl>'
            if s.get('table'):
                table=s['table']
                body+='<div class="case-table-wrap"><table class="case-table"><caption>'+t(table['caption'])+'</caption><thead><tr>'
                body+=''.join(f'<th scope="col">{t(v)}</th>' for v in table['headers'])+'</tr></thead><tbody>'
                for row in table['rows']:
                    body+='<tr><th scope="row">'+t(row[0])+'</th>'+''.join(f'<td>{t(v)}</td>' for v in row[1:])+'</tr>'
                body+='</tbody></table></div>'
            if s.get('gallery'):
                body+='<div class="case-gallery">'+''.join(f'<figure><img src="{asset}{src}" alt="{esc(t(caption))}" loading="lazy"><figcaption>{t(caption)}</figcaption></figure>' for src,caption in s['gallery'])+'</div>'
            if s.get('video'):
                body+=f'<figure class="evidence-figure"><video controls playsinline preload="none" poster="{asset}{s["poster"]}" aria-label="{esc(t(s["caption"]))}"><source src="{asset}{s["video"]}" type="video/mp4"></video><figcaption>{t(s["caption"])}</figcaption></figure>'
            if s.get('details'):
                body+=f'<details class="case-disclosure"><summary>{t(s["details"]["label"])}</summary>'+''.join(f'<p>{t(v)}</p>' for v in s['details']['paragraphs'])+'</details>'
            if s.get('stats'):body+=stats(s['stats'])
            if s.get('image'):body+=f'<figure class="evidence-figure {s.get("image_class", "")}"><img src="{asset}{s["image"]}" alt="{esc(t(s["image_alt"]))}" loading="lazy"><figcaption>{t(s["image_alt"])}</figcaption></figure>'
            if s.get('note'):body+=f'<p class="case-note">{t(s["note"])}</p>'
            body+='</div></section>'
        body+=f'<section class="case-block" id="sources"><h2>{L("코드와 근거","Code & evidence")}</h2><div class="case-text"><h3>{L("구현과 판단의 근거를 함께 남깁니다.","The implementation and the evidence behind it.")}</h3><p>{p["stack"]}</p><div class="case-links">'+''.join(external(label,url) for label,url in p['links'])+f'</div><p class="source-note">{L("2026.11.03 검토 · 개인 기여와 팀 성과, 완료한 실험과 진행 중인 연구를 구분했습니다.","Reviewed 3 November 2026 · Personal contributions, team outcomes, completed experiments, and ongoing research are distinguished.")}</p></div></section></div></div>'
        next_p=PROJECTS[(PROJECTS.index(p)+1)%len(PROJECTS)]
        body+=f'<section class="next-project section-wrap"><a href="{next_p["slug"]}.html"><span>{L("다음 프로젝트","Next project")}</span><h2>{t(next_p["title"])}</h2></a><a href="{next_p["slug"]}.html" aria-label="{esc(t(next_p["title"]))}">↗</a></section>'
    foot=f'</main><footer class="site-footer section-wrap"><a href="{home}">© 2026 Park Jiwoo</a><span>Curiosity into practice.</span><a href="#main">{L("맨 위로","Back to top")} ↑</a></footer></body></html>\n'
    target=ROOT/path
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(head+body+foot)

if __name__=='__main__':
    for lang in ['ko','en']:
        render(lang)
        for p in PROJECTS:render(lang,p['slug'])
    print('Built 16 static pages: Korean and English, 7 case studies each.')
