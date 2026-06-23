from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Pragathi Srinivasan | Portfolio API",
    description="Interactive backend portfolio highlighting security frameworks, IAM engineering, and enterprise backend automation.",
    version="1.0.0"
)

# --- SECURITY MIDDLEWARE ---
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    return response

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# --- PORTFOLIO DATA TARGETING SECURITY, IAM, & BACKEND ---
PROFILE = {
    "name": "Pragathi Srinivasan",
    "headline": "Research Project Assistant @ RF SUNY | MS Cybersecurity @ UAlbany | Ex-Software Engineer @ Bank of America",
    "target_tracks": ["Security Engineer", "Identity & Access Management (IAM) Engineer", "Backend Developer"],
    "location": "Albany, NY",
    "contact": {"email": "pragathisrinivasan0208@gmail.com", "linkedin": "linkedin.com/in/pragathi-020801sp"}
}

SKILLS = [
    {"category": "Security & IAM Engineering", "skills": ["OAuth 2.0", "Splunk SIEM", "Wireshark Traffic Analysis", "Incident Response", "Vulnerability Analysis", "GRC Concepts"]},
    {"category": "Backend & Cloud Infrastructure", "skills": ["Java (Spring Boot)", "Python (Pandas, NumPy)", "SQL (PostgreSQL, CockroachDB)", "Kafka Event Services", "AWS", "Docker", "Kubernetes", "CI/CD (Jenkins, GitHub Actions)"]}
]

EXPERIENCE = [
    {
        "role": "Research Project Assistant",
        "company": "The Research Foundation for State University of New York",
        "duration": "March 2025 - Present",
        "highlights": [
            "Automated a manual HR intake workflow using JotForm and Microsoft Power Automate, reducing processing time from two weeks to 24 hours.",
            "Digitalized legacy paper-based processes and designed backend automation workflows to improve data handling accuracy, process consistency, and audit readiness.",
            "Authored technical documentation and business requirement documents to support standardized rollout and long-term maintainability."
        ]
    },
    {
        "role": "SOFTWARE ENGINEER-1B",
        "company": "Bank of America - GBS",
        "duration": "July 2023 - January 2025",
        "highlights": [
            "Implemented OAuth 2.0 authentication and authorization flows, strengthening application security and reducing access-related issues by 30%.",
            "Developed real-time monitoring and health-check services using Java Spring Boot, improving platform observability and reducing error detection time by 40%.",
            "Designed Kafka-based event-driven services to support real-time processing and improve throughput while reducing latency by 25%.",
            "Created and optimized Splunk dashboards for system monitoring, log analysis, and operational reporting, reducing troubleshooting time by 40%.",
            "Tuned SQL queries across PostgreSQL and CockroachDB, reducing execution time by 35% and improving backend responsiveness."
        ]
    }
]

PROJECTS = [
    {
        "title": "Enron Email Behavioral Analysis & Insider Threat Detection",
        "type": "Digital Forensics & Machine Learning",
        "description": "Engineered a forensic pipeline to identify communication anomalies; utilized feature engineering for sentiment volatility and time-based clustering. Developed a Logistic Regression model to classify suspicious activity through behavioral signals."
    },
    {
        "title": "Apex Financial Web Server Breach - Forensic Investigation",
        "type": "Incident Response & Traffic Analysis",
        "description": "Conducted vulnerability scanning, log analysis, and incident review to identify system weaknesses. Built reports with Splunk dashboards and Wireshark traffic analysis, supporting compliance and audit requirements."
    }
]

RECOMMENDATIONS = [
    {
        "from": "Senior Software Engineer / Tech Lead (Bank of America)",
        "relationship": "Supervised Pragathi directly",
        "text": "Pragathi brings an incredible blend of backend development performance and application security awareness. Her implementation of OAuth 2.0 flows significantly minimized unauthorized structural vectors, and she optimizes databases masterfully."
    },
    {
        "from": "Operations Lead (Research Foundation for SUNY)",
        "relationship": "Managed Pragathi's automation tasks",
        "text": "Pragathi took absolute ownership of our legacy intake channels. By coding custom automated handlers, she brought our operations timeline down from weeks to under 24 hours. Her systems are safe, efficient, and exceptionally documented."
    }
]

@app.get("/")
def home():
    return HTMLResponse(content="""
    <html>
        <head><title>Pragathi Srinivasan | Portfolio API</title></head>
        <body style="font-family: sans-serif; text-align: center; padding-top: 100px; background-color: #f4f6f9;">
            <h1 style="color: #1E3A8A;">🛡️ Pragathi Srinivasan's Cybersecurity & Backend Portfolio API</h1>
            <p style="color: #4B5563;">Asynchronous API architecture built with FastAPI</p>
            <br>
            <a href="/docs" style="background-color: #2563EB; color: white; padding: 12px 24px; text-decoration: none; border-radius: 6px; font-weight: bold; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);">Explore & Interact with My Profile via Swagger UI</a>
        </body>
    </html>
    """)

@app.get("/api/profile")
def get_profile(): return PROFILE

@app.get("/api/skills")
def get_skills(): return SKILLS

@app.get("/api/experience")
def get_experience(): return EXPERIENCE

@app.get("/api/projects")
def get_projects(): return PROJECTS

@app.get("/api/recommendations")
def get_recommendations(): return RECOMMENDATIONS