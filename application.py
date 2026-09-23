from flask import Flask, render_template_string, jsonify
from datetime import datetime, timezone
import os

# ============================================================
# SLT-MOBITEL THEME - Flask Web Application
# ============================================================

GITHUB_REPO_URL = "https://github.com/your-username/your-repo-name"

application = Flask(__name__)

# ============================================================
# HTML TEMPLATE
# ============================================================

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>SLT-MOBITEL | IT Systems Dashboard</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>

    <!-- Google Font -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
        rel="stylesheet"
    >

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: #f4f6f8;
            color: #172033;
        }

        /* SLT-MOBITEL inspired colors */
        :root {
            --slt-red: #e30613;
            --slt-dark-red: #b8000d;
            --slt-navy: #111827;
            --slt-blue: #17365d;
            --light-gray: #f4f6f8;
        }

        .slt-red {
            background: var(--slt-red);
        }

        .slt-dark {
            background: var(--slt-navy);
        }

        .red-text {
            color: var(--slt-red);
        }

        /* Top red line */
        .top-line {
            height: 5px;
            background: linear-gradient(
                90deg,
                #e30613 0%,
                #e30613 70%,
                #111827 70%,
                #111827 100%
            );
        }

        /* Main cards */
        .dashboard-card {
            background: white;
            border-radius: 12px;
            border: 1px solid #e5e7eb;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.05);
        }

        .dashboard-card:hover {
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
            transform: translateY(-1px);
            transition: all 0.2s ease;
        }

        /* Status pulse */
        .status-dot {
            width: 10px;
            height: 10px;
            background: #16a34a;
            border-radius: 50%;
            position: relative;
        }

        .status-dot::after {
            content: "";
            position: absolute;
            inset: -4px;
            border-radius: 50%;
            border: 2px solid #22c55e;
            opacity: 0.4;
            animation: pulse 1.8s infinite;
        }

        @keyframes pulse {
            0% {
                transform: scale(0.8);
                opacity: 0.8;
            }

            70% {
                transform: scale(1.4);
                opacity: 0;
            }

            100% {
                transform: scale(1.4);
                opacity: 0;
            }
        }

        /* Terminal */
        .terminal {
            background: #111827;
            color: #d1d5db;
            border-radius: 10px;
            font-family: monospace;
        }

        .terminal-green {
            color: #4ade80;
        }

        /* Progress */
        .progress-bg {
            background: #e5e7eb;
            height: 7px;
            border-radius: 10px;
            overflow: hidden;
        }

        .progress-red {
            background: var(--slt-red);
            height: 100%;
            border-radius: 10px;
        }

        /* Navigation */
        .nav-link {
            color: #4b5563;
            font-size: 14px;
            font-weight: 500;
        }

        .nav-link:hover {
            color: var(--slt-red);
        }

        /* Button */
        .red-button {
            background: var(--slt-red);
            color: white;
            transition: all 0.2s ease;
        }

        .red-button:hover {
            background: var(--slt-dark-red);
            transform: translateY(-1px);
        }

    </style>

    <script>

        function updateClock() {

            const now = new Date();

            const formatted =
                now.toISOString()
                .replace("T", " ")
                .substring(0, 19) + " UTC";

            document.getElementById("server-time").textContent = formatted;
        }

        setInterval(updateClock, 1000);

    </script>

</head>


