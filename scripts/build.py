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
    head = f'''<!doctype html>
<html lang="{lang}" data-theme="light"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="theme-color" content="#ffffff">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:image" content="{BASE}assets/hero.jpg">
<link rel="canonical" href="{BASE}{path}"><link rel="alternate" hreflang="ko" href="{BASE}{local_path}"><link rel="alternate" hreflang="en" href="{BASE}en/{local_path}">
<script src="{asset}preferences.js"></script><link rel="icon" href="{asset}favicon.svg" type="image/svg+xml"><link rel="preload" as="font" href="{asset}pretendard.woff2" type="font/woff2" crossorigin>
<link rel="stylesheet" href="{asset}site.css"><link rel="stylesheet" href="{asset}refresh.css"><script src="{asset}site.js" defer></script></head>
<body class="{'project-page' if slug else 'home'}"><a class="skip-link" href="#main">{L('본문으로 바로가기','Skip to content')}</a>
<header class="site-header {'hero-header' if not slug else ''}"><a class="brand" href="{home}" aria-label="{L('박지우 홈','Park Jiwoo home')}"><span class="brand-symbol">©</span><span>Park Jiwoo</span></a>
<div class="header-controls"><nav class="desktop-nav" aria-label="{L('주요 메뉴','Main navigation')}">{links}</nav><div class="language-switch" aria-label="{L('언어','Language')}">{language_links}</div><button class="theme-toggle" type="button" data-theme-toggle aria-pressed="false" aria-label="{theme_label}" title="{theme_label}"><span class="theme-symbol" aria-hidden="true">◐</span><span class="theme-label">{L('다크','Dark')}</span></button><button class="menu-trigger" type="button" aria-controls="menu-dialog" aria-haspopup="dialog"><span class="menu-dot"></span>{L('메뉴','Menu')}</button></div></header>
<dialog id="menu-dialog" class="menu-dialog" aria-labelledby="menu-title"><div class="menu-top"><span id="menu-title">{L('메뉴','Navigation')}</span><button class="menu-close" aria-label="{L('메뉴 닫기','Close menu')}" type="button">{L('닫기','Close')} <span aria-hidden="true">×</span></button></div><nav aria-label="{L('모바일 메뉴','Mobile navigation')}">{links}</nav><a class="menu-email" href="mailto:psskej00@gmail.com">psskej00@gmail.com</a></dialog><main id="main">'''

    def external(label, url):
        return f'<a href="{esc(url)}" target="_blank" rel="noopener noreferrer">{t(label)} <span aria-hidden="true">↗</span></a>'

    def stats(items, cls='case-results'):
        return f'<dl class="{cls}">' + ''.join(f'<div><dt>{t(label)}</dt><dd>{t(value)}</dd></div>' for value,label in items) + '</dl>'

    def health():
        return f'''<div class="health-sheet"><div class="health-sheet-top"><span class="health-wordmark"><span class="health-plus">+</span> Conquer Health</span><span class="sheet-index">HealthBench</span></div><div class="health-sheet-heading">Better answers.<br>Measured.</div><div class="health-chart" aria-label="{L('팀 기록: 1라운드 46.17점, 2라운드 45.55점, 3라운드 47.82점','Team record: Round 1, 46.17; Round 2, 45.55; Round 3, 47.82')}">''' + ''.join(f'<div class="chart-column"><span>{score}</span><i style="--bar:{float(score)/60*100:.2f}%"></i><small>{L("라운드","Round")} {i}</small></div>' for i,score in enumerate(['46.17','45.55','47.82'],1)) + f'</div><div class="health-sheet-bottom"><span>Lunit L2-preview</span><span>{L("팀 최종 평가 기록","Team final evaluation record")}</span></div></div>'

    def media(p, detail=False):
        caption=t(p['caption'])
        if p.get('video'):
            video_id='preview-'+p['slug']
            video=p['video']
            if detail and p['slug']=='video-motion': video='basketball-mesh-demo.mp4'
            attrs='controls preload="metadata"' if detail else 'data-preview controls muted loop preload="none"'
            result=f'<video id="{video_id}" class="project-preview-video" {attrs} playsinline poster="{asset}{p["poster"]}" aria-label="{esc(caption)}"><source src="{asset}{video}" type="video/mp4"><a href="{asset}{video}">{L("시연 영상 보기","Open demo video")}</a></video>'
            if not detail: result+=f'<button class="preview-toggle" type="button" data-preview-toggle aria-controls="{video_id}" aria-label="{esc(caption)} {L("재생","Play")}"><span aria-hidden="true">▶</span><span class="preview-button-label">{L("재생","Play")}</span></button>'
        elif p.get('visual')=='health': result=health()
        else: result=''.join(f'<img src="{asset}{img}" alt="{esc(caption)} {i+1}" loading="lazy">' for i,img in enumerate(p['images']))
        if detail:
            cls='case-demo '+('health-demo' if p.get('visual')=='health' else 'phones-demo' if len(p.get('images',[]))==2 else 'image-demo' if p.get('images') else '')
            return f'<figure class="{cls}"><div>{result}</div><figcaption>{caption}</figcaption></figure>'
        cls='health-preview' if p.get('visual')=='health' else 'still-preview danzzan-still' if len(p.get('images',[]))==2 else 'still-preview fish-preview' if p.get('images') else 'mesh-preview'
        return f'<div class="preview-media {cls}">{result}<span class="media-caption">{caption}</span></div>'

    def card(p, featured=True):
        url=f'projects/{p["slug"]}.html'
        award=f'<a class="award-note" href="{url}#award">{t(p["award"])} <span aria-hidden="true">↗</span></a>' if p.get('award') else ''
        result=f'<article id="{p["slug"]}" class="work-entry {"featured-entry" if featured else "other-entry"} reveal">{media(p)}<div class="work-entry-copy"><p class="work-category">{t(p["category"])}</p><h3><a href="{url}">{t(p["title"])}<span aria-hidden="true">↗</span></a></h3>{award}<p class="work-description">{t(p["desc"])}</p>'
        if p.get('stats'):result+=stats(p['stats'],'work-metrics')
        result+=f'<p class="work-role"><span>{L("담당","Focus")}</span> {t(p["role"])}</p><p class="work-stack">{p["stack"]}</p><div class="work-entry-links"><a href="{url}">{L("프로젝트 자세히 보기","Read the case study")} <span aria-hidden="true">↗</span></a>{external("Code",p["repo"])}</div></div></article>'
        return result

    if not project:
        body=f'''<section class="hero" aria-labelledby="hero-title"><img class="hero-photo" src="{asset}hero.jpg" srcset="{asset}hero-mobile.jpg 1600w, {asset}hero.jpg 3600w" sizes="100vw" alt="{L('산과 호수 위에서 패러글라이딩을 즐기는 박지우','Jiwoo paragliding above mountains and a lake')}" width="3600" height="3150" fetchpriority="high"><div class="hero-introduction"><p class="hero-identity">{L('박지우','Jiwoo Park')} <span>AI / ML Developer</span></p><h1 id="hero-title">{t(content.HOME['headline'])}</h1></div><div class="hero-bottom"><a class="hero-scroll" href="#about">{L('조금 더 알아보기','More about me')} <span aria-hidden="true">↓</span></a><button class="motion-toggle" data-motion-toggle aria-pressed="false" type="button"><span class="motion-symbol" aria-hidden="true">Ⅱ</span><span class="motion-label">{L('움직임 멈추기','Pause motion')}</span></button></div></section>
<section class="about section-wrap" id="about" aria-labelledby="about-title"><div class="about-photo-wrap reveal"><img src="{asset}hero.jpg" srcset="{asset}hero-mobile.jpg 1600w, {asset}hero.jpg 3600w" sizes="(max-width: 700px) 100vw, 45vw" alt="{L('패러글라이딩 중인 박지우와 뒤로 펼쳐진 산과 호수','Jiwoo paragliding with mountains and a lake in the background')}" width="3600" height="3150" loading="lazy"><span>{L('새로운 시선이 시작되는 곳.','A different perspective.')}</span></div><div class="about-copy reveal"><span class="eyebrow">About me</span><h2 id="about-title">{t(content.HOME['about_title'])}</h2>''' + ''.join(f'<p>{t(p)}</p>' for p in content.HOME['about']) + f'''<div class="about-interests"><span>{L('지금 집중하는 분야','Current focus')}</span><p>Computer vision &amp; 3D motion<br>LLM inference &amp; evaluation<br>{L('실제 운영을 고려한 시스템 개발','Systems built for real-world use')}</p></div></div></section>
<section class="work section-wrap" id="work" aria-labelledby="work-title"><div class="section-heading work-heading"><div><h2 id="work-title">Selected work</h2><p>{L('연구에서 서비스 운영까지, 네 가지 대표 프로젝트.','Four projects, from research to live service operations.')}</p></div><button class="work-motion-toggle" type="button" data-motion-toggle aria-pressed="false"><span class="motion-symbol" aria-hidden="true">Ⅱ</span><span class="motion-label">{L('애니메이션 멈추기','Pause motion')}</span></button></div><div class="featured-work">''' + ''.join(card(p) for p in PROJECTS[:4]) + f'''</div><div class="other-work"><div class="section-heading other-work-heading"><div><h2>{L('다른 프로젝트','Other projects')}</h2><p>{L('직접 만들고 비교하며 넓혀온 경험.','Further experiments and applications.')}</p></div></div>''' + ''.join(card(p,False) for p in PROJECTS[4:]) + f'''</div><a class="text-link github-work" href="https://github.com/jiwoo1105" target="_blank" rel="noopener noreferrer">{L('GitHub에서 더 보기','Explore more on GitHub')} ↗</a></section>
<section class="credentials section-wrap" id="credentials" aria-labelledby="credentials-title"><div class="section-heading credentials-heading"><div><h2 id="credentials-title">{L('자격 및 교육','Credentials & training')}</h2><p>{L('자격 취득과 교육 수료 이력.','Professional qualification and completed courses.')}</p></div></div><div class="credential-list">'''
        rows=[('2025-06-27','SQLD · '+L('SQL 개발자','SQL Developer'),L('한국데이터산업진흥원 · 국가공인 자격 취득','Korea Data Agency · Nationally accredited qualification'),None),('2026-07-22','Generative AI Essentials on AWS',L('Amazon Web Services · 교육 수료','Amazon Web Services · Course completed'),'aws-generative-ai.pdf'),('2026-07-23','Agentic AI Foundations',L('Amazon Web Services · 교육 수료','Amazon Web Services · Course completed'),'aws-agentic-ai.pdf')]
        for date,name,issuer,pdf in rows:
            action=f'<a href="{asset}{pdf}" target="_blank" rel="noopener noreferrer" aria-label="{esc(name)} {L("수료증 PDF 새 탭에서 보기","certificate PDF, opens in a new tab")}">{L("수료증","Certificate")} ↗</a>' if pdf else f'<span class="credential-kind">{L("자격","Qualification")}</span>'
            body+=f'<article class="credential-row"><time datetime="{date}">{date.replace("-",".")}</time><div><h3>{name}</h3><p>{issuer}</p></div>{action}</article>'
        body+=f'''</div></section><section class="contact section-wrap" id="contact" aria-labelledby="contact-title"><div class="contact-top"><span class="eyebrow">{L('함께 풀어볼 문제가 있나요?','Have a problem we could work on together?')}</span><span class="contact-name">Park Jiwoo</span></div><div class="contact-heading"><h2 id="contact-title">Let’s talk<span class="blue-period">.</span></h2><a class="circle-link contact-circle magnetic" href="mailto:psskej00@gmail.com" aria-label="{L('박지우에게 이메일 보내기','Email Jiwoo')}" ><span aria-hidden="true">↗</span></a></div><div class="contact-actions"><a class="outline-link" href="mailto:psskej00@gmail.com">psskej00@gmail.com ↗</a><a class="outline-link" href="https://github.com/jiwoo1105" target="_blank" rel="noopener noreferrer">GitHub ↗</a><button class="copy-email" type="button" data-copy-email="psskej00@gmail.com">{L('이메일 복사','Copy email')}</button><span class="copy-status sr-only" role="status"></span></div></section>'''
    else:
        p=project
        body=f'<section class="case-header section-wrap"><a href="{home}#work" class="back-link">← {L("모든 프로젝트","All projects")}</a><h1 class="case-title editorial-title">{t(p["title"])}</h1><p class="case-subtitle">{t(p["subtitle"])}</p><dl class="case-meta">'
        for label,val in [(L('프로젝트','Project'),p['context']),(L('담당','My focus'),p['role']),(L('기간','When'),p['period'])]:body+=f'<div><dt>{label}</dt><dd>{t(val)}</dd></div>'
        body+='</dl></section><div class="section-wrap case-media-cover">'+media(p,True)+'</div>'
        body+=f'<nav class="case-toc section-wrap" aria-label="{L("프로젝트 목차","Case study sections")}">'+''.join(f'<a href="#{s["id"]}">{t(s["label"])}</a>' for s in p['sections'])+'</nav><div class="case-content">'
        for s in p['sections']:
            body+=f'<section class="case-block" id="{s["id"]}"><h2>{t(s["label"])}</h2><div class="case-text"><h3>{t(s["title"])}</h3>'
            body+=''.join(f'<p>{t(text)}</p>' for text in s['paragraphs'])
            if s.get('stats'):body+=stats(s['stats'])
            if s.get('image'):body+=f'<figure class="evidence-figure {s.get("image_class", "")}"><img src="{asset}{s["image"]}" alt="{esc(t(s["image_alt"]))}" loading="lazy"><figcaption>{t(s["image_alt"])}</figcaption></figure>'
            if s.get('note'):body+=f'<p class="case-note">{t(s["note"])}</p>'
            body+='</div></section>'
        body+=f'<section class="case-block" id="sources"><h2>{L("코드와 근거","Code & evidence")}</h2><div class="case-text"><p>{p["stack"]}</p><div class="case-links">'+''.join(external(label,url) for label,url in p['links'])+f'</div><p class="source-note">{L("2026.10.13 기준 · 공개 저장소, 프로젝트 기록 및 확인된 증빙을 바탕으로 작성했습니다.","Updated 13 October 2026 · Based on public repositories, project records, and verified evidence.")}</p></div></section></div>'
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
