```python
from flask import Flask, render_template_string, jsonify
from datetime import datetime, timezone
import os

application = Flask(__name__)

GITHUB_REPO_URL = "https://github.com/your-username/your-repo-name"


HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>SLT-MOBITEL | Enterprise IT Dashboard</title>

<script src="https://cdn.tailwindcss.com"></script>

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
rel="stylesheet">


<style>

/* =========================================================
   GLOBAL
========================================================= */

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    font-family: 'Inter', sans-serif;
    background: #070b14;
    color: white;
    overflow-x: hidden;
}


/* =========================================================
   ANIMATED BACKGROUND
========================================================= */

.background {
    position: fixed;
    inset: 0;
    z-index: -10;
    overflow: hidden;

    background:
        radial-gradient(
            circle at 10% 20%,
            rgba(227, 6, 19, 0.18),
            transparent 30%
        ),
        radial-gradient(
            circle at 85% 70%,
            rgba(20, 80, 180, 0.20),
            transparent 35%
        ),
        #070b14;
}


/* Animated grid */

.grid-background {
    position: absolute;
    inset: 0;

    background-image:
        linear-gradient(
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        ),
        linear-gradient(
            90deg,
            rgba(255,255,255,0.025) 1px,
            transparent 1px
        );

    background-size: 45px 45px;

    animation: gridMove 18s linear infinite;
}

@keyframes gridMove {

    0% {
        transform: translateY(0);
    }

    100% {
        transform: translateY(45px);
    }
}


/* =========================================================
   FLOATING GLOW ORBS
========================================================= */

.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(70px);
    opacity: 0.35;
}

.orb-red {
    width: 300px;
    height: 300px;
    background: #e30613;

    top: -100px;
    left: -100px;

    animation: floatRed 8s ease-in-out infinite;
}

.orb-blue {
    width: 350px;
    height: 350px;
    background: #1769aa;

    right: -120px;
    bottom: -120px;

    animation: floatBlue 10s ease-in-out infinite;
}

@keyframes floatRed {

    0%,100% {
        transform: translate(0,0);
    }

    50% {
        transform: translate(100px,80px);
    }
}

@keyframes floatBlue {

    0%,100% {
        transform: translate(0,0);
    }

    50% {
        transform: translate(-100px,-70px);
    }
}


/* =========================================================
   TOP RED LINE
========================================================= */

.top-line {

    height: 4px;

    background:
        linear-gradient(
            90deg,
            #e30613,
            #ff2433,
            #e30613,
            #17365d,
            #e30613
        );

    background-size: 300% 100%;

    animation: gradientMove 5s linear infinite;
}

@keyframes gradientMove {

    0% {
        background-position: 0%;
    }

    100% {
        background-position: 300%;
    }
}


/* =========================================================
   GLASS
========================================================= */

.glass {

    background:
        linear-gradient(
            135deg,
            rgba(255,255,255,0.08),
            rgba(255,255,255,0.025)
        );

    border: 1px solid rgba(255,255,255,0.09);

    backdrop-filter: blur(18px);

    box-shadow:
        0 20px 60px rgba(0,0,0,0.25);

    transition:
        transform .35s ease,
        border .35s ease,
        box-shadow .35s ease;
}

.glass:hover {

    transform: translateY(-5px);

    border-color:
        rgba(227,6,19,0.45);

    box-shadow:
        0 25px 70px rgba(0,0,0,0.45),
        0 0 30px rgba(227,6,19,0.08);
}


/* =========================================================
   ENTRY ANIMATION
========================================================= */

.fade-up {

    opacity: 0;

    transform: translateY(30px);

    animation:
        fadeUp .8s ease forwards;
}

.delay-1 {
    animation-delay: .15s;
}

.delay-2 {
    animation-delay: .30s;
}

.delay-3 {
    animation-delay: .45s;
}

.delay-4 {
    animation-delay: .60s;
}

@keyframes fadeUp {

    to {
        opacity: 1;
        transform: translateY(0);
    }
}


/* =========================================================
   LOGO
========================================================= */

.logo-slt {

    color: #ff2030;

    font-size: 32px;

    font-weight: 900;

    letter-spacing: -2px;

    text-shadow:
        0 0 25px rgba(227,6,19,.35);
}

.logo-mobitel {

    font-size: 27px;

    font-weight: 700;

    color: white;

    letter-spacing: -1px;
}


/* =========================================================
   STATUS
========================================================= */

.status-ring {

    width: 12px;
    height: 12px;

    background: #22c55e;

    border-radius: 50%;

    box-shadow:
        0 0 0 0 rgba(34,197,94,.6);

    animation:
        statusPulse 2s infinite;
}

@keyframes statusPulse {

    70% {
        box-shadow:
            0 0 0 12px rgba(34,197,94,0);
    }

    100% {
        box-shadow:
            0 0 0 0 rgba(34,197,94,0);
    }
}


/* =========================================================
   NUMBER
========================================================= */

.stat-number {

    font-size: 36px;

    font-weight: 800;

    background:
        linear-gradient(
            90deg,
            white,
            #ff4d59
        );

    -webkit-background-clip: text;

    color: transparent;
}


/* =========================================================
   PROGRESS
========================================================= */

.progress {

    height: 7px;

    background:
        rgba(255,255,255,.08);

    border-radius: 20px;

    overflow: hidden;
}

.progress-bar {

    height: 100%;

    border-radius: 20px;

    background:
        linear-gradient(
            90deg,
            #e30613,
            #ff5964
        );

    box-shadow:
        0 0 15px rgba(227,6,19,.5);

    animation:
        progressGlow 2s ease-in-out infinite alternate;
}

@keyframes progressGlow {

    from {
        filter: brightness(1);
    }

    to {
        filter: brightness(1.35);
    }
}


/* =========================================================
   TERMINAL
========================================================= */

.terminal {

    background:
        rgba(0,0,0,.55);

    border:
        1px solid rgba(255,255,255,.08);

    font-family:
        "Courier New",
        monospace;

    box-shadow:
        inset 0 0 30px rgba(0,0,0,.4);
}


/* terminal blinking */

.cursor {

    display: inline-block;

    width: 7px;
    height: 15px;

    background: #e30613;

    animation:
        blink 1s infinite;
}

@keyframes blink {

    50% {
        opacity: 0;
    }
}


/* =========================================================
   BUTTON
========================================================= */

.red-button {

    background:
        linear-gradient(
            135deg,
            #e30613,
            #b8000d
        );

    box-shadow:
        0 10px 30px rgba(227,6,19,.25);

    transition:
        all .3s ease;
}

.red-button:hover {

    transform:
        translateY(-3px)
        scale(1.02);

    box-shadow:
        0 15px 40px rgba(227,6,19,.4);
}


/* =========================================================
   ICON BOX
========================================================= */

.icon-box {

    width: 48px;
    height: 48px;

    border-radius: 14px;

    display: flex;

    align-items: center;

    justify-content: center;

    background:
        rgba(227,6,19,.10);

    border:
        1px solid rgba(227,6,19,.18);

    font-size: 22px;

    transition:
        transform .3s ease;
}

.glass:hover .icon-box {

    transform:
        rotate(8deg)
        scale(1.1);
}


/* =========================================================
   NAV
========================================================= */

.nav-item {

    position: relative;

    color: #9ca3af;

    transition:
        color .25s ease;
}

.nav-item:hover {

    color: white;
}

.nav-item::after {

    content: "";

    position: absolute;

    left: 0;
    right: 0;

    bottom: -10px;

    height: 2px;

    background: #e30613;

    transform:
        scaleX(0);

    transition:
        transform .25s ease;
}

.nav-item:hover::after {

    transform:
        scaleX(1);
}


/* =========================================================
   RESPONSIVE
========================================================= */

@media(max-width:768px) {

    .logo-slt {
        font-size: 25px;
    }

    .logo-mobitel {
        font-size: 21px;
    }

    .stat-number {
        font-size: 30px;
    }

}

</style>

</head>


<body>


<!-- ========================================================
     BACKGROUND
========================================================= -->

<div class="background">

    <div class="grid-background"></div>

    <div class="orb orb-red"></div>

    <div class="orb orb-blue"></div>

</div>


<div class="top-line"></div>


<!-- ========================================================
     HEADER
========================================================= -->

<header
class="glass sticky top-0 z-50 border-t-0 rounded-none">

<div class="max-w-7xl mx-auto px-6 py-4">

<div class="flex justify-between items-center">


<!-- LOGO -->

<div class="flex items-center gap-3">

<div>

<span class="logo-slt">
SLT
</span>

<span class="text-gray-500 mx-2">
|
</span>

<span class="logo-mobitel">
MOBITEL
</span>

</div>

<div class="hidden md:block">

<div class="text-[10px]
uppercase
tracking-[3px]
text-gray-500">

Enterprise Technology

</div>

<div class="text-xs text-gray-400">

Infrastructure Operations

</div>

</div>

</div>


<!-- USER -->

<div class="flex items-center gap-4">

<div class="hidden sm:block text-right">

<div class="text-[10px]
uppercase
tracking-widest
text-gray-500">

SYSTEM USER

</div>

<div class="text-sm font-semibold">

Prasad Wanigasooriya

</div>

</div>


<div
class="w-11 h-11 rounded-full
bg-gradient-to-br
from-red-500
to-red-800
flex items-center
justify-center
font-bold
shadow-lg
shadow-red-900/40">

PW

</div>

</div>

</div>


<!-- NAV -->

<div class="hidden md:flex
gap-8
mt-5
text-sm">

<a href="/" class="nav-item">
Dashboard
</a>

<a href="/health" class="nav-item">
Health
</a>

<a href="#" class="nav-item">
Servers
</a>

<a href="#" class="nav-item">
Databases
</a>

<a href="#" class="nav-item">
Virtualization
</a>

<a href="#" class="nav-item">
Monitoring
</a>

</div>

</div>

</header>


<!-- ========================================================
     MAIN
========================================================= -->

<main class="max-w-7xl mx-auto px-6 py-10">


<!-- HERO -->

<section class="fade-up mb-10">

<div class="flex flex-col lg:flex-row
justify-between
gap-8
items-start
lg:items-center">


<div>

<div class="flex items-center gap-3 mb-3">

<div class="status-ring"></div>

<span class="text-green-400
text-xs
font-semibold
tracking-widest">

ALL SYSTEMS OPERATIONAL

</span>

</div>


<h1
class="text-4xl md:text-6xl
font-extrabold
tracking-tight">

Enterprise

<span
class="text-transparent
bg-clip-text
bg-gradient-to-r
from-red-500
to-red-300">

IT Infrastructure

</span>

</h1>


<p class="text-gray-400
mt-4
max-w-2xl
leading-7">

Real-time infrastructure overview
for servers, databases, virtualization,
backup and monitoring services.

</p>

</div>


<!-- LIVE CLOCK -->

<div class="glass
rounded-2xl
px-6
py-5
min-w-[240px]">

<div class="text-[10px]
uppercase
tracking-widest
text-gray-500">

Server Time

</div>

<div
id="server-time"
class="font-mono
text-xl
font-bold
mt-2">

{{ current_time }}

</div>

<div class="text-xs
text-green-400
mt-2">

● LIVE UTC

</div>

</div>

</div>

</section>


<!-- ========================================================
     STAT CARDS
========================================================= -->

<section
class="grid
grid-cols-1
sm:grid-cols-2
lg:grid-cols-4
gap-5
mb-7">


<!-- SERVER -->

<div class="glass rounded-2xl p-6
fade-up delay-1">

<div class="flex justify-between">

<div>

<div class="text-xs
text-gray-500
uppercase
tracking-wider">

Production Servers

</div>

<div class="stat-number mt-2">

48

</div>

</div>

<div class="icon-box">

🖥️

</div>

</div>

<div class="mt-5
text-xs
text-green-400">

● 47 Online

</div>

</div>


<!-- DATABASE -->

<div class="glass rounded-2xl p-6
fade-up delay-2">

<div class="flex justify-between">

<div>

<div class="text-xs
text-gray-500
uppercase
tracking-wider">

Databases

</div>

<div class="stat-number mt-2">

26

</div>

</div>

<div class="icon-box">

🗄️

</div>

</div>

<div class="mt-5
text-xs
text-green-400">

● All Healthy

</div>

</div>


<!-- VM -->

<div class="glass rounded-2xl p-6
fade-up delay-3">

<div class="flex justify-between">

<div>

<div class="text-xs
text-gray-500
uppercase
tracking-wider">

Virtual Machines

</div>

<div class="stat-number mt-2">

124

</div>

</div>

<div class="icon-box">

☁️

</div>

</div>

<div class="mt-5
text-xs
text-green-400">

● VMware Cluster Online

</div>

</div>


<!-- BACKUP -->

<div class="glass rounded-2xl p-6
fade-up delay-4">

<div class="flex justify-between">

<div>

<div class="text-xs
text-gray-500
uppercase
tracking-wider">

Backup Success

</div>

<div class="stat-number mt-2">

98.7%

</div>

</div>

<div class="icon-box">

💾

</div>

</div>

<div class="mt-5
text-xs
text-green-400">

● Last backup successful

</div>

</div>

</section>


<!-- ========================================================
     MAIN GRID
========================================================= -->

<section
class="grid
grid-cols-1
lg:grid-cols-3
gap-6">


<!-- ======================================================
     LEFT
======================================================= -->

<div class="lg:col-span-2 space-y-6">


<!-- INFRASTRUCTURE -->

<div class="glass rounded-2xl p-7">

<div class="flex
justify-between
items-center
mb-7">

<div>

<h2 class="text-xl font-bold">

Infrastructure Health

</h2>

<p class="text-sm
text-gray-500
mt-1">

Live resource utilization

</p>

</div>

<div class="px-3 py-1
rounded-full
bg-green-500/10
border
border-green-500/20
text-green-400
text-xs">

HEALTHY

</div>

</div>


<!-- CPU -->

<div class="mb-7">

<div class="flex justify-between
text-sm mb-2">

<span class="text-gray-400">
CPU Utilization
</span>

<span class="font-bold">
42%
</span>

</div>

<div class="progress">

<div
class="progress-bar"
style="width:42%">

</div>

</div>

</div>


<!-- MEMORY -->

<div class="mb-7">

<div class="flex justify-between
text-sm mb-2">

<span class="text-gray-400">
Memory Utilization
</span>

<span class="font-bold">
61%
</span>

</div>

<div class="progress">

<div
class="progress-bar"
style="width:61%">

</div>

</div>

</div>


<!-- STORAGE -->

<div>

<div class="flex justify-between
text-sm mb-2">

<span class="text-gray-400">
Storage Utilization
</span>

<span class="font-bold">
68%
</span>

</div>

<div class="progress">

<div
class="progress-bar"
style="width:68%">

</div>

</div>

</div>

</div>


<!-- ====================================================
     TERMINAL
===================================================== -->

<div class="glass rounded-2xl p-6">

<div class="flex
justify-between
items-center
mb-4">

<h2 class="font-bold">

System Activity

</h2>

<div class="flex items-center gap-2">

<div class="status-ring"></div>

<span class="text-xs
text-green-400">

LIVE

</span>

</div>

</div>


<div class="terminal
rounded-xl
p-5
text-xs
md:text-sm
leading-7">

<p class="text-gray-500">

[ SYSTEM ]

<span class="text-gray-300">

Initializing infrastructure monitoring...

</span>

<span class="text-green-400">

OK

</span>

</p>


<p class="text-gray-500">

[ VMWARE ]

<span class="text-gray-300">

Checking vCenter connectivity...

</span>

<span class="text-green-400">

OK

</span>

</p>


<p class="text-gray-500">

[ ORACLE ]

<span class="text-gray-300">

Oracle Database monitoring...

</span>

<span class="text-green-400">

OK

</span>

</p>


<p class="text-gray-500">

[ RMAN ]

<span class="text-gray-300">

Backup verification...

</span>

<span class="text-green-400">

OK

</span>

</p>


<p class="text-gray-500">

[ SECURITY ]

<span class="text-gray-300">

Security monitoring...

</span>

<span class="text-green-400">

ACTIVE

</span>

</p>


<p class="text-green-400 mt-3">

> SYSTEM READY

<span class="cursor"></span>

</p>

</div>

</div>


<!-- ====================================================
     SERVICES
===================================================== -->

<div class="glass rounded-2xl p-6">

<h2 class="font-bold text-lg mb-5">

Core Services

</h2>


<div class="grid
grid-cols-2
md:grid-cols-4
gap-4">


<div class="bg-white/5
rounded-xl
p-4
border
border-white/5
hover:border-red-500/30
transition">

<div class="text-2xl mb-2">
⚙️
</div>

<div class="text-sm font-semibold">
VMware
</div>

<div class="text-xs
text-green-400
mt-1">

● Online

</div>

</div>


<div class="bg-white/5
rounded-xl
p-4
border
border-white/5
hover:border-red-500/30
transition">

<div class="text-2xl mb-2">
🛢️
</div>

<div class="text-sm font-semibold">
Oracle
</div>

<div class="text-xs
text-green-400
mt-1">

● Online

</div>

</div>


<div class="bg-white/5
rounded-xl
p-4
border
border-white/5
hover:border-red-500/30
transition">

<div class="text-2xl mb-2">
📡
</div>

<div class="text-sm font-semibold">
Monitoring
</div>

<div class="text-xs
text-green-400
mt-1">

● Active

</div>

</div>


<div class="bg-white/5
rounded-xl
p-4
border
border-white/5
hover:border-red-500/30
transition">

<div class="text-2xl mb-2">
🛡️
</div>

<div class="text-sm font-semibold">
Security
</div>

<div class="text-xs
text-green-400
mt-1">

● Protected

</div>

</div>

</div>

</div>

</div>


<!-- ======================================================
     RIGHT
======================================================= -->

<div class="space-y-6">


<!-- PROFILE -->

<div class="glass rounded-2xl p-6">

<div class="text-xs
uppercase
tracking-widest
text-gray-500
mb-5">

System Administrator

</div>


<div class="flex
items-center
gap-4">

<div
class="w-16
h-16
rounded-2xl
bg-gradient-to-br
from-red-500
to-red-900
flex
items-center
justify-center
text-xl
font-bold
shadow-lg
shadow-red-900/30">

PW

</div>


<div>

<div class="font-bold
text-lg">

Prasad Wanigasooriya

</div>

<div class="text-sm
text-gray-500">

IT & Network Officer - A9

</div>

</div>

</div>


<div class="mt-6
grid
grid-cols-2
gap-3">


<div class="bg-white/5
rounded-xl
p-3">

<div class="text-[10px]
text-gray-500
uppercase">

Section

</div>

<div class="text-sm
font-semibold
mt-1">

Systems

</div>

</div>


<div class="bg-white/5
rounded-xl
p-3">

<div class="text-[10px]
text-gray-500
uppercase">

Status

</div>

<div class="text-sm
font-semibold
text-green-400
mt-1">

Active

</div>

</div>

</div>

</div>


<!-- ENVIRONMENT -->

<div class="glass rounded-2xl p-6">

<h2 class="font-bold text-lg mb-5">

Environment

</h2>


<div class="space-y-5">


<div>

<div class="text-[10px]
uppercase
tracking-widest
text-gray-500">

AWS Region

</div>

<div class="font-semibold mt-1">

{{ aws_region }}

</div>

</div>


<div>

<div class="text-[10px]
uppercase
tracking-widest
text-gray-500">

Environment

</div>

<div class="font-semibold mt-1">

{{ env_name }}

</div>

</div>


<div>

<div class="text-[10px]
uppercase
tracking-widest
text-gray-500">

Runtime

</div>

<div class="font-semibold mt-1">

Python / Flask / Gunicorn

</div>

</div>

</div>

</div>


<!-- ACTIONS -->

<div class="glass rounded-2xl p-6">

<h2 class="font-bold mb-4">

Quick Actions

</h2>


<a
href="/health"
class="red-button
block
text-center
rounded-xl
py-3
font-semibold
text-sm">

RUN HEALTH CHECK

</a>


<a
href="{{ github_url }}"
target="_blank"
class="block
mt-3
text-center
rounded-xl
py-3
font-semibold
text-sm
border
border-white/10
bg-white/5
hover:bg-white/10
transition">

SOURCE CODE

</a>

</div>

</div>

</section>

</main>


<!-- ========================================================
     FOOTER
========================================================= -->

<footer
class="border-t
border-white/10
mt-10">

<div class="max-w-7xl
mx-auto
px-6
py-6">

<div class="flex
flex-col
md:flex-row
justify-between
gap-3
text-xs
text-gray-500">

<div>

SLT-MOBITEL Enterprise IT Infrastructure

</div>

<div>

AWS Elastic Beanstalk · Flask · Python

</div>

<div>

Prasad Wanigasooriya · 2026

</div>

</div>

</div>

</footer>


<!-- ========================================================
     JAVASCRIPT
========================================================= -->

<script>

/* =========================================================
   LIVE CLOCK
========================================================= */

function updateClock() {

    const now = new Date();

    const time =
        now.toISOString()
        .replace("T", " ")
        .substring(0, 19);

    document.getElementById(
        "server-time"
    ).textContent = time + " UTC";
}

updateClock();

setInterval(
    updateClock,
    1000
);


/* =========================================================
   MOUSE GLOW EFFECT
========================================================= */

document.addEventListener(
    "mousemove",
    function(event) {

        const x =
            event.clientX /
            window.innerWidth * 100;

        const y =
            event.clientY /
            window.innerHeight * 100;

        document.body.style.setProperty(
            "--mouse-x",
            x + "%"
        );

        document.body.style.setProperty(
            "--mouse-y",
            y + "%"
        );

    }
);

</script>


</body>

</html>
"""


# ============================================================
# HOME
# ============================================================

@application.route("/")
def home():

    now = datetime.now(
        timezone.utc
    ).strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    env_name = os.environ.get(
        "AWS_EB_ENVIRONMENT_NAME",
        "LOCAL_DEBUG"
    )

    aws_region = os.environ.get(
        "AWS_REGION",
        "ap-south-1"
    )

    return render_template_string(
        HTML_TEMPLATE,
        current_time=now,
        github_url=GITHUB_REPO_URL,
        env_name=env_name,
        aws_region=aws_region
    )


# ============================================================
# HEALTH API
# ============================================================

@application.route("/health")
def health_check():

    return jsonify({

        "status": "nominal",

        "application":
            "SLT-MOBITEL Enterprise IT Dashboard",

        "user":
            "Prasad Wanigasooriya",

        "service_id":
            "sltmobitel-systems-01",

        "environment":
            os.environ.get(
                "AWS_EB_ENVIRONMENT_NAME",
                "LOCAL_DEBUG"
            ),

        "region":
            os.environ.get(
                "AWS_REGION",
                "ap-south-1"
            ),

        "timestamp_utc":
            datetime.now(
                timezone.utc
            ).isoformat()

    }), 200


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    application.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
```
