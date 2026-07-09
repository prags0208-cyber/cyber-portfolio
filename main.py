from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(title="Pragathi Srinivasan | Security Engineering Portfolio")

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
    <html lang="en" class="scroll-smooth">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pragathi Srinivasan | Security & Systems Engineering HUD</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-slate-950 text-slate-100 font-sans selection:bg-teal-500 selection:text-slate-950">

        <header class="sticky top-0 z-50 bg-slate-950/80 backdrop-blur-md border-b border-slate-800/80 px-6 py-3">
            <div class="max-w-6xl mx-auto flex flex-wrap justify-between items-center gap-4">
                <div class="flex items-center gap-3">
                    <span class="flex h-2.5 w-2.5 relative">
                      <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-teal-400 opacity-75"></span>
                      <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-teal-500"></span>
                    </span>
                    <span class="font-mono text-xs font-bold text-slate-300 tracking-wider">PRAGATHI_SRINIVASAN // SEC_ENG</span>
                </div>

                <nav class="flex items-center gap-6 font-mono text-xs text-slate-400">
                    <a href="#about" class="hover:text-teal-400 transition">// 01. ABOUT</a>
                    <a href="#skills" class="hover:text-teal-400 transition">// 02. SKILLS</a>
                    <a href="#experience" class="hover:text-teal-400 transition">// 03. EXPERIENCE</a>
                    <a href="#projects" class="hover:text-teal-400 transition">// 04. PROJECTS</a>
                    <a href="#endorsements" class="hover:text-teal-400 transition">// 05. ENDORSEMENTS</a>
                </nav>
            </div>
        </header>

        <section class="border-b border-slate-800 bg-gradient-to-b from-slate-900/50 to-slate-950 py-20 px-6 relative overflow-hidden">
            <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#0ea5e9_1px,transparent_1px)] [background-size:16px_16px]"></div>
            <div class="max-w-6xl mx-auto relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-8">
                <div>
                    <div class="inline-flex items-center gap-2 bg-teal-500/10 border border-teal-500/30 text-teal-400 text-xs font-mono px-3 py-1 rounded-full mb-4 uppercase tracking-widest">
                        <i class="fa-solid fa-terminal text-xs"></i> System Status: Operational
                    </div>
                    <h1 class="text-4xl sm:text-5xl font-black tracking-tight text-white font-mono">Pragathi Srinivasan</h1>
                    <p class="text-base md:text-lg text-slate-400 mt-3 max-w-2xl leading-relaxed">
                        MS Cybersecurity @ UAlbany <span class="text-slate-700">|</span> Research Project Assistant @ RF SUNY <span class="text-slate-700">|</span> Former Enterprise Engineer @ Bank of America
                    </p>
                </div>

                <div class="bg-slate-900/90 border border-slate-800 p-5 rounded-xl space-y-3 font-mono text-xs w-full md:w-auto shadow-xl">
                    <div class="text-slate-500 uppercase tracking-widest text-[10px] mb-1">// DIRECT CONNECT</div>
                    <a href="mailto:pragathisrinivasan0208@gmail.com" class="flex items-center gap-3 text-slate-300 hover:text-teal-400 transition">
                        <i class="fa-solid fa-envelope text-teal-400 w-4"></i> pragathisrinivasan0208@gmail.com
                    </a>
                    <a href="https://linkedin.com/in/pragathi-020801sp" target="_blank" class="flex items-center gap-3 text-slate-300 hover:text-teal-400 transition">
                        <i class="fa-brands fa-linkedin text-teal-400 w-4"></i> linkedin.com/in/pragathi-020801sp
                    </a>
                    <div class="text-slate-400 flex items-center gap-2 pt-1 border-t border-slate-800/80">
                        <i class="fa-solid fa-location-dot text-slate-500"></i> Albany, NY // Open to Relocation
                    </div>
                </div>
            </div>
        </section>

        <main class="max-w-6xl mx-auto px-6 py-16 space-y-24">

            <section id="about" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>01</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>PROFILE & OBJECTIVE</span>
                </div>
                <h2 class="text-2xl font-bold text-white font-mono mb-6">About Me & Target Roles</h2>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="md:col-span-2 bg-slate-900/40 border border-slate-800 p-8 rounded-2xl relative">
                        <p class="text-slate-300 text-sm leading-relaxed mb-4">
                            I am a Cybersecurity Graduate Student at the University at Albany with a strong foundation in enterprise systems engineering from my tenure as a Software Engineer at Bank of America (GOMT / GTS). My work bridges software development, real-time access management, large-scale data infrastructure, and AI integration—building resilient systems designed to operate securely under high enterprise demand.
                        </p>
                        <p class="text-slate-300 text-sm leading-relaxed">
                            Having automated critical enterprise intake platforms, managed dynamic OAuth certificate lifecycles, engineered distributed Kafka/Redis streaming pipelines, and supported AI research initiatives leveraging RAG, Neo4j vector databases, and LLaMA models, I bring a high-agency, problem-solving mindset. I am actively seeking <strong class="text-teal-400 font-normal">Security Engineering</strong> and <strong class="text-teal-400 font-normal">SecOps / Cloud Security</strong> roles to protect mission-critical architectures.
                        </p>
                    </div>

                    <div class="bg-slate-900/70 border border-slate-800 p-6 rounded-2xl flex flex-col justify-between space-y-4">
                        <div class="font-mono text-xs text-slate-400 uppercase tracking-wider">// TARGET FOCUS</div>
                        <div class="space-y-3 font-mono text-xs">
                            <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 flex items-center gap-3 text-teal-300">
                                <i class="fa-solid fa-shield-cat text-teal-400 text-base"></i> Security Engineering
                            </div>
                            <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 flex items-center gap-3 text-sky-300">
                                <i class="fa-solid fa-key text-sky-400 text-base"></i> IAM & OAuth 2.0 Arch
                            </div>
                            <div class="bg-slate-950 p-3 rounded-lg border border-slate-800 flex items-center gap-3 text-purple-300">
                                <i class="fa-solid fa-microchip text-purple-400 text-base"></i> SecOps & SIEM Analytics
                            </div>
                        </div>
                        <div class="text-[10px] text-slate-500 font-mono">
                            Available for Full-time Roles & Internships
                        </div>
                    </div>
                </div>
            </section>

            <section id="skills" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>02</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>CAPABILITIES & ENGINE</span>
                </div>
                <h2 class="text-2xl font-bold text-white font-mono mb-8">Technical Inventory</h2>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="bg-slate-900/40 border border-slate-800/80 p-6 rounded-xl hover:border-slate-700 transition">
                        <div class="text-teal-400 text-xl mb-3"><i class="fa-solid fa-lock"></i></div>
                        <h3 class="font-mono font-bold text-sm text-white mb-3">Security & Identity</h3>
                        <ul class="space-y-2 font-mono text-xs text-slate-400">
                            <li>• OAuth 2.0 & Cert Lifecycle</li>
                            <li>• Splunk SIEM Core & Analytics</li>
                            <li>• Wireshark Packet Analysis</li>
                            <li>• Vulnerability Remediation</li>
                            <li>• GRC & Audit Frameworks</li>
                        </ul>
                    </div>

                    <div class="bg-slate-900/40 border border-slate-800/80 p-6 rounded-xl hover:border-slate-700 transition">
                        <div class="text-sky-400 text-xl mb-3"><i class="fa-solid fa-database"></i></div>
                        <h3 class="font-mono font-bold text-sm text-white mb-3">Data & Cloud DBs</h3>
                        <ul class="space-y-2 font-mono text-xs text-slate-400">
                            <li>• CockroachDB (CRDB) & SQL</li>
                            <li>• Redis & Apache Kafka</li>
                            <li>• Cassandra & Hadoop DBs</li>
                            <li>• Neo4j Vector DB</li>
                            <li>• Azure Cloud Databases</li>
                        </ul>
                    </div>

                    <div class="bg-slate-900/40 border border-slate-800/80 p-6 rounded-xl hover:border-slate-700 transition">
                        <div class="text-purple-400 text-xl mb-3"><i class="fa-solid fa-code"></i></div>
                        <h3 class="font-mono font-bold text-sm text-white mb-3">Languages & Dev</h3>
                        <ul class="space-y-2 font-mono text-xs text-slate-400">
                            <li>• Java (Spring Boot Framework)</li>
                            <li>• Python (Pandas, Scikit)</li>
                            <li>• PostgreSQL & SQL Scripting</li>
                            <li>• RESTful API Architecture</li>
                            <li>• Jira & Confluence Workflow</li>
                        </ul>
                    </div>

                    <div class="bg-slate-900/40 border border-slate-800/80 p-6 rounded-xl hover:border-slate-700 transition">
                        <div class="text-amber-400 text-xl mb-3"><i class="fa-solid fa-brain"></i></div>
                        <h3 class="font-mono font-bold text-sm text-white mb-3">AI & Automation</h3>
                        <ul class="space-y-2 font-mono text-xs text-slate-400">
                            <li>• RAG & LLM Architectures</li>
                            <li>• LLaMA Model Integration</li>
                            <li>• Power Automate & JotForm</li>
                            <li>• Power BI Executive Dashboards</li>
                            <li>• Machine Learning Classifiers</li>
                        </ul>
                    </div>
                </div>
            </section>

            <section id="experience" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>03</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>CHRONOLOGY</span>
                </div>
                <h2 class="text-2xl font-bold text-white font-mono mb-8">Workplace History</h2>

                <div class="space-y-8">
                    <div class="bg-slate-900/40 border border-slate-800 p-8 rounded-2xl relative hover:border-slate-700 transition">
                        <div class="flex flex-wrap justify-between items-start gap-4 mb-4">
                            <div>
                                <span class="bg-teal-500/10 text-teal-400 font-mono text-[10px] px-2.5 py-1 rounded border border-teal-500/20 uppercase">RESEARCH & ACADEMIC INITIATIVE</span>
                                <h3 class="text-xl font-bold text-white font-mono mt-2">Research Project Assistant</h3>
                                <p class="text-xs font-mono text-slate-400">The Research Foundation for State University of New York (RF SUNY)</p>
                            </div>
                            <span class="font-mono text-xs text-slate-500 bg-slate-950 px-3 py-1.5 rounded-full border border-slate-800">2025 — PRESENT</span>
                        </div>

                        <ul class="space-y-3 text-xs text-slate-300 font-mono mb-6 leading-relaxed">
                            <li class="flex items-start gap-2.5"><span class="text-teal-400 font-bold">&gt;</span> <span><strong>Enterprise Workflow Automation:</strong> Streamlined complex institutional intake processes by configuring custom JotForm forms, Microsoft Power Automate flows, and SharePoint hubs, slashing manual execution latency from 2 weeks down to under 24 hours.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-teal-400 font-bold">&gt;</span> <span><strong>AI Platform Support (GrantsMate App):</strong> Provided technical system support for the GrantsMate App engineered for research collaborators, gaining direct hands-on experience with Retrieval-Augmented Generation (RAG) pipelines, LLaMA LLM architectures, Neo4j vector databases, and Azure database environments.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-teal-400 font-bold">&gt;</span> <span><strong>Analytics & Governance:</strong> Built executive Power BI dashboards to track data governance metrics, digitize legacy structures, and establish audit-ready records.</span></li>
                        </ul>

                        <div class="bg-amber-500/5 border border-amber-500/20 p-3.5 rounded-xl flex items-center gap-3 text-xs font-mono text-amber-300">
                            <i class="fa-solid fa-award text-amber-400 text-base"></i>
                            <span><strong>RECOGNITION:</strong> Awarded Graduate Tuition Fee Scholarship for outstanding project initiatives and automation impact.</span>
                        </div>
                    </div>

                    <div class="bg-slate-900/40 border border-slate-800 p-8 rounded-2xl relative hover:border-slate-700 transition">
                        <div class="flex flex-wrap justify-between items-start gap-4 mb-4">
                            <div>
                                <span class="bg-sky-500/10 text-sky-400 font-mono text-[10px] px-2.5 py-1 rounded border border-sky-500/20 uppercase">ENTERPRISE FINANCIAL SYSTEMS</span>
                                <h3 class="text-xl font-bold text-white font-mono mt-2">Software Engineer - 1B</h3>
                                <p class="text-xs font-mono text-slate-400">Bank of America — Global Organization & Modernization Tech (GOMT) / GTS Team</p>
                            </div>
                            <span class="font-mono text-xs text-slate-500 bg-slate-950 px-3 py-1.5 rounded-full border border-slate-800">2023 — 2025</span>
                        </div>

                        <ul class="space-y-3 text-xs text-slate-300 font-mono mb-6 leading-relaxed">
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>Next-Gen Migration & Spring Boot Tooling:</strong> Contributed to the enterprise Next-Gen Platform Migration using Spring Boot, developing a specialized comparison tool that mapped inter-team dependencies into a consolidated summary with 98% prediction accuracy.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>Identity & OAuth Cert Automation:</strong> Handled on-the-fly OAuth 2.0 authentication and resolved critical identity issues by managing automated certificate swaps immediately following expiration.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>Post-Market Stock Trading & Distributed Streaming:</strong> Engineered a consolidated application frontend backed by Redis and Apache Kafka to process day and night shift incoming market stock transactions (buy/sell orders) after market close, alongside hands-on management of Cassandra and Hadoop databases.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>CRDB Error Reduction & Executive Reporting:</strong> Engineered a dynamic migration utility that significantly reduced CockroachDB (CRDB) operational errors and automated daily tracking reports sent to higher-level management.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>Observability & Agile Operations:</strong> Built custom Splunk dashboards for real-time error finding and root-cause localization while maintaining project tracking via Jira and Confluence documentation.</span></li>
                        </ul>

                        <div class="bg-amber-500/5 border border-amber-500/20 p-3.5 rounded-xl flex flex-wrap items-center gap-6 text-xs font-mono text-amber-300">
                            <span class="flex items-center gap-2"><i class="fa-solid fa-trophy text-amber-400"></i> Gold Award</span>
                            <span class="flex items-center gap-2"><i class="fa-solid fa-star text-amber-400"></i> High-Five Award</span>
                            <span class="flex items-center gap-2"><i class="fa-solid fa-medal text-amber-400"></i> Bronze Award</span>
                        </div>
                    </div>
                </div>
            </section>

            <section id="projects" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>04</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>REPOS & RESEARCH</span>
                </div>
                <h2 class="text-2xl font-bold text-white font-mono mb-8">Forensic & Security Projects</h2>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="bg-slate-900/40 border border-slate-800 p-6 rounded-2xl flex flex-col justify-between hover:border-slate-700 transition">
                        <div>
                            <span class="font-mono text-[10px] uppercase text-teal-400 bg-teal-500/10 px-2.5 py-1 rounded border border-teal-500/20 tracking-wider">BEHAVIORAL ANALYTICS // ML</span>
                            <h3 class="font-bold text-white font-mono text-base mt-4">Enron Email Behavioral Insider Threat Pipeline</h3>
                            <p class="text-slate-400 text-xs mt-3 leading-relaxed font-mono">Built an end-to-end forensic data processing pipeline using Python to detect insider anomalies across raw text corpora. Mapped behavioral shifts through sentiment analysis, TF-IDF vectorization, and clustering, leveraging a Logistic Regression engine to highlight risky communication patterns.</p>
                        </div>
                        <div class="mt-6 pt-4 border-t border-slate-800/80 font-mono text-[11px] text-slate-500">
                            Tools: Python, Scikit-learn, TF-IDF, NLP, Clustering
                        </div>
                    </div>

                    <div class="bg-slate-900/40 border border-slate-800 p-6 rounded-2xl flex flex-col justify-between hover:border-slate-700 transition">
                        <div>
                            <span class="font-mono text-[10px] uppercase text-purple-400 bg-purple-500/10 px-2.5 py-1 rounded border border-purple-500/20 tracking-wider">NETWORK FORENSICS // SIEM</span>
                            <h3 class="font-bold text-white font-mono text-base mt-4">Apex Financial Web Server Breach Investigation</h3>
                            <p class="text-slate-400 text-xs mt-3 leading-relaxed font-mono">Executed deep packet analysis on adversarial intrusion captures inside Wireshark to isolate exploit paths and malicious payloads. Correlated host event telemetry into actionable Splunk dashboards to establish an audit-ready incident reconstruction timeline.</p>
                        </div>
                        <div class="mt-6 pt-4 border-t border-slate-800/80 font-mono text-[11px] text-slate-500">
                            Tools: Wireshark, Splunk SIEM, PCAP Parsing, Forensics
                        </div>
                    </div>
                </div>
            </section>

            <section id="endorsements" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>05</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>VERIFIED REVIEWS</span>
                </div>
                <h2 class="text-2xl font-bold text-white font-mono mb-8">Professional References</h2>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="bg-slate-900/30 border border-slate-800 p-6 rounded-xl flex flex-col justify-between">
                        <p class="text-xs text-slate-400 italic font-mono leading-relaxed">
                            "I worked with Pragati on an GTS project while collaborating between GTS and the Bank of America EDPAS team. She has strong technical expertise in Java, SQL, Python, and banking domain, a clear understanding of requirements, and excellent communication. Despite limited experience, she demonstrated strong analytical skills, attention to detail, and a mature problem-solving approach."
                        </p>
                        <div class="mt-4 pt-4 border-t border-slate-800/80 text-right">
                            <h4 class="text-xs font-mono text-teal-400 font-bold">Tarun Bonam</h4>
                            <p class="text-[10px] font-mono text-slate-500">Engineer II @ S&P Global</p>
                        </div>
                    </div>

                    <div class="bg-slate-900/30 border border-slate-800 p-6 rounded-xl flex flex-col justify-between">
                        <p class="text-xs text-slate-400 italic font-mono leading-relaxed">
                            "Pragathi is extremely professional and strives to give her best at anything she does. She is a great team player and is an asset to any team that she is a part of. I wish her the best!"
                        </p>
                        <div class="mt-4 pt-4 border-t border-slate-800/80 text-right">
                            <h4 class="text-xs font-mono text-teal-400 font-bold">Nathamayil Natesh</h4>
                            <p class="text-[10px] font-mono text-slate-500">Software Engineer @ Bank of America</p>
                        </div>
                    </div>

                    <div class="bg-slate-900/30 border border-slate-800 p-6 rounded-xl flex flex-col justify-between">
                        <p class="text-xs text-slate-400 italic font-mono leading-relaxed">
                            "Pragathi is a great colleague and team player who is professional, reliable, and easy to work with. She is dependable, committed to her work, and always supportive of the team."
                        </p>
                        <div class="mt-4 pt-4 border-t border-slate-800/80 text-right">
                            <h4 class="text-xs font-mono text-teal-400 font-bold">Neha Rathod</h4>
                            <p class="text-[10px] font-mono text-slate-500">Software Engineer @ Bank of America</p>
                        </div>
                    </div>
                </div>
            </section>

        </main>

        <footer class="bg-slate-950 text-slate-600 text-[11px] font-mono py-8 text-center border-t border-slate-900 mt-20">
            <p>© 2026 PRAGATHI_SRINIVASAN // TACTICAL COMMAND PORTFOLIO</p>
        </footer>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)