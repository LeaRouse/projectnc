<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cosmic Dashboard</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/feather-icons"></script>
    <script src="https://cdn.jsdelivr.net/npm/feather-icons/dist/feather.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vanta@latest/dist/vanta.globe.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&display=swap');
        
        body {
            font-family: 'Space Grotesk', sans-serif;
            overflow-x: hidden;
        }
        
        .vanta-bg {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -1;
            pointer-events: none;
        }
        
        .bg-overlay {
            background: rgba(0, 0, 0, 0.6);
        }
        
        .nav-button {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        .nav-button:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
            border-color: rgba(255, 255, 255, 0.3);
        }
        
        .icon-container {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 100%;
        }
        
        .icon-container i {
            width: 60%;
            height: 60%;
        }
        
        .content-section {
            animation: fadeIn 0.8s ease-out forwards;
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body class="text-gray-100">
    <!-- Vanta.js Background -->
    <div id="vanta-bg" class="vanta-bg"></div>
    <div class="bg-overlay fixed inset-0 z-0"></div>

    <!-- Main Content -->
    <div class="min-h-screen flex">
        <!-- Left Navigation -->
        <div class="fixed left-0 top-0 h-full w-64 p-4 flex flex-col space-y-6 z-10">
            <div id="btn-home" class="nav-button bg-gray-800/70 rounded-xl h-48 flex flex-col items-center justify-center cursor-pointer">
                <div class="icon-container">
                    <i data-feather="home"></i>
                </div>
                <span class="mt-4 text-xl font-medium">Home</span>
            </div>
            
            <div id="btn-craft" class="nav-button bg-gray-800/70 rounded-xl h-48 flex flex-col items-center justify-center cursor-pointer">
                <div class="icon-container">
                    <i data-feather="tool"></i>
                </div>
                <span class="mt-4 text-xl font-medium">Craft</span>
            </div>
            
            <div id="btn-mat" class="nav-button bg-gray-800/70 rounded-xl h-48 flex flex-col items-center justify-center cursor-pointer">
                <div class="icon-container">
                    <i data-feather="box"></i>
                </div>
                <span class="mt-4 text-xl font-medium">Materials</span>
            </div>
        </div>

        <!-- Right Navigation -->
        <div class="fixed right-0 top-0 h-full p-4 flex flex-col space-y-6 items-end z-10">
            <div id="btn-spec" class="nav-button bg-gray-800/70 rounded-full w-20 h-20 flex items-center justify-center cursor-pointer">
                <i data-feather="settings"></i>
            </div>
            
            <div id="btn-config" class="nav-button bg-gray-800/70 rounded-full w-20 h-20 flex items-center justify-center cursor-pointer mt-auto mb-6">
                <i data-feather="sliders"></i>
            </div>
        </div>

        <!-- Page Content -->
        <div class="flex-1 ml-64 p-8">
            <!-- Home Content (Default) -->
            <div id="home-content" class="content-section">
                <div class="flex flex-col items-center justify-center min-h-screen">
                    <h1 class="text-7xl font-bold mb-8 text-center bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-purple-600">
                        AstroCycle
                    </h1>
                    <div class="max-w-2xl">
                        <img src="http://static.photos/technology/1024x576/42" alt="Logo" class="rounded-xl shadow-2xl border border-gray-700/50">
                    </div>
                </div>
            </div>

            <!-- Craft Content (Hidden by default) -->
            <div id="craft-content" class="content-section hidden">
                <div class="py-12">
                    <h2 class="text-4xl font-bold mb-8 flex items-center">
                        <i data-feather="tool" class="mr-4"></i> Craft Zone
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700/50">
                            <h3 class="text-2xl font-semibold mb-4">Prototype Builder</h3>
                            <p class="text-gray-300 mb-6">Interactive interface for constructing your space prototype with real-time feedback.</p>
                            <button class="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-lg transition-all">
                                Start Building
                            </button>
                        </div>
                        <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700/50">
                            <h3 class="text-2xl font-semibold mb-4">Component Library</h3>
                            <p class="text-gray-300 mb-6">Browse through our collection of space-grade components and materials.</p>
                            <button class="bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg transition-all">
                                Explore Components
                            </button>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Materials Content (Hidden by default) -->
            <div id="materials-content" class="content-section hidden">
                <div class="py-12">
                    <h2 class="text-4xl font-bold mb-8 flex items-center">
                        <i data-feather="box" class="mr-4"></i> Materials Inventory
                    </h2>
                    <div class="overflow-x-auto">
                        <table class="w-full bg-gray-800/50 rounded-xl overflow-hidden border border-gray-700/50">
                            <thead class="bg-gray-700/50">
                                <tr>
                                    <th class="py-4 px-6 text-left">Material</th>
                                    <th class="py-4 px-6 text-left">Quantity</th>
                                    <th class="py-4 px-6 text-left">Status</th>
                                    <th class="py-4 px-6 text-left">Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-700/30 hover:bg-gray-700/30 transition-colors">
                                    <td class="py-4 px-6">Titanium Alloy</td>
                                    <td class="py-4 px-6">42 units</td>
                                    <td class="py-4 px-6">
                                        <span class="px-3 py-1 bg-green-600/30 text-green-300 rounded-full text-sm">In Stock</span>
                                    </td>
                                    <td class="py-4 px-6">
                                        <button class="text-blue-400 hover:text-blue-300 mr-4">
                                            <i data-feather="edit-2" class="w-4 h-4"></i>
                                        </button>
                                        <button class="text-red-400 hover:text-red-300">
                                            <i data-feather="trash-2" class="w-4 h-4"></i>
                                        </button>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-700/30 hover:bg-gray-700/30 transition-colors">
                                    <td class="py-4 px-6">Carbon Fiber</td>
                                    <td class="py-4 px-6">28 units</td>
                                    <td class="py-4 px-6">
                                        <span class="px-3 py-1 bg-yellow-600/30 text-yellow-300 rounded-full text-sm">Low Stock</span>
                                    </td>
                                    <td class="py-4 px-6">
                                        <button class="text-blue-400 hover:text-blue-300 mr-4">
                                            <i data-feather="edit-2" class="w-4 h-4"></i>
                                        </button>
                                        <button class="text-red-400 hover:text-red-300">
                                            <i data-feather="trash-2" class="w-4 h-4"></i>
                                        </button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-gray-700/30 transition-colors">
                                    <td class="py-4 px-6">Ceramic Tiles</td>
                                    <td class="py-4 px-6">15 units</td>
                                    <td class="py-4 px-6">
                                        <span class="px-3 py-1 bg-red-600/30 text-red-300 rounded-full text-sm">Critical</span>
                                    </td>
                                    <td class="py-4 px-6">
                                        <button class="text-blue-400 hover:text-blue-300 mr-4">
                                            <i data-feather="edit-2" class="w-4 h-4"></i>
                                        </button>
                                        <button class="text-red-400 hover:text-red-300">
                                            <i data-feather="trash-2" class="w-4 h-4"></i>
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Specifications Content (Hidden by default) -->
            <div id="specifications-content" class="content-section hidden">
                <div class="py-12">
                    <h2 class="text-4xl font-bold mb-8 flex items-center">
                        <i data-feather="settings" class="mr-4"></i> Specifications
                    </h2>
                    <div class="bg-gray-800/50 rounded-xl border border-gray-700/50 p-6 mb-8">
                        <h3 class="text-2xl font-semibold mb-4">3D Model Viewer</h3>
                        <div class="aspect-w-16 aspect-h-9 bg-gray-900/50 rounded-lg overflow-hidden border border-gray-700/50">
                            <iframe src="https://learouse.github.io/prototipo/" class="w-full h-[600px]" frameborder="0"></iframe>
                        </div>
                    </div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700/50">
                            <h3 class="text-2xl font-semibold mb-4">Technical Data</h3>
                            <ul class="space-y-3">
                                <li class="flex justify-between">
                                    <span class="text-gray-400">Weight:</span>
                                    <span class="font-medium">245 kg</span>
                                </li>
                                <li class="flex justify-between">
                                    <span class="text-gray-400">Dimensions:</span>
                                    <span class="font-medium">1.2m × 0.8m × 0.6m</span>
                                </li>
                                <li class="flex justify-between">
                                    <span class="text-gray-400">Power Consumption:</span>
                                    <span class="font-medium">120W</span>
                                </li>
                                <li class="flex justify-between">
                                    <span class="text-gray-400">Max Temperature:</span>
                                    <span class="font-medium">1200°C</span>
                                </li>
                            </ul>
                        </div>
                        <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700/50">
                            <h3 class="text-2xl font-semibold mb-4">Performance Metrics</h3>
                            <div class="space-y-4">
                                <div>
                                    <div class="flex justify-between mb-1">
                                        <span class="text-gray-400">Structural Integrity</span>
                                        <span class="font-medium">92%</span>
                                    </div>
                                    <div class="w-full bg-gray-700 rounded-full h-2.5">
                                        <div class="bg-green-500 h-2.5 rounded-full" style="width: 92%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between mb-1">
                                        <span class="text-gray-400">Thermal Resistance</span>
                                        <span class="font-medium">87%</span>
                                    </div>
                                    <div class="w-full bg-gray-700 rounded-full h-2.5">
                                        <div class="bg-blue-500 h-2.5 rounded-full" style="width: 87%"></div>
                                    </div>
                                </div>
                                <div>
                                    <div class="flex justify-between mb-1">
                                        <span class="text-gray-400">Radiation Shielding</span>
                                        <span class="font-medium">95%</span>
                                    </div>
                                    <div class="w-full bg-gray-700 rounded-full h-2.5">
                                        <div class="bg-purple-500 h-2.5 rounded-full" style="width: 95%"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Configuration Content (Hidden by default) -->
            <div id="configuration-content" class="content-section hidden">
                <div class="py-12">
                    <h2 class="text-4xl font-bold mb-8 flex items-center">
                        <i data-feather="sliders" class="mr-4"></i> Configuration
                    </h2>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                        <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700/50">
                            <h3 class="text-2xl font-semibold mb-6">Appearance</h3>
                            <div class="space-y-6">
                                <div>
                                    <label class="block text-gray-400 mb-2">Theme</label>
                                    <div class="flex space-x-4">
                                        <button class="px-4 py-2 bg-gray-700 rounded-lg hover:bg-gray-600 transition-colors">
                                            Dark
                                        </button>
                                        <button class="px-4 py-2 bg-gray-700 rounded-lg hover:bg-gray-600 transition-colors">
                                            Light
                                        </button>
                                        <button class="px-4 py-2 bg-gray-700 rounded-lg hover:bg-gray-600 transition-colors">
                                            System
                                        </button>
                                    </div>
                                </div>
                                <div>
                                    <label class="block text-gray-400 mb-2">Accent Color</label>
                                    <div class="flex flex-wrap gap-2">
                                        <div class="w-8 h-8 rounded-full bg-blue-500 cursor-pointer border-2 border-transparent hover:border-white"></div>
                                        <div class="w-8 h-8 rounded-full bg-purple-500 cursor-pointer border-2 border-transparent hover:border-white"></div>
                                        <div class="w-8 h-8 rounded-full bg-green-500 cursor-pointer border-2 border-transparent hover:border-white"></div>
                                        <div class="w-8 h-8 rounded-full bg-red-500 cursor-pointer border-2 border-transparent hover:border-white"></div>
                                        <div class="w-8 h-8 rounded-full bg-yellow-500 cursor-pointer border-2 border-transparent hover:border-white"></div>
                                        <div class="w-8 h-8 rounded-full bg-pink-500 cursor-pointer border-2 border-transparent hover:border-white"></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700/50">
                            <h3 class="text-2xl font-semibold mb-6">System Settings</h3>
                            <div class="space-y-6">
                                <div>
                                    <label class="block text-gray-400 mb-2">Animation Intensity</label>
                                    <input type="range" min="0" max="100" value="75" class="w-full h-2 bg-gray-700 rounded-lg appearance-none cursor-pointer">
                                </div>
                                <div>
                                    <label class="flex items-center space-x-3">
                                        <input type="checkbox" class="form-checkbox h-5 w-5 text-blue-600 bg-gray-700 border-gray-600 rounded" checked>
                                        <span class="text-gray-300">Enable Haptic Feedback</span>
                                    </label>
                                </div>
                                <div>
                                    <label class="flex items-center space-x-3">
                                        <input type="checkbox" class="form-checkbox h-5 w-5 text-blue-600 bg-gray-700 border-gray-600 rounded" checked>
                                        <span class="text-gray-300">Show Tooltips</span>
                                    </label>
                                </div>
                                <div>
                                    <label class="flex items-center space-x-3">
                                        <input type="checkbox" class="form-checkbox h-5 w-5 text-blue-600 bg-gray-700 border-gray-600 rounded">
                                        <span class="text-gray-300">Dark Mode Only</span>
                                    </label>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <script>
        // Initialize Vanta.js background
        VANTA.GLOBE({
            el: "#vanta-bg",
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x3a86ff,
            backgroundColor: 0x101017,
            size: 0.8
        });

        // Initialize Feather Icons
        feather.replace();
        
        // Page navigation
        document.addEventListener('DOMContentLoaded', function() {
            // Hide all content sections except home
            document.querySelectorAll('.content-section').forEach(section => {
                if (section.id !== 'home-content') {
                    section.classList.add('hidden');
                }
            });
            
            // Button event listeners
            document.getElementById('btn-home').addEventListener('click', function() {
                showContent('home-content');
            });
            
            document.getElementById('btn-craft').addEventListener('click', function() {
                showContent('craft-content');
            });
            
            document.getElementById('btn-mat').addEventListener('click', function() {
                showContent('materials-content');
            });
            
            document.getElementById('btn-spec').addEventListener('click', function() {
                showContent('specifications-content');
            });
            
            document.getElementById('btn-config').addEventListener('click', function() {
                showContent('configuration-content');
            });
            
            function showContent(contentId) {
                document.querySelectorAll('.content-section').forEach(section => {
                    section.classList.add('hidden');
                });
                document.getElementById(contentId).classList.remove('hidden');
                
                // Add animation class and remove it after animation completes
                const content = document.getElementById(contentId);
                content.classList.add('animate-fadeIn');
                setTimeout(() => {
                    content.classList.remove('animate-fadeIn');
                }, 800);
            }
        });
    </script>
</body>
</html>