<body>

    <!-- =====================================================
         TOP BRAND LINE
    ====================================================== -->

    <div class="top-line"></div>


    <!-- =====================================================
         HEADER
    ====================================================== -->

    <header class="bg-white border-b border-gray-200">

        <div class="max-w-7xl mx-auto px-6 py-4">

            <div class="flex flex-col md:flex-row
                        justify-between items-center gap-4">

                <!-- Brand -->

                <div class="flex items-center gap-4">

                    <div class="flex items-center">

                        <div class="text-3xl font-extrabold
                                    tracking-tight text-red-600">

                            SLT

                        </div>

                        <div class="mx-2 text-gray-400">
                            |
                        </div>

                        <div class="text-2xl font-bold
                                    text-gray-800">

                            MOBITEL

                        </div>

                    </div>

                    <div class="hidden md:block
                                h-8 w-px bg-gray-300">
                    </div>

                    <div class="hidden md:block">

                        <p class="text-xs
                                  text-gray-400
                                  uppercase
                                  tracking-wider">

                            Enterprise IT

                        </p>

                        <p class="text-sm font-semibold
                                  text-gray-700">

                            Systems Management Portal

                        </p>

                    </div>

                </div>


                <!-- User -->

                <div class="flex items-center gap-4">

                    <div class="text-right">

                        <p class="text-xs text-gray-400">
                            LOGGED IN USER
                        </p>

                        <p class="text-sm font-semibold
                                  text-gray-800">

                            Prasad Wanigasooriya

                        </p>

                    </div>

                    <div class="w-10 h-10 rounded-full
                                bg-red-600
                                text-white
                                flex items-center
                                justify-center
                                font-bold">

                        PW

                    </div>

                </div>

            </div>

        </div>

    </header>


    <!-- =====================================================
         NAVIGATION
    ====================================================== -->

    <nav class="bg-white border-b border-gray-200">

        <div class="max-w-7xl mx-auto px-6">

            <div class="flex gap-8 py-3">

                <a href="/" class="nav-link">
                    Dashboard
                </a>

                <a href="/health" class="nav-link">
                    System Health
                </a>

                <a href="#" class="nav-link">
                    Servers
                </a>

                <a href="#" class="nav-link">
                    Databases
                </a>

                <a href="#" class="nav-link">
                    Monitoring
                </a>

            </div>

        </div>

    </nav>


    <!-- =====================================================
         MAIN
    ====================================================== -->

    <main class="max-w-7xl mx-auto px-6 py-8">


        <!-- Page Heading -->

        <div class="flex flex-col md:flex-row
                    justify-between
                    md:items-center
                    gap-4 mb-8">

            <div>

                <p class="text-sm text-gray-500">
                    IT & SYSTEMS / DASHBOARD
                </p>

                <h1 class="text-3xl font-bold
                           text-gray-900 mt-1">

                    Infrastructure Overview

                </h1>

                <p class="text-gray-500 mt-1">

                    SLT-MOBITEL Enterprise Systems Monitoring

                </p>

            </div>


            <!-- System Status -->

            <div class="flex items-center gap-3
                        bg-white border
                        border-gray-200
                        rounded-lg px-4 py-3">

                <div class="status-dot"></div>

                <div>

                    <p class="text-xs text-gray-400">
                        SYSTEM STATUS
                    </p>

                    <p class="text-sm font-bold text-green-600">
                        OPERATIONAL
                    </p>

                </div>

            </div>

        </div>


        <!-- =================================================
             STATISTICS
        ================================================== -->

        <div class="grid grid-cols-1
                    sm:grid-cols-2
                    lg:grid-cols-4
                    gap-5 mb-6">


            <!-- Servers -->

            <div class="dashboard-card p-5">

                <div class="flex justify-between">

                    <div>

                        <p class="text-xs
                                  uppercase
                                  tracking-wider
                                  text-gray-400">

                            Production Servers

                        </p>

                        <p class="text-3xl font-bold
                                  text-gray-900 mt-2">

                            48

                        </p>

                    </div>

                    <div class="w-11 h-11
                                rounded-lg
                                bg-red-50
                                flex items-center
                                justify-center
                                text-red-600">

                        🖥️

                    </div>

                </div>

                <p class="text-xs text-green-600 mt-3">
                    ● 47 Online / 1 Maintenance
                </p>

            </div>


            <!-- Databases -->

            <div class="dashboard-card p-5">

                <div class="flex justify-between">

                    <div>

                        <p class="text-xs
                                  uppercase
                                  tracking-wider
                                  text-gray-400">

                            Databases

                        </p>

                        <p class="text-3xl font-bold
                                  text-gray-900 mt-2">

                            26

                        </p>

                    </div>

                    <div class="w-11 h-11
                                rounded-lg
                                bg-red-50
                                flex items-center
                                justify-center
                                text-red-600">

                        🗄️

                    </div>

                </div>

                <p class="text-xs text-green-600 mt-3">
                    ● All Database Services Healthy
                </p>

            </div>


            <!-- VMware -->

            <div class="dashboard-card p-5">

                <div class="flex justify-between">

                    <div>

                        <p class="text-xs
                                  uppercase
                                  tracking-wider
                                  text-gray-400">

                            Virtual Machines

                        </p>

                        <p class="text-3xl font-bold
                                  text-gray-900 mt-2">

                            124

                        </p>

                    </div>

                    <div class="w-11 h-11
                                rounded-lg
                                bg-red-50
                                flex items-center
                                justify-center">

                        ☁️

                    </div>

                </div>

                <p class="text-xs text-green-600 mt-3">
                    ● VMware Cluster Healthy
                </p>

            </div>


            <!-- Backup -->

            <div class="dashboard-card p-5">

                <div class="flex justify-between">

                    <div>

                        <p class="text-xs
                                  uppercase
                                  tracking-wider
                                  text-gray-400">

                            Backup Status

                        </p>

                        <p class="text-3xl font-bold
                                  text-gray-900 mt-2">

                            98.7%

                        </p>

                    </div>

                    <div class="w-11 h-11
                                rounded-lg
                                bg-red-50
                                flex items-center
                                justify-center">

                        💾

                    </div>

                </div>

                <p class="text-xs text-green-600 mt-3">
                    ● Backup Operations Normal
                </p>

            </div>

        </div>


        <!-- =================================================
             MAIN GRID
        ================================================== -->

        <div class="grid grid-cols-1
                    lg:grid-cols-3
                    gap-6">


            <!-- LEFT -->

            <div class="lg:col-span-2 space-y-6">


                <!-- Infrastructure -->

                <div class="dashboard-card p-6">

                    <div class="flex justify-between
                                items-center
                                border-b
                                border-gray-200
                                pb-4 mb-5">

                        <div>

                            <h2 class="text-lg font-bold
                                       text-gray-900">

                                Infrastructure Health

                            </h2>

                            <p class="text-sm text-gray-500">

                                Current environment status

                            </p>

                        </div>

                        <span class="text-xs
                                     px-3 py-1
                                     rounded-full
                                     bg-green-100
                                     text-green-700
                                     font-semibold">

                            HEALTHY

                        </span>

                    </div>


                    <!-- CPU -->

                    <div class="mb-5">

                        <div class="flex justify-between mb-2">

                            <span class="text-sm
                                         font-medium
                                         text-gray-700">

                                CPU Utilization

                            </span>

                            <span class="text-sm
                                         font-semibold">

                                42%

                            </span>

                        </div>

                        <div class="progress-bg">

                            <div class="progress-red"
                                 style="width:42%">
                            </div>

                        </div>

                    </div>


                    <!-- Memory -->

                    <div class="mb-5">

                        <div class="flex justify-between mb-2">

                            <span class="text-sm
                                         font-medium
                                         text-gray-700">

                                Memory Utilization

                            </span>

                            <span class="text-sm
                                         font-semibold">

                                61%

                            </span>

                        </div>

                        <div class="progress-bg">

                            <div class="progress-red"
                                 style="width:61%">
                            </div>

                        </div>

                    </div>


                    <!-- Storage -->

                    <div>

                        <div class="flex justify-between mb-2">

                            <span class="text-sm
                                         font-medium
                                         text-gray-700">

                                Storage Utilization

                            </span>

                            <span class="text-sm
                                         font-semibold">

                                68%

                            </span>

                        </div>

                        <div class="progress-bg">

                            <div class="progress-red"
                                 style="width:68%">
                            </div>

                        </div>

                    </div>

                </div>


                <!-- Terminal -->

                <div class="dashboard-card p-6">

                    <div class="flex justify-between
                                items-center mb-4">

                        <h2 class="text-lg font-bold">
                            System Activity
                        </h2>

                        <span class="text-xs
                                     text-gray-400">

                            LIVE

                        </span>

                    </div>


                    <div class="terminal p-5 text-sm
                                leading-7">

                        <p>
                            <span class="text-gray-500">
                                [SYSTEM]
                            </span>
                            Initializing monitoring services...
                            <span class="terminal-green">
                                OK
                            </span>
                        </p>

                        <p>
                            <span class="text-gray-500">
                                [VMWARE]
                            </span>
                            vCenter connectivity check...
                            <span class="terminal-green">
                                OK
                            </span>
                        </p>

                        <p>
                            <span class="text-gray-500">
                                [ORACLE]
                            </span>
                            Database monitoring...
                            <span class="terminal-green">
                                OK
                            </span>
                        </p>

                        <p>
                            <span class="text-gray-500">
                                [BACKUP]
                            </span>
                            RMAN backup verification...
                            <span class="terminal-green">
                                OK
                            </span>
                        </p>

                        <p>
                            <span class="text-gray-500">
                                [SECURITY]
                            </span>
                            Endpoint security status...
                            <span class="terminal-green">
                                ACTIVE
                            </span>
                        </p>

                        <p class="text-green-400 mt-2">
                            > SYSTEM READY
                        </p>

                    </div>

                </div>

            </div>


            <!-- RIGHT -->

            <div class="space-y-6">


                <!-- User Profile -->

                <div class="dashboard-card p-6">

                    <h2 class="text-lg font-bold
                               text-gray-900
                               border-b
                               border-gray-200
                               pb-3 mb-5">

                        User Profile

                    </h2>


                    <div class="flex items-center gap-4">

                        <div class="w-14 h-14
                                    rounded-full
                                    bg-red-600
                                    text-white
                                    flex items-center
                                    justify-center
                                    text-lg
                                    font-bold">

                            PW

                        </div>

                        <div>

                            <p class="font-bold
                                      text-gray-900">

                                Prasad Wanigasooriya

                            </p>

                            <p class="text-sm
                                      text-gray-500">

                                IT & Network Officer - A9

                            </p>

                        </div>

                    </div>


                    <div class="mt-5
                                bg-gray-50
                                rounded-lg
                                p-4">

                        <p class="text-xs
                                  text-gray-400
                                  uppercase">

                            Department

                        </p>

                        <p class="text-sm
                                  font-semibold
                                  text-gray-800
                                  mt-1">

                            Systems Section

                        </p>

                    </div>

                </div>


                <!-- Environment -->

                <div class="dashboard-card p-6">

                    <h2 class="text-lg font-bold
                               text-gray-900
                               border-b
                               border-gray-200
                               pb-3 mb-5">

                        Environment

                    </h2>


                    <div class="space-y-4">


                        <div>

                            <p class="text-xs text-gray-400">
                                AWS REGION
                            </p>

                            <p class="font-semibold mt-1">
                                {{ aws_region }}
                            </p>

                        </div>


                        <div>

                            <p class="text-xs text-gray-400">
                                EB ENVIRONMENT
                            </p>

                            <p class="font-semibold mt-1">
                                {{ env_name }}
                            </p>

                        </div>


                        <div>

                            <p class="text-xs text-gray-400">
                                SERVER TIME
                            </p>

                            <p id="server-time"
                               class="font-semibold mt-1">

                                {{ current_time }}

                            </p>

                        </div>


                        <div>

                            <p class="text-xs text-gray-400">
                                APPLICATION
                            </p>

                            <p class="font-semibold mt-1">
                                Flask / Gunicorn
                            </p>

                        </div>

                    </div>

                </div>


                <!-- Actions -->

                <div class="dashboard-card p-6">

                    <h2 class="text-lg font-bold
                               text-gray-900 mb-4">

                        Quick Actions

                    </h2>


                    <div class="space-y-3">

                        <a href="/health"
                           class="red-button
                                  block
                                  text-center
                                  rounded-lg
                                  px-4 py-3
                                  font-semibold
                                  text-sm">

                            RUN SYSTEM HEALTH CHECK

                        </a>


                        <a href="{{ github_url }}"
                           target="_blank"
                           class="block
                                  text-center
                                  rounded-lg
                                  px-4 py-3
                                  font-semibold
                                  text-sm
                                  border
                                  border-gray-300
                                  text-gray-700
                                  hover:bg-gray-50">

                            VIEW SOURCE CODE

                        </a>

                    </div>

                </div>

            </div>

        </div>

    </main>


    <!-- =====================================================
         FOOTER
    ====================================================== -->

    <footer class="bg-gray-900 text-gray-400 mt-8">

        <div class="max-w-7xl mx-auto
                    px-6 py-5">

            <div class="flex flex-col
                        md:flex-row
                        justify-between
                        gap-3
                        text-xs">

                <p>
                    SLT-MOBITEL Enterprise IT Systems Portal
                </p>

                <p>
                    Flask v3.x | Python | AWS Elastic Beanstalk
                </p>

                <p>
                    © 2026 Prasad Wanigasooriya
                </p>

            </div>

        </div>

    </footer>

</body>

</html>
"""


# ============================================================
# HOME ROUTE
# ============================================================

@application.route("/")
def home():

    now = datetime.now(timezone.utc).strftime(
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
# HEALTH CHECK API
# ============================================================

@application.route("/health")
def health_check():

    return jsonify({
        "status": "nominal",
        "application": "SLT-MOBITEL IT Systems Dashboard",
        "user": "Prasad Wanigasooriya",
        "service_id": "sltmobitel-systems-01",
        "environment": os.environ.get(
            "AWS_EB_ENVIRONMENT_NAME",
            "LOCAL_DEBUG"
        ),
        "region": os.environ.get(
            "AWS_REGION",
            "ap-south-1"
        ),
        "timestamp_utc": datetime.now(
            timezone.utc
        ).isoformat()
    }), 200


# ============================================================
# APPLICATION START
# ============================================================

if __name__ == "__main__":

    application.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
