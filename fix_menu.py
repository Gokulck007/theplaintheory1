import os
import glob

html_files = glob.glob('*.html')

nav_target = """            <div class="flex items-center gap-4">
                <button class="hover:text-brand-green transition-colors"><i data-lucide="search" class="w-5 h-5"></i></button>
                <button class="hover:text-brand-green transition-colors"><i data-lucide="user" class="w-5 h-5"></i></button>
                <button class="hover:text-brand-green transition-colors relative">
                    <i data-lucide="shopping-bag" class="w-5 h-5"></i>
                    <span class="absolute -top-1 -right-1 bg-brand-green text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center">0</span>
                </button>
            </div>"""

nav_replacement = """            <div class="flex items-center gap-4">
                <button class="hover:text-brand-green transition-colors"><i data-lucide="search" class="w-5 h-5"></i></button>
                <button class="hover:text-brand-green transition-colors hidden sm:block"><i data-lucide="user" class="w-5 h-5"></i></button>
                <button class="hover:text-brand-green transition-colors relative">
                    <i data-lucide="shopping-bag" class="w-5 h-5"></i>
                    <span class="absolute -top-1 -right-1 bg-brand-green text-white text-[10px] w-4 h-4 rounded-full flex items-center justify-center">0</span>
                </button>
                <button id="mobile-menu-btn" class="md:hidden hover:text-brand-green transition-colors ml-2"><i data-lucide="menu" class="w-6 h-6"></i></button>
            </div>"""

mobile_menu_html = """
    <!-- Mobile Menu Overlay -->
    <div id="mobile-menu" class="fixed inset-0 bg-[#f7f6f2] z-40 hidden flex-col pt-24 px-6 pb-6 overflow-y-auto">
        <div class="flex flex-col gap-6 text-2xl font-serif">
            <a href="shop.html" class="hover:text-brand-green border-b border-brand-beige pb-4">Shop</a>
            <a href="about.html" class="hover:text-brand-green border-b border-brand-beige pb-4">Our Story</a>
            <a href="ingredients.html" class="hover:text-brand-green border-b border-brand-beige pb-4">Ingredients</a>
        </div>
    </div>
"""

js_target = "lucide.createIcons();"
js_replacement = """lucide.createIcons();
        
        // Mobile Menu Toggle
        const mobileBtn = document.getElementById('mobile-menu-btn');
        const mobileMenu = document.getElementById('mobile-menu');
        if (mobileBtn && mobileMenu) {
            mobileBtn.addEventListener('click', () => {
                const isHidden = mobileMenu.classList.contains('hidden');
                if (isHidden) {
                    mobileMenu.classList.remove('hidden');
                    mobileMenu.classList.add('flex');
                    mobileBtn.innerHTML = '<i data-lucide="x" class="w-6 h-6"></i>';
                } else {
                    mobileMenu.classList.add('hidden');
                    mobileMenu.classList.remove('flex');
                    mobileBtn.innerHTML = '<i data-lucide="menu" class="w-6 h-6"></i>';
                }
                lucide.createIcons();
            });
        }"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if nav_target in content:
        content = content.replace(nav_target, nav_replacement)
        
        if "</nav>" in content and 'id="mobile-menu"' not in content:
            content = content.replace("</nav>", "</nav>\n" + mobile_menu_html)
            
        if js_target in content and 'Mobile Menu Toggle' not in content:
            content = content.replace(js_target, js_replacement, 1)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Skipped {file} (target not found)")
