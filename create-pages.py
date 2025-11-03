#!/usr/bin/env python3
"""
Script to generate all website pages from templates
"""

# Common head section
HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} | Zic0n Engineering</title>
  <meta name="description" content="{description}" />
  <meta name="theme-color" content="#0b1220" />
  <meta name="author" content="Zic0n Engineering" />
  <meta name="keywords" content="geotechnical engineering, transportation design, pavement engineering, civil engineering, roadway design, foundation design, San Diego, Philadelphia" />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://zic0n.com/{page}" />
  <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path fill='%2322d3ee' d='M3 12L12 3l9 9-9 9-9-9Z'/><path fill='%2360a5fa' d='M12 7v10M7 12h10'/></svg>" />
  <script src="https://cdn.tailwindcss.com" defer></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
  <script src="https://unpkg.com/feather-icons" defer></script>
  <meta property="og:title" content="{title} | Zic0n Engineering" />
  <meta property="og:description" content="{description}" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://zic0n.com/{page}" />
  <style>
    :root {{ --bg: #0b1220; --card: #111a2c; --muted: #94a3b8; --brand: #22d3ee; --accent: #60a5fa; --lime: #a3e635; }}
    html, body {{ font-family: Inter, system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; background: var(--bg); color: #e5e7eb; }}
    .glass {{ background: linear-gradient(140deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02)); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.08); }}
    .card {{ background: var(--card); border: 1px solid rgba(255,255,255,0.06); }}
    .gradient-text {{ background: linear-gradient(90deg, var(--brand), var(--accent)); -webkit-background-clip: text; background-clip: text; color: transparent; }}
    .tag {{ border: 1px dashed rgba(255,255,255,0.15); }}
    .shadow-soft {{ box-shadow: 0 10px 30px rgba(0,0,0,0.35); }}
    .section {{ scroll-margin-top: 90px; }}
    details[open] summary .chev {{ transform: rotate(180deg); }}
    .badge {{ border:1px solid rgba(255,255,255,0.12); border-radius:.5rem; padding:.25rem .5rem; font-size:.75rem; color:#cbd5e1 }}
    .grid-cols-auto {{ grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }}
    html {{ scroll-behavior: smooth; }}
    .sr-only {{ position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); white-space: nowrap; border-width: 0; }}
    .sr-only.focus\\:not-sr-only:focus {{ position: static; width: auto; height: auto; padding: inherit; margin: inherit; overflow: visible; clip: auto; white-space: normal; }}
    *:focus-visible {{ outline: 2px solid #22d3ee; outline-offset: 2px; }}
  </style>
</head>

<body class="antialiased">
  <a href="#main-content" class="sr-only focus:not-sr-only focus:absolute focus:top-4 focus:left-4 focus:z-50 focus:px-4 focus:py-2 focus:bg-cyan-500 focus:text-black focus:rounded-lg">Skip to main content</a>
'''

# Common header/nav
HEADER = '''  <header class="sticky top-0 z-50 bg-[#0b1220]/80 backdrop-blur border-b border-white/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
      <a href="index.html" class="flex items-center gap-3" aria-label="Zic0n Engineering Home">
        <div class="h-8 w-8 rounded-lg bg-cyan-400/20 grid place-items-center" aria-hidden="true">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M3 12L12 3l9 9-9 9-9-9Z" stroke="#22d3ee" stroke-width="1.5"/><path d="M12 7v10M7 12h10" stroke="#60a5fa" stroke-width="1.5"/></svg>
        </div>
        <span class="font-semibold tracking-wide">Zic0n Engineering</span>
      </a>
      <nav class="hidden md:flex items-center gap-8 text-sm text-slate-300">
        <a href="about.html" class="hover:text-white">About</a>
        <a href="services.html" class="hover:text-white">Services</a>
        <a href="markets.html" class="hover:text-white">Markets</a>
        <a href="capabilities.html" class="hover:text-white">Capabilities</a>
        <a href="projects.html" class="hover:text-white">Projects</a>
        <a href="approach.html" class="hover:text-white">Approach</a>
        <a href="leadership.html" class="hover:text-white">Leadership</a>
        <a href="advisory.html" class="hover:text-white">Advisory Panel</a>
        <a href="newsletter.html" class="hover:text-white">Newsletter</a>
        <a href="faqs.html" class="hover:text-white">FAQs</a>
        <a href="contact.html" class="hover:text-white">Contact</a>
      </nav>
      <button id="menuBtn" class="md:hidden p-2 rounded hover:bg-white/10" aria-label="Open menu">
        <i data-feather="menu"></i>
      </button>
    </div>
    <div id="mobileMenu" class="md:hidden hidden border-t border-white/10">
      <nav class="px-4 py-3 space-y-2 text-slate-300">
        <a href="about.html" class="block hover:text-white">About</a>
        <a href="services.html" class="block hover:text-white">Services</a>
        <a href="markets.html" class="block hover:text-white">Markets</a>
        <a href="capabilities.html" class="block hover:text-white">Capabilities</a>
        <a href="projects.html" class="block hover:text-white">Projects</a>
        <a href="approach.html" class="block hover:text-white">Approach</a>
        <a href="leadership.html" class="block hover:text-white">Leadership</a>
        <a href="advisory.html" class="block hover:text-white">Advisory Panel</a>
        <a href="newsletter.html" class="block hover:text-white">Newsletter</a>
        <a href="faqs.html" class="block hover:text-white">FAQs</a>
        <a href="contact.html" class="block hover:text-white">Contact</a>
      </nav>
    </div>
  </header>
'''

# Common footer
FOOTER = '''  <footer class="border-t border-white/10 py-10">
    <div class="max-w-7xl mx-auto px-6">
      <div class="flex flex-col md:flex-row items-start md:items-center justify-between gap-6">
        <div>
          <div class="flex items-center gap-3">
            <div class="h-8 w-8 rounded-lg bg-cyan-400/20 grid place-items-center">
              <svg width="20" height="20" viewBox="0 0 24 24" fill="none"><path d="M3 12L12 3l9 9-9 9-9-9Z" stroke="#22d3ee" stroke-width="1.5"/><path d="M12 7v10M7 12h10" stroke="#60a5fa" stroke-width="1.5"/></svg>
            </div>
            <span class="font-semibold">Zic0n Engineering</span>
          </div>
          <p class="text-slate-400 text-sm mt-2">© <span id="year"></span> Zic0n Engineering. All rights reserved.</p>
        </div>
        <div class="text-slate-400 text-sm grid sm:grid-cols-2 gap-x-10 gap-y-2">
          <div>San Diego, CA • Philadelphia, PA</div>
          <div>info@zic0n.com</div>
        </div>
        <div class="flex items-center gap-4 text-slate-400">
          <a href="https://www.linkedin.com/company/zic0n" target="_blank" rel="noopener noreferrer" class="hover:text-white transition" aria-label="Zic0n Engineering on LinkedIn"><i data-feather="linkedin" aria-hidden="true"></i></a>
          <a href="https://github.com/Arash-MH68/zic0n.github.io" target="_blank" rel="noopener noreferrer" class="hover:text-white transition" aria-label="Zic0n Engineering on GitHub"><i data-feather="github" aria-hidden="true"></i></a>
          <a href="mailto:info@zic0n.com" class="hover:text-white transition" aria-label="Send email to Zic0n Engineering"><i data-feather="mail" aria-hidden="true"></i></a>
        </div>
      </div>
    </div>
  </footer>

  <script>
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', function() {
        feather.replace();
        initializeApp();
      });
    } else {
      feather.replace();
      initializeApp();
    }
    function initializeApp() {
      const yearEl = document.getElementById('year');
      if (yearEl) yearEl.textContent = new Date().getFullYear();
      
      // Active navigation highlighting
      const currentPage = window.location.pathname.split('/').pop() || 'index.html';
      const navLinks = document.querySelectorAll('nav a[href]');
      navLinks.forEach(link => {
        const linkHref = link.getAttribute('href');
        if (linkHref === currentPage || (currentPage === '' && linkHref === 'index.html')) {
          link.classList.add('text-cyan-400', 'font-medium');
        }
      });
      
      const menuBtn = document.getElementById('menuBtn');
      const mobileMenu = document.getElementById('mobileMenu');
      if (menuBtn && mobileMenu) {
        menuBtn.addEventListener('click', () => {
          mobileMenu.classList.toggle('hidden');
          const icon = menuBtn.querySelector('i');
          if (icon) {
            if (mobileMenu.classList.contains('hidden')) {
              icon.setAttribute('data-feather', 'menu');
            } else {
              icon.setAttribute('data-feather', 'x');
            }
            feather.replace();
          }
        });
        const mobileLinks = mobileMenu.querySelectorAll('a');
        mobileLinks.forEach(link => {
          link.addEventListener('click', () => {
            mobileMenu.classList.add('hidden');
            const icon = menuBtn.querySelector('i');
            if (icon) {
              icon.setAttribute('data-feather', 'menu');
              feather.replace();
            }
          });
        });
      }
    }
  </script>
</body>
</html>
'''

# Page content templates
PAGES = {
    'about.html': {
        'title': 'About Us',
        'description': 'Learn about Zic0n Engineering, a partner-led civil engineering practice providing geotechnical, transportation, pavements & materials expertise.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="grid md:grid-cols-3 gap-10">
        <div class="md:col-span-2">
          <h1 class="text-4xl font-bold mb-3">About Zic0n</h1>
          <p class="text-slate-300/90 leading-relaxed mb-6">
            Zic0n is an applied civil engineering practice co-founded by two Ph.D. P.E.s. One founder is rooted in
            geotechnical and geo-structural design and instrumentation, while the other focuses on transportation and roadway design
            and asphalt materials. Together, we provide end-to-end support including site investigations, roadway and
            drainage plans, foundation and wall systems, pavement design and rehabilitation, lab testing, and analytics.
          </p>
          <ul class="grid sm:grid-cols-2 gap-3 text-slate-300/90">
            <li class="flex items-start gap-3"><i data-feather="check-circle" class="text-cyan-400 mt-0.5"></i> Foundations (shallow/deep, drilled shafts, piles), slope stability, seepage, ground improvement, and basin/levee assessments.</li>
            <li class="flex items-start gap-3"><i data-feather="check-circle" class="text-cyan-400 mt-0.5"></i> Roadway geometrics & alignments, roadside safety details, drainage inlets/culverts, signing & striping, quantities & estimates.</li>
            <li class="flex items-start gap-3"><i data-feather="check-circle" class="text-cyan-400 mt-0.5"></i> Pavements (AASHTO & mechanistic-empirical), asphalt binder/mixture testing, QA/QC, forensic & rehabilitation strategies, LCA.</li>
            <li class="flex items-start gap-3"><i data-feather="check-circle" class="text-cyan-400 mt-0.5"></i> Instrumentation programs (thermal/adfreeze, settlement), data QA/QC, parametric & Monte Carlo analyses, reporting pipelines.</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-6">
          <h2 class="font-semibold text-lg mb-2">Quick Facts</h2>
          <div class="space-y-2 text-slate-300">
            <div class="flex items-center justify-between"><span>Headquarters</span><span>San Diego, CA</span></div>
            <div class="flex items-center justify-between"><span>Regional Hubs</span><span>San Diego • Philadelphia</span></div>
            <div class="flex items-center justify-between"><span>Practice Areas</span><span>Geo • Transportation • Pavements • Materials • Data</span></div>
            <div class="flex items-center justify-between"><span>Delivery</span><span>Planning • Design • PM/CM • Advisory</span></div>
            <div class="flex items-center justify-between"><span>Licensure</span><span>PE (multi-state)</span></div>
          </div>
          <div class="mt-4 flex flex-wrap gap-2">
            <span class="badge">AASHTO</span><span class="badge">FHWA</span><span class="badge">USACE (select)</span><span class="badge">NAVFAC (select)</span>
          </div>
          <a href="contact.html" class="mt-4 inline-flex items-center gap-2 text-cyan-300 hover:text-cyan-200">
            Work with us <i data-feather="arrow-right"></i>
          </a>
        </div>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'services.html': {
        'title': 'Services',
        'description': 'Comprehensive civil engineering services including geotechnical, transportation, pavement design, materials testing, and data analytics.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h1 class="text-4xl sm:text-5xl font-bold mb-4">Our Services</h1>
        <p class="text-slate-300/90 text-lg">End-to-end civil engineering solutions from planning through construction and performance verification.</p>
      </div>
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="card rounded-2xl p-6">
          <div class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center mb-4">
            <i data-feather="layers" class="text-cyan-400"></i>
          </div>
          <h2 class="text-xl font-semibold mb-2">Geotechnical Engineering</h2>
          <p class="text-slate-300/90 text-sm mb-4">Foundations, slope stability, seepage analysis, ground improvement, and basin/levee assessments.</p>
          <ul class="text-sm text-slate-400 space-y-1">
            <li>• Shallow & deep foundations</li>
            <li>• Drilled shafts & piles</li>
            <li>• Retaining wall systems</li>
            <li>• Slope stability & erosion control</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-6">
          <div class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center mb-4">
            <i data-feather="map" class="text-cyan-400"></i>
          </div>
          <h2 class="text-xl font-semibold mb-2">Transportation Design</h2>
          <p class="text-slate-300/90 text-sm mb-4">Roadway geometrics, alignments, drainage systems, safety features, and cost estimation.</p>
          <ul class="text-sm text-slate-400 space-y-1">
            <li>• Roadway geometrics & alignments</li>
            <li>• Drainage inlets & culverts</li>
            <li>• Signing & striping</li>
            <li>• Roadside safety details</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-6">
          <div class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center mb-4">
            <i data-feather="grid" class="text-cyan-400"></i>
          </div>
          <h2 class="text-xl font-semibold mb-2">Pavement Engineering</h2>
          <p class="text-slate-300/90 text-sm mb-4">AASHTO and mechanistic-empirical design, forensic analysis, rehabilitation strategies, and LCA.</p>
          <ul class="text-sm text-slate-400 space-y-1">
            <li>• Pavement design & analysis</li>
            <li>• Forensic investigation</li>
            <li>• Rehabilitation strategies</li>
            <li>• Life cycle assessment (LCA)</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-6">
          <div class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center mb-4">
            <i data-feather="flask" class="text-cyan-400"></i>
          </div>
          <h2 class="text-xl font-semibold mb-2">Materials Testing</h2>
          <p class="text-slate-300/90 text-sm mb-4">Asphalt binder and mixture testing, QA/QC programs, and performance verification.</p>
          <ul class="text-sm text-slate-400 space-y-1">
            <li>• Asphalt binder testing</li>
            <li>• Mixture design & testing</li>
            <li>• QA/QC programs</li>
            <li>• Performance verification</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-6">
          <div class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center mb-4">
            <i data-feather="activity" class="text-cyan-400"></i>
          </div>
          <h2 class="text-xl font-semibold mb-2">Instrumentation</h2>
          <p class="text-slate-300/90 text-sm mb-4">Thermal/adfreeze monitoring, settlement tracking, data QA/QC, and reporting pipelines.</p>
          <ul class="text-sm text-slate-400 space-y-1">
            <li>• Thermal & adfreeze monitoring</li>
            <li>• Settlement tracking</li>
            <li>• Data acquisition systems</li>
            <li>• Real-time reporting</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-6">
          <div class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center mb-4">
            <i data-feather="bar-chart-2" class="text-cyan-400"></i>
          </div>
          <h2 class="text-xl font-semibold mb-2">Data Analytics</h2>
          <p class="text-slate-300/90 text-sm mb-4">Parametric and Monte Carlo analyses, machine learning applications, and predictive modeling.</p>
          <ul class="text-sm text-slate-400 space-y-1">
            <li>• Parametric & Monte Carlo analysis</li>
            <li>• Machine learning applications</li>
            <li>• Predictive modeling</li>
            <li>• Performance prediction</li>
          </ul>
        </div>
      </div>
      <div class="mt-12 text-center">
        <a href="contact.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-cyan-500 text-black font-semibold hover:bg-cyan-400 transition">
          Discuss Your Project <i data-feather="arrow-right"></i>
        </a>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'markets.html': {
        'title': 'Markets',
        'description': 'Zic0n Engineering serves energy, DOT, water, and industrial markets across the United States.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h1 class="text-4xl sm:text-5xl font-bold mb-4">Markets We Serve</h1>
        <p class="text-slate-300/90 text-lg">Delivering engineering solutions across diverse sectors throughout the United States.</p>
      </div>
      <div class="grid md:grid-cols-2 gap-8 mb-12">
        <div class="card rounded-2xl p-8">
          <div class="h-16 w-16 rounded-xl bg-cyan-400/20 grid place-items-center mb-6">
            <i data-feather="zap" class="text-cyan-400 w-8 h-8"></i>
          </div>
          <h2 class="text-2xl font-semibold mb-4">Energy</h2>
          <p class="text-slate-300/90 mb-4">Supporting solar, wind, BESS, and traditional energy infrastructure projects with geotechnical and civil engineering expertise.</p>
          <ul class="text-sm text-slate-400 space-y-2">
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Solar & wind farm foundations</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Battery energy storage systems (BESS)</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Site development & access roads</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Geotechnical investigations</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-8">
          <div class="h-16 w-16 rounded-xl bg-cyan-400/20 grid place-items-center mb-6">
            <i data-feather="truck" class="text-cyan-400 w-8 h-8"></i>
          </div>
          <h2 class="text-2xl font-semibold mb-4">Transportation (DOT)</h2>
          <p class="text-slate-300/90 mb-4">State and federal transportation projects including highways, bridges, and infrastructure rehabilitation.</p>
          <ul class="text-sm text-slate-400 space-y-2">
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Highway & roadway design</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Bridge approach design</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Pavement rehabilitation</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Drainage & stormwater</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-8">
          <div class="h-16 w-16 rounded-xl bg-cyan-400/20 grid place-items-center mb-6">
            <i data-feather="droplet" class="text-cyan-400 w-8 h-8"></i>
          </div>
          <h2 class="text-2xl font-semibold mb-4">Water Infrastructure</h2>
          <p class="text-slate-300/90 mb-4">Water treatment facilities, reservoirs, levees, and water resource infrastructure projects.</p>
          <ul class="text-sm text-slate-400 space-y-2">
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Levee & basin assessments</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Water treatment facilities</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Seepage analysis</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Ground improvement</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-8">
          <div class="h-16 w-16 rounded-xl bg-cyan-400/20 grid place-items-center mb-6">
            <i data-feather="building" class="text-cyan-400 w-8 h-8"></i>
          </div>
          <h2 class="text-2xl font-semibold mb-4">Industrial</h2>
          <p class="text-slate-300/90 mb-4">Commercial and industrial facilities requiring geotechnical, structural, and materials engineering services.</p>
          <ul class="text-sm text-slate-400 space-y-2">
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Site investigations</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Foundation design</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Pavement design</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Materials testing</li>
          </ul>
        </div>
      </div>
      <div class="card rounded-2xl p-8 text-center bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
        <h2 class="text-2xl font-semibold mb-4">Service Areas</h2>
        <p class="text-slate-300/90 mb-6">We serve clients throughout the United States with regional hubs in San Diego, CA and Philadelphia, PA.</p>
        <div class="flex flex-wrap justify-center gap-4 text-sm">
          <span class="badge">West Coast</span>
          <span class="badge">Southwest</span>
          <span class="badge">Mountain States</span>
          <span class="badge">Mid-Atlantic</span>
          <span class="badge">Nationwide</span>
        </div>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'capabilities.html': {
        'title': 'Capabilities',
        'description': 'Technical capabilities and expertise in geotechnical, transportation, pavement engineering, materials testing, and data analytics.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h1 class="text-4xl sm:text-5xl font-bold mb-4">Technical Capabilities</h1>
        <p class="text-slate-300/90 text-lg">Advanced engineering expertise backed by research, innovation, and practical application.</p>
      </div>
      <div class="space-y-12">
        <div class="grid md:grid-cols-2 gap-8 items-center">
          <div>
            <h2 class="text-3xl font-semibold mb-4">Geotechnical & Geo-Structural</h2>
            <p class="text-slate-300/90 mb-6">Comprehensive geotechnical engineering services from site characterization to design and monitoring.</p>
            <div class="grid sm:grid-cols-2 gap-4">
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Foundation Design</h3>
                <p class="text-sm text-slate-400">Shallow and deep foundations, drilled shafts, driven and drilled piles.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Slope Stability</h3>
                <p class="text-sm text-slate-400">Limit equilibrium and finite element analyses for slopes and embankments.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Ground Improvement</h3>
                <p class="text-sm text-slate-400">Vibro-compaction, dynamic deep compaction, and other improvement techniques.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Seepage Analysis</h3>
                <p class="text-sm text-slate-400">Seepage modeling for dams, levees, and retaining structures.</p>
              </div>
            </div>
          </div>
          <div class="card rounded-2xl p-6">
            <div class="aspect-video rounded-lg overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
              <img src="https://images.unsplash.com/photo-1583195764036-6dc248ac07d9?w=800&h=600&fit=crop&q=80" alt="Geotechnical drilling rig and soil investigation" class="w-full h-full object-cover opacity-50">
            </div>
          </div>
        </div>
        <div class="grid md:grid-cols-2 gap-8 items-center">
          <div class="card rounded-2xl p-6 order-2 md:order-1">
            <div class="aspect-video rounded-lg overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
              <img src="https://images.unsplash.com/photo-1519791883288-dc8bd696e667?w=800&h=600&fit=crop&q=80" alt="Highway and roadway infrastructure design" class="w-full h-full object-cover opacity-50">
            </div>
          </div>
          <div class="order-1 md:order-2">
            <h2 class="text-3xl font-semibold mb-4">Transportation & Roadway</h2>
            <p class="text-slate-300/90 mb-6">Complete transportation engineering services from planning through detailed design.</p>
            <div class="grid sm:grid-cols-2 gap-4">
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Roadway Design</h3>
                <p class="text-sm text-slate-400">Geometrics, alignments, superelevation, and sight distance.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Drainage Design</h3>
                <p class="text-sm text-slate-400">Stormwater management, inlets, culverts, and drainage systems.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Safety Features</h3>
                <p class="text-sm text-slate-400">Roadside safety, guardrails, and traffic control design.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Cost Estimation</h3>
                <p class="text-sm text-slate-400">Quantity takeoffs and cost estimates for projects.</p>
              </div>
            </div>
          </div>
        </div>
        <div class="grid md:grid-cols-2 gap-8 items-center">
          <div>
            <h2 class="text-3xl font-semibold mb-4">Pavements & Materials</h2>
            <p class="text-slate-300/90 mb-6">Advanced pavement engineering and materials science with research-backed methodologies.</p>
            <div class="grid sm:grid-cols-2 gap-4">
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Pavement Design</h3>
                <p class="text-sm text-slate-400">AASHTO and mechanistic-empirical design methods.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Materials Testing</h3>
                <p class="text-sm text-slate-400">Asphalt binder and mixture testing, QC/QA programs.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Forensic Analysis</h3>
                <p class="text-sm text-slate-400">Failure investigation and rehabilitation planning.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Life Cycle Assessment</h3>
                <p class="text-sm text-slate-400">LCA for sustainable pavement solutions.</p>
              </div>
            </div>
          </div>
          <div class="card rounded-2xl p-6">
            <div class="aspect-video rounded-lg overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
              <img src="https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=800&h=600&fit=crop&q=80" alt="Pavement engineering and road construction" class="w-full h-full object-cover opacity-50">
            </div>
          </div>
        </div>
        <div class="grid md:grid-cols-2 gap-8 items-center">
          <div class="card rounded-2xl p-6 order-2 md:order-1">
            <div class="aspect-video rounded-lg overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
              <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop&q=80" alt="Data analytics and infrastructure monitoring" class="w-full h-full object-cover opacity-50">
            </div>
          </div>
          <div class="order-1 md:order-2">
            <h2 class="text-3xl font-semibold mb-4">Data & Analytics</h2>
            <p class="text-slate-300/90 mb-6">Leveraging machine learning and advanced analytics for infrastructure performance prediction.</p>
            <div class="grid sm:grid-cols-2 gap-4">
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Machine Learning</h3>
                <p class="text-sm text-slate-400">Predictive modeling for pavement and infrastructure performance.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Monte Carlo Analysis</h3>
                <p class="text-sm text-slate-400">Probabilistic analysis for uncertainty quantification.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Instrumentation</h3>
                <p class="text-sm text-slate-400">Real-time monitoring and data acquisition systems.</p>
              </div>
              <div class="card rounded-xl p-4">
                <h3 class="font-semibold mb-2">Data Pipelines</h3>
                <p class="text-sm text-slate-400">Automated reporting and data management systems.</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'projects.html': {
        'title': 'Projects',
        'description': 'Featured engineering projects showcasing Zic0n\'s expertise in geotechnical, transportation, and pavement engineering.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h1 class="text-4xl sm:text-5xl font-bold mb-4">Project Highlights</h1>
        <p class="text-slate-300/90 text-lg">Featured projects demonstrating our engineering expertise across diverse applications.</p>
      </div>
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <div class="card rounded-2xl overflow-hidden hover:scale-[1.02] transition-transform">
          <div class="aspect-video overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
            <img src="https://images.unsplash.com/photo-1473341304170-971dccb5ac1e?w=800&h=600&fit=crop&q=80" alt="Solar energy infrastructure project" class="w-full h-full object-cover opacity-70">
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 mb-2">
              <span class="badge text-xs">Energy</span>
              <span class="badge text-xs">Geotechnical</span>
            </div>
            <h2 class="text-xl font-semibold mb-2">Solar & BESS Foundation Design</h2>
            <p class="text-sm text-slate-300/90 mb-4">Comprehensive geotechnical investigation and foundation design for large-scale solar and battery energy storage systems.</p>
            <ul class="text-xs text-slate-400 space-y-1">
              <li>• Site characterization & testing</li>
              <li>• Foundation system design</li>
              <li>• Slope stability analysis</li>
              <li>• Construction support</li>
            </ul>
          </div>
        </div>
        <div class="card rounded-2xl overflow-hidden hover:scale-[1.02] transition-transform">
          <div class="aspect-video overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
            <img src="https://images.unsplash.com/photo-1519791883288-dc8bd696e667?w=800&h=600&fit=crop&q=80" alt="Highway infrastructure and roadway rehabilitation" class="w-full h-full object-cover opacity-70">
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 mb-2">
              <span class="badge text-xs">Transportation</span>
              <span class="badge text-xs">Roadway</span>
            </div>
            <h2 class="text-xl font-semibold mb-2">Highway Rehabilitation Project</h2>
            <p class="text-sm text-slate-300/90 mb-4">Complete roadway design including geometrics, drainage, pavement design, and cost estimation for major highway project.</p>
            <ul class="text-xs text-slate-400 space-y-1">
              <li>• Roadway geometrics & alignments</li>
              <li>• Drainage system design</li>
              <li>• Pavement rehabilitation strategy</li>
              <li>• Construction documents</li>
            </ul>
          </div>
        </div>
        <div class="card rounded-2xl overflow-hidden hover:scale-[1.02] transition-transform">
          <div class="aspect-video overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
            <img src="https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=800&h=600&fit=crop&q=80" alt="Asphalt paving and pavement construction" class="w-full h-full object-cover opacity-70">
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 mb-2">
              <span class="badge text-xs">Pavement</span>
              <span class="badge text-xs">Materials</span>
            </div>
            <h2 class="text-xl font-semibold mb-2">Pavement Performance Study</h2>
            <p class="text-sm text-slate-300/90 mb-4">Machine learning-based pavement deterioration prediction and optimization for transportation agency.</p>
            <ul class="text-xs text-slate-400 space-y-1">
              <li>• Performance data analysis</li>
              <li>• Machine learning modeling</li>
              <li>• Maintenance planning</li>
              <li>• Life cycle optimization</li>
            </ul>
          </div>
        </div>
        <div class="card rounded-2xl overflow-hidden hover:scale-[1.02] transition-transform">
          <div class="aspect-video overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
            <img src="https://images.unsplash.com/photo-1583195764036-6dc248ac07d9?w=800&h=600&fit=crop&q=80" alt="Deep foundation construction with drilling rigs and piles" class="w-full h-full object-cover opacity-70">
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 mb-2">
              <span class="badge text-xs">Geotechnical</span>
              <span class="badge text-xs">Foundation</span>
            </div>
            <h2 class="text-xl font-semibold mb-2">Deep Foundation Design</h2>
            <p class="text-sm text-slate-300/90 mb-4">Drilled shaft and driven pile foundation design for industrial facility on challenging soil conditions.</p>
            <ul class="text-xs text-slate-400 space-y-1">
              <li>• Comprehensive site investigation</li>
              <li>• Deep foundation design</li>
              <li>• Load testing program</li>
              <li>• Construction observation</li>
            </ul>
          </div>
        </div>
        <div class="card rounded-2xl overflow-hidden hover:scale-[1.02] transition-transform">
          <div class="aspect-video overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
            <img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&h=600&fit=crop&q=80" alt="Water infrastructure and civil engineering project" class="w-full h-full object-cover opacity-70">
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 mb-2">
              <span class="badge text-xs">Water</span>
              <span class="badge text-xs">Geotechnical</span>
            </div>
            <h2 class="text-xl font-semibold mb-2">Levee Assessment & Design</h2>
            <p class="text-sm text-slate-300/90 mb-4">Geotechnical evaluation and seepage analysis for levee system improvements and flood protection.</p>
            <ul class="text-xs text-slate-400 space-y-1">
              <li>• Levee condition assessment</li>
              <li>• Seepage analysis</li>
              <li>• Stability evaluation</li>
              <li>• Improvement recommendations</li>
            </ul>
          </div>
        </div>
        <div class="card rounded-2xl overflow-hidden hover:scale-[1.02] transition-transform">
          <div class="aspect-video overflow-hidden bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
            <img src="https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?w=800&h=600&fit=crop&q=80" alt="Materials testing and laboratory analysis" class="w-full h-full object-cover opacity-70">
          </div>
          <div class="p-6">
            <div class="flex items-center gap-2 mb-2">
              <span class="badge text-xs">Materials</span>
              <span class="badge text-xs">Testing</span>
            </div>
            <h2 class="text-xl font-semibold mb-2">Asphalt Materials Research</h2>
            <p class="text-sm text-slate-300/90 mb-4">Laboratory testing and performance evaluation program for innovative asphalt binder and mixture technologies.</p>
            <ul class="text-xs text-slate-400 space-y-1">
              <li>• Advanced binder testing</li>
              <li>• Mixture design optimization</li>
              <li>• Performance verification</li>
              <li>• Quality control programs</li>
            </ul>
          </div>
        </div>
      </div>
      <div class="mt-12 text-center">
        <p class="text-slate-300/90 mb-6">Interested in learning more about our project experience?</p>
        <a href="contact.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-cyan-500 text-black font-semibold hover:bg-cyan-400 transition">
          Contact Us <i data-feather="arrow-right"></i>
        </a>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'approach.html': {
        'title': 'Approach',
        'description': 'Zic0n Engineering\'s methodology: research-backed solutions, data-driven decisions, and client-focused delivery.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h1 class="text-4xl sm:text-5xl font-bold mb-4">Our Approach</h1>
        <p class="text-slate-300/90 text-lg">Research-backed solutions, data-driven decisions, and client-focused delivery.</p>
      </div>
      <div class="grid md:grid-cols-2 gap-8 mb-12">
        <div class="card rounded-2xl p-8">
          <div class="h-16 w-16 rounded-xl bg-cyan-400/20 grid place-items-center mb-6">
            <i data-feather="book-open" class="text-cyan-400 w-8 h-8"></i>
          </div>
          <h2 class="text-2xl font-semibold mb-4">Research-Backed</h2>
          <p class="text-slate-300/90 mb-4">Our practice is founded on Ph.D.-level research expertise. We stay current with the latest advances in geotechnical engineering, pavement science, and materials technology.</p>
          <ul class="text-sm text-slate-400 space-y-2">
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Active research in pavement engineering & materials</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Published peer-reviewed research</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Integration of latest methodologies</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Innovation in applied engineering</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-8">
          <div class="h-16 w-16 rounded-xl bg-cyan-400/20 grid place-items-center mb-6">
            <i data-feather="database" class="text-cyan-400 w-8 h-8"></i>
          </div>
          <h2 class="text-2xl font-semibold mb-4">Data-Driven</h2>
          <p class="text-slate-300/90 mb-4">We leverage advanced analytics, machine learning, and probabilistic methods to make informed engineering decisions and optimize solutions.</p>
          <ul class="text-sm text-slate-400 space-y-2">
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Machine learning for performance prediction</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Monte Carlo & probabilistic analysis</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Real-time instrumentation & monitoring</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Data-driven optimization</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-8">
          <div class="h-16 w-16 rounded-xl bg-cyan-400/20 grid place-items-center mb-6">
            <i data-feather="target" class="text-cyan-400 w-8 h-8"></i>
          </div>
          <h2 class="text-2xl font-semibold mb-4">Client-Focused</h2>
          <p class="text-slate-300/90 mb-4">We prioritize understanding client needs, delivering practical solutions, and providing responsive support throughout the project lifecycle.</p>
          <ul class="text-sm text-slate-400 space-y-2">
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Partner-led project delivery</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Clear communication & collaboration</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Practical, constructible solutions</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Responsive support & service</li>
          </ul>
        </div>
        <div class="card rounded-2xl p-8">
          <div class="h-16 w-16 rounded-xl bg-cyan-400/20 grid place-items-center mb-6">
            <i data-feather="leaf" class="text-cyan-400 w-8 h-8"></i>
          </div>
          <h2 class="text-2xl font-semibold mb-4">Sustainability</h2>
          <p class="text-slate-300/90 mb-4">We integrate life cycle assessment, environmental considerations, and sustainable practices into our engineering solutions.</p>
          <ul class="text-sm text-slate-400 space-y-2">
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Life cycle assessment (LCA)</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Environmental impact evaluation</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Sustainable material selection</li>
            <li class="flex items-start gap-2"><i data-feather="check" class="text-cyan-400 mt-0.5 w-4 h-4"></i> Long-term performance optimization</li>
          </ul>
        </div>
      </div>
      <div class="card rounded-2xl p-8 bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
        <h2 class="text-2xl font-semibold mb-4 text-center">Quality Assurance</h2>
        <p class="text-slate-300/90 text-center mb-6 max-w-2xl mx-auto">All work is performed under the direct supervision of licensed Professional Engineers (PE) with multi-state licensure. We maintain rigorous quality control and adhere to industry standards including AASHTO, FHWA, and applicable state and federal guidelines.</p>
        <div class="flex flex-wrap justify-center gap-4">
          <span class="badge">PE Licensed</span>
          <span class="badge">AASHTO Standards</span>
          <span class="badge">FHWA Guidelines</span>
          <span class="badge">Quality Assured</span>
        </div>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'leadership.html': {
        'title': 'Leadership',
        'description': 'Meet the leadership team at Zic0n Engineering: Ph.D. P.E.s with expertise in geotechnical and transportation engineering.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h1 class="text-4xl sm:text-5xl font-bold mb-4">Leadership Team</h1>
        <p class="text-slate-300/90 text-lg">Partner-led engineering practice with Ph.D. and Professional Engineering expertise.</p>
      </div>
      <div class="grid md:grid-cols-2 gap-12 mb-16">
        <div class="card rounded-2xl p-8 text-center">
          <div class="aspect-square max-w-xs mx-auto mb-6 rounded-2xl overflow-hidden bg-gradient-to-br from-cyan-400/20 to-blue-400/20">
            <img src="https://images.unsplash.com/photo-1560250097-0b93528c311a?w=600&h=600&fit=crop&q=80" alt="Professional engineer and co-founder" class="w-full h-full object-cover opacity-80">
          </div>
          <h2 class="text-2xl font-semibold mb-2">Co-Founder</h2>
          <p class="text-cyan-400 mb-4">Ph.D., P.E.</p>
          <p class="text-slate-300/90 mb-4">Geotechnical & Geo-Structural Engineering</p>
          <p class="text-sm text-slate-400 mb-6">Expertise in geotechnical design, instrumentation, slope stability, foundations, and ground improvement. Specialized experience with thermal/adfreeze systems and settlement monitoring programs.</p>
          <div class="flex flex-wrap justify-center gap-2 mb-4">
            <span class="badge text-xs">Geotechnical</span>
            <span class="badge text-xs">Foundation Design</span>
            <span class="badge text-xs">Instrumentation</span>
          </div>
        </div>
        <div class="card rounded-2xl p-8 text-center">
          <div class="aspect-square max-w-xs mx-auto mb-6 rounded-2xl overflow-hidden bg-gradient-to-br from-cyan-400/20 to-blue-400/20">
            <img src="https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?w=600&h=600&fit=crop&q=80" alt="Professional engineer and co-founder" class="w-full h-full object-cover opacity-80">
          </div>
          <h2 class="text-2xl font-semibold mb-2">Co-Founder</h2>
          <p class="text-cyan-400 mb-4">Ph.D., P.E.</p>
          <p class="text-slate-300/90 mb-4">Transportation & Pavement Engineering</p>
          <p class="text-sm text-slate-400 mb-6">Expertise in roadway design, pavement engineering, asphalt materials, and machine learning applications. Active research in pavement performance prediction and deterioration modeling.</p>
          <div class="flex flex-wrap justify-center gap-2 mb-4">
            <span class="badge text-xs">Transportation</span>
            <span class="badge text-xs">Pavement</span>
            <span class="badge text-xs">Materials</span>
          </div>
          <div class="mt-6">
            <a href="newsletter.html" class="inline-flex items-center gap-2 text-cyan-300 hover:text-cyan-200 text-sm">
              View Research Profile <i data-feather="arrow-right" class="w-4 h-4"></i>
            </a>
          </div>
        </div>
      </div>
      <div class="card rounded-2xl p-8 bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
        <h2 class="text-2xl font-semibold mb-4 text-center">Our Commitment</h2>
        <p class="text-slate-300/90 text-center mb-6 max-w-2xl mx-auto">Both founders are licensed Professional Engineers with multi-state licensure and maintain active research programs. This unique combination of practical engineering experience and research innovation allows us to deliver cutting-edge solutions grounded in proven methodologies.</p>
        <div class="flex flex-wrap justify-center gap-4">
          <span class="badge">Multi-State PE Licensed</span>
          <span class="badge">Active Research</span>
          <span class="badge">Published Research</span>
          <span class="badge">Industry Experience</span>
        </div>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'advisory.html': {
        'title': 'Advisory Panel',
        'description': 'Zic0n Engineering\'s advisory panel: industry experts providing strategic guidance and technical expertise.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h1 class="text-4xl sm:text-5xl font-bold mb-4">Advisory Panel</h1>
        <p class="text-slate-300/90 text-lg">Industry experts providing strategic guidance and technical expertise to advance our engineering practice.</p>
      </div>
      <div class="grid md:grid-cols-2 gap-12 max-w-5xl mx-auto">
        <div class="card rounded-2xl p-8 text-center">
          <div class="aspect-square max-w-xs mx-auto mb-6 rounded-2xl overflow-hidden">
            <img src="images/Arash_Hosseini.jpg" alt="Dr. Arash Hosseini" class="w-full h-full object-cover" onerror="this.src='https://images.unsplash.com/photo-1560250097-0b93528c311a?w=600&h=600&fit=crop&q=80'; this.onerror=null;">
          </div>
          <h2 class="text-2xl font-semibold mb-2">Dr. Arash Hosseini</h2>
          <p class="text-cyan-400 mb-4">Advisory Panel Member</p>
          <p class="text-slate-300/90 mb-4">Expert in geotechnical engineering, pavement engineering, and materials science with extensive research and industry experience.</p>
          <div class="flex flex-wrap justify-center gap-2">
            <span class="badge text-xs">Geotechnical</span>
            <span class="badge text-xs">Pavement</span>
            <span class="badge text-xs">Research</span>
          </div>
        </div>
        <div class="card rounded-2xl p-8 text-center">
          <div class="aspect-square max-w-xs mx-auto mb-6 rounded-2xl overflow-hidden bg-gradient-to-br from-cyan-400/20 to-blue-400/20 flex items-center justify-center">
            <i data-feather="user" class="w-24 h-24 text-cyan-400/50"></i>
          </div>
          <h2 class="text-2xl font-semibold mb-2">Dr. Ahmed Abdalla</h2>
          <p class="text-cyan-400 mb-4">Advisory Panel Member</p>
          <p class="text-slate-300/90 mb-4">Expert in civil engineering with specialized knowledge in infrastructure systems and engineering practice.</p>
          <div class="flex flex-wrap justify-center gap-2">
            <span class="badge text-xs">Infrastructure</span>
            <span class="badge text-xs">Engineering</span>
            <span class="badge text-xs">Advisory</span>
          </div>
        </div>
      </div>
      <div class="mt-16 card rounded-2xl p-8 bg-gradient-to-br from-cyan-400/10 to-blue-400/10 text-center max-w-3xl mx-auto">
        <h2 class="text-2xl font-semibold mb-4">Advisory Panel Mission</h2>
        <p class="text-slate-300/90">Our advisory panel provides strategic guidance, technical review, and industry insights to ensure Zic0n Engineering maintains the highest standards of engineering excellence and remains at the forefront of technological innovation.</p>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'faqs.html': {
        'title': 'FAQs',
        'description': 'Frequently asked questions about Zic0n Engineering\'s services, expertise, and project delivery.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-4xl mx-auto px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h1 class="text-4xl sm:text-5xl font-bold mb-4">Frequently Asked Questions</h1>
        <p class="text-slate-300/90 text-lg">Common questions about our services, expertise, and how we work.</p>
      </div>
      <div class="space-y-4">
        <details class="card rounded-xl p-6 group">
          <summary class="flex items-center justify-between cursor-pointer list-none">
            <h2 class="text-xl font-semibold">What services does Zic0n Engineering provide?</h2>
            <i data-feather="chevron-down" class="chev transition-transform text-cyan-400"></i>
          </summary>
          <div class="mt-4 pt-4 border-t border-white/10">
            <p class="text-slate-300/90">Zic0n Engineering provides comprehensive civil engineering services including geotechnical and geo-structural design, transportation and roadway design, pavement engineering, asphalt materials testing, instrumentation programs, and data analytics. We serve energy, DOT, water, and industrial markets.</p>
          </div>
        </details>
        <details class="card rounded-xl p-6 group">
          <summary class="flex items-center justify-between cursor-pointer list-none">
            <h2 class="text-xl font-semibold">Where is Zic0n Engineering located?</h2>
            <i data-feather="chevron-down" class="chev transition-transform text-cyan-400"></i>
          </summary>
          <div class="mt-4 pt-4 border-t border-white/10">
            <p class="text-slate-300/90">Zic0n Engineering has headquarters in San Diego, CA and a regional hub in Philadelphia, PA. We serve clients throughout the United States, including West Coast, Southwest, Mountain States, and Mid-Atlantic regions.</p>
          </div>
        </details>
        <details class="card rounded-xl p-6 group">
          <summary class="flex items-center justify-between cursor-pointer list-none">
            <h2 class="text-xl font-semibold">What makes Zic0n Engineering unique?</h2>
            <i data-feather="chevron-down" class="chev transition-transform text-cyan-400"></i>
          </summary>
          <div class="mt-4 pt-4 border-t border-white/10">
            <p class="text-slate-300/90">Zic0n is co-founded by two Ph.D. P.E.s who combine deep research expertise with practical engineering experience. We integrate machine learning, advanced analytics, and research-backed methodologies into our engineering solutions. Our partner-led approach ensures direct involvement of senior engineers in every project.</p>
          </div>
        </details>
        <details class="card rounded-xl p-6 group">
          <summary class="flex items-center justify-between cursor-pointer list-none">
            <h2 class="text-xl font-semibold">Are your engineers licensed?</h2>
            <i data-feather="chevron-down" class="chev transition-transform text-cyan-400"></i>
          </summary>
          <div class="mt-4 pt-4 border-t border-white/10">
            <p class="text-slate-300/90">Yes, both co-founders are licensed Professional Engineers (P.E.) with multi-state licensure. All engineering work is performed under the direct supervision of licensed engineers in compliance with state licensing requirements.</p>
          </div>
        </details>
        <details class="card rounded-xl p-6 group">
          <summary class="flex items-center justify-between cursor-pointer list-none">
            <h2 class="text-xl font-semibold">Do you work on federal projects?</h2>
            <i data-feather="chevron-down" class="chev transition-transform text-cyan-400"></i>
          </summary>
          <div class="mt-4 pt-4 border-t border-white/10">
            <p class="text-slate-300/90">Yes, we provide select services for USACE (U.S. Army Corps of Engineers) and NAVFAC (Naval Facilities Engineering Systems Command) projects, in addition to state DOT, energy, water, and industrial projects.</p>
          </div>
        </details>
        <details class="card rounded-xl p-6 group">
          <summary class="flex items-center justify-between cursor-pointer list-none">
            <h2 class="text-xl font-semibold">How do you use machine learning in engineering?</h2>
            <i data-feather="chevron-down" class="chev transition-transform text-cyan-400"></i>
          </summary>
          <div class="mt-4 pt-4 border-t border-white/10">
            <p class="text-slate-300/90">We apply machine learning techniques to predict infrastructure performance, optimize maintenance strategies, and analyze large datasets. Our research includes pavement deterioration prediction, roughness index forecasting, and performance modeling. These methods complement traditional engineering approaches to provide more accurate predictions and cost-effective solutions.</p>
          </div>
        </details>
        <details class="card rounded-xl p-6 group">
          <summary class="flex items-center justify-between cursor-pointer list-none">
            <h2 class="text-xl font-semibold">What types of projects do you typically handle?</h2>
            <i data-feather="chevron-down" class="chev transition-transform text-cyan-400"></i>
          </summary>
          <div class="mt-4 pt-4 border-t border-white/10">
            <p class="text-slate-300/90">We handle projects ranging from small site investigations to large infrastructure programs. Typical projects include solar and BESS foundation design, highway rehabilitation, pavement performance studies, deep foundation design, levee assessments, and materials testing programs. Project sizes vary from feasibility studies to complete design and construction support.</p>
          </div>
        </details>
        <details class="card rounded-xl p-6 group">
          <summary class="flex items-center justify-between cursor-pointer list-none">
            <h2 class="text-xl font-semibold">How do I get started with a project?</h2>
            <i data-feather="chevron-down" class="chev transition-transform text-cyan-400"></i>
          </summary>
          <div class="mt-4 pt-4 border-t border-white/10">
            <p class="text-slate-300/90">Contact us through our contact page or email info@zic0n.com. We'll schedule a consultation to discuss your project needs, scope, timeline, and budget. Our partner-led approach means you'll speak directly with senior engineers who understand your requirements.</p>
          </div>
        </details>
      </div>
      <div class="mt-12 text-center">
        <p class="text-slate-300/90 mb-6">Have additional questions?</p>
        <a href="contact.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-lg bg-cyan-500 text-black font-semibold hover:bg-cyan-400 transition">
          Contact Us <i data-feather="arrow-right"></i>
        </a>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'contact.html': {
        'title': 'Contact',
        'description': 'Contact Zic0n Engineering for engineering consultation, project inquiries, or to discuss your infrastructure needs.',
        'content': '''  <main id="main-content">
  <section class="section py-20">
    <div class="max-w-7xl mx-auto px-6">
      <div class="text-center max-w-3xl mx-auto mb-16">
        <h1 class="text-4xl sm:text-5xl font-bold mb-4">Contact Us</h1>
        <p class="text-slate-300/90 text-lg">Get in touch to discuss your engineering project needs. We're here to help.</p>
      </div>
      <div class="grid md:grid-cols-2 gap-12">
        <div class="card rounded-2xl p-8">
          <h2 class="text-2xl font-semibold mb-6">Send Us a Message</h2>
          <form action="mailto:info@zic0n.com" method="post" enctype="text/plain" class="space-y-6">
            <div>
              <label for="name" class="block text-sm font-medium text-slate-300 mb-2">Name</label>
              <input type="text" id="name" name="name" required class="w-full px-4 py-3 rounded-lg bg-white/5 border border-white/10 focus:outline-none focus:ring-2 focus:ring-cyan-500 text-white" placeholder="Your name">
            </div>
            <div>
              <label for="email" class="block text-sm font-medium text-slate-300 mb-2">Email</label>
              <input type="email" id="email" name="email" required class="w-full px-4 py-3 rounded-lg bg-white/5 border border-white/10 focus:outline-none focus:ring-2 focus:ring-cyan-500 text-white" placeholder="your.email@example.com">
            </div>
            <div>
              <label for="subject" class="block text-sm font-medium text-slate-300 mb-2">Subject</label>
              <input type="text" id="subject" name="subject" required class="w-full px-4 py-3 rounded-lg bg-white/5 border border-white/10 focus:outline-none focus:ring-2 focus:ring-cyan-500 text-white" placeholder="Project inquiry">
            </div>
            <div>
              <label for="message" class="block text-sm font-medium text-slate-300 mb-2">Message</label>
              <textarea id="message" name="message" rows="6" required class="w-full px-4 py-3 rounded-lg bg-white/5 border border-white/10 focus:outline-none focus:ring-2 focus:ring-cyan-500 text-white resize-none" placeholder="Tell us about your project..."></textarea>
            </div>
            <button type="submit" class="w-full px-6 py-3 rounded-lg bg-cyan-500 text-black font-semibold hover:bg-cyan-400 transition">
              Send Message
            </button>
          </form>
        </div>
        <div class="space-y-8">
          <div class="card rounded-2xl p-8">
            <h2 class="text-2xl font-semibold mb-6">Contact Information</h2>
            <div class="space-y-6">
              <div class="flex items-start gap-4">
                <div class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center flex-shrink-0">
                  <i data-feather="mail" class="text-cyan-400"></i>
                </div>
                <div>
                  <h3 class="font-semibold mb-1">Email</h3>
                  <a href="mailto:info@zic0n.com" class="text-cyan-300 hover:text-cyan-200">info@zic0n.com</a>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <div class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center flex-shrink-0">
                  <i data-feather="map-pin" class="text-cyan-400"></i>
                </div>
                <div>
                  <h3 class="font-semibold mb-1">Locations</h3>
                  <p class="text-slate-300/90">San Diego, CA (Headquarters)</p>
                  <p class="text-slate-300/90">Philadelphia, PA (Regional Hub)</p>
                </div>
              </div>
              <div class="flex items-start gap-4">
                <div class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center flex-shrink-0">
                  <i data-feather="globe" class="text-cyan-400"></i>
                </div>
                <div>
                  <h3 class="font-semibold mb-1">Service Areas</h3>
                  <p class="text-slate-300/90">United States (West Coast, Southwest, Mountain States, Mid-Atlantic, Nationwide)</p>
                </div>
              </div>
            </div>
          </div>
          <div class="card rounded-2xl p-8">
            <h2 class="text-2xl font-semibold mb-4">Connect With Us</h2>
            <p class="text-slate-300/90 mb-6">Follow us for updates on projects, research, and industry insights.</p>
            <div class="flex gap-4">
              <a href="https://www.linkedin.com/company/zic0n" target="_blank" rel="noopener noreferrer" class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center hover:bg-cyan-400/30 transition">
                <i data-feather="linkedin" class="text-cyan-400"></i>
              </a>
              <a href="https://github.com/Arash-MH68/zic0n.github.io" target="_blank" rel="noopener noreferrer" class="h-12 w-12 rounded-lg bg-cyan-400/20 grid place-items-center hover:bg-cyan-400/30 transition">
                <i data-feather="github" class="text-cyan-400"></i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  </main>
'''
    },
    'newsletter.html': {
        'title': 'Newsletter',
        'description': 'Stay updated with the latest news, insights, and publications from Zic0n Engineering.',
        'content': '''  <main id="main-content">
    <section class="relative py-20">
      <div class="absolute inset-0 bg-[radial-gradient(70%_60%_at_50%_-20%,rgba(34,211,238,0.20),transparent_60%)]"></div>
      <div class="max-w-7xl mx-auto px-6 py-12 relative">
        <div class="text-center max-w-3xl mx-auto">
          <h1 class="text-4xl sm:text-5xl font-extrabold mb-4">
            Newsletter & <span class="gradient-text">Research Updates</span>
          </h1>
          <p class="text-slate-300/90 text-lg">
            Stay informed about the latest research, publications, and insights from Zic0n Engineering in geotechnical engineering, pavements, materials science, and infrastructure innovation.
          </p>
        </div>
      </div>
    </section>

    <section class="py-12">
      <div class="max-w-7xl mx-auto px-6">
        <div class="grid md:grid-cols-2 gap-8 mb-12">
          <article class="card rounded-2xl overflow-hidden hover:scale-[1.02] transition-transform">
            <div class="aspect-video bg-gradient-to-br from-cyan-400/10 to-blue-400/10 relative overflow-hidden">
              <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?w=1200&h=675&fit=crop&q=80" alt="Professional engineering podcast recording studio" class="w-full h-full object-cover">
              <div class="absolute inset-0 bg-gradient-to-t from-[#0b1220]/90 to-transparent flex items-end p-6">
                <div class="text-white">
                  <div class="text-xs uppercase tracking-wider text-cyan-300 mb-2">Featured Podcast</div>
                  <h3 class="text-xl font-semibold mb-2">Engineering the Future with Earth's Oldest Materials</h3>
                </div>
              </div>
            </div>
            <div class="p-6">
              <p class="text-slate-300/90 text-sm mb-4">
                Explore how ancient materials and modern engineering intersect. Dr. Arash Hosseini discusses innovative approaches to geotechnical engineering, soil improvement techniques, and sustainable infrastructure solutions using earth's foundational materials.
              </p>
              <a href="https://metergroup.com/podcasts/episode-45-engineering-the-future-with-earths-oldest-materials/" 
                 target="_blank" 
                 rel="noopener noreferrer" 
                 class="inline-flex items-center gap-2 px-4 py-2 bg-cyan-500 text-black font-semibold rounded-lg hover:bg-cyan-400 transition">
                <i data-feather="play-circle" class="w-5 h-5"></i>
                Listen to Podcast
              </a>
            </div>
          </article>

          <article class="card rounded-2xl overflow-hidden">
            <div class="p-6">
              <div class="flex items-center gap-4 mb-4">
                <div class="h-12 w-12 rounded-full bg-cyan-400/20 grid place-items-center">
                  <i data-feather="book-open" class="text-cyan-400"></i>
                </div>
                <div>
                  <h3 class="text-xl font-semibold">Research Publications</h3>
                  <p class="text-sm text-slate-400">Google Scholar Profile</p>
                </div>
              </div>
              <div class="grid grid-cols-3 gap-4 mb-6">
                <div class="text-center">
                  <div class="text-2xl font-bold text-cyan-400">386</div>
                  <div class="text-xs text-slate-400">Citations</div>
                </div>
                <div class="text-center">
                  <div class="text-2xl font-bold text-cyan-400">9</div>
                  <div class="text-xs text-slate-400">h-index</div>
                </div>
                <div class="text-center">
                  <div class="text-2xl font-bold text-cyan-400">9</div>
                  <div class="text-xs text-slate-400">i10-index</div>
                </div>
              </div>
              <p class="text-slate-300/90 text-sm mb-4">
                Explore Dr. Arash Hosseini's published research on pavement engineering, machine learning applications in infrastructure, electrokinetic soil improvement, and unsaturated soil mechanics.
              </p>
              <a href="https://scholar.google.com/citations?user=ckcFqa0AAAAJ&hl=en" 
                 target="_blank" 
                 rel="noopener noreferrer" 
                 class="inline-flex items-center gap-2 px-4 py-2 border border-white/15 hover:bg-white/5 rounded-lg transition">
                <i data-feather="external-link" class="w-5 h-5"></i>
                View Research Profile
              </a>
            </div>
          </article>
        </div>

        <div class="mb-12">
          <h2 class="text-3xl font-bold mb-8">Key Research Areas</h2>
          <div class="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div class="card rounded-xl overflow-hidden hover:scale-105 transition-transform">
              <div class="aspect-[4/3] overflow-hidden">
                <img src="https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=800&h=600&fit=crop&q=80" alt="Road construction and asphalt paving" class="w-full h-full object-cover">
              </div>
              <div class="p-6 text-center">
                <h3 class="font-semibold mb-2">Pavement Engineering</h3>
                <p class="text-xs text-slate-400">Machine learning, performance prediction, and deterioration modeling</p>
              </div>
            </div>
            <div class="card rounded-xl overflow-hidden hover:scale-105 transition-transform">
              <div class="aspect-[4/3] overflow-hidden">
                <img src="https://images.unsplash.com/photo-1583195764036-6dc248ac07d9?w=800&h=600&fit=crop&q=80" alt="Geotechnical drilling and soil investigation" class="w-full h-full object-cover">
              </div>
              <div class="p-6 text-center">
                <h3 class="font-semibold mb-2">Soil Improvement</h3>
                <p class="text-xs text-slate-400">Electrokinetic stabilization, nanomaterials, and collapsible soils</p>
              </div>
            </div>
            <div class="card rounded-xl overflow-hidden hover:scale-105 transition-transform">
              <div class="aspect-[4/3] overflow-hidden">
                <img src="https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=800&h=600&fit=crop&q=80" alt="Ground improvement and soil stabilization techniques" class="w-full h-full object-cover">
              </div>
              <div class="p-6 text-center">
                <h3 class="font-semibold mb-2">Unsaturated Soils</h3>
                <p class="text-xs text-slate-400">Mechanical behavior and engineering properties</p>
              </div>
            </div>
            <div class="card rounded-xl overflow-hidden hover:scale-105 transition-transform">
              <div class="aspect-[4/3] overflow-hidden">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop&q=80" alt="Data visualization and analytics dashboard" class="w-full h-full object-cover">
              </div>
              <div class="p-6 text-center">
                <h3 class="font-semibold mb-2">Data Analytics</h3>
                <p class="text-xs text-slate-400">Machine learning for infrastructure performance</p>
              </div>
            </div>
          </div>
        </div>

        <div class="mb-12">
          <h2 class="text-3xl font-bold mb-8">Featured Publications</h2>
          <div class="space-y-4">
            <div class="card rounded-xl overflow-hidden hover:border-cyan-400/30 transition">
              <div class="aspect-video overflow-hidden">
                <img src="https://images.unsplash.com/photo-1589939705384-5185137a7f0f?w=1200&h=675&fit=crop&q=80" alt="Pavement engineering and road infrastructure" class="w-full h-full object-cover opacity-50">
              </div>
              <div class="p-6">
                <div class="flex items-start justify-between gap-4">
                  <div class="flex-1">
                    <div class="flex items-center gap-2 mb-2">
                      <span class="text-xs px-2 py-1 bg-cyan-400/20 text-cyan-300 rounded">88 Citations</span>
                      <span class="text-xs text-slate-400">2019</span>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Parametric Study of Pavement Deterioration Using Machine Learning Algorithms</h3>
                    <p class="text-sm text-slate-300/90 mb-3">
                      A comprehensive study leveraging machine learning to predict and model pavement deterioration patterns, providing valuable insights for infrastructure maintenance planning.
                    </p>
                    <div class="flex flex-wrap gap-2">
                      <span class="text-xs px-2 py-1 bg-white/5 rounded">Machine Learning</span>
                      <span class="text-xs px-2 py-1 bg-white/5 rounded">Pavement Performance</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="card rounded-xl overflow-hidden hover:border-cyan-400/30 transition">
              <div class="aspect-video overflow-hidden">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=1200&h=675&fit=crop&q=80" alt="Data analytics and machine learning for infrastructure" class="w-full h-full object-cover opacity-50">
              </div>
              <div class="p-6">
                <div class="flex items-start justify-between gap-4">
                  <div class="flex-1">
                    <div class="flex items-center gap-2 mb-2">
                      <span class="text-xs px-2 py-1 bg-cyan-400/20 text-cyan-300 rounded">81 Citations</span>
                      <span class="text-xs text-slate-400">2021</span>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Machine Learning Approach to Predict International Roughness Index Using Long-Term Pavement Performance Data</h3>
                    <p class="text-sm text-slate-300/90 mb-3">
                      Advanced machine learning techniques applied to long-term pavement performance data to accurately predict International Roughness Index, enabling proactive maintenance strategies.
                    </p>
                    <div class="flex flex-wrap gap-2">
                      <span class="text-xs px-2 py-1 bg-white/5 rounded">Data Analytics</span>
                      <span class="text-xs px-2 py-1 bg-white/5 rounded">Predictive Modeling</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="card rounded-xl overflow-hidden hover:border-cyan-400/30 transition">
              <div class="aspect-video overflow-hidden">
                <img src="https://images.unsplash.com/photo-1583195764036-6dc248ac07d9?w=1200&h=675&fit=crop&q=80" alt="Geotechnical engineering drilling and foundation work" class="w-full h-full object-cover opacity-50">
              </div>
              <div class="p-6">
                <div class="flex items-start justify-between gap-4">
                  <div class="flex-1">
                    <div class="flex items-center gap-2 mb-2">
                      <span class="text-xs px-2 py-1 bg-cyan-400/20 text-cyan-300 rounded">41 Citations</span>
                      <span class="text-xs text-slate-400">2019</span>
                    </div>
                    <h3 class="font-semibold text-lg mb-2">Feasibility of Using Electrokinetics and Nanomaterials to Stabilize and Improve Collapsible Soils</h3>
                    <p class="text-sm text-slate-300/90 mb-3">
                      Innovative research exploring the combination of electrokinetic techniques and nanomaterials for stabilizing collapsible soils, opening new possibilities for problematic soil treatment.
                    </p>
                    <div class="flex flex-wrap gap-2">
                      <span class="text-xs px-2 py-1 bg-white/5 rounded">Soil Improvement</span>
                      <span class="text-xs px-2 py-1 bg-white/5 rounded">Electrokinetics</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>

        <div class="card rounded-2xl p-8 text-center bg-gradient-to-br from-cyan-400/10 to-blue-400/10">
          <i data-feather="mail" class="w-16 h-16 text-cyan-400 mx-auto mb-4"></i>
          <h2 class="text-2xl font-bold mb-3">Stay Updated</h2>
          <p class="text-slate-300/90 mb-6 max-w-2xl mx-auto">
            Subscribe to receive updates on new research publications, industry insights, and engineering innovations from Zic0n Engineering.
          </p>
          <form action="mailto:info@zic0n.com" method="GET" enctype="text/plain" class="max-w-md mx-auto flex gap-3">
            <input type="email" name="subject" placeholder="your.email@example.com" required 
                   class="flex-1 rounded-lg bg-white/5 border border-white/10 px-4 py-3 focus:outline-none focus:ring-2 focus:ring-cyan-500" />
            <input type="hidden" name="body" value="Newsletter subscription request" />
            <button type="submit" class="px-6 py-3 bg-cyan-500 text-black font-semibold rounded-lg hover:bg-cyan-400 transition">
              Subscribe
            </button>
          </form>
        </div>
      </div>
    </section>
  </main>
'''
    }
}

# Generate pages
for page_file, page_data in PAGES.items():
    content = HEAD.format(
        title=page_data['title'],
        description=page_data['description'],
        page=page_file
    ) + HEADER + page_data['content'] + FOOTER
    
    with open(page_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Created {page_file}')

