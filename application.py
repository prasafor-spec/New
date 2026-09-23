<!DOCTYPE html>
<html lang="en" class="h-full bg-slate-950 text-slate-100">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SLT-MOBITEL Enterprise Systems Management</title>
    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    colors: {
                        brand: {
                            red: '#E30613',
                            navy: '#0A192F',
                            deepSlate: '#0F172A',
                            gold: '#FFB800',
                            goldHover: '#E0A200',
                            accentBlue: '#00D2FF',
                            accentGreen: '#10B981',
                        }
                    },
                    fontFamily: {
                        sans: ['Inter', 'sans-serif'],
                        mono: ['JetBrains Mono', 'Fira Code', 'Consolas', 'monospace']
                    }
                }
            }
        }
    </script>
    <!-- Google Fonts & Lucide Icons -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <!-- Chart.js CDN -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    
    <style>
        /* Custom scrollbars and glassmorphic styling */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: rgba(15, 23, 42, 0.6);
        }
        ::-webkit-scrollbar-thumb {
            background: rgba(51, 65, 85, 0.8);
            border-radius: 4px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #E30613;
        }
        .glass-panel {
            background: rgba(15, 23, 42, 0.75);
            backdrop-filter: blur(12px);
            -webkit-backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        .glass-header {
            background: rgba(10, 25, 47, 0.85);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        .glow-red {
            box-shadow: 0 0 15px rgba(227, 6, 19, 0.25);
        }
        .glow-gold {
            box-shadow: 0 0 15px rgba(255, 184, 0, 0.2);
        }
        .terminal-bg {
            background-color: #050B14;
        }
    </style>
</head>
<body class="h-full flex flex-col font-sans antialiased overflow-x-hidden selection:bg-brand-red selection:text-white">

    <!-- Top Glassmorphic Navigation Bar -->
    <header class="glass-header sticky top-0 z-50 h-16 px-4 md:px-6 flex items-center justify-between shrink-0 shadow-lg">
        <div class="flex items-center space-x-4">
            <!-- Mobile Sidebar Toggle Button -->
            <button id="mobileMenuBtn" class="lg:hidden p-2 text-slate-300 hover:text-white rounded-lg hover:bg-slate-800 transition">
                <i data-lucide="menu" class="w-6 h-6"></i>
            </button>
            
            <!-- Corporate Brand Logo & Title -->
            <div class="flex items-center space-x-3">
                <div class="relative flex items-center justify-center w-10 h-10 rounded-xl bg-gradient-to-br from-brand-red to-red-700 text-white font-bold text-lg shadow-md border border-red-500/30">
                    <span class="tracking-tighter">SLT</span>
                    <span class="absolute -bottom-1 -right-1 w-3.5 h-3.5 bg-brand-gold rounded-full border-2 border-slate-950"></span>
                </div>
                <div>
                    <div class="flex items-center space-x-2">
                        <span class="font-extrabold text-lg tracking-tight text-white">SLT<span class="text-brand-red">-MOBITEL</span></span>
                        <span class="text-xs px-2 py-0.5 rounded bg-brand-gold/10 text-brand-gold border border-brand-gold/30 font-mono font-medium hidden sm:inline-block">ENTERPRISE</span>
                    </div>
                    <p class="text-[10px] text-slate-400 font-medium tracking-wider uppercase">Systems Management Platform</p>
                </div>
            </div>
        </div>

        <!-- Global Search Bar -->
        <div class="hidden md:flex items-center flex-1 max-w-md mx-8">
            <div class="relative w-full">
                <i data-lucide="search" class="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-slate-400"></i>
                <input type="text" placeholder="Search servers, IP addresses, cluster nodes, or metrics..." 
                       class="w-full bg-slate-900/80 text-sm text-slate-200 placeholder-slate-500 pl-10 pr-4 py-2 rounded-xl border border-slate-700/60 focus:outline-none focus:border-brand-red focus:ring-1 focus:ring-brand-red transition">
                <kbd class="absolute right-3 top-1/2 -translate-y-1/2 text-[10px] bg-slate-800 text-slate-400 px-1.5 py-0.5 rounded border border-slate-700">⌘K</kbd>
            </div>
        </div>

        <!-- Header Actions & Status Indicators -->
        <div class="flex items-center space-x-3 md:space-x-5">
            <!-- System Status Indicator -->
            <div class="hidden xl:flex items-center space-x-2 px-3 py-1.5 rounded-full bg-slate-900/80 border border-slate-800 text-xs">
                <span class="relative flex h-2.5 w-2.5">
                    <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                    <span class="relative inline-flex rounded-full h-2.5 w-2.5 bg-emerald-500"></span>
                </span>
                <span class="text-slate-300 font-medium">Core Grid Operational</span>
            </div>

            <!-- Live UTC Clock -->
            <div class="hidden sm:flex flex-col items-end border-l border-slate-800 pl-4 font-mono text-xs">
                <span id="liveClock" class="font-semibold text-slate-200">14:25:08 UTC</span>
                <span id="liveDate" class="text-[10px] text-slate-400">23 SEP 2026</span>
            </div>

            <!-- Notification Bell -->
            <button class="relative p-2 text-slate-300 hover:text-white rounded-lg hover:bg-slate-800/80 transition" title="System Notifications">
                <i data-lucide="bell" class="w-5 h-5"></i>
                <span class="absolute top-1.5 right-1.5 w-2 h-2 bg-brand-red rounded-full ring-2 ring-slate-950"></span>
            </button>

            <!-- User Profile Badge -->
            <div class="flex items-center space-x-3 pl-2 sm:pl-3 border-l border-slate-800">
                <div class="relative">
                    <img src="https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=150" 
                         alt="Prasad Wanigasooriya" 
                         class="w-9 h-9 rounded-xl object-cover ring-2 ring-brand-red/50"
                         onerror="this.onerror=null; this.src='https://placehold.co/150x150/0F172A/FFFFFF?text=PW';">
                    <span class="absolute bottom-0 right-0 w-2.5 h-2.5 bg-emerald-500 rounded-full border-2 border-slate-950"></span>
                </div>
                <div class="hidden sm:block text-left">
                    <div class="text-xs font-semibold text-slate-100 leading-tight">Prasad Wanigasooriya</div>
                    <div class="text-[10px] text-brand-gold font-medium">IT & Network Officer</div>
                </div>
            </div>
        </div>
    </header>

    <div class="flex flex-1 overflow-hidden relative">
        <!-- Interactive Sidebar Navigation -->
        <aside id="sidebar" class="fixed inset-y-0 left-0 z-40 w-64 glass-panel border-r border-slate-800/80 transform -translate-x-full lg:translate-x-0 transition-transform duration-300 ease-in-out flex flex-col pt-16 lg:pt-0">
            <!-- Navigation Links -->
            <nav class="flex-1 px-3 py-6 space-y-1 overflow-y-auto">
                <div class="px-3 pb-2 text-[10px] font-bold text-slate-500 uppercase tracking-wider">Main Operations</div>
                
                <a href="#" data-tab="dashboard" class="sidebar-item active flex items-center px-3.5 py-2.5 text-sm font-medium rounded-xl text-white bg-gradient-to-r from-brand-red to-red-700 shadow-md transition group">
                    <i data-lucide="layout-dashboard" class="w-4 h-4 mr-3 text-white"></i>
                    <span>Dashboard</span>
                </a>
                
                <a href="#" data-tab="health" class="sidebar-item flex items-center px-3.5 py-2.5 text-sm font-medium rounded-xl text-slate-400 hover:text-slate-100 hover:bg-slate-800/60 transition group">
                    <i data-lucide="activity" class="w-4 h-4 mr-3 text-slate-400 group-hover:text-brand-gold transition"></i>
                    <span>System Health</span>
                    <span class="ml-auto px-2 py-0.5 text-[10px] rounded-full bg-emerald-500/10 text-emerald-400 font-mono">99.8%</span>
                </a>

                <a href="#" data-tab="servers" class="sidebar-item flex items-center px-3.5 py-2.5 text-sm font-medium rounded-xl text-slate-400 hover:text-slate-100 hover:bg-slate-800/60 transition group">
                    <i data-lucide="server" class="w-4 h-4 mr-3 text-slate-400 group-hover:text-brand-gold transition"></i>
                    <span>Servers Node</span>
                    <span class="ml-auto px-2 py-0.5 text-[10px] rounded-full bg-slate-800 text-slate-300 font-mono">48</span>
                </a>

                <a href="#" data-tab="databases" class="sidebar-item flex items-center px-3.5 py-2.5 text-sm font-medium rounded-xl text-slate-400 hover:text-slate-100 hover:bg-slate-800/60 transition group">
                    <i data-lucide="database" class="w-4 h-4 mr-3 text-slate-400 group-hover:text-brand-gold transition"></i>
                    <span>Databases</span>
                    <span class="ml-auto px-2 py-0.5 text-[10px] rounded-full bg-slate-800 text-slate-300 font-mono">26</span>
                </a>

                <a href="#" data-tab="virtualization" class="sidebar-item flex items-center px-3.5 py-2.5 text-sm font-medium rounded-xl text-slate-400 hover:text-slate-100 hover:bg-slate-800/60 transition group">
                    <i data-lucide="layers" class="w-4 h-4 mr-3 text-slate-400 group-hover:text-brand-gold transition"></i>
                    <span>Virtualization</span>
                    <span class="ml-auto px-2 py-0.5 text-[10px] rounded-full bg-slate-800 text-slate-300 font-mono">124</span>
                </a>

                <a href="#" data-tab="network" class="sidebar-item flex items-center px-3.5 py-2.5 text-sm font-medium rounded-xl text-slate-400 hover:text-slate-100 hover:bg-slate-800/60 transition group">
                    <i data-lucide="network" class="w-4 h-4 mr-3 text-slate-400 group-hover:text-brand-gold transition"></i>
                    <span>Network & Traffic</span>
                </a>

                <div class="pt-4 px-3 pb-2 text-[10px] font-bold text-slate-500 uppercase tracking-wider">Data Protection</div>

                <a href="#" data-tab="backups" class="sidebar-item flex items-center px-3.5 py-2.5 text-sm font-medium rounded-xl text-slate-400 hover:text-slate-100 hover:bg-slate-800/60 transition group">
                    <i data-lucide="hard-drive-download" class="w-4 h-4 mr-3 text-slate-400 group-hover:text-brand-gold transition"></i>
                    <span>Backup Vault</span>
                    <span class="ml-auto w-2 h-2 bg-emerald-500 rounded-full"></span>
                </a>

                <a href="#" data-tab="analytics" class="sidebar-item flex items-center px-3.5 py-2.5 text-sm font-medium rounded-xl text-slate-400 hover:text-slate-100 hover:bg-slate-800/60 transition group">
                    <i data-lucide="bar-chart-3" class="w-4 h-4 mr-3 text-slate-400 group-hover:text-brand-gold transition"></i>
                    <span>Analytics & Reports</span>
                </a>
            </nav>

            <!-- Bottom Infrastructure Quick Summary -->
            <div class="p-4 m-3 rounded-2xl bg-slate-900/90 border border-slate-800/80">
                <div class="flex items-center justify-between mb-2">
                    <span class="text-xs font-medium text-slate-400">AWS Cloud Sync</span>
                    <span class="text-[10px] text-emerald-400 font-mono flex items-center">
                        <i data-lucide="check-circle" class="w-3 h-3 mr-1"></i> Active
                    </span>
                </div>
                <div class="w-full bg-slate-800 rounded-full h-1.5 mb-2 overflow-hidden">
                    <div class="bg-gradient-to-r from-brand-gold to-emerald-400 h-1.5 rounded-full" style="width: 82%"></div>
                </div>
                <div class="flex justify-between text-[10px] text-slate-500 font-mono">
                    <span>Region: ap-south-1</span>
                    <span>82% Alloc</span>
                </div>
            </div>
        </aside>

        <!-- Overlay for Mobile Sidebar -->
        <div id="sidebarOverlay" class="fixed inset-0 bg-slate-950/80 backdrop-blur-sm z-30 hidden lg:hidden"></div>

        <!-- Main Content Area -->
        <main class="flex-1 overflow-y-auto lg:pl-64 p-4 md:p-6 space-y-6">

            <!-- Section Header Banner -->
            <div class="flex flex-col md:flex-row md:items-center justify-between gap-4 glass-panel p-5 rounded-2xl relative overflow-hidden">
                <div class="absolute -right-12 -top-12 w-48 h-48 bg-brand-red/10 rounded-full blur-3xl pointer-events-none"></div>
                <div class="absolute -left-12 -bottom-12 w-48 h-48 bg-brand-gold/10 rounded-full blur-3xl pointer-events-none"></div>
                
                <div class="relative z-10">
                    <div class="flex items-center space-x-2 text-xs font-semibold text-brand-gold tracking-wide uppercase mb-1">
                        <i data-lucide="shield-check" class="w-4 h-4"></i>
                        <span>SLT-MOBITEL Infrastructure Command Center</span>
                    </div>
                    <h1 class="text-2xl md:text-3xl font-extrabold text-white tracking-tight">Enterprise Systems Dashboard</h1>
                    <p class="text-xs md:text-sm text-slate-400 mt-1">Real-time telecommunications infrastructure monitoring, virtualized clusters & database node status.</p>
                </div>

                <div class="flex items-center space-x-3 relative z-10 shrink-0">
                    <button id="btnAutoRefresh" class="flex items-center space-x-2 px-3.5 py-2 rounded-xl bg-slate-900/90 text-slate-300 text-xs font-medium border border-slate-700/80 hover:border-slate-500 hover:text-white transition">
                        <i data-lucide="refresh-cw" class="w-3.5 h-3.5 text-brand-gold animate-spin"></i>
                        <span>Live Syncing</span>
                    </button>
                    <button class="flex items-center space-x-2 px-4 py-2 rounded-xl bg-gradient-to-r from-brand-red to-red-700 text-white text-xs font-semibold shadow-md hover:brightness-110 transition glow-red">
                        <i data-lucide="download" class="w-3.5 h-3.5"></i>
                        <span>System Report</span>
                    </button>
                </div>
            </div>

            <!-- 4 Top Metric KPI Cards -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
                <!-- Card 1: Production Servers -->
                <div class="glass-panel p-5 rounded-2xl hover:border-brand-red/40 transition duration-300 relative group overflow-hidden">
                    <div class="flex items-center justify-between mb-3">
                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Production Servers</span>
                        <div class="p-2 rounded-xl bg-red-500/10 text-brand-red border border-red-500/20 group-hover:scale-110 transition">
                            <i data-lucide="server" class="w-5 h-5"></i>
                        </div>
                    </div>
                    <div class="flex items-baseline space-x-2">
                        <span class="text-3xl font-extrabold text-white font-mono">48</span>
                        <span class="text-xs text-slate-400">Total Nodes</span>
                    </div>
                    <div class="mt-4 flex items-center justify-between text-xs pt-3 border-t border-slate-800">
                        <div class="flex items-center text-emerald-400 font-medium">
                            <i data-lucide="check-circle-2" class="w-3.5 h-3.5 mr-1"></i> 47 Online
                        </div>
                        <div class="flex items-center text-amber-400 font-medium">
                            <i data-lucide="wrench" class="w-3.5 h-3.5 mr-1"></i> 1 Maintenance
                        </div>
                    </div>
                </div>

                <!-- Card 2: Enterprise Databases -->
                <div class="glass-panel p-5 rounded-2xl hover:border-brand-gold/40 transition duration-300 relative group overflow-hidden">
                    <div class="flex items-center justify-between mb-3">
                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Enterprise Databases</span>
                        <div class="p-2 rounded-xl bg-amber-500/10 text-brand-gold border border-amber-500/20 group-hover:scale-110 transition">
                            <i data-lucide="database" class="w-5 h-5"></i>
                        </div>
                    </div>
                    <div class="flex items-baseline space-x-2">
                        <span class="text-3xl font-extrabold text-white font-mono">26</span>
                        <span class="text-xs text-slate-400">Instances</span>
                    </div>
                    <div class="mt-4 flex items-center justify-between text-xs pt-3 border-t border-slate-800">
                        <div class="flex items-center text-emerald-400 font-medium">
                            <i data-lucide="shield-check" class="w-3.5 h-3.5 mr-1"></i> 100% Healthy
                        </div>
                        <div class="text-slate-500 font-mono text-[10px]">Oracle/PostgreSQL</div>
                    </div>
                </div>

                <!-- Card 3: VMware Virtual Machines -->
                <div class="glass-panel p-5 rounded-2xl hover:border-cyan-500/40 transition duration-300 relative group overflow-hidden">
                    <div class="flex items-center justify-between mb-3">
                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">VMware Virtual VMs</span>
                        <div class="p-2 rounded-xl bg-cyan-500/10 text-brand-accentBlue border border-cyan-500/20 group-hover:scale-110 transition">
                            <i data-lucide="cpu" class="w-5 h-5"></i>
                        </div>
                    </div>
                    <div class="flex items-baseline space-x-2">
                        <span class="text-3xl font-extrabold text-white font-mono">124</span>
                        <span class="text-xs text-slate-400">Active Guests</span>
                    </div>
                    <div class="mt-4 flex items-center justify-between text-xs pt-3 border-t border-slate-800">
                        <div class="flex items-center text-emerald-400 font-medium">
                            <i data-lucide="trending-up" class="w-3.5 h-3.5 mr-1"></i> 99.9% Uptime
                        </div>
                        <span class="text-slate-500 font-mono text-[10px]">ESXi 8.0 Update 2</span>
                    </div>
                </div>

                <!-- Card 4: Backup Operations -->
                <div class="glass-panel p-5 rounded-2xl hover:border-emerald-500/40 transition duration-300 relative group overflow-hidden">
                    <div class="flex items-center justify-between mb-3">
                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider">Backup Vault</span>
                        <div class="p-2 rounded-xl bg-emerald-500/10 text-emerald-400 border border-emerald-500/20 group-hover:scale-110 transition">
                            <i data-lucide="hard-drive" class="w-5 h-5"></i>
                        </div>
                    </div>
                    <div class="flex items-baseline space-x-2">
                        <span class="text-3xl font-extrabold text-white font-mono">98.7%</span>
                        <span class="text-xs text-slate-400">Success Rate</span>
                    </div>
                    <div class="mt-4 flex items-center justify-between text-xs pt-3 border-t border-slate-800">
                        <div class="flex items-center text-emerald-400 font-medium">
                            <i data-lucide="clock" class="w-3.5 h-3.5 mr-1"></i> Sync: 12 mins ago
                        </div>
                        <span class="text-slate-500 font-mono text-[10px]">Veeam/AWS S3</span>
                    </div>
                </div>
            </div>

            <!-- Interactive Charts Grid -->
            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                <!-- Chart 1: System Resource Utilization -->
                <div class="glass-panel p-5 rounded-2xl flex flex-col justify-between">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-4">
                        <div>
                            <h3 class="text-base font-bold text-white flex items-center">
                                <i data-lucide="activity" class="w-4 h-4 mr-2 text-brand-red"></i>
                                Resource Utilization Load
                            </h3>
                            <p class="text-xs text-slate-400">Real-time aggregate CPU, Memory & Storage throughput</p>
                        </div>
                        <!-- Controls for Resource Chart -->
                        <div class="flex items-center space-x-1 bg-slate-900 p-1 rounded-xl border border-slate-800 self-start sm:self-auto">
                            <button id="resFilter1H" class="res-btn active text-xs font-medium px-2.5 py-1 rounded-lg bg-brand-red text-white transition">1H</button>
                            <button id="resFilter6H" class="res-btn text-xs font-medium px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition">6H</button>
                            <button id="resFilter24H" class="res-btn text-xs font-medium px-2.5 py-1 rounded-lg text-slate-400 hover:text-white transition">24H</button>
                        </div>
                    </div>
                    
                    <div class="relative h-64 w-full">
                        <canvas id="resourceChart"></canvas>
                    </div>

                    <div class="mt-4 grid grid-cols-3 gap-2 pt-3 border-t border-slate-800/80 text-center">
                        <div class="p-2 rounded-xl bg-slate-900/50">
                            <span class="text-[10px] text-slate-400 block uppercase">CPU Load</span>
                            <span class="text-sm font-bold text-brand-red font-mono">42.8 %</span>
                        </div>
                        <div class="p-2 rounded-xl bg-slate-900/50">
                            <span class="text-[10px] text-slate-400 block uppercase">RAM Allocation</span>
                            <span class="text-sm font-bold text-brand-gold font-mono">68.4 %</span>
                        </div>
                        <div class="p-2 rounded-xl bg-slate-900/50">
                            <span class="text-[10px] text-slate-400 block uppercase">Disk IOPS</span>
                            <span class="text-sm font-bold text-cyan-400 font-mono">1.8k /s</span>
                        </div>
                    </div>
                </div>

                <!-- Chart 2: Network Traffic & Bandwidth Activity -->
                <div class="glass-panel p-5 rounded-2xl flex flex-col justify-between">
                    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 mb-4">
                        <div>
                            <h3 class="text-base font-bold text-white flex items-center">
                                <i data-lucide="arrow-left-right" class="w-4 h-4 mr-2 text-brand-gold"></i>
                                Network Traffic & Throughput
                            </h3>
                            <p class="text-xs text-slate-400">Inbound (In) vs Outbound (Out) Gbps enterprise link</p>
                        </div>
                        <div class="flex items-center space-x-2 text-xs font-mono">
                            <span class="flex items-center text-emerald-400"><span class="w-2.5 h-2.5 rounded-full bg-emerald-500 inline-block mr-1"></span> In: 14.2 Gbps</span>
                            <span class="flex items-center text-cyan-400"><span class="w-2.5 h-2.5 rounded-full bg-cyan-400 inline-block mr-1"></span> Out: 8.7 Gbps</span>
                        </div>
                    </div>

                    <div class="relative h-64 w-full">
                        <canvas id="networkChart"></canvas>
                    </div>

                    <div class="mt-4 grid grid-cols-2 gap-3 pt-3 border-t border-slate-800/80 text-xs">
                        <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900/50">
                            <span class="text-slate-400">Main MPLS Backbone:</span>
                            <span class="text-emerald-400 font-mono font-semibold">Operational (100G)</span>
                        </div>
                        <div class="flex items-center justify-between p-2 rounded-xl bg-slate-900/50">
                            <span class="text-slate-400">Packet Loss Rate:</span>
                            <span class="text-white font-mono font-semibold">0.002%</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Infrastructure Health Breakdown & Environment Details -->
            <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
                <!-- Infrastructure Health Breakdown (Gauges / Progress Bars) -->
                <div class="lg:col-span-2 glass-panel p-5 rounded-2xl space-y-4">
                    <div class="flex items-center justify-between">
                        <div>
                            <h3 class="text-base font-bold text-white flex items-center">
                                <i data-lucide="shield-alert" class="w-4 h-4 mr-2 text-brand-gold"></i>
                                Key Infrastructure Health Breakdown
                            </h3>
                            <p class="text-xs text-slate-400">Cluster degradation, capacity headroom and load stability metrics</p>
                        </div>
                        <span class="px-2.5 py-1 rounded-full bg-emerald-500/10 text-emerald-400 text-xs font-mono border border-emerald-500/20">All Subsystems Green</span>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 pt-2">
                        <!-- vSphere Cluster -->
                        <div class="p-4 rounded-xl bg-slate-900/70 border border-slate-800/80 hover:border-slate-700 transition">
                            <div class="flex justify-between items-center mb-2">
                                <span class="text-xs font-semibold text-slate-200 flex items-center">
                                    <i data-lucide="layers" class="w-3.5 h-3.5 mr-1.5 text-cyan-400"></i>
                                    vSphere Enterprise Cluster
                                </span>
                                <span class="text-xs font-mono text-emerald-400 font-bold">96.4%</span>
                            </div>
                            <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden mb-2">
                                <div class="bg-gradient-to-r from-emerald-500 to-cyan-400 h-2 rounded-full" style="width: 96.4%"></div>
                            </div>
                            <div class="flex justify-between text-[11px] text-slate-400 font-mono">
                                <span>32 ESXi Hosts</span>
                                <span>124 Active VMs</span>
                            </div>
                        </div>

                        <!-- Oracle DB Cluster -->
                        <div class="p-4 rounded-xl bg-slate-900/70 border border-slate-800/80 hover:border-slate-700 transition">
                            <div class="flex justify-between items-center mb-2">
                                <span class="text-xs font-semibold text-slate-200 flex items-center">
                                    <i data-lucide="database" class="w-3.5 h-3.5 mr-1.5 text-brand-gold"></i>
                                    Oracle DB RAC Cluster
                                </span>
                                <span class="text-xs font-mono text-emerald-400 font-bold">99.1%</span>
                            </div>
                            <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden mb-2">
                                <div class="bg-gradient-to-r from-brand-gold to-amber-500 h-2 rounded-full" style="width: 99.1%"></div>
                            </div>
                            <div class="flex justify-between text-[11px] text-slate-400 font-mono">
                                <span>8 Nodes RAC</span>
                                <span>ASM Redundancy High</span>
                            </div>
                        </div>

                        <!-- RHEL Linux Nodes -->
                        <div class="p-4 rounded-xl bg-slate-900/70 border border-slate-800/80 hover:border-slate-700 transition">
                            <div class="flex justify-between items-center mb-2">
                                <span class="text-xs font-semibold text-slate-200 flex items-center">
                                    <i data-lucide="terminal" class="w-3.5 h-3.5 mr-1.5 text-brand-red"></i>
                                    RHEL Enterprise Linux Nodes
                                </span>
                                <span class="text-xs font-mono text-amber-400 font-bold">88.5%</span>
                            </div>
                            <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden mb-2">
                                <div class="bg-gradient-to-r from-brand-red to-orange-400 h-2 rounded-full" style="width: 88.5%"></div>
                            </div>
                            <div class="flex justify-between text-[11px] text-slate-400 font-mono">
                                <span>28 Linux Servers</span>
                                <span>Kernel 5.14.0 High-Load</span>
                            </div>
                        </div>

                        <!-- Windows Domain Controllers -->
                        <div class="p-4 rounded-xl bg-slate-900/70 border border-slate-800/80 hover:border-slate-700 transition">
                            <div class="flex justify-between items-center mb-2">
                                <span class="text-xs font-semibold text-slate-200 flex items-center">
                                    <i data-lucide="shield" class="w-3.5 h-3.5 mr-1.5 text-blue-400"></i>
                                    Windows Active Directory DCs
                                </span>
                                <span class="text-xs font-mono text-emerald-400 font-bold">99.8%</span>
                            </div>
                            <div class="w-full bg-slate-800 rounded-full h-2 overflow-hidden mb-2">
                                <div class="bg-gradient-to-r from-blue-500 to-emerald-400 h-2 rounded-full" style="width: 99.8%"></div>
                            </div>
                            <div class="flex justify-between text-[11px] text-slate-400 font-mono">
                                <span>4 Secondary DCs</span>
                                <span>Sync Delay < 1s</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Environment Details & Quick Actions Card -->
                <div class="glass-panel p-5 rounded-2xl flex flex-col justify-between space-y-4">
                    <div>
                        <div class="flex items-center justify-between mb-3">
                            <h3 class="text-base font-bold text-white flex items-center">
                                <i data-lucide="cloud-cog" class="w-4 h-4 mr-2 text-brand-accentBlue"></i>
                                Environment Config
                            </h3>
                            <span class="px-2 py-0.5 rounded bg-brand-gold/10 text-brand-gold text-[10px] font-mono border border-brand-gold/30">DEBUG MODE</span>
                        </div>

                        <div class="space-y-2.5 text-xs font-mono">
                            <div class="flex justify-between p-2 rounded-lg bg-slate-900/70 border border-slate-800">
                                <span class="text-slate-400">AWS Region</span>
                                <span class="text-white font-semibold">ap-south-1 (Mumbai)</span>
                            </div>
                            <div class="flex justify-between p-2 rounded-lg bg-slate-900/70 border border-slate-800">
                                <span class="text-slate-400">EB Environment</span>
                                <span class="text-brand-gold font-semibold">LOCAL_DEBUG</span>
                            </div>
                            <div class="flex justify-between p-2 rounded-lg bg-slate-900/70 border border-slate-800">
                                <span class="text-slate-400">App Runtime</span>
                                <span class="text-emerald-400 font-semibold">Flask / Gunicorn 21.2</span>
                            </div>
                            <div class="flex justify-between p-2 rounded-lg bg-slate-900/70 border border-slate-800">
                                <span class="text-slate-400">Python Version</span>
                                <span class="text-cyan-400 font-semibold">v3.11.8 Enterprise</span>
                            </div>
                        </div>
                    </div>

                    <!-- Quick Actions Panel -->
                    <div class="pt-4 border-t border-slate-800/80">
                        <span class="text-xs font-semibold text-slate-400 uppercase tracking-wider block mb-2">Quick Commands</span>
                        <div class="grid grid-cols-2 gap-2">
                            <button id="btnHealthCheck" class="flex items-center justify-center space-x-1.5 p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 text-xs font-medium border border-slate-700/60 hover:border-brand-gold transition">
                                <i data-lucide="play-circle" class="w-3.5 h-3.5 text-brand-gold"></i>
                                <span>Health Check</span>
                            </button>
                            <button id="btnRestartService" class="flex items-center justify-center space-x-1.5 p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 text-xs font-medium border border-slate-700/60 hover:border-brand-red transition">
                                <i data-lucide="rotate-ccw" class="w-3.5 h-3.5 text-brand-red"></i>
                                <span>Restart Daemon</span>
                            </button>
                            <button id="btnViewSource" class="flex items-center justify-center space-x-1.5 p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 text-xs font-medium border border-slate-700/60 hover:border-cyan-400 transition">
                                <i data-lucide="code" class="w-3.5 h-3.5 text-cyan-400"></i>
                                <span>View Config</span>
                            </button>
                            <button id="btnExportLogs" class="flex items-center justify-center space-x-1.5 p-2 rounded-xl bg-slate-900 hover:bg-slate-800 text-slate-200 text-xs font-medium border border-slate-700/60 hover:border-emerald-400 transition">
                                <i data-lucide="file-text" class="w-3.5 h-3.5 text-emerald-400"></i>
                                <span>Export Logs</span>
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Real-Time Live Log Terminal -->
            <div class="glass-panel rounded-2xl overflow-hidden border border-slate-800/80 shadow-2xl">
                <!-- Terminal Header Bar -->
                <div class="bg-slate-900/90 px-4 py-3 border-b border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
                    <div class="flex items-center space-x-3">
                        <div class="flex space-x-1.5">
                            <span class="w-3 h-3 rounded-full bg-red-500/80 inline-block"></span>
                            <span class="w-3 h-3 rounded-full bg-yellow-500/80 inline-block"></span>
                            <span class="w-3 h-3 rounded-full bg-green-500/80 inline-block"></span>
                        </div>
                        <div class="flex items-center space-x-2">
                            <i data-lucide="terminal" class="w-4 h-4 text-brand-gold"></i>
                            <span class="text-xs font-mono font-bold text-slate-200">SLT-MOBITEL Infrastructure Live System Audit Log</span>
                        </div>
                    </div>

                    <!-- Terminal Controls -->
                    <div class="flex items-center space-x-2">
                        <div class="relative">
                            <i data-lucide="filter" class="absolute left-2.5 top-1/2 -translate-y-1/2 w-3.5 h-3.5 text-slate-500"></i>
                            <input type="text" id="logFilter" placeholder="Filter logs (e.g. ERROR, DB, SSH)..." 
                                   class="bg-slate-950 text-xs text-slate-200 placeholder-slate-500 pl-8 pr-3 py-1 rounded-lg border border-slate-800 focus:outline-none focus:border-brand-red font-mono w-48 sm:w-64">
                        </div>
                        <button id="btnClearLog" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition" title="Clear Console">
                            <i data-lucide="trash-2" class="w-3.5 h-3.5"></i>
                        </button>
                        <button id="btnTogglePauseLog" class="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition" title="Pause Stream">
                            <i data-lucide="pause" class="w-3.5 h-3.5" id="pauseIcon"></i>
                        </button>
                    </div>
                </div>

                <!-- Terminal Content Window -->
                <div id="terminalWindow" class="terminal-bg p-4 h-64 overflow-y-auto font-mono text-xs space-y-1.5 text-slate-300 selection:bg-brand-red selection:text-white">
                    <div class="text-slate-500 italic pb-1 border-b border-slate-900">// Initialized SLT-MOBITEL Systems Monitor Console - Stream active...</div>
                </div>

                <!-- Terminal Command Line Prompt Footer -->
                <div class="bg-slate-950 px-4 py-2 border-t border-slate-900 flex items-center space-x-2 text-xs font-mono text-slate-400">
                    <span class="text-brand-red font-bold">slt-admin@sysmon:~$</span>
                    <input type="text" id="cmdInput" placeholder="Enter CLI command (e.g., 'help', 'status', 'ping db-cluster', 'clear')..." 
                           class="flex-1 bg-transparent text-slate-200 focus:outline-none placeholder-slate-600">
                    <span class="text-[10px] text-slate-600">Press ENTER to run</span>
                </div>
            </div>

            <!-- Footer -->
            <footer class="pt-4 pb-6 border-t border-slate-800/60 flex flex-col sm:flex-row items-center justify-between text-xs text-slate-500 gap-2">
                <div>
                    © 2026 <span class="font-semibold text-slate-400">SLT-MOBITEL Enterprise Systems</span>. All Rights Reserved.
                </div>
                <div class="flex items-center space-x-4">
                    <a href="#" class="hover:text-slate-300 transition">Security Policy</a>
                    <a href="#" class="hover:text-slate-300 transition">SLA Terms</a>
                    <a href="#" class="hover:text-slate-300 transition">Helpdesk Support</a>
                </div>
            </footer>
        </main>
    </div>

    <!-- Notification Toast Element -->
    <div id="toast" class="fixed bottom-5 right-5 z-50 transform translate-y-20 opacity-0 transition-all duration-300 flex items-center space-x-3 px-4 py-3 rounded-xl bg-slate-900 border border-brand-red/50 text-slate-100 shadow-2xl">
        <i data-lucide="info" id="toastIcon" class="w-5 h-5 text-brand-gold"></i>
        <div class="text-xs">
            <div id="toastTitle" class="font-bold text-white">Notification</div>
            <div id="toastMsg" class="text-slate-300">Action executed successfully.</div>
        </div>
    </div>

    <script>
        // Initialize Lucide Icons
        lucide.createIcons();

        // System State
        let logStreamPaused = false;
        let resourceChartInstance = null;
        let networkChartInstance = null;

        // Clock Update Logic
        function updateClock() {
            const now = new Date();
            const utcString = now.toUTCString().split(' ');
            const timeStr = utcString[4] + ' UTC';
            const dateStr = `${utcString[1]} ${utcString[2].toUpperCase()} ${utcString[3]}`;
            
            document.getElementById('liveClock').textContent = timeStr;
            document.getElementById('liveDate').textContent = dateStr;
        }
        setInterval(updateClock, 1000);
        updateClock();

        // Toast Helper
        function showToast(title, message, type = 'info') {
            const toast = document.getElementById('toast');
            const toastTitle = document.getElementById('toastTitle');
            const toastMsg = document.getElementById('toastMsg');
            const toastIcon = document.getElementById('toastIcon');

            toastTitle.textContent = title;
            toastMsg.textContent = message;

            if (type === 'success') {
                toast.className = toast.className.replace(/border-[^\s]+/, 'border-emerald-500/50');
                toastIcon.setAttribute('data-lucide', 'check-circle-2');
                toastIcon.className = 'w-5 h-5 text-emerald-400';
            } else if (type === 'warning') {
                toast.className = toast.className.replace(/border-[^\s]+/, 'border-amber-500/50');
                toastIcon.setAttribute('data-lucide', 'alert-triangle');
                toastIcon.className = 'w-5 h-5 text-amber-400';
            } else {
                toast.className = toast.className.replace(/border-[^\s]+/, 'border-brand-red/50');
                toastIcon.setAttribute('data-lucide', 'info');
                toastIcon.className = 'w-5 h-5 text-brand-gold';
            }
            lucide.createIcons();

            toast.classList.remove('translate-y-20', 'opacity-0');
            setTimeout(() => {
                toast.classList.add('translate-y-20', 'opacity-0');
            }, 3500);
        }

        // Mobile Sidebar Toggle
        const mobileMenuBtn = document.getElementById('mobileMenuBtn');
        const sidebar = document.getElementById('sidebar');
        const sidebarOverlay = document.getElementById('sidebarOverlay');

        function toggleSidebar() {
            sidebar.classList.toggle('-translate-x-full');
            sidebarOverlay.classList.toggle('hidden');
        }

        mobileMenuBtn.addEventListener('click', toggleSidebar);
        sidebarOverlay.addEventListener('click', toggleSidebar);

        // Sidebar Navigation Active Switch
        const sidebarItems = document.querySelectorAll('.sidebar-item');
        sidebarItems.forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                sidebarItems.forEach(i => {
                    i.classList.remove('active', 'bg-gradient-to-r', 'from-brand-red', 'to-red-700', 'text-white', 'shadow-md');
                    i.classList.add('text-slate-400', 'hover:bg-slate-800/60');
                });
                item.classList.add('active', 'bg-gradient-to-r', 'from-brand-red', 'to-red-700', 'text-white', 'shadow-md');
                item.classList.remove('text-slate-400', 'hover:bg-slate-800/60');

                const tabName = item.getAttribute('data-tab');
                showToast('Tab Switched', `Navigated to ${tabName.toUpperCase()} View`, 'info');

                if (window.innerWidth < 1024) {
                    toggleSidebar();
                }
            });
        });

        // Chart.js Configuration & Instantiation
        function initCharts() {
            // Chart 1: Resource Utilization Area Chart
            const ctxRes = document.getElementById('resourceChart').getContext('2d');
            
            const gradientCpu = ctxRes.createLinearGradient(0, 0, 0, 240);
            gradientCpu.addColorStop(0, 'rgba(227, 6, 19, 0.4)');
            gradientCpu.addColorStop(1, 'rgba(227, 6, 19, 0.0)');

            const gradientRam = ctxRes.createLinearGradient(0, 0, 0, 240);
            gradientRam.addColorStop(0, 'rgba(255, 184, 0, 0.3)');
            gradientRam.addColorStop(1, 'rgba(255, 184, 0, 0.0)');

            resourceChartInstance = new Chart(ctxRes, {
                type: 'line',
                data: {
                    labels: ['14:00', '14:05', '14:10', '14:15', '14:20', '14:25', '14:30'],
                    datasets: [
                        {
                            label: 'CPU Utilization (%)',
                            data: [38, 45, 41, 58, 49, 43, 42],
                            borderColor: '#E30613',
                            backgroundColor: gradientCpu,
                            fill: true,
                            tension: 0.4,
                            borderWidth: 2,
                            pointRadius: 3,
                            pointHoverRadius: 6
                        },
                        {
                            label: 'RAM Allocation (%)',
                            data: [62, 64, 65, 70, 68, 67, 68],
                            borderColor: '#FFB800',
                            backgroundColor: gradientRam,
                            fill: true,
                            tension: 0.4,
                            borderWidth: 2,
                            pointRadius: 3,
                            pointHoverRadius: 6
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top',
                            labels: { color: '#94A3B8', font: { family: 'Inter', size: 11 } }
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                            backgroundColor: '#0F172A',
                            titleColor: '#F8FAFC',
                            bodyColor: '#CBD5E1',
                            borderColor: '#334155',
                            borderWidth: 1
                        }
                    },
                    scales: {
                        x: {
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: { color: '#64748B', font: { family: 'JetBrains Mono', size: 10 } }
                        },
                        y: {
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: { color: '#64748B', font: { family: 'JetBrains Mono', size: 10 } },
                            min: 0,
                            max: 100
                        }
                    }
                }
            });

            // Chart 2: Network Traffic Line Chart
            const ctxNet = document.getElementById('networkChart').getContext('2d');
            networkChartInstance = new Chart(ctxNet, {
                type: 'line',
                data: {
                    labels: ['14:00', '14:05', '14:10', '14:15', '14:20', '14:25', '14:30'],
                    datasets: [
                        {
                            label: 'Inbound (Gbps)',
                            data: [12.1, 13.5, 11.8, 15.2, 14.8, 13.9, 14.2],
                            borderColor: '#10B981',
                            backgroundColor: '#10B981',
                            borderWidth: 2,
                            tension: 0.3,
                            pointRadius: 2
                        },
                        {
                            label: 'Outbound (Gbps)',
                            data: [7.2, 8.1, 8.5, 9.4, 8.9, 8.3, 8.7],
                            borderColor: '#00D2FF',
                            backgroundColor: '#00D2FF',
                            borderWidth: 2,
                            tension: 0.3,
                            pointRadius: 2
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top',
                            labels: { color: '#94A3B8', font: { family: 'Inter', size: 11 } }
                        },
                        tooltip: {
                            mode: 'index',
                            intersect: false,
                            backgroundColor: '#0F172A',
                            borderColor: '#334155',
                            borderWidth: 1
                        }
                    },
                    scales: {
                        x: {
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: { color: '#64748B', font: { family: 'JetBrains Mono', size: 10 } }
                        },
                        y: {
                            grid: { color: 'rgba(255, 255, 255, 0.05)' },
                            ticks: { color: '#64748B', font: { family: 'JetBrains Mono', size: 10 } },
                            min: 0
                        }
                    }
                }
            });
        }

        // Live Dynamic Data Updates for Charts
        setInterval(() => {
            if (resourceChartInstance && networkChartInstance) {
                const now = new Date();
                const timeLabel = `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}`;

                // Push new data points
                resourceChartInstance.data.labels.shift();
                resourceChartInstance.data.labels.push(timeLabel);
                resourceChartInstance.data.datasets[0].data.shift();
                resourceChartInstance.data.datasets[0].data.push(Math.floor(Math.random() * 25) + 35);
                resourceChartInstance.data.datasets[1].data.shift();
                resourceChartInstance.data.datasets[1].data.push(Math.floor(Math.random() * 10) + 62);
                resourceChartInstance.update('none');

                networkChartInstance.data.labels.shift();
                networkChartInstance.data.labels.push(timeLabel);
                networkChartInstance.data.datasets[0].data.shift();
                networkChartInstance.data.datasets[0].data.push((Math.random() * 3 + 12).toFixed(1));
                networkChartInstance.data.datasets[1].data.shift();
                networkChartInstance.data.datasets[1].data.push((Math.random() * 2 + 7.5).toFixed(1));
                networkChartInstance.update('none');
            }
        }, 4000);

        // Chart Filter Buttons Logic
        document.querySelectorAll('.res-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                document.querySelectorAll('.res-btn').forEach(b => {
                    b.classList.remove('bg-brand-red', 'text-white');
                    b.classList.add('text-slate-400');
                });
                btn.classList.add('bg-brand-red', 'text-white');
                btn.classList.remove('text-slate-400');
                showToast('Chart View Updated', `Time range filtered to ${btn.textContent}`, 'info');
            });
        });

        // Real-Time Log Generator Logic
        const terminalWindow = document.getElementById('terminalWindow');
        const sampleLogs = [
            { level: 'INFO', msg: '[AWS-SYNC] ap-south-1 connection verified. Latency: 18ms', color: 'text-slate-300' },
            { level: 'SUCCESS', msg: '[VME-CLUSTER] Heartbeat ping from node esxi-prod-08.slt.lk OK', color: 'text-emerald-400' },
            { level: 'INFO', msg: '[GUNICORN] Worker pid:10425 handled request GET /api/v2/metrics HTTP/1.1 200', color: 'text-cyan-400' },
            { level: 'WARNING', msg: '[ORA-DB] Active sessions query elevated on instance RAC-02 (42/50 conns)', color: 'text-amber-400' },
            { level: 'SUCCESS', msg: '[BACKUP-JOB] Veeam Incremental Snap ID #88411 completed in 41s', color: 'text-emerald-400' },
            { level: 'INFO', msg: '[AUTH-SERVICE] User Prasad Wanigasooriya granted root audit privilege token', color: 'text-brand-gold' },
            { level: 'ERROR', msg: '[MPLS-ROUTE] Transient packet delay on redund-gateway-02. Remapped via primary link.', color: 'text-brand-red font-bold' }
        ];

        function appendLog(logObj) {
            if (logStreamPaused) return;

            const now = new Date();
            const timestamp = now.toISOString().split('T')[1].slice(0, 8);
            
            const logRow = document.createElement('div');
            logRow.className = `flex items-start space-x-2 log-entry`;
            logRow.innerHTML = `
                <span class="text-slate-600 shrink-0">[${timestamp}]</span>
                <span class="px-1 py-0.2 rounded text-[10px] font-bold ${getBadgeClass(logObj.level)}">${logObj.level}</span>
                <span class="${logObj.color} break-all">${logObj.msg}</span>
            `;

            terminalWindow.appendChild(logRow);
            
            // Auto scroll to bottom
            terminalWindow.scrollTop = terminalWindow.scrollHeight;

            // Keep terminal capped at 100 rows
            if (terminalWindow.children.length > 100) {
                terminalWindow.removeChild(terminalWindow.children[1]);
            }
        }

        function getBadgeClass(level) {
            switch(level) {
                case 'ERROR': return 'bg-red-500/20 text-red-400 border border-red-500/30';
                case 'WARNING': return 'bg-yellow-500/20 text-yellow-400 border border-yellow-500/30';
                case 'SUCCESS': return 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30';
                default: return 'bg-blue-500/20 text-blue-400 border border-blue-500/30';
            }
        }

        // Periodically inject realistic logs
        setInterval(() => {
            const randomLog = sampleLogs[Math.floor(Math.random() * sampleLogs.length)];
            appendLog(randomLog);
        }, 2800);

        // Filter Terminal Logs
        document.getElementById('logFilter').addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase();
            const entries = terminalWindow.querySelectorAll('.log-entry');
            entries.forEach(entry => {
                if (entry.textContent.toLowerCase().includes(term)) {
                    entry.style.display = 'flex';
                } else {
                    entry.style.display = 'none';
                }
            });
        });

        // Clear Log Console
        document.getElementById('btnClearLog').addEventListener('click', () => {
            terminalWindow.innerHTML = '<div class="text-slate-500 italic pb-1 border-b border-slate-900">// Log console cleared by operator.</div>';
            showToast('Console Cleared', 'System logs wiped from UI session', 'info');
        });

        // Pause/Resume Log Stream
        const btnTogglePauseLog = document.getElementById('btnTogglePauseLog');
        const pauseIcon = document.getElementById('pauseIcon');
        btnTogglePauseLog.addEventListener('click', () => {
            logStreamPaused = !logStreamPaused;
            if (logStreamPaused) {
                pauseIcon.setAttribute('data-lucide', 'play');
                btnTogglePauseLog.classList.add('bg-brand-gold/20', 'text-brand-gold');
                showToast('Stream Paused', 'Log streaming paused', 'warning');
            } else {
                pauseIcon.setAttribute('data-lucide', 'pause');
                btnTogglePauseLog.classList.remove('bg-brand-gold/20', 'text-brand-gold');
                showToast('Stream Resumed', 'Live log streaming active', 'success');
            }
            lucide.createIcons();
        });

        // CLI Terminal Input Logic
        const cmdInput = document.getElementById('cmdInput');
        cmdInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                const cmd = cmdInput.value.trim();
                if (!cmd) return;

                appendLog({ level: 'CMD', msg: `slt-admin Executed: "${cmd}"`, color: 'text-brand-gold font-bold' });
                
                // Process basic mock commands
                if (cmd.toLowerCase() === 'help') {
                    appendLog({ level: 'INFO', msg: 'Available commands: help, status, ping, clear, restart-daemon', color: 'text-slate-300' });
                } else if (cmd.toLowerCase() === 'status') {
                    appendLog({ level: 'SUCCESS', msg: 'SYSTEM ALL GREEN. 48 Servers Online. RAC DB Healthy.', color: 'text-emerald-400' });
                } else if (cmd.toLowerCase() === 'clear') {
                    document.getElementById('btnClearLog').click();
                } else if (cmd.toLowerCase().startsWith('ping')) {
                    appendLog({ level: 'INFO', msg: `PING ${cmd.split(' ')[1] || 'core-gateway'} (10.128.0.1): 56 data bytes. 64 bytes: icmp_seq=1 ttl=64 time=0.82ms`, color: 'text-cyan-400' });
                } else {
                    appendLog({ level: 'WARNING', msg: `Command not recognized: "${cmd}". Type "help" for options.`, color: 'text-amber-400' });
                }

                cmdInput.value = '';
            }
        });

        // Quick Action Buttons Logic
        document.getElementById('btnHealthCheck').addEventListener('click', () => {
            showToast('Health Diagnostics', 'Running full diagnostics across 48 production servers...', 'info');
            appendLog({ level: 'INFO', msg: '[DIAGNOSTIC] Initiated manual comprehensive health probe across core grid...', color: 'text-brand-gold' });
            setTimeout(() => {
                showToast('Diagnostics Complete', 'All 48 nodes responded with zero fatal errors.', 'success');
                appendLog({ level: 'SUCCESS', msg: '[DIAGNOSTIC] Probing completed: 100% network nodes verified.', color: 'text-emerald-400' });
            }, 2000);
        });

        document.getElementById('btnRestartService').addEventListener('click', () => {
            showToast('Daemon Restart', 'Initiating rolling restart for Flask Gunicorn service...', 'warning');
            appendLog({ level: 'WARNING', msg: '[SERVICE] Rolling restart initiated for Flask / Gunicorn cluster worker group.', color: 'text-amber-400' });
            setTimeout(() => {
                showToast('Service Restarted', 'Gunicorn WSGI cluster workers reloaded successfully.', 'success');
                appendLog({ level: 'SUCCESS', msg: '[SERVICE] Gunicorn WSGI master process reload finished. PID: 10892', color: 'text-emerald-400' });
            }, 1800);
        });

        document.getElementById('btnViewSource').addEventListener('click', () => {
            showToast('Config Active', 'Environment: LOCAL_DEBUG | AWS Region: ap-south-1', 'info');
            appendLog({ level: 'INFO', msg: '[CONFIG] Fetched active runtime environment secrets from Vault.', color: 'text-cyan-400' });
        });

        document.getElementById('btnExportLogs').addEventListener('click', () => {
            showToast('Export Logs', 'Bundled current audit logs into slt_sysmon_audit.log', 'success');
            appendLog({ level: 'SUCCESS', msg: '[EXPORT] Dumped 500 lines to /var/log/slt/audit_export.json', color: 'text-emerald-400' });
        });

        // Initialize Charts on Load
        window.addEventListener('load', () => {
            initCharts();
            // Initializing introductory logs
            setTimeout(() => appendLog({ level: 'SUCCESS', msg: '[INIT] Enterprise Systems Management Platform v4.2 Loaded.', color: 'text-emerald-400' }), 400);
            setTimeout(() => appendLog({ level: 'INFO', msg: '[SECURITY] Authenticated session for Prasad Wanigasooriya.', color: 'text-brand-gold' }), 800);
        });
    </script>
</body>
</html>
