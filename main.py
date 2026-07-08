from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(title="Pragathi Srinivasan | Portfolio")

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
        <title>Pragathi Srinivasan | Security Engineering & Core Systems</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-slate-950 text-slate-100 font-sans selection:bg-teal-500 selection:text-slate-950">

        <!-- SECURITY TELEMETRY BAR -->
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

        <!-- HERO COMMAND CENTER -->
        <header class="border-b border-slate-800 bg-slate-900/40 py-16 px-6 relative overflow-hidden">
            <div class="absolute inset-0 opacity-5 bg-[linear-gradient(to_right,#0284c7_1px,transparent_1px),linear-gradient(to_bottom,#0284c7_1px,transparent_1px)] [background-size:24px_24px]"></div>
            <div class="max-w-5xl mx-auto relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-6">
                <div>
                    <div class="inline-flex items-center gap-2 bg-teal-500/10 border border-teal-500/20 text-teal-400 text-xs font-mono px-3 py-1 rounded mb-4 tracking-wider uppercase">
                        <i class="fa-solid fa-shield-halved"></i> Security Engineering & System Architecture
                    </div>
                    <h1 class="text-4xl md:text-5xl font-extrabold tracking-tight text-white font-mono">Pragathi Srinivasan</h1>
                    <p class="text-md md:text-lg text-slate-400 mt-3 max-w-2xl leading-relaxed">
                        MS Cybersecurity @ UAlbany <span class="text-slate-600">|</span> Research Project Assistant @ RF SUNY <span class="text-slate-600">|</span> Former Enterprise Engineer @ Bank of America
                    </p>
                </div>
                <div class="flex flex-col sm:flex-row md:flex-col gap-3 w-full md:w-auto text-xs font-mono">
                    <a href="mailto:pragathisrinivasan0208@gmail.com" class="flex items-center gap-2 justify-center bg-slate-900 border border-slate-800 hover:border-slate-700 text-slate-300 px-4 py-2.5 rounded transition shadow-sm"><i class="fa-solid fa-envelope text-teal-400"></i> email</a>
                    <a href="https://linkedin.com/in/pragathi-020801sp" target="_blank" class="flex items-center gap-2 justify-center bg-slate-900 border border-slate-800 hover:border-teal-500/40 text-slate-300 px-4 py-2.5 rounded transition shadow-sm group"><i class="fa-brands fa-linkedin text-teal-400 group-hover:scale-105 transition"></i> linkedin_profile</a>
                </div>
            </div>
        </header>

        <main class="max-w-5xl mx-auto px-6 py-16 space-y-16">

            <!-- PROFESSIONAL NARRATIVE & FIT PARAGRAPH -->
            <section class="bg-slate-900/60 p-8 rounded-xl border border-slate-800 hover:border-slate-700 transition space-y-4">
                <h2 class="text-xl font-bold text-white font-mono flex items-center gap-2">
                    <i class="fa-solid fa-user-shield text-teal-400"></i> ABOUT MY WORK & TARGET ROLES
                </h2>
                <p class="text-sm text-slate-300 leading-relaxed">
                    I am a Cybersecurity Graduate Student at the University at Albany with a strong foundation in enterprise systems engineering from my tenure as a Software Engineer at Bank of America. My work bridges the gap between software development, access management, and security operations—building infrastructure that is resilient by design rather than retrofitted after deployment.
                </p>
                <p class="text-sm text-slate-300 leading-relaxed">
                    Having deployed federated OAuth 2.0 access protocols, constructed high-throughput data pipelines, and engineered automated workflows to streamline enterprise intake routines, I excel at solving complex technical problems with high agency. I am actively seeking <strong class="text-teal-400 font-normal">Security Engineering</strong> and <strong class="text-teal-400 font-normal">SecOps / Cloud Security</strong> positions where I can leverage code automation, SIEM observability, and threat detection pipelines to protect mission-critical infrastructure.
                </p>
            </section>

            <!-- CORE AREAS OF EXPERTISE -->
            <section class="space-y-6">
                <h2 class="text-xl font-bold text-white font-mono flex items-center gap-2">
                    <i class="fa-solid fa-diagram-project text-teal-400"></i> DOMAIN EXPERTISE & TECHNICAL CAPABILITIES
                </h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-slate-900/40 p-6 rounded-lg border border-slate-800">
                        <h3 class="font-bold text-base text-white font-mono mb-2 flex items-center gap-2">
                            <i class="fa-solid fa-key text-teal-400"></i> Identity, Access & Platform Security
                        </h3>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            Specializing in securing identity boundaries, token validation, and federated authorization architectures (OAuth 2.0). Experienced in auditing cloud resource permissions, standardizing access control policies across distributed applications, and integrating security checks into CI/CD pipelines to enforce secure-by-default runtime environments.
                        </p>
                    </div>
                    <div class="bg-slate-900/40 p-6 rounded-lg border border-slate-800">
                        <h3 class="font-bold text-base text-white font-mono mb-2 flex items-center gap-2">
                            <i class="fa-solid fa-chart-line text-sky-400"></i> SecOps, SIEM & Automated Telemetry
                        </h3>
                        <p class="text-xs text-slate-400 leading-relaxed">
                            Adept at configuring custom log ingestion streams, tuning SIEM detection alerts inside Splunk, and automating vulnerability triage routines. Skilled in analyzing raw network packet captures (Wireshark) and leveraging machine learning pipelines (Logistic Regression, clustering) to detect behavioral anomalies and insider threats in enterprise communications.
                        </p>
                    </div>
                </div>
            </section>

            <!-- DETAILED TECHNICAL TOOL INVENTORY -->
            <section class="bg-slate-900/40 border border-slate-800/80 p-8 rounded-xl">
                <h2 class="text-xl font-bold text-white font-mono mb-6 flex items-center gap-2"><i class="fa-solid fa-microchip text-teal-400"></i> SECURITY ENGINE & TOOL MATRIX</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div>
                        <h4 class="text-xs font-mono font-bold uppercase tracking-widest text-slate-500 mb-3">// Security Operations & Identity</h4>
                        <div class="flex flex-wrap gap-2">
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">OAuth 2.0 / Token Verification</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Splunk SIEM Core & Dashboarding</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Wireshark Traffic Analysis</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Vulnerability Triage & Remediation</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">GRC & Audit Controls</span>
                        </div>
                    </div>
                    <div>
                        <h4 class="text-xs font-mono font-bold uppercase tracking-widest text-slate-500 mb-3">// Development, Data & Automation</h4>
                        <div class="flex flex-wrap gap-2">
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Python (Pandas, NumPy, Scikit-learn)</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">SQL (PostgreSQL, CockroachDB)</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">Microsoft Power Automate & JotForm</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">CI/CD Security Workflows</span>
                            <span class="bg-slate-900 text-slate-300 font-mono text-xs px-3 py-1.5 rounded border border-slate-800">FastAPI Async Systems</span>
                        </div>
                    </div>
                </div>
                <div class="mt-6 pt-6 border-t border-slate-800/60 flex flex-wrap gap-6 text-xs text-slate-400 font-mono">
                    <span><i class="fa-solid fa-certificate text-teal-400 mr-1.5"></i> Google Cybersecurity Certified</span>
                    <span><i class="fa-solid fa-certificate text-teal-400 mr-1.5"></i> IBM Cybersecurity Compliance Certified</span>
                </div>
            </section>

            <!-- DETAILED WORKSPACE EXPERIENCE LOGS -->
            <section class="space-y-6">
                <h2 class="text-xl font-bold text-white font-mono flex items-center gap-2"><i class="fa-solid fa-list-check text-teal-400"></i> PROFESSIONAL WORKSPACE HISTORY</h2>
                
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
                        <li class="flex items-start gap-2"><span class="text-teal-400 font-bold">&gt;</span> <span>Automated manual enterprise intake routines by designing custom JotForm and Microsoft Power Automate flows, eliminating operational bottlenecks and cutting process execution latency from 2 weeks down to under 24 hours.</span></li>
                        <li class="flex items-start gap-2"><span class="text-teal-400 font-bold">&gt;</span> <span>Digitized legacy system architectures and structured programmatic, audit-ready data governance workflows to maintain strict compliance standards.</span></li>
                        <li class="flex items-start gap-2"><span class="text-teal-400 font-bold">&gt;</span> <span>Authored comprehensive Business Requirement Documents (BRDs), architectural diagrams, and system integration playbooks to ensure standardized cross-team deployment.</span></li>
                    </ul>
                </div>

                <!-- JOB 2 -->
                <div class="bg-slate-900/40 p-6 md:p-8 rounded-xl border border-slate-800 relative group hover:border-slate-700 transition">
                    <div class="flex flex-wrap justify-between items-start gap-2 mb-4">
                        <div>
                            <h3 class="text-lg font-bold text-white font-mono">Software Engineer - 1B</h3>
                            <p class="text-sm font-medium text-slate-400 mt-0.5">Bank of America - Global Technology & Operations (GBS)</p>
                        </div>
                        <span class="bg-slate-900 text-slate-400 font-mono text-xs px-2.5 py-1 rounded border border-slate-800">2023 - 2025</span>
                    </div>
                    <ul class="space-y-3 text-slate-400 text-xs font-mono list-none pl-0">
                        <li class="flex items-start gap-2"><span class="text-slate-500 font-bold">&gt;</span> <span>Implemented core OAuth 2.0 authentication and token verification frameworks across enterprise financial microservices, resolving identity authorization vulnerabilities and reducing platform authorization defects by 30%.</span></li>
                        <li class="flex items-start gap-2"><span class="text-slate-500 font-bold">&gt;</span> <span>Engineered automated system health monitoring hooks and telemetry trackers, providing real-time operational observability and cutting incident localization times by 40%.</span></li>
                        <li class="flex items-start gap-2"><span class="text-slate-500 font-bold">&gt;</span> <span>Optimized database query indexing and schema partitioning across PostgreSQL and CockroachDB architectures to sustain high-availability, low-latency transaction processing.</span></li>
                        <li class="flex items-start gap-2"><span class="text-slate-500 font-bold">&gt;</span> <span>Designed custom Splunk monitoring dashboards and log parsing views for real-time threat discovery, system auditability, and immediate incident mitigation.</span></li>
                    </ul>
                </div>
            </section>

            <!-- FORENSIC & SECURITY RESEARCH -->
            <section class="space-y-6">
                <h2 class="text-xl font-bold text-white font-mono flex items-center gap-2"><i class="fa-solid fa-folder-open text-teal-400"></i> SECURITY RESEARCH & INVESTIGATIONS</h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-slate-900/30 border border-slate-800 p-6 rounded-lg">
                        <span class="font-mono text-[10px] uppercase text-teal-400 bg-teal-500/10 px-2 py-0.5 rounded tracking-widest">BEHAVIORAL_ANALYTICS // ML</span>
                        <h4 class="font-bold text-white font-mono text-base mt-3">Enron Email Behavioral Insider Threat Pipeline</h4>
                        <p class="text-slate-400 text-xs mt-2 leading-relaxed">Built an end-to-end forensic data processing pipeline using Python to detect insider anomalies across raw text corpora. Mapped behavioral shifts through sentiment analysis, TF-IDF vectorization, and clustering, leveraging a Logistic Regression engine to highlight risky communication patterns.</p>
                    </div>
                    <div class="bg-slate-900/30 border border-slate-800 p-6 rounded-lg">
                        <span class="font-mono text-[10px] uppercase text-purple-400 bg-purple-500/10 px-2 py-0.5 rounded tracking-widest">NETWORK_FORENSICS // SIEM</span>
                        <h4 class="font-bold text-white font-mono text-base mt-3">Apex Financial Web Server Breach Investigation</h4>
                        <p class="text-slate-400 text-xs mt-2 leading-relaxed">Executed deep packet analysis on adversarial intrusion captures inside Wireshark to isolate exploit paths and malicious payloads. Correlated host event telemetry into actionable Splunk dashboards to establish an audit-ready incident reconstruction timeline.</p>
                    </div>
                </div>
            </section>

            <!-- VERIFIED ENDORSEMENTS -->
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
            <p>© 2026 PRAGATHI_SRINIVASAN </p>
        </footer>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)