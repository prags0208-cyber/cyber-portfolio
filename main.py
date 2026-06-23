from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(title="Pragathi Srinivasan | Cybersecurity Portfolio")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pragathi Srinivasan | Cybersecurity & Core Infrastructure Portfolio</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-slate-950 text-slate-100 font-sans selection:bg-teal-500 selection:text-slate-950">

        <!-- SECURITY TOP TELEMETRY BAR -->
        <div class="bg-slate-900 border-b border-slate-800 px-6 py-2 text-xs text-slate-400 flex flex-wrap justify-between items-center gap-2 cursor-default">
            <div class="flex items-center gap-4">
                <span class="flex items-center gap-1.5 font-mono"><span class="h-2 w-2 rounded-full bg-emerald-500 animate-pulse"></span> PORTFOLIO STATUS: SECURE</span>
                <span class="hidden sm:inline text-slate-600">|</span>
                <span class="hidden sm:inline font-mono">FRAMEWORK: FASTAPI ASYNC ENGINE</span>
            </div>
            <div class="font-mono text-slate-500 text-right">
                LOCATION: ALBANY, NY // ID: PRAGATHI_SRINIVASAN
            </div>
        </div>

        <!-- MAIN COMMAND CENTER HERO -->
        <header class="border-b border-slate-800 bg-slate-900/40 py-16 px-6 relative overflow-hidden">
            <div class="absolute inset-0 opacity-5 bg-[linear-gradient(to_right,#0284c7_1px,transparent_1px),linear-gradient(to_bottom,#0284c7_1px,transparent_1px)] [background-size:24px_24px]"></div>
            <div class="max-w-5xl mx-auto relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
                <div>
                    <div class="inline-flex items-center gap-2 bg-teal-500/10 border border-teal-500/20 text-teal-400 text-xs font-mono px-3 py-1 rounded mb-4 tracking-wider uppercase">
                        <i class="fa-solid fa-shield-halved"></i> Digital Trust & Threat Mitigation
                    </div>
                    <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight text-white font-mono">Pragathi Srinivasan</h1>
                    <p class="text-md md:text-lg text-slate-400 mt-3 max-w-2xl leading-relaxed">
                        Research Project Assistant @ RF SUNY <span class="text-slate-600">|</span> MS Cybersecurity @ UAlbany <span class="text-slate-600">|</span> Former Enterprise Engineer @ Bank of America
                    </p>
                </div>
                <div class="flex flex-col sm:flex-row md:flex-col gap-3 w-full md:w-auto text-xs font-mono">
                    <a href="mailto:pragathisrinivasan0208@gmail.com" class="flex items-center gap-2 justify-center bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 px-4 py-2.5 rounded transition shadow-sm"><i class="fa-solid fa-envelope text-teal-400"></i> email</a>
                    <a href="https://linkedin.com/in/pragathi-020801sp" target="_blank" class="flex items-center gap-2 justify-center bg-slate-900 border border-slate-800 hover:border-teal-500/40 text-slate-300 px-4 py-2.5 rounded transition shadow-sm group"><i class="fa-brands fa-linkedin text-teal-400 group-hover:scale-105 transition"></i> linkedin_profile</a>
                </div>
            </div>
        </header>

        <main class="max-w-5xl mx-auto px-6 py-16 space-y-16">

            <!-- CORE TARGET ROLES AREA -->
            <section class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="bg-slate-900/60 p-6 rounded-lg border border-slate-800 hover:border-slate-700 transition">
                    <div class="text-teal-400 font-mono text-xs mb-2 tracking-wider flex items-center justify-between">
                        <span>TRACK_01</span> <i class="fa-solid fa-circle-nodes"></i>
                    </div>
                    <h3 class="font-bold text-lg text-white font-mono mb-2">Security Engineering</h3>
                    <p class="text-xs text-slate-400 leading-relaxed">Remediating software vulnerabilities, implementing system configuration baselines, managing SIEM pipelines, and analyzing raw packet traffic captures.</p>
                </div>
                <div class="bg-slate-900/60 p-6 rounded-lg border border-slate-800 hover:border-slate-700 transition">
                    <div class="text-sky-400 font-mono text-xs mb-2 tracking-wider flex items-center justify-between">
                        <span>TRACK_02</span> <i class="fa-solid fa-fingerprint"></i>
                    </div>
                    <h3 class="font-bold text-lg text-white font-mono mb-2">IAM Architecture</h3>
                    <p class="text-xs text-slate-400 leading-relaxed">Securing authentication vectors, token verification, managing federated protocols, and deploying secure OAuth 2.0 runtime models.</p>
                </div>
                <div class="bg-slate-900/60 p-6 rounded-lg border border-slate-800 hover:border-slate-700 transition">
                    <div class="text-purple-400 font-mono text-xs mb-2 tracking-wider flex items-center justify-between">
                        <span>TRACK_03</span> <i class="fa-solid fa-terminal"></i>
                    </div>
                    <h3 class="font-bold text-lg text-white font-mono mb-2">Secure Backend Dev</h3>
                    <p class="text-xs text-slate-400 leading-relaxed">Building resilient, low-latency API logic, high-throughput message consumer pipelines, and optimizing high-availability structural database queries.</p>
                </div>
            </section>

            <!-- INFRASTRUCTURE & TOOLS MATRIX -->
            <section class="bg-slate-900/40 border border-slate-800/80 p-8 rounded-xl">
                <h2 class="text-xl font-bold text-white font-mono mb-6 flex items-center gap-2"><i class="fa-solid fa-microchip text-teal-400"></i> SECURITY ENGINE & TOOL INVENTORY</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                        <h4 class="text-xs font-mono font-bold uppercase tracking-widest text-slate-500 mb-3">// Security Controls & Monitoring</h4>
                        <div class="flex flex-wrap gap-2">
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">OAuth 2.0 Architecture</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Splunk SIEM Core</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Wireshark Traffic Analysis</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Incident Mitigation</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Vulnerability Analysis</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">GRC Risk Frameworks</span>
                        </div>
                    </div>
                    <div>
                        <h4 class="text-xs font-mono font-bold uppercase tracking-widest text-slate-500 mb-3">// Backend & Systems Automation</h4>
                        <div class="flex flex-wrap gap-2">
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Java (Spring Boot)</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Python (Pandas, NumPy, Scikit)</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">SQL (PostgreSQL, CockroachDB)</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Kafka Data Streaming</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">AWS Cloud, Docker, K8s</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Secure CI/CD Pipelines</span>
                        </div>
                    </div>
                </div>
                <div class="mt-6 pt-6 border-t border-slate-800/60 flex flex-wrap gap-6 text-xs text-slate-400 font-mono">
                    <span><i class="fa-solid fa-certificate text-teal-400 mr-1.5"></i> Google Cybersecurity Certified</span>
                    <span><i class="fa-solid fa-certificate text-teal-400 mr-1.5"></i> IBM Cybersecurity Compliance Certified</span>
                </div>
            </section>

            <!-- PROFESSIONAL AUDIT HISTORY -->
            <section class="space-y-6">
                <h2 class="text-xl font-bold text-white font-mono flex items-center gap-2"><i class="fa-solid fa-list-check text-teal-400"></i> EXPERIENCE LOGS</h2>
                
                <!-- JOB 1 -->
                <div class="bg-slate-900/40 p-6 md:p-8 rounded-xl border border-slate-800 relative group hover:border-slate-700 transition">
                    <div class="flex flex-wrap justify-between items-start gap-2 mb-4">
                        <div>
                            <h3 class="text-lg font-bold text-white font-mono">Research Project Assistant</h3>
                            <p class="text-sm font-medium text-teal-400 mt-0.5">The Research Foundation for State University of New York (RF SUNY)</p>
                        </div>
                        <span class="bg-slate-900 text-slate-400 font-mono text-xs px-2.5 py-1 rounded border border-slate-800">2025 - PRESENT</span>
                    </div>
                    <ul class="space-y-3 text-slate-400 text-xs font-mono list-none pl-0">
                        <li class="flex items-start gap-2"><span class="text-teal-400 font-bold">&gt;</span> <span>Automated manual enterprise intake routines with JotForm and Microsoft Power Automate, eliminating operational bottlenecks and lowering processing latency from 2 weeks down to under 24 hours.</span></li>
                        <li class="flex items-start gap-2"><span class="text-teal-400 font-bold">&gt;</span> <span>Digitized legacy system architectures and structured programmatic audit-ready controls to support long-term data governance criteria.</span></li>
                        <li class="flex items-start gap-2"><span class="text-teal-400 font-bold">&gt;</span> <span>Authored strict Business Requirement Documents (BRDs) and system integration playbooks to maintain standardized process rollouts.</span></li>
                    </ul>
                </div>

                <!-- JOB 2 -->
                <div class="bg-slate-900/40 p-6 md:p-8 rounded-xl border border-slate-800 relative group hover:border-slate-700 transition">
                    <div class="flex flex-wrap justify-between items-start gap-2 mb-4">
                        <div>
                            <h3 class="text-lg font-bold text-white font-mono">Software Engineer - 1B</h3>
                            <p class="text-sm font-medium text-slate-400 mt-0.5">Bank of America - GBS</p>
                        </div>
                        <span class="bg-slate-900 text-slate-400 font-mono text-xs px-2.5 py-1 rounded border border-slate-800">2023 - 2025</span>
                    </div>
                    <ul class="space-y-3 text-slate-400 text-xs font-mono list-none pl-0">
                        <li class="flex items-start gap-2"><span class="text-slate-500 font-bold">&gt;</span> <span>Deployed core OAuth 2.0 authentication and identity authorization configurations, reducing structural authorization issues across platforms by 30%.</span></li>
                        <li class="flex items-start gap-2"><span class="text-slate-500 font-bold">&gt;</span> <span>Built telemetry trackers and automated system health hooks with Java Spring Boot, increasing observability metrics and cutting error localization times by 40%.</span></li>
                        <li class="flex items-start gap-2"><span class="text-slate-500 font-bold">&gt;</span> <span>Engineered Kafka data loops and optimized heavy query processing indices inside PostgreSQL/CockroachDB architectures to streamline high-throughput platforms.</span></li>
                        <li class="flex items-start gap-2"><span class="text-slate-500 font-bold">&gt;</span> <span>Constructed tailored Splunk dashboards for real-time log monitoring, forensic discovery, and production troubleshooting mitigation.</span></li>
                    </ul>
                </div>
            </section>

            <!-- FORENSIC INVESTIGATIONS SECTION -->
            <section class="space-y-6">
                <h2 class="text-xl font-bold text-white font-mono flex items-center gap-2"><i class="fa-solid fa-folder-open text-teal-400"></i> FORENSIC RESEARCH & DEPLOYED REPOS</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-slate-900/30 border border-slate-800 p-6 rounded-lg">
                        <span class="font-mono text-[10px] uppercase text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded tracking-widest">DATA_FORENSICS // ML</span>
                        <h4 class="font-bold text-white font-mono text-base mt-3">Enron Email Behavioral Insider Threat Pipeline</h4>
                        <p class="text-slate-400 text-xs mt-2 leading-relaxed">Engineered a data forensic ingestion pipeline designed to extract anomalies from corpus text records. Mapped behavioral signals via sentiment variance indicators and clustering models, leveraging a Logistic Regression engine to isolate anomalous access trajectories.</p>
                    </div>
                    <div class="bg-slate-900/30 border border-slate-800 p-6 rounded-lg">
                        <span class="font-mono text-[10px] uppercase text-purple-400 bg-purple-500/10 px-2 py-0.5 rounded tracking-widest">INCIDENT_RESPONSE // SIEM</span>
                        <h4 class="font-bold text-white font-mono text-base mt-3">Apex Financial Server Breach Investigation</h4>
                        <p class="text-slate-400 text-xs mt-2 leading-relaxed">Conducted deep parsing of adversarial network intrusion signatures by sorting capture telemetry inside Wireshark. Aggregated host system events into actionable Splunk tracking interfaces to build audit records map paths.</p>
                    </div>
                </div>
            </section>

          <section class="space-y-6">
                <h2 class="text-xl font-bold text-white font-mono flex items-center gap-2"><i class="fa-solid fa-award text-teal-400"></i> VERIFIED PROFESSIONAL ENDORSEMENTS</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    
                    <div class="bg-slate-900/50 border border-slate-800/60 p-6 rounded-xl flex flex-col justify-between">
                        <p class="text-xs text-slate-400 italic font-mono leading-relaxed">
                            "I worked with Pragati on an GTS project while collaborating between GTS and the Bank of America EDPAS team. She has strong technical expertise in Java, SQL, Python, and banking domain, a clear understanding of requirements, and excellent communication. Despite limited experience, she demonstrated strong analytical skills, attention to detail, and a mature problem-solving approach. I highly recommend her for technical data and development focused roles."
                        </p>
                        <div class="mt-4 pt-4 border-t border-slate-800/50 text-right">
                            <h5 class="text-[11px] font-mono text-teal-400 font-bold">Tarun Bonam</h5>
                            <p class="text-[9px] font-mono text-slate-500">Engineer II Software Development @ S&P Global</p>
                        </div>
                    </div>

                    <div class="bg-slate-900/50 border border-slate-800/60 p-6 rounded-xl flex flex-col justify-between">
                        <p class="text-xs text-slate-400 italic font-mono leading-relaxed">
                            "Pragathi is extremely professional and strives to give her best at anything she does. She is a great team player and is an asset to any team that she is a part of. I wish her the best!"
                        </p>
                        <div class="mt-4 pt-4 border-t border-slate-800/50 text-right">
                            <h5 class="text-[11px] font-mono text-teal-400 font-bold">Nathamayil Natesh</h5>
                            <p class="text-[9px] font-mono text-slate-500">Software Engineer @ Bank of America | App Security</p>
                        </div>
                    </div>

                    <div class="bg-slate-900/50 border border-slate-800/60 p-6 rounded-xl flex flex-col justify-between">
                        <p class="text-xs text-slate-400 italic font-mono leading-relaxed">
                            "Pragathi is a great colleague and team player who is professional, reliable, and easy to work with. She is dependable, committed to her work, and always supportive of the team. Her ability to collaborate effectively and handle responsibilities with dedication makes her a valuable person to work with."
                        </p>
                        <div class="mt-4 pt-4 border-t border-slate-800/50 text-right">
                            <h5 class="text-[11px] font-mono text-teal-400 font-bold">Neha Rathod</h5>
                            <p class="text-[9px] font-mono text-slate-500">Software Engineer @ Bank of America</p>
                        </div>
                    </div>

                    <div class="bg-slate-900/50 border border-slate-800/60 p-6 rounded-xl flex flex-col justify-between">
                        <p class="text-xs text-slate-400 italic font-mono leading-relaxed">
                            "Pragathi is a good team player and positive person. She is extremely professional and committed to her work. Her passion towards her assignments was commendable."
                        </p>
                        <div class="mt-4 pt-4 border-t border-slate-800/50 text-right">
                            <h5 class="text-[11px] font-mono text-teal-400 font-bold">Vinitha R</h5>
                            <p class="text-[9px] font-mono text-slate-500">Software Engineer @ Bank of America (Mentor)</p>
                        </div>
                    </div>

                    <div class="bg-slate-900/50 border border-slate-800/60 p-6 rounded-xl flex flex-col justify-between md:col-span-2 lg:col-span-1">
                        <p class="text-xs text-slate-400 italic font-mono leading-relaxed">
                            "I have known Pragathi since the past 4 years and have done more than 5 projects together. She's extremely talented and punctual. Pragathi can work as both team leader and a team member. She has a lot of knowledge on programming languages like Python and Java... She is very creative and is enthusiastic."
                        </p>
                        <div class="mt-4 pt-4 border-t border-slate-800/50 text-right">
                            <h5 class="text-[11px] font-mono text-teal-400 font-bold">Lakshmi Sravya D</h5>
                            <p class="text-[9px] font-mono text-slate-500">Site Reliability Engineer | Associate</p>
                        </div>
                    </div>

                </div>
            </section>

        </main>

        <footer class="bg-slate-900/60 text-slate-600 text-[10px] font-mono py-8 text-center border-t border-slate-900 mt-12">
            <p>© 2026 PRAGATHI_SRINIVASAN // ARCHITECTURE RUNNING ON SECURED FASTAPI ENGINE</p>
        </footer>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)