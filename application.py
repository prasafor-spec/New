```python
from flask import Flask, render_template_string, jsonify
from datetime import datetime, timezone
import os

# ============================================================
# CONFIGURATION
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
    <link rel="preconnect"
          href="https://fonts.gstatic.com"
          crossorigin>

    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap"
          rel="stylesheet">

    <style>

        /* =====================================================
           GLOBAL
        ===================================================== */

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: 'Inter', Arial, sans-serif;
            background: #f5f6f8;
            color: #172033;
        }

        /* SLT-inspired colors */

        :root {
            --slt-red: #e30613;
            --slt-dark-red: #bd0010;
            --slt-navy: #172033;
            --slt-blue: #17365d;
            --border: #e5e7eb;
            --background: #f5f6f8;
        }


        /* =====================================================
           TOP BRAND BAR
        ===================================================== */

        .brand-line {
            height: 5px;
            background: linear-gradient(
                90deg,
                #e30613 0%,
                #e30613 72%,
                #172033 72%,
                #172033 100%
            );
        }


        /* =====================================================
           HEADER
        ===================================================== */

        .main-header {
            background: white;
            border-bottom: 1px solid #e5e7eb;
        }

        .logo-slt {
            color: #e30613;
            font-size: 31px;
            font-weight: 800;
            letter-spacing: -1.5px;
        }

        .logo-mobitel {
            color: #172033;
            font-size: 27px;
            font-weight: 700;
            letter-spacing: -1px;
        }


        /* =====================================================
           NAVIGATION
        ===================================================== */

        .nav-link {
            color: #667085;
            font-size: 14px;
            font-weight: 500;
            padding: 8px 0;
            border-bottom: 2px solid transparent;
            transition: all 0.2s ease;
        }

        .nav-link:hover {
            color: #e30613;
            border-bottom-color: #e30613;
        }

        .nav-link.active {
            color: #e30613;
            border-bottom-color: #e30613;
        }


        /* =====================================================
           CARDS
        ===================================================== */

        .card {
            background: white;
            border: 1px solid var(--border);
            border-radius: 12px;
            box-shadow: 0 2px 8px rgba(16, 24, 40, 0.04);
        }

        .card:hover {
            box-shadow: 0 5px 18px rgba(16, 24, 40, 0.08);
            transition: box-shadow 0.2s ease;
        }


        /* =====================================================
           STAT CARDS
        ===================================================== */

        .stat-icon {
            width: 46px;
            height: 46px;
            border-radius: 10px;

            display: flex;
            align-items: center;
            justify-content: center;

            background: #fff1f2;
            color: #e30613;

            font-size: 20px;
        }

        .stat-number {
            font-size: 30px;
            line-height: 1;
            font-weight: 800;
            color: #172033;
        }


        /* =====================================================
           STATUS
        ===================================================== */

        .status-dot {
            width: 9px;
            height: 9px;
            background: #16a34a;
            border-radius: 50%;
        }


        /* =====================================================
           PROGRESS BARS
        ===================================================== */

        .progress-container {
            width: 100%;
            height: 7px;
            background: #edf0f2;
            border-radius: 20px;
            overflow: hidden;
        }

        .progress-red {
            height: 100%;
            background: #e30613;
            border-radius: 20px;
        }

        .progress-blue {
            height: 100%;
            background: #315b88;
            border-radius: 20px;
        }

        .progress-green {
            height: 100%;
            background: #16a34a;
            border-radius: 20px;
        }


        /* =====================================================
           SERVICE STATUS
        ===================================================== */

        .service-row {
            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 14px 0;

            border-bottom: 1px solid #eef0f2;
        }

        .service-row:last-child {
            border-bottom: none;
        }


        /* =====================================================
           TERMINAL
        ===================================================== */

        .terminal {
            background: #111827;
            color: #d1d5db;
            border-radius: 9px;
            font-family: "Courier New", monospace;
        }


        /* =====================================================
           BUTTONS
        ===================================================== */

        .primary-button {
            display: block;
            width: 100%;

            background: #e30613;
            color: white;

            padding: 12px 18px;

            border-radius: 8px;

            text-align: center;

            font-size: 13px;
            font-weight: 600;

            transition: background 0.2s ease;
        }

        .primary-button:hover {
            background: #bd0010;
        }

        .secondary-button {
            display: block;
            width: 100%;

            background: white;
            color: #344054;

            padding: 12px 18px;

            border-radius: 8px;

            text-align: center;

            font-size: 13px;
            font-weight: 600;

            border: 1px solid #d0d5dd;

            transition: background 0.2s ease;
        }

        .secondary-button:hover {
            background: #f9fafb;
        }


        /* =====================================================
           PROFILE
        ===================================================== */

        .profile-avatar {
            width: 56px;
            height: 56px;

            border-radius: 50%;

            display: flex;
            align-items: center;
            justify-content: center;

            background: #e30613;
            color: white;

            font-size: 17px;
            font-weight: 700;
        }


        /* =====================================================
           BADGES
        ===================================================== */

        .badge-green {
            display: inline-flex;
            align-items: center;
            gap: 6px;

            padding: 5px 10px;

            border-radius: 20px;

            background: #ecfdf3;
            color: #027a48;

            font-size: 11px;
            font-weight: 600;
        }

        .badge-red {
            display: inline-flex;
            align-items: center;
            gap: 6px;

            padding: 5px 10px;

            border-radius: 20px;

            background: #fff1f2;
            color: #c01048;

            font-size: 11px;
            font-weight: 600;
        }


        /* =====================================================
           FOOTER
        ===================================================== */

        footer {
            background: #172033;
            color: #98a2b3;
        }


        /* =====================================================
           MOBILE
        ===================================================== */

        @media (max-width: 768px) {

            .logo-slt {
                font-size: 26px;
            }

            .logo-mobitel {
                font-size: 22px;
            }

            .stat-number {
                font-size: 27px;
            }

        }

    </style>

</head>


<body>


<!-- =========================================================
     BRAND LINE
========================================================== -->

<div class="brand-line"></div>


<!-- =========================================================
     HEADER
========================================================== -->

<header class="main-header">

    <div class="max-w-7xl mx-auto px-5 lg:px-8">

        <div class="flex items-center justify-between py-4">

            <!-- LOGO -->

            <div class="flex items-center gap-4">

                <div class="flex items-center">

                    <span class="logo-slt">
                        SLT
                    </span>

                    <span class="mx-2 text-gray-300 text-xl">
                        |
                    </span>

                    <span class="logo-mobitel">
                        MOBITEL
                    </span>

                </div>

                <div class="hidden md:block
                            border-l border-gray-200
                            pl-4">

                    <div class="text-[10px]
                                uppercase
                                tracking-wider
                                text-gray-400">

                        Enterprise IT

                    </div>

                    <div class="text-xs
                                font-medium
                                text-gray-600">

                        Systems & Infrastructure

                    </div>

                </div>

            </div>


            <!-- USER -->

            <div class="flex items-center gap-3">

                <div class="hidden sm:block text-right">

                    <div class="text-[10px]
                                uppercase
                                tracking-wider
                                text-gray-400">

                        Logged in

                    </div>

                    <div class="text-sm
                                font-semibold
                                text-gray-800">

                        Prasad Wanigasooriya

                    </div>

                </div>

                <div class="profile-avatar">
                    PW
                </div>

            </div>

        </div>


        <!-- NAVIGATION -->

        <div class="hidden md:flex items-center gap-8">

            <a href="/" class="nav-link active">
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
                Virtualization
            </a>

            <a href="#" class="nav-link">
                Monitoring
            </a>

        </div>

        <div class="h-px bg-gray-100 mt-3"></div>

    </div>

</header>


<!-- =========================================================
     MAIN CONTENT
========================================================== -->

<main class="max-w-7xl mx-auto px-5 lg:px-8 py-8">


    <!-- =====================================================
         PAGE HEADER
    ====================================================== -->

    <div class="flex flex-col
                lg:flex-row
                lg:items-center
                lg:justify-between
                gap-5
                mb-7">

        <div>

            <div class="text-xs
                        uppercase
                        tracking-wider
                        text-gray-400
                        mb-2">

                IT & SYSTEMS / DASHBOARD

            </div>

            <h1 class="text-3xl
                       font-bold
                       text-gray-900">

                Infrastructure Overview

            </h1>

            <p class="text-sm
                      text-gray-500
                      mt-2">

                Enterprise systems and infrastructure
                monitoring dashboard

            </p>

        </div>


        <!-- SYSTEM STATUS -->

        <div class="card px-5 py-4
                    flex items-center gap-3">

            <div class="status-dot"></div>

            <div>

                <div class="text-[10px]
                            uppercase
                            tracking-wider
                            text-gray-400">

                    System Status

                </div>

                <div class="text-sm
                            font-semibold
                            text-green-600">

                    All Systems Operational

                </div>

            </div>

        </div>

    </div>


    <!-- =====================================================
         STATISTICS
    ====================================================== -->

    <div class="grid
                grid-cols-1
                sm:grid-cols-2
                lg:grid-cols-4
                gap-5
                mb-6">


        <!-- SERVERS -->

        <div class="card p-5">

            <div class="flex
                        items-start
                        justify-between">

                <div>

                    <div class="text-xs
                                uppercase
                                tracking-wider
                                text-gray-400">

                        Production Servers

                    </div>

                    <div class="stat-number mt-3">
                        48
                    </div>

                    <div class="text-xs
                                text-green-600
                                mt-3">

                        ● 47 Online

                    </div>

                </div>

                <div class="stat-icon">
                    🖥
                </div>

            </div>

        </div>


        <!-- DATABASE -->

        <div class="card p-5">

            <div class="flex
                        items-start
                        justify-between">

                <div>

                    <div class="text-xs
                                uppercase
                                tracking-wider
                                text-gray-400">

                        Databases

                    </div>

                    <div class="stat-number mt-3">
                        26
                    </div>

                    <div class="text-xs
                                text-green-600
                                mt-3">

                        ● All Healthy

                    </div>

                </div>

                <div class="stat-icon">
                    🗄
                </div>

            </div>

        </div>


        <!-- VM -->

        <div class="card p-5">

            <div class="flex
                        items-start
                        justify-between">

                <div>

                    <div class="text-xs
                                uppercase
                                tracking-wider
                                text-gray-400">

                        Virtual Machines

                    </div>

                    <div class="stat-number mt-3">
                        124
                    </div>

                    <div class="text-xs
                                text-green-600
                                mt-3">

                        ● VMware Healthy

                    </div>

                </div>

                <div class="stat-icon">
                    ☁
                </div>

            </div>

        </div>


        <!-- BACKUP -->

        <div class="card p-5">

            <div class="flex
                        items-start
                        justify-between">

                <div>

                    <div class="text-xs
                                uppercase
                                tracking-wider
                                text-gray-400">

                        Backup Success

                    </div>

                    <div class="stat-number mt-3">
                        98.7%
                    </div>

                    <div class="text-xs
                                text-green-600
                                mt-3">

                        ● Last Backup Successful

                    </div>

                </div>

                <div class="stat-icon">
                    💾
                </div>

            </div>

        </div>

    </div>


    <!-- =====================================================
         MAIN GRID
    ====================================================== -->

    <div class="grid
                grid-cols-1
                lg:grid-cols-3
                gap-6">


        <!-- =================================================
             LEFT COLUMN
        ================================================== -->

        <div class="lg:col-span-2 space-y-6">


            <!-- INFRASTRUCTURE HEALTH -->

            <div class="card p-6">

                <div class="flex
                            items-center
                            justify-between
                            border-b
                            border-gray-100
                            pb-4
                            mb-6">

                    <div>

                        <h2 class="text-lg
                                   font-bold
                                   text-gray-900">

                            Infrastructure Health

                        </h2>

                        <p class="text-xs
                                  text-gray-500
                                  mt-1">

                            Current resource utilization

                        </p>

                    </div>

                    <span class="badge-green">

                        <span class="status-dot"></span>

                        HEALTHY

                    </span>

                </div>


                <!-- CPU -->

                <div class="mb-6">

                    <div class="flex
                                justify-between
                                mb-2">

                        <span class="text-sm
                                     font-medium
                                     text-gray-700">

                            CPU Utilization

                        </span>

                        <span class="text-sm
                                     font-semibold
                                     text-gray-900">

                            42%

                        </span>

                    </div>

                    <div class="progress-container">

                        <div class="progress-red"
                             style="width:42%">
                        </div>

                    </div>

                </div>


                <!-- MEMORY -->

                <div class="mb-6">

                    <div class="flex
                                justify-between
                                mb-2">

                        <span class="text-sm
                                     font-medium
                                     text-gray-700">

                            Memory Utilization

                        </span>

                        <span class="text-sm
                                     font-semibold
                                     text-gray-900">

                            61%

                        </span>

                    </div>

                    <div class="progress-container">

                        <div class="progress-blue"
                             style="width:61%">
                        </div>

                    </div>

                </div>


                <!-- STORAGE -->

                <div>

                    <div class="flex
                                justify-between
                                mb-2">

                        <span class="text-sm
                                     font-medium
                                     text-gray-700">

                            Storage Utilization

                        </span>

                        <span class="text-sm
                                     font-semibold
                                     text-gray-900">

                            68%

                        </span>

                    </div>

                    <div class="progress-container">

                        <div class="progress-red"
                             style="width:68%">
                        </div>

                    </div>

                </div>

            </div>


            <!-- CORE SERVICES -->

            <div class="card p-6">

                <div class="flex
                            items-center
                            justify-between
                            mb-4">

                    <div>

                        <h2 class="text-lg
                                   font-bold
                                   text-gray-900">

                            Core Services

                        </h2>

                        <p class="text-xs
                                  text-gray-500
                                  mt-1">

                            Infrastructure service status

                        </p>

                    </div>

                </div>


                <div>


                    <!-- VMware -->

                    <div class="service-row">

                        <div class="flex items-center gap-3">

                            <div class="w-9 h-9
                                        rounded-lg
                                        bg-gray-100
                                        flex items-center
                                        justify-center">

                                🖥

                            </div>

                            <div>

                                <div class="text-sm
                                            font-semibold">

                                    VMware vSphere

                                </div>

                                <div class="text-xs
                                            text-gray-500">

                                    vCenter / ESXi

                                </div>

                            </div>

                        </div>

                        <span class="badge-green">
                            ONLINE
                        </span>

                    </div>


                    <!-- Oracle -->

                    <div class="service-row">

                        <div class="flex items-center gap-3">

                            <div class="w-9 h-9
                                        rounded-lg
                                        bg-gray-100
                                        flex items-center
                                        justify-center">

                                🗄

                            </div>

                            <div>

                                <div class="text-sm
                                            font-semibold">

                                    Oracle Database

                                </div>

                                <div class="text-xs
                                            text-gray-500">

                                    OEM / RMAN

                                </div>

                            </div>

                        </div>

                        <span class="badge-green">
                            ONLINE
                        </span>

                    </div>


                    <!-- Monitoring -->

                    <div class="service-row">

                        <div class="flex items-center gap-3">

                            <div class="w-9 h-9
                                        rounded-lg
                                        bg-gray-100
                                        flex items-center
                                        justify-center">

                                📊

                            </div>

                            <div>

                                <div class="text-sm
                                            font-semibold">

                                    Infrastructure Monitoring

                                </div>

                                <div class="text-xs
                                            text-gray-500">

                                    Nagios / OEM

                                </div>

                            </div>

                        </div>

                        <span class="badge-green">
                            ACTIVE
                        </span>

                    </div>


                    <!-- Security -->

                    <div class="service-row">

                        <div class="flex items-center gap-3">

                            <div class="w-9 h-9
                                        rounded-lg
                                        bg-gray-100
                                        flex items-center
                                        justify-center">

                                🛡

                            </div>

                            <div>

                                <div class="text-sm
                                            font-semibold">

                                    Security Monitoring

                                </div>

                                <div class="text-xs
                                            text-gray-500">

                                    Endpoint Protection

                                </div>

                            </div>

                        </div>

                        <span class="badge-green">
                            PROTECTED
                        </span>

                    </div>

                </div>

            </div>


            <!-- SYSTEM LOG -->

            <div class="card p-6">

                <div class="flex
                            justify-between
                            items-center
                            mb-4">

                    <div>

                        <h2 class="text-lg
                                   font-bold">

                            Recent System Activity

                        </h2>

                        <p class="text-xs
                                  text-gray-500
                                  mt-1">

                            Latest infrastructure events

                        </p>

                    </div>

                    <span class="text-xs
                                 text-gray-400">

                        LIVE

                    </span>

                </div>


                <div class="terminal p-5
                            text-xs
                            leading-7">

                    <div>

                        <span class="text-gray-500">
                            [INFO]
                        </span>

                        vCenter connectivity verified

                        <span class="text-green-400">
                            [OK]
                        </span>

                    </div>

                    <div>

                        <span class="text-gray-500">
                            [INFO]
                        </span>

                        Oracle OEM monitoring active

                        <span class="text-green-400">
                            [OK]
                        </span>

                    </div>

                    <div>

                        <span class="text-gray-500">
                            [INFO]
                        </span>

                        RMAN backup verification completed

                        <span class="text-green-400">
                            [OK]
                        </span>

                    </div>

                    <div>

                        <span class="text-gray-500">
                            [INFO]
                        </span>

                        Infrastructure health check completed

                        <span class="text-green-400">
                            [OK]
                        </span>

                    </div>

                </div>

            </div>

        </div>


        <!-- =================================================
             RIGHT COLUMN
        ================================================== -->

        <div class="space-y-6">


            <!-- PROFILE -->

            <div class="card p-6">

                <div class="text-xs
                            uppercase
                            tracking-wider
                            text-gray-400
                            mb-5">

                    System User

                </div>


                <div class="flex
                            items-center
                            gap-4">

                    <div class="profile-avatar">
                        PW
                    </div>

                    <div>

                        <h3 class="font-bold
                                   text-gray-900">

                            Prasad Wanigasooriya

                        </h3>

                        <p class="text-xs
                                  text-gray-500
                                  mt-1">

                            IT & Network Officer - A9

                        </p>

                    </div>

                </div>


                <div class="mt-5
                            pt-5
                            border-t
                            border-gray-100">

                    <div class="grid grid-cols-2 gap-4">

                        <div>

                            <div class="text-[10px]
                                        uppercase
                                        text-gray-400">

                                Section

                            </div>

                            <div class="text-sm
                                        font-semibold
                                        mt-1">

                                Systems

                            </div>

                        </div>

                        <div>

                            <div class="text-[10px]
                                        uppercase
                                        text-gray-400">

                                Status

                            </div>

                            <div class="text-sm
                                        font-semibold
                                        text-green-600
                                        mt-1">

                                Active

                            </div>

                        </div>

                    </div>

                </div>

            </div>


            <!-- ENVIRONMENT -->

            <div class="card p-6">

                <h2 class="text-lg
                           font-bold
                           text-gray-900
                           mb-5">

                    Environment

                </h2>


                <div class="space-y-5">


                    <div>

                        <div class="text-[10px]
                                    uppercase
                                    tracking-wider
                                    text-gray-400">

                            AWS Region

                        </div>

                        <div class="text-sm
                                    font-semibold
                                    mt-1">

                            {{ aws_region }}

                        </div>

                    </div>


                    <div>

                        <div class="text-[10px]
                                    uppercase
                                    tracking-wider
                                    text-gray-400">

                            EB Environment

                        </div>

                        <div class="text-sm
                                    font-semibold
                                    mt-1">

                            {{ env_name }}

                        </div>

                    </div>


                    <div>

                        <div class="text-[10px]
                                    uppercase
                                    tracking-wider
                                    text-gray-400">

                            Application

                        </div>

                        <div class="text-sm
                                    font-semibold
                                    mt-1">

                            Flask / Gunicorn

                        </div>

                    </div>


                    <div>

                        <div class="text-[10px]
                                    uppercase
                                    tracking-wider
                                    text-gray-400">

                            Server Time UTC

                        </div>

                        <div id="server-time"
                             class="text-sm
                                    font-semibold
                                    mt-1">

                            {{ current_time }}

                        </div>

                    </div>

                </div>

            </div>


            <!-- QUICK ACTIONS -->

            <div class="card p-6">

                <h2 class="text-lg
                           font-bold
                           text-gray-900
                           mb-4">

                    Quick Actions

                </h2>


                <a href="/health"
                   class="primary-button">

                    RUN SYSTEM HEALTH CHECK

                </a>


                <a href="{{ github_url }}"
                   target="_blank"
                   class="secondary-button mt-3">

                    VIEW SOURCE CODE

                </a>

            </div>


            <!-- SYSTEM INFORMATION -->

            <div class="card p-6">

                <h2 class="text-lg
                           font-bold
                           text-gray-900
                           mb-4">

                    System Information

                </h2>


                <div class="space-y-3
                            text-sm">


                    <div class="flex
                                justify-between">

                        <span class="text-gray-500">
                            Python
                        </span>

                        <span class="font-medium">
                            3.x
                        </span>

                    </div>


                    <div class="flex
                                justify-between">

                        <span class="text-gray-500">
                            Framework
                        </span>

                        <span class="font-medium">
                            Flask 3.x
                        </span>

                    </div>


                    <div class="flex
                                justify-between">

                        <span class="text-gray-500">
                            Server
                        </span>

                        <span class="font-medium">
                            Gunicorn
                        </span>

                    </div>


                    <div class="flex
                                justify-between">

                        <span class="text-gray-500">
                            Platform
                        </span>

                        <span class="font-medium">
                            AWS EB
                        </span>

                    </div>

                </div>

            </div>

        </div>

    </div>

</main>


<!-- =========================================================
     FOOTER
========================================================== -->

<footer>

    <div class="max-w-7xl mx-auto px-5 lg:px-8 py-5">

        <div class="flex
                    flex-col
                    md:flex-row
                    md:justify-between
                    gap-2
                    text-xs">

            <div>
                SLT-MOBITEL Enterprise IT Systems Portal
            </div>

            <div>
                Flask · Python · Gunicorn · AWS Elastic Beanstalk
            </div>

            <div>
                © 2026 Prasad Wanigasooriya
            </div>

        </div>

    </div>

</footer>


<!-- =========================================================
     LIVE CLOCK
========================================================== -->

<script>

function updateClock() {

    const now = new Date();

    const formatted =
        now.toISOString()
        .replace("T", " ")
        .substring(0, 19);

    document.getElementById(
        "server-time"
    ).textContent = formatted + " UTC";
}

updateClock();

setInterval(
    updateClock,
    1000
);

</script>


</body>
</html>
"""


# ============================================================
# HOME ROUTE
# ============================================================

@application.route("/")
def home():

    current_time = datetime.now(
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
        current_time=current_time,
        github_url=GITHUB_REPO_URL,
        env_name=env_name,
        aws_region=aws_region
    )


# ============================================================
# HEALTH CHECK
# ============================================================

@application.route("/health")
def health_check():

    return jsonify({

        "status": "nominal",

        "application":
            "SLT-MOBITEL IT Systems Dashboard",

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
# APPLICATION START
# ============================================================

if __name__ == "__main__":

    application.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
```
