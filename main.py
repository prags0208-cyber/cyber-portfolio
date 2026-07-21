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
    <html lang="en" class="scroll-smooth">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pragathi Srinivasan </title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    </head>
    <body class="bg-slate-950 text-slate-100 font-sans selection:bg-teal-500 selection:text-slate-950">

        <!-- HEADER / NAVIGATION -->
        <header class="sticky top-0 z-50 bg-slate-950/80 backdrop-blur-md border-b border-slate-800/80 px-6 py-3">
            <div class="max-w-6xl mx-auto flex flex-wrap justify-between items-center gap-4">
                <div class="flex items-center gap-3">
                    <span class="flex h-2.5 w-2.5 relative">
                      <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-teal-400 opacity-75"></span>
                      <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-teal-500"></span>
                    </span>
                    <span class="font-mono text-xs font-bold text-slate-300 tracking-wider">PRAGATHI_SRINIVASAN/span>
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

        <!-- HERO / COMMAND BAR -->
        <section class="border-b border-slate-800 bg-gradient-to-b from-slate-900/50 to-slate-950 py-20 px-6 relative overflow-hidden">
            <div class="absolute inset-0 opacity-10 bg-[radial-gradient(#0ea5e9_1px,transparent_1px)] [background-size:16px_16px]"></div>
            <div class="max-w-6xl mx-auto relative z-10 flex flex-col md:flex-row justify-between items-start md:items-center gap-8">
                <div>
                    <div class="inline-flex items-center gap-2 bg-teal-500/10 border border-teal-500/30 text-teal-400 text-xs font-mono px-3 py-1 rounded-full mb-4 uppercase tracking-widest">
                        <i class="fa-solid fa-terminal text-xs"></i> System Status: Operational
                    </div>
                    <h1 class="text-4xl sm:text-5xl font-black tracking-tight text-white font-mono">Pragathi Srinivasan</h1>
                    <p class="text-base md:text-lg text-slate-400 mt-3 max-w-2xl leading-relaxed">
                        MS Cybersecurity @ UAlbany (GPA 3.8/4.0) <span class="text-slate-700">|</span> Research Project Assistant @ RF SUNY <span class="text-slate-700">|</span> Former Software Engineer @ Bank of America
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

            <!-- 01. PROFILE & OBJECTIVE -->
            <section id="about" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>01</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>PROFILE & OBJECTIVE</span>
                </div>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="md:col-span-2 bg-slate-900/40 border border-slate-800 p-8 rounded-2xl relative">
                        <p class="text-slate-300 text-sm leading-relaxed mb-4">
                            I am a Cybersecurity Graduate Student at the University at Albany (GPA 3.8/4.0) with a proven enterprise foundation as a former Software Engineer at Bank of America. My expertise bridges full-stack backend development, security engineering (IAM, OAuth 2.0, Zero-Trust boundaries), technical GRC automation (NIST CSF, ISO 27001, HIPAA), cloud security, and data analytics—building secure, automated, and audit-ready systems.
                        </p>
                        <p class="text-slate-300 text-sm leading-relaxed">
                            From architecting high-throughput Java Spring Boot APIs and auditing distributed transaction stores to designing automated compliance evidence pipelines and ML-driven fraud detection models, I solve complex technical challenges across the full system lifecycle. I am actively seeking positions in <strong class="text-teal-400 font-normal">Security Engineering</strong>, <strong class="text-teal-400 font-normal">Technical GRC</strong>, <strong class="text-teal-400 font-normal">Software Engineering</strong>, <strong class="text-teal-400 font-normal">IAM & Cloud Security</strong>, and <strong class="text-teal-400 font-normal">Risk & Data Analytics</strong>.
                        </p>
                    </div>

                    <div class="bg-slate-900/70 border border-slate-800 p-6 rounded-2xl flex flex-col justify-between space-y-4">
                        <div class="font-mono text-xs text-slate-400 uppercase tracking-wider">// CORE PILLARS</div>
                        <div class="space-y-2 font-mono text-xs">
                            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 flex items-center gap-2.5 text-teal-300">
                                <i class="fa-solid fa-shield-halved text-teal-400 text-sm"></i> Security Engineering & IAM
                            </div>
                            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 flex items-center gap-2.5 text-sky-300">
                                <i class="fa-solid fa-clipboard-check text-sky-400 text-sm"></i> Technical GRC & Compliance
                            </div>
                            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 flex items-center gap-2.5 text-emerald-300">
                                <i class="fa-solid fa-code text-emerald-400 text-sm"></i> Software Engineering & APIs
                            </div>
                            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 flex items-center gap-2.5 text-purple-300">
                                <i class="fa-solid fa-chart-line text-purple-400 text-sm"></i> Risk, Fraud & Data Analytics
                            </div>
                            <div class="bg-slate-950 p-2 rounded-lg border border-slate-800 flex items-center gap-2.5 text-amber-300">
                                <i class="fa-solid fa-cloud text-amber-400 text-sm"></i> Cloud Sec & AI Infrastructures
                            </div>
                        </div>
                        <div class="text-[10px] text-slate-500 font-mono">
                            Available for Full-time Roles & Internships (Eligible for CPT / OPT)
                        </div>
                    </div>
                </div>
            </section>

            <!-- 02. TECHNICAL INVENTORY -->
            <section id="skills" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>02</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>ENGINEERING & TECHNICAL CAPABILITIES</span>
                </div>
                <h2 class="text-2xl font-bold text-white font-mono mb-8">Technical Inventory</h2>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                    <!-- Column 1 -->
                    <div class="bg-slate-900/40 border border-slate-800/80 p-6 rounded-xl hover:border-slate-700 transition">
                        <div class="text-teal-400 text-xl mb-3"><i class="fa-solid fa-shield-halved"></i></div>
                        <h3 class="font-mono font-bold text-sm text-white mb-3">Security & IAM Engineering</h3>
                        <ul class="space-y-2 font-mono text-xs text-slate-400">
                            <li>• OAuth 2.0 & OIDC Auth Systems</li>
                            <li>• Access Controls & Isolation</li>
                            <li>• Cryptographic Cert-Swaps</li>
                            <li>• Zero-Trust Access Rules</li>
                            <li>• Identity Lifecycle Management</li>
                            <li>• SIEM Alerting & Monitoring</li>
                        </ul>
                    </div>

                    <!-- Column 2 -->
                    <div class="bg-slate-900/40 border border-slate-800/80 p-6 rounded-xl hover:border-slate-700 transition">
                        <div class="text-sky-400 text-xl mb-3"><i class="fa-solid fa-clipboard-check"></i></div>
                        <h3 class="font-mono font-bold text-sm text-white mb-3">Technical GRC & Risk</h3>
                        <ul class="space-y-2 font-mono text-xs text-slate-400">
                            <li>• NIST CSF & RMF Frameworks</li>
                            <li>• ISO/IEC 27001 Implementation</li>
                            <li>• HIPAA/HITECH Data Protection</li>
                            <li>• CIS Benchmark Mapping</li>
                            <li>• Evidence Automation Pipelines</li>
                            <li>• Data-Flow Diagram Mapping</li>
                        </ul>
                    </div>

                    <!-- Column 3 -->
                    <div class="bg-slate-900/40 border border-slate-800/80 p-6 rounded-xl hover:border-slate-700 transition">
                        <div class="text-emerald-400 text-xl mb-3"><i class="fa-solid fa-code"></i></div>
                        <h3 class="font-mono font-bold text-sm text-white mb-3">Software & Backend</h3>
                        <ul class="space-y-2 font-mono text-xs text-slate-400">
                            <li>• Java (Spring Boot REST APIs)</li>
                            <li>• Python (Automation, Data Scripts)</li>
                            <li>• Microservices & Design Patterns</li>
                            <li>• PostgreSQL, CockroachDB, SQL</li>
                            <li>• Cassandra & Hadoop Auditing</li>
                            <li>• Git, CI/CD, Agile / SDLC</li>
                        </ul>
                    </div>

                    <!-- Column 4 -->
                    <div class="bg-slate-900/40 border border-slate-800/80 p-6 rounded-xl hover:border-slate-700 transition">
                        <div class="text-purple-400 text-xl mb-3"><i class="fa-solid fa-brain"></i></div>
                        <h3 class="font-mono font-bold text-sm text-white mb-3">Data Analytics, Cloud & AI</h3>
                        <ul class="space-y-2 font-mono text-xs text-slate-400">
                            <li>• Scikit-learn, Pandas, TF-IDF</li>
                            <li>• Anomaly & Fraud Detection</li>
                            <li>• Power BI Executive Dashboards</li>
                            <li>• Azure Cloud Infrastructure</li>
                            <li>• RAG Pipelines & Neo4j Vector Stores</li>
                            <li>• Power Automate Workflows</li>
                        </ul>
                    </div>
                </div>
            </section>

            <!-- 03. EXPERIENCE -->
            <section id="experience" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>03</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>ENGINEERING & GOVERNANCE CHRONOLOGY</span>
                </div>
                <h2 class="text-2xl font-bold text-white font-mono mb-8">Workplace History</h2>

                <div class="space-y-8">
                    <!-- RF SUNY -->
                    <div class="bg-slate-900/40 border border-slate-800 p-8 rounded-2xl relative hover:border-slate-700 transition">
                        <div class="flex flex-wrap justify-between items-start gap-4 mb-4">
                            <div>
                                <span class="bg-teal-500/10 text-teal-400 font-mono text-[10px] px-2.5 py-1 rounded border border-teal-500/20 uppercase">AUTOMATION, CLOUD SEC & GRC INITIATIVES</span>
                                <h3 class="text-xl font-bold text-white font-mono mt-2">Research Project Assistant</h3>
                                <p class="text-xs font-mono text-slate-400">The Research Foundation for State University of New York (RF SUNY)</p>
                            </div>
                            <span class="font-mono text-xs text-slate-500 bg-slate-950 px-3 py-1.5 rounded-full border border-slate-800">2025 — PRESENT</span>
                        </div>

                        <ul class="space-y-3 text-xs text-slate-300 font-mono mb-6 leading-relaxed">
                            <li class="flex items-start gap-2.5"><span class="text-teal-400 font-bold">&gt;</span> <span><strong>Compliance Evidence Automation:</strong> Architected an automated institutional intake and compliance evaluation platform utilizing custom JotForm conditional logic and Microsoft Power Automate pipelines, shrinking manual workflow execution latency from 2 weeks down to under 24 hours while keeping strict process audit trails.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-teal-400 font-bold">&gt;</span> <span><strong>Data-Flow Mapping & Risk Mitigation:</strong> Documented internal controls and mapped comprehensive system dependency data-flows to verify how sensitive information crosses operational thresholds, highlighting policy and control gaps for proactive technical remediation.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-teal-400 font-bold">&gt;</span> <span><strong>Executive Risk Dashboards:</strong> Constructed interactive Power BI analytics platforms to trace data governance metrics, digitize outdated ingestion structures, and establish structured, audit-ready operational records.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-teal-400 font-bold">&gt;</span> <span><strong>Cloud Infrastructure & AI Platform Support:</strong> Maintained system infrastructure support for the specialized GrantsMate tool, managing environments leveraging Retrieval-Augmented Generation (RAG) loops, LLaMA model integration, Neo4j vector maps, and secure Azure cloud stores.</span></li>
                        </ul>

                        <div class="bg-amber-500/5 border border-amber-500/20 p-3.5 rounded-xl flex items-center gap-3 text-xs font-mono text-amber-300">
                            <i class="fa-solid fa-award text-amber-400 text-base"></i>
                            <span><strong>RECOGNITION:</strong> Awarded Graduate Tuition Fee Scholarship for outstanding technical execution, workflow optimization, and automation impact.</span>
                        </div>
                    </div>

                    <!-- Bank of America -->
                    <div class="bg-slate-900/40 border border-slate-800 p-8 rounded-2xl relative hover:border-slate-700 transition">
                        <div class="flex flex-wrap justify-between items-start gap-4 mb-4">
                            <div>
                                <span class="bg-sky-500/10 text-sky-400 font-mono text-[10px] px-2.5 py-1 rounded border border-sky-500/20 uppercase">ENTERPRISE FINANCIAL SYSTEMS & IAM ENGINEERING</span>
                                <h3 class="text-xl font-bold text-white font-mono mt-2">Former Software Engineer - 1B</h3>
                                <p class="text-xs font-mono text-slate-400">Bank of America — Global Organization & Modernization Tech (GOMT) / GTS Team</p>
                            </div>
                            <span class="font-mono text-xs text-slate-500 bg-slate-950 px-3 py-1.5 rounded-full border border-slate-800">2023 — 2025</span>
                        </div>

                        <ul class="space-y-3 text-xs text-slate-300 font-mono mb-6 leading-relaxed">
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>Access Control Governance (IAM):</strong> Configured real-time OAuth 2.0 authentication configurations and managed access isolation metrics, engineering secure, dynamic cryptographic certificate-swap mechanisms to reduce identity expiration vulnerability windows.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>Backend Service Development:</strong> Engineered high-availability Java Spring Boot RESTful microservices processing large volumes of enterprise transaction data with strict fault tolerance and data validation requirements.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>Data Integrity Auditing & Migration:</strong> Co-developed a specialized dependency-verification tool for a large-scale Next-Gen Platform Migration using Spring Boot, evaluating cross-team architecture patterns to maintain 98% tracking accuracy.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>Distributed Ledger Control Verification:</strong> Programmed validation scripts that systematically reduced database exception rates in CockroachDB (CRDB) and managed telemetry tracking logic across Cassandra and Hadoop historical transaction data stores.</span></li>
                            <li class="flex items-start gap-2.5"><span class="text-sky-400 font-bold">&gt;</span> <span><strong>Continuous Observability Audits:</strong> Formulated tailored Splunk SIEM dashboards to track system operational anomalies, establish alerts for unmapped errors, and preserve deterministic tracking data trails for root-cause analysis.</span></li>
                        </ul>

                        <div class="bg-amber-500/5 border border-amber-500/20 p-3.5 rounded-xl flex flex-wrap items-center gap-6 text-xs font-mono text-amber-300">
                            <span class="flex items-center gap-2"><i class="fa-solid fa-trophy text-amber-400"></i> Gold Award</span>
                            <span class="flex items-center gap-2"><i class="fa-solid fa-star text-amber-400"></i> High-Five Award</span>
                            <span class="flex items-center gap-2"><i class="fa-solid fa-medal text-amber-400"></i> Bronze Award</span>
                        </div>
                    </div>
                </div>
            </section>

            <!-- 04. PROJECTS -->
            <section id="projects" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>04</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>FEATURED TECHNICAL PROJECTS</span>
                </div>
                <h2 class="text-2xl font-bold text-white font-mono mb-8">Projects Highlighting Full Skill Spectrum</h2>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <!-- Project 1 -->
                    <div class="bg-slate-900/40 border border-slate-800 p-6 rounded-2xl flex flex-col justify-between hover:border-slate-700 transition">
                        <div>
                            <span class="font-mono text-[10px] uppercase text-teal-400 bg-teal-500/10 px-2.5 py-1 rounded border border-teal-500/20 tracking-wider">RISK ANALYTICS // SPAM DETECTION // ML</span>
                            <h3 class="font-bold text-white font-mono text-base mt-4">SMS Spam Detection & Automated Classification Pipeline</h3>
                            <p class="text-slate-400 text-xs mt-3 leading-relaxed font-mono">
                                Engineered an end-to-end machine learning pipeline to identify and classify spam behavior across 5,000+ SMS messages using TF-IDF vectorization. Evaluated Logistic Regression, Random Forest, and Naive Bayes models using precision, recall, F1-score, and confusion matrices to assess false-positive tradeoffs for fraud prevention systems.
                            </p>
                        </div>
                        <div class="mt-6 pt-4 border-t border-slate-800/80 font-mono text-[11px] text-slate-500">
                            Highlights: Python, Pandas, Scikit-learn, TF-IDF, Fraud & Anomaly Analytics
                        </div>
                    </div>

                    <!-- Project 2 -->
                    <div class="bg-slate-900/40 border border-slate-800 p-6 rounded-2xl flex flex-col justify-between hover:border-slate-700 transition">
                        <div>
                            <span class="font-mono text-[10px] uppercase text-sky-400 bg-sky-500/10 px-2.5 py-1 rounded border border-sky-500/20 tracking-wider">BEHAVIORAL ANALYTICS // INSIDER THREAT</span>
                            <h3 class="font-bold text-white font-mono text-base mt-4">Enron Email Behavioral Analysis & Insider Threat Pipeline</h3>
                            <p class="text-slate-400 text-xs mt-3 leading-relaxed font-mono">
                                Engineered a Python-based behavioral analytics engine for large unstructured communication datasets. Applied feature engineering, sentiment analysis, TF-IDF vectorization, time-based clustering, and Logistic Regression to translate behavioral signals into measurable risk indicators and isolate policy violations or insider threats.
                            </p>
                        </div>
                        <div class="mt-6 pt-4 border-t border-slate-800/80 font-mono text-[11px] text-slate-500">
                            Highlights: NLP, Behavioral Analytics, Risk Classification, Clustering, Data Pipelines
                        </div>
                    </div>

                    <!-- Project 3 -->
                    <div class="bg-slate-900/40 border border-slate-800 p-6 rounded-2xl flex flex-col justify-between hover:border-slate-700 transition">
                        <div>
                            <span class="font-mono text-[10px] uppercase text-purple-400 bg-purple-500/10 px-2.5 py-1 rounded border border-purple-500/20 tracking-wider">NETWORK FORENSICS // FINANCIAL SECURITY</span>
                            <h3 class="font-bold text-white font-mono text-base mt-4">Apex Financial Web Server Breach Investigation</h3>
                            <p class="text-slate-400 text-xs mt-3 leading-relaxed font-mono">
                                Reconstructed a simulated financial web server breach by analyzing malicious network traffic, host logs, and attack artifacts. Executed PCAP analysis in Wireshark and correlated security events in Splunk SIEM to trace credential-harvesting behavior, establish an evidence-based incident timeline, and formulate security remediation controls.
                            </p>
                        </div>
                        <div class="mt-6 pt-4 border-t border-slate-800/80 font-mono text-[11px] text-slate-500">
                            Highlights: Wireshark, Splunk SIEM, PCAP Traffic Parsing, Forensics, Root-Cause Analysis
                        </div>
                    </div>

                    <!-- Project 4 (New: Generative AI, Cloud & API Security) -->
                    <div class="bg-slate-900/40 border border-slate-800 p-6 rounded-2xl flex flex-col justify-between hover:border-slate-700 transition">
                        <div>
                            <span class="font-mono text-[10px] uppercase text-amber-400 bg-amber-500/10 px-2.5 py-1 rounded border border-amber-500/20 tracking-wider">CLOUD SEC // AI PIPELINES // SOFTWARE ENG</span>
                            <h3 class="font-bold text-white font-mono text-base mt-4">Generative AI Platform Infrastructure & RAG Tooling (GrantsMate)</h3>
                            <p class="text-slate-400 text-xs mt-3 leading-relaxed font-mono">
                                Implemented backend infrastructure and cloud data-security controls supporting AI agents with Retrieval-Augmented Generation (RAG). Integrated Neo4j vector maps, LLaMA model pipelines, and secure Azure data stores while managing API endpoints, access boundary checks, and operational monitoring.
                            </p>
                        </div>
                        <div class="mt-6 pt-4 border-t border-slate-800/80 font-mono text-[11px] text-slate-500">
                            Highlights: Azure Cloud, Java/Python APIs, Neo4j, LLM Security, RAG Architecture
                        </div>
                    </div>
                </div>
            </section>

            <!-- 05. ENDORSEMENTS -->
            <section id="endorsements" class="scroll-mt-20">
                <div class="flex items-center gap-3 font-mono text-xs text-teal-400 mb-2 uppercase tracking-widest">
                    <span>05</span> <span class="h-px bg-teal-500/30 flex-grow"></span> <span>VERIFIED REVIEWS</span>
                </div>
                <h2 class="text-2xl font-bold text-white font-mono mb-8">Professional References</h2>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <div class="bg-slate-900/30 border border-slate-800 p-6 rounded-xl flex flex-col justify-between">
                        <p class="text-xs text-slate-400 italic font-mono leading-relaxed">
                            "I worked with Pragati on a GTS project while collaborating between GTS and the Bank of America EDPAS team. She has strong technical expertise in Java, SQL, Python, and banking domain, a clear understanding of requirements, and excellent communication. Despite limited experience, she demonstrated strong analytical skills, attention to detail, and a mature problem-solving approach."
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
            <p>© 2026 PRAGATHI_SRINIVASAN</p>
        </footer>

    </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)