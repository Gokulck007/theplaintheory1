import glob

# 1. Update Footer Links
html_files = glob.glob('*.html')

faq_target = '<li><a href="#" class="hover:text-brand-green transition-colors">FAQ</a></li>'
faq_replacement = '<li><a href="faq.html" class="hover:text-brand-green transition-colors">FAQ</a></li>'

contact_target = '<li><a href="#" class="hover:text-brand-green transition-colors">Contact Us</a></li>'
contact_replacement = '<li><a href="contact.html" class="hover:text-brand-green transition-colors">Contact Us</a></li>'

for file in html_files:
    if file in ['faq.html', 'contact.html']:
        continue # Already correct in the newly created files
        
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    content = content.replace(faq_target, faq_replacement)
    content = content.replace(contact_target, contact_replacement)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
        
print("Updated footer links in older HTML files.")

# 2. Add Reviews section to index.html
reviews_html = """
    <!-- Reviews / Social Proof -->
    <section class="py-24 bg-brand-light px-6 border-y border-brand-beige">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-16 reveal">
                <h2 class="text-3xl md:text-4xl font-serif mb-4">What people are saying.</h2>
                <p class="text-gray-500 font-light">Feedback from our initial pilot testing batch.</p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Review 1 -->
                <div class="bg-white p-8 rounded-xl border border-brand-beige reveal">
                    <div class="flex text-brand-green mb-4">
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                    </div>
                    <p class="text-gray-600 font-light leading-relaxed mb-6">"Finally, a natural deodorant that actually lasts. I bought the EVEN variant and it easily got me through a humid 10-hour workday without having to reapply. The packaging feels incredibly premium for the price."</p>
                    <p class="font-medium text-sm text-brand-black">— Anjali M.</p>
                </div>
                
                <!-- Review 2 -->
                <div class="bg-white p-8 rounded-xl border border-brand-beige reveal delay-1">
                    <div class="flex text-brand-green mb-4">
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                    </div>
                    <p class="text-gray-600 font-light leading-relaxed mb-6">"I have extremely sensitive skin and usually break out from the baking soda in other natural brands. This alum-based formula is completely different. No irritation, no staining my white shirts, just clean scent."</p>
                    <p class="font-medium text-sm text-brand-black">— Rohan K.</p>
                </div>

                <!-- Review 3 -->
                <div class="bg-white p-8 rounded-xl border border-brand-beige reveal delay-2">
                    <div class="flex text-brand-green mb-4">
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                        <i data-lucide="star" class="w-4 h-4 fill-current"></i>
                    </div>
                    <p class="text-gray-600 font-light leading-relaxed mb-6">"I love that it's truly unisex. My partner and I both use the GROUND scent now. It's woody but subtle. And it's true—one bottle seems to last forever because the roller doesn't dump out half the liquid at once."</p>
                    <p class="font-medium text-sm text-brand-black">— Priya S.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->"""

with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

if "What people are saying" not in index_content:
    index_content = index_content.replace('<!-- Footer -->', reviews_html)
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("Added reviews section to index.html")
else:
    print("Reviews section already exists in index.html")
