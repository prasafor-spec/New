<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SLT-MOBITEL Enterprise Systems Management</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        slt: {
                            red: '#e30613',
                            blue: '#00529c',
                            dark: '#0f172a',
                            panel: '#1e293b',
                            card: 'rgba(30, 41, 59, 0.7)',
                            accent: '#38bdf8'
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'Fira Code', 'monospace']
                    }
                }
            }
        }
    </script>
    <!-- FontAwesome & Google Fonts -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        /* Glassmorphism styling */
        .glass-panel {
            background: rgba(30, 41, 59, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glass-card {
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(15, 23, 42, 0.5);
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(227, 6, 19, 0.4);
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: rgba(227, 6, 19, 0.8);
        }
        /* Pulse Animation */
        @keyframes pulse-fast {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.3; }
        }
        .animate-pulse-fast {
            animation: pulse-fast 1.2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 font-sans antialiased min-h-screen flex flex-col selection:bg-red-600 selection:text-white">

    <header class="sticky top-0 z-40 bg-slate-900/90 backdrop-blur-md border-b border-slate-800 px-4 lg:px-6 py-2.5">
        <div class="flex flex-col md:flex-row md:items-center justify-between gap-3">
            <!-- Brand Logo & System Title -->
            <div class="flex items-center space-x-3">
                <div class="bg-gradient-to-r from-red-600 to-blue-600 p-2 rounded-lg flex items-center justify-center shadow-lg shadow-red-900/20">
                    <i class="fa-solid me-1 fa-network-wired text-white text-xl"></i>
                </div>
                <div>
                    <div class="flex items-center space-x-2">
                        <span class="text-xs font-bold px-1.5 py-0.5 rounded bg-slt-red text-white uppercase tracking-wider">SLT-MOBITEL</span>
                        <h1 class="text-base font-bold text-slate-100 tracking-tight">Enterprise Systems Operations Hub</h1>
                    </div>
                    <p class="text-xs text-slate-400">IT & Infrastructure Systems Management Division</p>
                </div>
            </div>

            <!-- Clocks & Operational Status Indicator -->
            <div class="flex flex-wrap items-center gap-4 text-xs">
                <!-- Status Badge -->
                <div class="flex items-center space-x-2 bg-slate-800/80 px-3 py-1.5 rounded-full border border-slate-700">
                    <span class="relative flex h-2.5 w-2.5">
                        <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                        <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
                    </span>
                    <span class="font-medium text-emerald-400">Systems Operational</span>
                </div>

                <!-- SLST Clock -->
                <div class="bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700 flex items-center space-x-2">
                    <i class="fa-regular fa-clock text-slt-red"></i>
                    <div>
                        <span class="text-slate-400 font-medium">SLST:</span>
                        <span id="slst-time" class="font-mono text-slate-200 font-semibold ml-1">--:--:--</span>
                    </div>
                </div>

                <!-- UTC Clock -->
                <div class="bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700 flex items-center space-x-2">
                    <i class="fa-solid fa-globe text-slt-blue"></i>
                    <div>
                        <span class="text-slate-400 font-medium">UTC:</span>
                        <span id="utc-time" class="font-mono text-slate-200 font-semibold ml-1">--:--:--</span>
                    </div>
                </div>

                <!-- User Quick Info -->
                <button onclick="toggleProfileModal()" class="flex items-center space-x-2 bg-slate-800 hover:bg-slate-700 px-3 py-1.5 rounded-lg border border-slate-700 transition">
                    <div class="w-5 h-5 rounded-full bg-slt-red flex items-center justify-center text-white font-bold text-[10px]">PW</div>
                    <span class="hidden xl:inline text-slate-200 font-medium">Prasad W.</span>
                    <i class="fa-solid fa-circle-info text-slate-400"></i>
                </button>
            </div>
        </div>

        <!-- Navigation Tabs -->
        <nav class="flex space-x-1 mt-3 border-t border-slate-800/80 pt-2 overflow-x-auto no-scrollbar">
            <button onclick="switchTab('overview')" id="tab-overview" class="tab-btn px-4 py-2 text-xs font-semibold rounded-lg flex items-center space-x-2 bg-slt-red text-white shadow-sm transition">
                <i class="fa-solid fa-chart-line"></i>
                <span>Infrastructure Overview</span>
            </button>
            <button onclick="switchTab('vmware')" id="tab-vmware" class="tab-btn px-4 py-2 text-xs font-semibold rounded-lg flex items-center space-x-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition">
                <i class="fa-solid fa-server"></i>
                <span>VMware Clusters</span>
            </button>
            <button onclick="switchTab('database')" id="tab-database" class="tab-btn px-4 py-2 text-xs font-semibold rounded-lg flex items-center space-x-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition">
                <i class="fa-solid fa-database"></i>
                <span>Database Monitoring</span>
            </button>
            <button onclick="switchTab('health')" id="tab-health" class="tab-btn px-4 py-2 text-xs font-semibold rounded-lg flex items-center space-x-2 text-slate-400 hover:text-slate-200 hover:bg-slate-800/60 transition">
                <i class="fa-solid fa-heart-pulse"></i>
                <span>System Health & Diagnostics</span>
            </button>
        </nav>
    </header>

    <main class="flex-grow p-4 lg:p-6 space-y-6 max-w-[1920px] mx-auto w-full">

        <!-- Top KPI Cards Row -->
        <section class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4">
            <!-- Card 1: Production Servers -->
            <div class="glass-panel p-4 rounded-xl relative overflow-hidden group hover:border-slt-red/50 transition duration-300">
                <div class="absolute -right-3 -bottom-3 text-slate-800/40 text-6xl group-hover:text-slt-red/10 transition">
                    <i class="fa-solid fa-server"></i>
                </div>
                <div class="flex justify-between items-start">
                    <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Production Servers</p>
                    <span class="p-1.5 rounded-lg bg-emerald-500/10 text-emerald-400 text-xs">
                        <i class="fa-solid fa-check-double"></i>
                    </span>
                </div>
                <div class="mt-2 flex items-baseline space-x-2">
                    <h3 class="text-2xl font-bold text-slate-100">48</h3>
                    <span class="text-xs text-emerald-400 font-medium">100% Online</span>
                </div>
                <p class="text-[11px] text-slate-400 mt-1">HQ & Regional Data Hubs</p>
            </div>

            <!-- Card 2: Active Databases -->
            <div class="glass-panel p-4 rounded-xl relative overflow-hidden group hover:border-slt-blue/50 transition duration-300">
                <div class="absolute -right-3 -bottom-3 text-slate-800/40 text-6xl group-hover:text-slt-blue/10 transition">
                    <i class="fa-solid fa-database"></i>
                </div>
                <div class="flex justify-between items-start">
                    <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Active Databases</p>
                    <span class="p-1.5 rounded-lg bg-blue-500/10 text-blue-400 text-xs">
                        <i class="fa-solid fa-bolt"></i>
                    </span>
                </div>
                <div class="mt-2 flex items-baseline space-x-2">
                    <h3 class="text-2xl font-bold text-slate-100">26</h3>
                    <span class="text-xs text-slate-400">Oracle & PostgreSQL</span>
                </div>
                <p class="text-[11px] text-slate-400 mt-1">Avg Latency: <span class="text-slate-200">2.4ms</span></p>
            </div>

            <!-- Card 3: VMware VMs -->
            <div class="glass-panel p-4 rounded-xl relative overflow-hidden group hover:border-cyan-500/50 transition duration-300">
                <div class="absolute -right-3 -bottom-3 text-slate-800/40 text-6xl group-hover:text-cyan-500/10 transition">
                    <i class="fa-solid fa-cubes"></i>
                </div>
                <div class="flex justify-between items-start">
                    <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">VMware VMs</p>
                    <span class="p-1.5 rounded-lg bg-cyan-500/10 text-cyan-400 text-xs">
                        <i class="fa-solid fa-layer-group"></i>
                    </span>
                </div>
                <div class="mt-2 flex items-baseline space-x-2">
                    <h3 class="text-2xl font-bold text-slate-100">124</h3>
                    <span class="text-xs text-cyan-400 font-medium">3 ESXi Clusters</span>
                </div>
                <p class="text-[11px] text-slate-400 mt-1">vSphere 8.0 Enterprise+</p>
            </div>

            <!-- Card 4: Backup Success Rate -->
            <div class="glass-panel p-4 rounded-xl relative overflow-hidden group hover:border-emerald-500/50 transition duration-300">
                <div class="absolute -right-3 -bottom-3 text-slate-800/40 text-6xl group-hover:text-emerald-500/10 transition">
                    <i class="fa-solid fa-shield-halved"></i>
                </div>
                <div class="flex justify-between items-start">
                    <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Backup Success</p>
                    <span class="p-1.5 rounded-lg bg-emerald-500/10 text-emerald-400 text-xs">
                        <i class="fa-solid fa-cloud-arrow-up"></i>
                    </span>
                </div>
                <div class="mt-2 flex items-baseline space-x-2">
                    <h3 class="text-2xl font-bold text-slate-100">98.7%</h3>
                    <span class="text-xs text-emerald-400 font-medium">+0.3% w/w</span>
                </div>
                <p class="text-[11px] text-slate-400 mt-1">Veeam Backup & Replication</p>
            </div>

            <!-- Card 5: Active Incidents -->
            <div class="glass-panel p-4 rounded-xl relative overflow-hidden group hover:border-amber-500/50 transition duration-300">
                <div class="absolute -right-3 -bottom-3 text-slate-800/40 text-6xl group-hover:text-amber-500/10 transition">
                    <i class="fa-solid fa-triangle-exclamation"></i>
                </div>
                <div class="flex justify-between items-start">
                    <p class="text-xs font-medium text-slate-400 uppercase tracking-wider">Active Alerts</p>
                    <span class="p-1.5 rounded-lg bg-amber-500/10 text-amber-400 text-xs">
                        <i class="fa-solid fa-bell"></i>
                    </span>
                </div>
                <div class="mt-2 flex items-baseline space-x-2">
                    <h3 class="text-2xl font-bold text-amber-400">2</h3>
                    <span class="text-xs text-amber-300 font-medium">Low Priority</span>
                </div>
                <p class="text-[11px] text-slate-400 mt-1">0 Critical Issues</p>
            </div>
        </section>

        <div id="view-overview" class="tab-view space-y-6">
            <!-- Dynamic Telemetry Charts Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <!-- CPU & Memory Utilization Real-time Chart -->
                <div class="glass-panel p-5 rounded-xl flex flex-col space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <h2 class="text-sm font-semibold text-slate-100 flex items-center space-x-2">
                                <i class="fa-solid fa-microchip text-slt-red"></i>
                                <span>Cluster CPU & Memory Load</span>
                            </h2>
                            <p class="text-xs text-slate-400">Real-time aggregate consumption across HQ nodes</p>
                        </div>
                        <div class="flex items-center space-x-3 text-xs">
                            <span class="flex items-center space-x-1">
                                <span class="w-3 h-3 rounded-full bg-red-500 inline-block"></span>
                                <span class="text-slate-300">CPU Load</span>
                            </span>
                            <span class="flex items-center space-x-1">
                                <span class="w-3 h-3 rounded-full bg-blue-500 inline-block"></span>
                                <span class="text-slate-300">Memory RAM</span>
                            </span>
                        </div>
                    </div>
                    <div class="h-64 relative">
                        <canvas id="chart-cpu-memory"></canvas>
                    </div>
                </div>

                <!-- Disk I/O & Network Throughput Chart -->
                <div class="glass-panel p-5 rounded-xl flex flex-col space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <h2 class="text-sm font-semibold text-slate-100 flex items-center space-x-2">
                                <i class="fa-solid fa-network-wired text-slt-blue"></i>
                                <span>Network Throughput & Disk IOPS</span>
                            </h2>
                            <p class="text-xs text-slate-400">Core switch traffic and SAN storage throughput</p>
                        </div>
                        <div class="flex items-center space-x-3 text-xs">
                            <span class="flex items-center space-x-1">
                                <span class="w-3 h-3 rounded-full bg-emerald-400 inline-block"></span>
                                <span class="text-slate-300">Network (Gbps)</span>
                            </span>
                            <span class="flex items-center space-x-1">
                                <span class="w-3 h-3 rounded-full bg-purple-400 inline-block"></span>
                                <span class="text-slate-300">Disk IOPS (x100)</span>
                            </span>
                        </div>
                    </div>
                    <div class="h-64 relative">
                        <canvas id="chart-network-disk"></canvas>
                    </div>
                </div>
            </div>

            <!-- Regional Data Center Node Status & Search Filter -->
            <div class="glass-panel p-5 rounded-xl space-y-4">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                    <div>
                        <h2 class="text-sm font-semibold text-slate-100 flex items-center space-x-2">
                            <i class="fa-solid fa-server text-emerald-400"></i>
                            <span>Monitored Regional Infrastructure Nodes</span>
                        </h2>
                        <p class="text-xs text-slate-400">Primary SLT-Mobitel Enterprise Data Hubs</p>
                    </div>

                    <!-- Search & Filter Controls -->
                    <div class="flex items-center space-x-3">
                        <div class="relative">
                            <i class="fa-solid fa-magnifying-glass absolute left-3 top-2.5 text-slate-400 text-xs"></i>
                            <input type="text" id="node-search" onkeyup="filterNodes()" placeholder="Search node or IP..." class="bg-slate-900 text-xs text-slate-200 pl-8 pr-4 py-2 rounded-lg border border-slate-700 focus:outline-none focus:border-slt-red w-48 sm:w-64 transition">
                        </div>
                        <select id="region-filter" onchange="filterNodes()" class="bg-slate-900 text-xs text-slate-200 px-3 py-2 rounded-lg border border-slate-700 focus:outline-none focus:border-slt-red">
                            <option value="ALL">All Hubs</option>
                            <option value="Colombo HQ">Colombo HQ</option>
                            <option value="Kandy">Kandy DC</option>
                            <option value="Badulla">Badulla DC</option>
                        </select>
                    </div>
                </div>

                <!-- Table of Nodes -->
                <div class="overflow-x-auto">
                    <table class="w-full text-left text-xs border-collapse" id="nodes-table">
                        <thead>
                            <tr class="border-b border-slate-800 text-slate-400 uppercase tracking-wider font-semibold">
                                <th class="py-3 px-4">Node / Host ID</th>
                                <th class="py-3 px-4">Location Hub</th>
                                <th class="py-3 px-4">IP Address</th>
                                <th class="py-3 px-4">Role / Service</th>
                                <th class="py-3 px-4">CPU Load</th>
                                <th class="py-3 px-4">RAM Util</th>
                                <th class="py-3 px-4">Status</th>
                                <th class="py-3 px-4 text-right">Actions</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-800/60 font-mono text-slate-300" id="node-table-body">
                            <!-- Dynamic Content Inserted by JS -->
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <div id="view-vmware" class="tab-view hidden space-y-6">
            <div class="glass-panel p-5 rounded-xl space-y-4">
                <div class="flex items-center justify-between">
                    <div>
                        <h2 class="text-sm font-semibold text-slate-100 flex items-center space-x-2">
                            <i class="fa-solid fa-cubes text-cyan-400"></i>
                            <span>VMware vSphere Enterprise Cluster Health</span>
                        </h2>
                        <p class="text-xs text-slate-400">Managed ESXi Hypervisors & High Availability Status</p>
                    </div>
                    <button onclick="triggerQuickAction('VMware Cluster Rescan Initiated')" class="px-3 py-1.5 bg-slate-800 hover:bg-slate-700 text-xs text-slate-200 rounded-lg border border-slate-700 transition">
                        <i class="fa-solid fa-arrows-rotate me-1 text-cyan-400"></i> Rescan Clusters
                    </button>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <!-- Cluster 1 -->
                    <div class="glass-card p-4 rounded-xl border border-slate-800">
                        <div class="flex justify-between items-center mb-2">
                            <span class="font-bold text-slate-200 text-sm">Cluster-HQ-PROD-01</span>
                            <span class="px-2 py-0.5 rounded text-[10px] bg-emerald-500/10 text-emerald-400 font-medium">HA Active</span>
                        </div>
                        <p class="text-xs text-slate-400">Hosts: 8 ESXi 8.0u2 | VMs: 58 Running</p>
                        <div class="mt-4 space-y-2 text-xs">
                            <div>
                                <div class="flex justify-between text-[11px] mb-1">
                                    <span class="text-slate-400">CPU Allocation</span>
                                    <span class="text-slate-200">54% (172 / 320 GHz)</span>
                                </div>
                                <div class="w-full bg-slate-800 rounded-full h-1.5">
                                    <div class="bg-cyan-500 h-1.5 rounded-full" style="width: 54%"></div>
                                </div>
                            </div>
                            <div>
                                <div class="flex justify-between text-[11px] mb-1">
                                    <span class="text-slate-400">Memory Allocation</span>
                                    <span class="text-slate-200">68% (1.38 TB / 2.04 TB)</span>
                                </div>
                                <div class="w-full bg-slate-800 rounded-full h-1.5">
                                    <div class="bg-blue-500 h-1.5 rounded-full" style="width: 68%"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Cluster 2 -->
                    <div class="glass-card p-4 rounded-xl border border-slate-800">
                        <div class="flex justify-between items-center mb-2">
                            <span class="font-bold text-slate-200 text-sm">Cluster-KANDY-DR-02</span>
                            <span class="px-2 py-0.5 rounded text-[10px] bg-emerald-500/10 text-emerald-400 font-medium">DR Standby</span>
                        </div>
                        <p class="text-xs text-slate-400">Hosts: 4 ESXi 8.0u2 | VMs: 42 Standby</p>
                        <div class="mt-4 space-y-2 text-xs">
                            <div>
                                <div class="flex justify-between text-[11px] mb-1">
                                    <span class="text-slate-400">CPU Allocation</span>
                                    <span class="text-slate-200">22% (35 / 160 GHz)</span>
                                </div>
                                <div class="w-full bg-slate-800 rounded-full h-1.5">
                                    <div class="bg-cyan-500 h-1.5 rounded-full" style="width: 22%"></div>
                                </div>
                            </div>
                            <div>
                                <div class="flex justify-between text-[11px] mb-1">
                                    <span class="text-slate-400">Memory Allocation</span>
                                    <span class="text-slate-200">31% (317 GB / 1.02 TB)</span>
                                </div>
                                <div class="w-full bg-slate-800 rounded-full h-1.5">
                                    <div class="bg-blue-500 h-1.5 rounded-full" style="width: 31%"></div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Cluster 3 -->
                    <div class="glass-card p-4 rounded-xl border border-slate-800">
                        <div class="flex justify-between items-center mb-2">
                            <span class="font-bold text-slate-200 text-sm">Cluster-BADULLA-EDGE</span>
                            <span class="px-2 py-0.5 rounded text-[10px] bg-emerald-500/10 text-emerald-400 font-medium">HA Active</span>
                        </div>
                        <p class="text-xs text-slate-400">Hosts: 3 ESXi 7.0u3 | VMs: 24 Running</p>
                        <div class="mt-4 space-y-2 text-xs">
                            <div>
                                <div class="flex justify-between text-[11px] mb-1">
                                    <span class="text-slate-400">CPU Allocation</span>
                                    <span class="text-slate-200">41% (49 / 120 GHz)</span>
                                </div>
                                <div class="w-full bg-slate-800 rounded-full h-1.5">
                                    <div class="bg-cyan-500 h-1.5 rounded-full" style="width: 41%"></div>
                                </div>
                            </div>
                            <div>
                                <div class="flex justify-between text-[11px] mb-1">
                                    <span class="text-slate-400">Memory Allocation</span>
                                    <span class="text-slate-200">49% (250 GB / 512 GB)</span>
                                </div>
                                <div class="w-full bg-slate-800 rounded-full h-1.5">
                                    <div class="bg-blue-500 h-1.5 rounded-full" style="width: 49%"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div id="view-database" class="tab-view hidden space-y-6">
            <div class="glass-panel p-5 rounded-xl space-y-4">
                <div class="flex items-center justify-between">
                    <div>
                        <h2 class="text-sm font-semibold text-slate-100 flex items-center space-x-2">
                            <i class="fa-solid fa-database text-slt-blue"></i>
                            <span>Enterprise Database Instance Monitoring</span>
                        </h2>
                        <p class="text-xs text-slate-400">Oracle RAC, PostgreSQL HA, and MySQL Performance Metrics</p>
                    </div>
                    <span class="text-xs bg-blue-500/10 text-blue-400 border border-blue-500/20 px-3 py-1 rounded-full font-mono">
                        Active Connections: 1,482
                    </span>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 font-mono text-xs">
                    <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="text-slate-100 font-bold">ORACLE-RAC-BILLING</span>
                            <span class="px-2 py-0.5 rounded text-[10px] bg-emerald-500/10 text-emerald-400">HEALTHY</span>
                        </div>
                        <p class="text-slate-400 font-sans text-xs">Primary Customer Billing DB</p>
                        <div class="pt-2 border-t border-slate-800/80 space-y-1 text-[11px] text-slate-300">
                            <div class="flex justify-between"><span>Buffer Cache Hit:</span><span class="text-emerald-400">99.4%</span></div>
                            <div class="flex justify-between"><span>Active Sessions:</span><span>342 / 500</span></div>
                            <div class="flex justify-between"><span>Tablespace Used:</span><span>78.2%</span></div>
                        </div>
                    </div>

                    <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="text-slate-100 font-bold">PG-CRM-PROD-PRIMARY</span>
                            <span class="px-2 py-0.5 rounded text-[10px] bg-emerald-500/10 text-emerald-400">HEALTHY</span>
                        </div>
                        <p class="text-slate-400 font-sans text-xs">Enterprise CRM System</p>
                        <div class="pt-2 border-t border-slate-800/80 space-y-1 text-[11px] text-slate-300">
                            <div class="flex justify-between"><span>Replication Lag:</span><span class="text-emerald-400">0.02ms</span></div>
                            <div class="flex justify-between"><span>Active Connections:</span><span>188 / 300</span></div>
                            <div class="flex justify-between"><span>WAL Storage:</span><span>42.1 GB</span></div>
                        </div>
                    </div>

                    <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="text-slate-100 font-bold">MYSQL-PORTAL-WEB</span>
                            <span class="px-2 py-0.5 rounded text-[10px] bg-emerald-500/10 text-emerald-400">HEALTHY</span>
                        </div>
                        <p class="text-slate-400 font-sans text-xs">SLT Self-Care Web Portal</p>
                        <div class="pt-2 border-t border-slate-800/80 space-y-1 text-[11px] text-slate-300">
                            <div class="flex justify-between"><span>QPS (Queries/Sec):</span><span>1,850</span></div>
                            <div class="flex justify-between"><span>Slow Queries (1h):</span><span class="text-amber-400">2</span></div>
                            <div class="flex justify-between"><span>InnoDB Buffer:</span><span>92%</span></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div id="view-health" class="tab-view hidden space-y-6">
            <div class="glass-panel p-5 rounded-xl space-y-4">
                <div class="flex items-center justify-between">
                    <div>
                        <h2 class="text-sm font-semibold text-slate-100 flex items-center space-x-2">
                            <i class="fa-solid fa-heart-pulse text-slt-red"></i>
                            <span>System Diagnostics & Health Check Suite</span>
                        </h2>
                        <p class="text-xs text-slate-400">Automated integration and system validation suite</p>
                    </div>
                    <button onclick="runHealthCheckModal()" class="px-4 py-2 bg-slt-red hover:bg-red-700 text-white font-semibold text-xs rounded-lg shadow transition flex items-center space-x-2">
                        <i class="fa-solid fa-play"></i>
                        <span>Run Diagnostics Now</span>
                    </button>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                    <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="font-semibold text-slate-200">SAN Storage Array</span>
                            <i class="fa-solid fa-hard-drive text-emerald-400"></i>
                        </div>
                        <p class="text-slate-400">PureStorage FlashArray//X</p>
                        <span class="inline-block px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 text-[10px] font-bold">100% Operational</span>
                    </div>

                    <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="font-semibold text-slate-200">Network Backbone</span>
                            <i class="fa-solid fa-sitemap text-emerald-400"></i>
                        </div>
                        <p class="text-slate-400">Core MPLS & DWDM Rings</p>
                        <span class="inline-block px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 text-[10px] font-bold">Optimal Redundancy</span>
                    </div>

                    <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="font-semibold text-slate-200">Active Directory / LDAP</span>
                            <i class="fa-solid fa-users-gear text-emerald-400"></i>
                        </div>
                        <p class="text-slate-400">HQ Domain Controllers</p>
                        <span class="inline-block px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 text-[10px] font-bold">Sync In-Step</span>
                    </div>

                    <div class="glass-card p-4 rounded-xl border border-slate-800 space-y-2">
                        <div class="flex items-center justify-between">
                            <span class="font-semibold text-slate-200">AWS Hybrid Gateway</span>
                            <i class="fa-brands fa-aws text-emerald-400"></i>
                        </div>
                        <p class="text-slate-400">DirectConnect ap-south-1</p>
                        <span class="inline-block px-2 py-0.5 rounded bg-emerald-500/10 text-emerald-400 text-[10px] font-bold">10 Gbps Active</span>
                    </div>
                </div>
            </div>
        </div>

        <section class="grid grid-cols-1 lg:grid-cols-3 gap-6">
            <!-- Interactive Live System Terminal (2 Cols) -->
            <div class="lg:col-span-2 glass-panel p-5 rounded-xl flex flex-col space-y-3">
                <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800/80 pb-3">
                    <div class="flex items-center space-x-2">
                        <div class="flex space-x-1.5">
                            <span class="w-3 h-3 rounded-full bg-red-500/80 inline-block"></span>
                            <span class="w-3 h-3 rounded-full bg-amber-500/80 inline-block"></span>
                            <span class="w-3 h-3 rounded-full bg-emerald-500/80 inline-block"></span>
                        </div>
                        <span class="text-xs font-mono font-bold text-slate-300 ml-2">sys-admin@slt-mobitel-hq:~ (Live Stream)</span>
                    </div>

                    <!-- Log Filtering & Controls -->
                    <div class="flex items-center space-x-2 text-xs">
                        <select id="log-filter" onchange="filterLogs()" class="bg-slate-900 text-slate-300 px-2.5 py-1 rounded border border-slate-700 text-[11px] focus:outline-none">
                            <option value="ALL">LOG LEVEL: ALL</option>
                            <option value="INFO">INFO ONLY</option>
                            <option value="WARN">WARN ONLY</option>
                            <option value="ERR">ERR ONLY</option>
                        </select>
                        <button id="toggle-feed-btn" onclick="toggleLogPause()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded border border-slate-700 text-[11px] transition">
                            <i class="fa-solid fa-pause me-1"></i> Pause
                        </button>
                        <button onclick="clearTerminalLog()" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 rounded border border-slate-700 text-[11px] transition">
                            <i class="fa-solid fa-trash me-1"></i> Clear
                        </button>
                    </div>
                </div>

                <!-- Live Log Stream Container -->
                <div id="terminal-logs" class="bg-slate-950 font-mono text-[11px] p-3 rounded-lg h-56 overflow-y-auto space-y-1.5 border border-slate-900 text-slate-300 leading-relaxed">
                    <!-- Logs stream dynamic content -->
                </div>

                <!-- Custom Command Input Prompt -->
                <form onsubmit="handleTerminalCommand(event)" class="flex items-center space-x-2 bg-slate-950 px-3 py-1.5 rounded-lg border border-slate-800">
                    <span class="text-slt-red font-mono text-xs font-bold">$</span>
                    <input type="text" id="terminal-input" autocomplete="off" placeholder="Type command ('help', 'ping', 'status', 'health', 'clear')..." class="bg-transparent border-none focus:outline-none font-mono text-xs text-slate-100 flex-grow">
                    <button type="submit" class="text-xs text-slate-400 hover:text-slate-200"><i class="fa-solid fa-paper-plane"></i></button>
                </form>
            </div>

            <!-- Quick Action & Control Panel Column (1 Col) -->
            <div class="glass-panel p-5 rounded-xl flex flex-col justify-between space-y-4">
                <div>
                    <h2 class="text-sm font-semibold text-slate-100 flex items-center space-x-2 mb-1">
                        <i class="fa-solid fa-sliders text-slt-red"></i>
                        <span>Control & Administrative Actions</span>
                    </h2>
                    <p class="text-xs text-slate-400 mb-4">Execute administrative automated routines</p>

                    <div class="space-y-2.5">
                        <button onclick="runHealthCheckModal()" class="w-full text-left px-3.5 py-2.5 rounded-lg bg-slate-800/80 hover:bg-slt-red/20 border border-slate-700/80 hover:border-slt-red/50 text-slate-200 text-xs font-medium transition flex items-center justify-between group">
                            <span class="flex items-center space-x-2.5">
                                <i class="fa-solid fa-heart-pulse text-slt-red group-hover:scale-110 transition"></i>
                                <span>Run Automated System Health Check</span>
                            </span>
                            <i class="fa-solid fa-chevron-right text-slate-500 text-[10px]"></i>
                        </button>

                        <button onclick="triggerQuickAction('On-Demand Snapshot Backup Executed')" class="w-full text-left px-3.5 py-2.5 rounded-lg bg-slate-800/80 hover:bg-blue-600/20 border border-slate-700/80 hover:border-blue-500/50 text-slate-200 text-xs font-medium transition flex items-center justify-between group">
                            <span class="flex items-center space-x-2.5">
                                <i class="fa-solid fa-cloud-arrow-up text-slt-blue group-hover:scale-110 transition"></i>
                                <span>Trigger On-Demand Veeam Backup</span>
                            </span>
                            <i class="fa-solid fa-chevron-right text-slate-500 text-[10px]"></i>
                        </button>

                        <button onclick="triggerQuickAction('Redis & Application Caches Flushed')" class="w-full text-left px-3.5 py-2.5 rounded-lg bg-slate-800/80 hover:bg-amber-600/20 border border-slate-700/80 hover:border-amber-500/50 text-slate-200 text-xs font-medium transition flex items-center justify-between group">
                            <span class="flex items-center space-x-2.5">
                                <i class="fa-solid fa-broom text-amber-400 group-hover:scale-110 transition"></i>
                                <span>Flush Application & Redis Cache</span>
                            </span>
                            <i class="fa-solid fa-chevron-right text-slate-500 text-[10px]"></i>
                        </button>

                        <!-- Export Log Buttons -->
                        <div class="grid grid-cols-2 gap-2 pt-1">
                            <button onclick="exportLogs('json')" class="px-3 py-2 bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-300 text-[11px] rounded-lg transition flex items-center justify-center space-x-1.5">
                                <i class="fa-solid fa-file-code text-cyan-400"></i>
                                <span>Export (JSON)</span>
                            </button>
                            <button onclick="exportLogs('csv')" class="px-3 py-2 bg-slate-900 hover:bg-slate-800 border border-slate-700 text-slate-300 text-[11px] rounded-lg transition flex items-center justify-center space-x-1.5">
                                <i class="fa-solid fa-file-csv text-emerald-400"></i>
                                <span>Export (CSV)</span>
                            </button>
                        </div>
                    </div>
                </div>

                <!-- Environment Runtime Metadata Badge -->
                <div class="p-3 bg-slate-900/90 rounded-lg border border-slate-800 text-[11px] text-slate-400 space-y-1">
                    <div class="flex justify-between">
                        <span>AWS Region:</span>
                        <span class="font-mono text-slate-200">ap-south-1 (Mumbai)</span>
                    </div>
                    <div class="flex justify-between"><span>Deployment Engine:</span><span class="font-mono text-slate-200">Elastic Beanstalk</span></div>
                    <div class="flex justify-between"><span>Runtime Architecture:</span><span class="font-mono text-slate-200">Flask / Gunicorn 21.2</span></div>
                </div>
            </div>
        </section>
    </main>

    <footer class="border-t border-slate-800/80 bg-slate-950 py-3 px-6 text-xs text-slate-400 flex flex-col sm:flex-row items-center justify-between gap-2 mt-auto">
        <p>© 2026 Sri Lanka Telecom PLC - Systems Management & Operations. All Rights Reserved.</p>
        <div class="flex items-center space-x-4">
            <span class="text-slate-400">SLT-Mobitel IT Headquarters - Colombo 01</span>
            <span class="w-1.5 h-1.5 rounded-full bg-slate-700"></span>
            <span class="text-slate-400">v4.8.2-Enterprise</span>
        </div>
    </footer>

    <!-- Modal 1: Prasad Wanigasooriya Profile Modal -->
    <div id="modal-profile" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="glass-panel max-w-md w-full p-6 rounded-2xl border border-slate-700 shadow-2xl relative space-y-4">
            <button onclick="toggleProfileModal()" class="absolute top-4 right-4 text-slate-400 hover:text-slate-200 text-base">
                <i class="fa-solid fa-xmark"></i>
            </button>

            <div class="flex items-center space-x-4">
                <div class="w-14 h-14 rounded-full bg-gradient-to-tr from-slt-red to-slt-blue flex items-center justify-center text-white font-bold text-xl shadow-lg">
                    PW
                </div>
                <div>
                    <h3 class="text-lg font-bold text-slate-100">Prasad Wanigasooriya</h3>
                    <p class="text-xs text-slt-red font-semibold">IT & Network Officer - Systems Section</p>
                    <p class="text-xs text-slate-400">SLT-Mobitel HQ, Colombo 01</p>
                </div>
            </div>

            <div class="border-t border-slate-800 pt-3 space-y-2 text-xs">
                <div class="flex justify-between py-1 border-b border-slate-800/50">
                    <span class="text-slate-400">Department:</span>
                    <span class="text-slate-200 font-medium">Enterprise Infrastructure Operations</span>
                </div>
                <div class="flex justify-between py-1 border-b border-slate-800/50">
                    <span class="text-slate-400">Access Level:</span>
                    <span class="text-emerald-400 font-medium font-mono">Tier-3 System Administrator</span>
                </div>
                <div class="flex justify-between py-1 border-b border-slate-800/50">
                    <span class="text-slate-400">Shift Status:</span>
                    <span class="text-slate-200 font-medium">On-Duty (Primary Systems Lead)</span>
                </div>
                <div class="flex justify-between py-1">
                    <span class="text-slate-400">Active Session:</span>
                    <span class="text-slate-200 font-mono">192.168.10.42 (Encrypted SSL)</span>
                </div>
            </div>

            <button onclick="toggleProfileModal()" class="w-full py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold rounded-lg transition">
                Close
            </button>
        </div>
    </div>

    <!-- Modal 2: System Health Diagnostic Report Dialog -->
    <div id="modal-health" class="fixed inset-0 bg-slate-950/85 backdrop-blur-sm z-50 hidden flex items-center justify-center p-4">
        <div class="glass-panel max-w-xl w-full p-6 rounded-2xl border border-slate-700 shadow-2xl space-y-4">
            <div class="flex items-center justify-between border-b border-slate-800 pb-3">
                <div class="flex items-center space-x-2">
                    <i class="fa-solid fa-heart-pulse text-slt-red text-lg"></i>
                    <h3 class="text-base font-bold text-slate-100">SLT-Mobitel Infrastructure Diagnostic Report</h3>
                </div>
                <button onclick="closeHealthModal()" class="text-slate-400 hover:text-slate-200">
                    <i class="fa-solid fa-xmark"></i>
                </button>
            </div>

            <!-- Health Test Progress / Results Container -->
            <div id="health-check-results" class="space-y-3 font-mono text-xs max-h-80 overflow-y-auto pr-1">
                <!-- Dynamically populated test suite items -->
            </div>

            <div class="flex justify-between items-center pt-3 border-t border-slate-800">
                <span id="health-status-summary" class="text-xs text-slate-400">Diagnostic scan completed.</span>
                <button onclick="closeHealthModal()" class="px-4 py-2 bg-slt-red hover:bg-red-700 text-white text-xs font-semibold rounded-lg transition">
                    Acknowledge & Dismiss
                </button>
            </div>
        </div>
    </div>

    <script>
        // Global Datasets & State Variables
        const nodeData = [
            { id: "HQ-DC-SRV01", location: "Colombo HQ", ip: "10.100.4.12", role: "Primary Domain Controller", cpu: 32, ram: 48, status: "ONLINE" },
            { id: "HQ-DC-SRV02", location: "Colombo HQ", ip: "10.100.4.13", role: "Oracle RAC Node 1", cpu: 64, ram: 78, status: "ONLINE" },
            { id: "HQ-DC-SRV03", location: "Colombo HQ", ip: "10.100.4.14", role: "Veeam Backup Server", cpu: 18, ram: 35, status: "ONLINE" },
            { id: "KND-DC-SRV01", location: "Kandy", ip: "10.200.2.10", role: "Disaster Recovery Node", cpu: 28, ram: 42, status: "ONLINE" },
            { id: "KND-DC-SRV02", location: "Kandy", ip: "10.200.2.11", role: "PostgreSQL Replica", cpu: 45, ram: 60, status: "ONLINE" },
            { id: "BDL-DC-SRV01", location: "Badulla", ip: "10.300.1.05", role: "Edge Gateways & DNS", cpu: 22, ram: 38, status: "ONLINE" },
            { id: "BDL-DC-SRV02", location: "Badulla", ip: "10.300.1.06", role: "Regional Cache Proxy", cpu: 39, ram: 52, status: "ONLINE" }
        ];

        let logsList = [];
        let isLogPaused = false;
        let cpuMemoryChart, networkDiskChart;

        // Initialize Clocks, Tables, Charts, and Logs on Window Load
        window.onload = function () {
            startRealTimeClocks();
            renderNodeTable(nodeData);
            initCharts();
            seedInitialTerminalLogs();
            startLiveLogStream();
            startTelemetryUpdates();
        };

        function startRealTimeClocks() {
            function updateClocks() {
                const now = new Date();
                
                // UTC Time
                const utcStr = now.toISOString().substring(11, 19);
                document.getElementById('utc-time').innerText = utcStr;

                // SLST (Asia/Colombo UTC+5:30)
                const slstFormatter = new Intl.DateTimeFormat('en-GB', {
                    timeZone: 'Asia/Colombo',
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit',
                    hour12: false
                });
                document.getElementById('slst-time').innerText = slstFormatter.format(now);
            }
            updateClocks();
            setInterval(updateClocks, 1000);
        }

        function switchTab(tabKey) {
            document.querySelectorAll('.tab-view').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(btn => {
                btn.classList.remove('bg-slt-red', 'text-white', 'shadow-sm');
                btn.classList.add('text-slate-400', 'hover:text-slate-200', 'hover:bg-slate-800/60');
            });

            document.getElementById(`view-${tabKey}`).classList.remove('hidden');
            const activeBtn = document.getElementById(`tab-${tabKey}`);
            activeBtn.classList.remove('text-slate-400', 'hover:text-slate-200', 'hover:bg-slate-800/60');
            activeBtn.classList.add('bg-slt-red', 'text-white', 'shadow-sm');
        }

        function renderNodeTable(nodes) {
            const tbody = document.getElementById('node-table-body');
            tbody.innerHTML = '';

            nodes.forEach(node => {
                const tr = document.createElement('tr');
                tr.className = "hover:bg-slate-800/40 transition border-b border-slate-800/40";
                
                let cpuColor = node.cpu > 75 ? 'text-red-400' : 'text-slate-200';
                let ramColor = node.ram > 75 ? 'text-red-400' : 'text-slate-200';

                tr.innerHTML = `
                    <td class="py-3 px-4 font-bold text-slate-100">${node.id}</td>
                    <td class="py-3 px-4 text-slate-300 font-sans">${node.location}</td>
                    <td class="py-3 px-4 text-slate-400">${node.ip}</td>
                    <td class="py-3 px-4 text-slate-300 font-sans">${node.role}</td>
                    <td class="py-3 px-4 ${cpuColor}">${node.cpu}%</td>
                    <td class="py-3 px-4 ${ramColor}">${node.ram}%</td>
                    <td class="py-3 px-4">
                        <span class="px-2 py-0.5 rounded text-[10px] font-sans font-bold bg-emerald-500/10 text-emerald-400 border border-emerald-500/20">
                            ${node.status}
                        </span>
                    </td>
                    <td class="py-3 px-4 text-right font-sans">
                        <button onclick="pingSingleNode('${node.id}', '${node.ip}')" class="px-2 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 text-[11px] rounded transition">
                            <i class="fa-solid fa-terminal me-1 text-xs"></i> Ping
                        </button>
                    </td>
                `;
                tbody.appendChild(tr);
            });
        }

        function filterNodes() {
            const query = document.getElementById('node-search').value.toLowerCase();
            const region = document.getElementById('region-filter').value;

            const filtered = nodeData.filter(node => {
                const matchesSearch = node.id.toLowerCase().includes(query) || node.ip.includes(query) || node.role.toLowerCase().includes(query);
                const matchesRegion = (region === 'ALL') || node.location === region;
                return matchesSearch && matchesRegion;
            });

            renderNodeTable(filtered);
        }

        function initCharts() {
            const timeLabels = ['13:35', '13:36', '13:37', '13:38', '13:39', '13:40', '13:41', '13:42'];

            // Chart 1: CPU & Memory
            const ctx1 = document.getElementById('chart-cpu-memory').getContext('2d');
            cpuMemoryChart = new Chart(ctx1, {
                type: 'line',
                data: {
                    labels: timeLabels,
                    datasets: [
                        {
                            label: 'CPU Load (%)',
                            data: [42, 45, 48, 52, 49, 44, 47, 43],
                            borderColor: '#e30613',
                            backgroundColor: 'rgba(227, 6, 19, 0.1)',
                            fill: true,
                            tension: 0.4
                        },
                        {
                            label: 'RAM Load (%)',
                            data: [61, 62, 60, 63, 65, 64, 62, 63],
                            borderColor: '#3b82f6',
                            backgroundColor: 'rgba(59, 130, 246, 0.05)',
                            fill: true,
                            tension: 0.4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#94a3b8' } },
                        y: { min: 0, max: 100, grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#94a3b8' } }
                    }
                }
            });

            // Chart 2: Network & Disk
            const ctx2 = document.getElementById('chart-network-disk').getContext('2d');
            networkDiskChart = new Chart(ctx2, {
                type: 'line',
                data: {
                    labels: timeLabels,
                    datasets: [
                        {
                            label: 'Network (Gbps)',
                            data: [3.2, 3.8, 4.1, 3.9, 4.5, 4.2, 3.7, 4.0],
                            borderColor: '#34d399',
                            tension: 0.4
                        },
                        {
                            label: 'Disk IOPS (x100)',
                            data: [28, 31, 35, 30, 29, 34, 38, 32],
                            borderColor: '#c084fc',
                            tension: 0.4
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        x: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#94a3b8' } },
                        y: { grid: { color: 'rgba(255, 255, 255, 0.05)' }, ticks: { color: '#94a3b8' } }
                    }
                }
            });
        }

        function startTelemetryUpdates() {
            setInterval(() => {
                if (!cpuMemoryChart || !networkDiskChart) return;

                const now = new Date();
                const timeStr = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}`;

                // Update CPU Chart
                cpuMemoryChart.data.labels.shift();
                cpuMemoryChart.data.labels.push(timeStr);
                
                const nextCpu = Math.floor(38 + Math.random() * 20);
                const nextRam = Math.floor(60 + Math.random() * 8);

                cpuMemoryChart.data.datasets[0].data.shift();
                cpuMemoryChart.data.datasets[0].data.push(nextCpu);
                cpuMemoryChart.data.datasets[1].data.shift();
                cpuMemoryChart.data.datasets[1].data.push(nextRam);
                cpuMemoryChart.update('none');

                // Update Network Chart
                networkDiskChart.data.labels.shift();
                networkDiskChart.data.labels.push(timeStr);

                const nextNet = +(3.5 + Math.random() * 1.2).toFixed(2);
                const nextIops = Math.floor(25 + Math.random() * 15);

                networkDiskChart.data.datasets[0].data.shift();
                networkDiskChart.data.datasets[0].data.push(nextNet);
                networkDiskChart.data.datasets[1].data.shift();
                networkDiskChart.data.datasets[1].data.push(nextIops);
                networkDiskChart.update('none');
            }, 3000);
        }

        function seedInitialTerminalLogs() {
            const initial = [
                { time: getFormattedTime(), level: "INFO", msg: "SLT-Mobitel Enterprise Core Hub monitoring initialized." },
                { time: getFormattedTime(), level: "INFO", msg: "Connected to VMware vSphere vCenter (v8.0u2) - 3 Clusters Online." },
                { time: getFormattedTime(), level: "WARN", msg: "High read query volume detected on ORACLE-RAC-BILLING." },
                { time: getFormattedTime(), level: "INFO", msg: "Automatic Veeam snapshot completed for HQ-DC-SRV01 [100% OK]." }
            ];
            logsList = initial;
            renderLogs();
        }

        function getFormattedTime() {
            const d = new Date();
            return d.toTimeString().split(' ')[0];
        }

        function appendLog(level, msg) {
            const entry = { time: getFormattedTime(), level, msg };
            logsList.push(entry);
            if (logsList.length > 80) logsList.shift();
            renderLogs();
        }

        function renderLogs() {
            const container = document.getElementById('terminal-logs');
            const filter = document.getElementById('log-filter').value;
            container.innerHTML = '';

            const filtered = logsList.filter(l => filter === 'ALL' || l.level === filter);

            filtered.forEach(item => {
                let badgeColor = "text-blue-400";
                if (item.level === "WARN") badgeColor = "text-amber-400 font-bold";
                if (item.level === "ERR") badgeColor = "text-red-500 font-bold";

                const div = document.createElement('div');
                div.className = "flex items-start space-x-2";
                div.innerHTML = `
                    <span class="text-slate-500">[${item.time}]</span>
                    <span class="${badgeColor}">[${item.level}]</span>
                    <span class="text-slate-200 flex-grow">${item.msg}</span>
                `;
                container.appendChild(div);
            });

            if (!isLogPaused) {
                container.scrollTop = container.scrollHeight;
            }
        }

        function startLiveLogStream() {
            const sampleLogs = [
                { level: "INFO", msg: "BGP Route advertisement refresh - Core Ring Colombo HQ." },
                { level: "INFO", msg: "PostgreSQL WAL Archive sync completed successfully." },
                { level: "WARN", msg: "Transient jitter detected on Badulla DC MPLS link (12ms)." },
                { level: "INFO", msg: "Active Directory Domain Controller replication heartbeat verified." },
                { level: "INFO", msg: "AWS DirectConnect gateway health check ping: 2.1ms." }
            ];

            setInterval(() => {
                if (!isLogPaused && Math.random() > 0.4) {
                    const randomItem = sampleLogs[Math.floor(Math.random() * sampleLogs.length)];
                    appendLog(randomItem.level, randomItem.msg);
                }
            }, 4500);
        }

        function toggleLogPause() {
            isLogPaused = !isLogPaused;
            const btn = document.getElementById('toggle-feed-btn');
            if (isLogPaused) {
                btn.innerHTML = `<i class="fa-solid fa-play me-1"></i> Resume`;
                btn.classList.add('bg-slt-red/30', 'text-slt-red');
            } else {
                btn.innerHTML = `<i class="fa-solid fa-pause me-1"></i> Pause`;
                btn.classList.remove('bg-slt-red/30', 'text-slt-red');
            }
        }

        function filterLogs() {
            renderLogs();
        }

        function clearTerminalLog() {
            logsList = [];
            renderLogs();
        }

        function handleTerminalCommand(e) {
            e.preventDefault();
            const input = document.getElementById('terminal-input');
            const cmd = input.value.trim().toLowerCase();
            if (!cmd) return;

            appendLog("INFO", `Executing prompt: ${cmd}`);
            input.value = '';

            setTimeout(() => {
                if (cmd === 'help') {
                    appendLog("INFO", "Available commands: 'ping [host]', 'status', 'health', 'clear', 'help'");
                } else if (cmd.startsWith('ping')) {
                    appendLog("INFO", "PING 10.100.4.12 (HQ-DC-SRV01) 56(84) bytes of data.");
                    appendLog("INFO", "64 bytes from 10.100.4.12: icmp_seq=1 ttl=64 time=0.82 ms");
                    appendLog("INFO", "64 bytes from 10.100.4.12: icmp_seq=2 ttl=64 time=0.74 ms");
                } else if (cmd === 'status') {
                    appendLog("INFO", "SYSTEM STATUS: All 48 Core Servers, 3 VMware Clusters, and 26 DBs fully functional.");
                } else if (cmd === 'health') {
                    runHealthCheckModal();
                } else if (cmd === 'clear') {
                    clearTerminalLog();
                } else {
                    appendLog("ERR", `Command not recognized: '${cmd}'. Type 'help' for options.`);
                }
            }, 300);
        }

        function pingSingleNode(nodeId, ip) {
            appendLog("INFO", `Initiating direct ping diagnostic to ${nodeId} (${ip})...`);
            setTimeout(() => {
                appendLog("INFO", `Reply from ${ip}: bytes=32 time=0.9ms TTL=128 - Status HEALTHY`);
            }, 400);
        }

        function triggerQuickAction(actionName) {
            appendLog("INFO", `Quick Action Initiated: ${actionName}`);
            setTimeout(() => {
                appendLog("INFO", `Quick Action Completed: ${actionName} [SUCCESS]`);
            }, 1000);
        }

        function exportLogs(format) {
            if (logsList.length === 0) {
                alert("No logs available to export.");
                return;
            }

            let dataStr = "";
            let fileName = `slt_mobitel_system_logs_${Date.now()}.${format}`;

            if (format === 'json') {
                dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(logsList, null, 2));
            } else {
                let csv = "Timestamp,Level,Message\n";
                logsList.forEach(l => {
                    csv += `"${l.time}","${l.level}","${l.msg.replace(/"/g, '""')}"\n`;
                });
                dataStr = "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
            }

            const downloadAnchor = document.createElement('a');
            downloadAnchor.setAttribute("href", dataStr);
            downloadAnchor.setAttribute("download", fileName);
            document.body.appendChild(downloadAnchor);
            downloadAnchor.click();
            downloadAnchor.remove();

            appendLog("INFO", `System logs exported successfully as ${format.toUpperCase()}`);
        }

        function toggleProfileModal() {
            const modal = document.getElementById('modal-profile');
            modal.classList.toggle('hidden');
        }

        function runHealthCheckModal() {
            const modal = document.getElementById('modal-health');
            const resultsContainer = document.getElementById('health-check-results');
            const summaryText = document.getElementById('health-status-summary');

            resultsContainer.innerHTML = '';
            summaryText.innerText = "Running comprehensive infrastructure diagnostics...";
            modal.classList.remove('hidden');

            const tests = [
                "1. Ping Core MPLS Gateway (10.100.0.1)",
                "2. Check Oracle RAC Billing Connectivity & Latency",
                "3. Verify VMware vSphere ESXi Cluster HA Heartbeats",
                "4. Storage Multipath I/O Health Scan (SAN Array)",
                "5. AWS DirectConnect Hybrid Link Integrity Test",
                "6. Veeam Backup Replication Repository Status Check"
            ];

            let index = 0;
            const interval = setInterval(() => {
                if (index < tests.length) {
                    const div = document.createElement('div');
                    div.className = "flex justify-between items-center bg-slate-900/80 p-2.5 rounded border border-slate-800";
                    div.innerHTML = `
                        <span class="text-slate-300">${tests[index]}</span>
                        <span class="text-emerald-400 font-bold flex items-center space-x-1">
                            <i class="fa-solid fa-circle-check"></i>
                            <span>PASSED</span>
                        </span>
                    `;
                    resultsContainer.appendChild(div);
                    resultsContainer.scrollTop = resultsContainer.scrollHeight;
                    index++;
                } else {
                    clearInterval(interval);
                    summaryText.innerText = "All 6 Diagnostic Tests PASSED - Systems 100% Operational.";
                    appendLog("INFO", "Full System Health Check Diagnostics completed without error.");
                }
            }, 400);
        }

        function closeHealthModal() {
            document.getElementById('modal-health').classList.add('hidden');
        }
    </script>
</body>
</html>
