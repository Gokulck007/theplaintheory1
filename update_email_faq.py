import os

# 1. Update Emails in contact.html
contact_file = 'contact.html'
with open(contact_file, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('hello@theplaintheory.com', 'info@theplaintheory.com')
content = content.replace('partnerships@theplaintheory.com', 'info@theplaintheory.com')

with open(contact_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated emails in contact.html")


# 2. Add Skin Types section to faq.html
faq_file = 'faq.html'
with open(faq_file, 'r', encoding='utf-8') as f:
    faq_content = f.read()

new_faq_section = """
                <h3 class="text-xl font-serif mt-12 mb-4 border-b border-brand-beige pb-2">Skin Types & Care</h3>

                <details class="group bg-white rounded-lg border border-brand-beige p-6">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-lg">
                        <span>Is it suitable for dry or easily irritated skin?</span>
                        <span class="transition group-open:rotate-180">
                            <i data-lucide="chevron-down" class="w-5 h-5 text-gray-400"></i>
                        </span>
                    </summary>
                    <div class="text-gray-500 font-light mt-4 leading-relaxed">
                        Absolutely. We purposely formulated this with a generous amount of Plant-Derived Glycerin (3%). Glycerin is a powerful humectant that draws moisture to the surface of your skin, preventing the dry, chalky feeling that many natural deodorants leave behind.
                    </div>
                </details>

                <details class="group bg-white rounded-lg border border-brand-beige p-6">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-lg">
                        <span>Will it cause underarm darkening or pigmentation?</span>
                        <span class="transition group-open:rotate-180">
                            <i data-lucide="chevron-down" class="w-5 h-5 text-gray-400"></i>
                        </span>
                    </summary>
                    <div class="text-gray-500 font-light mt-4 leading-relaxed">
                        Underarm darkening is commonly caused by friction, irritation from baking soda, or harsh synthetic alcohols drying out the skin. Our formula is completely free from baking soda and synthetic alcohols. The smooth roll-on application minimizes friction, helping to maintain your natural skin tone.
                    </div>
                </details>

                <details class="group bg-white rounded-lg border border-brand-beige p-6">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-lg">
                        <span>Can I use it if I'm a heavy sweater or have oily skin?</span>
                        <span class="transition group-open:rotate-180">
                            <i data-lucide="chevron-down" class="w-5 h-5 text-gray-400"></i>
                        </span>
                    </summary>
                    <div class="text-gray-500 font-light mt-4 leading-relaxed">
                        Yes! Remember, odor doesn't come from sweat itself; it comes from bacteria breaking down the sweat. By targeting the bacteria with antimicrobial Potassium Alum, heavy sweaters can enjoy all-day freshness. For best results, ensure your underarms are completely clean and dry before applying.
                    </div>
                </details>

                <details class="group bg-white rounded-lg border border-brand-beige p-6">
                    <summary class="flex justify-between items-center font-medium cursor-pointer list-none text-lg">
                        <span>Can I apply it immediately after shaving or waxing?</span>
                        <span class="transition group-open:rotate-180">
                            <i data-lucide="chevron-down" class="w-5 h-5 text-gray-400"></i>
                        </span>
                    </summary>
                    <div class="text-gray-500 font-light mt-4 leading-relaxed">
                        Potassium Alum is traditionally used as a soothing aftershave to calm the skin and prevent bumps. However, because it's a mineral salt, it may cause a brief, mild tingling sensation if you have micro-cuts from a razor. We recommend waiting 10-15 minutes after shaving before application.
                    </div>
                </details>

            </div>"""

target_split = "            </div>\n\n            <div class=\"mt-16 text-center reveal\">"

if "Skin Types & Care" not in faq_content:
    parts = faq_content.split(target_split)
    if len(parts) == 2:
        new_content = parts[0] + new_faq_section + "\n\n            <div class=\"mt-16 text-center reveal\">" + parts[1]
        with open(faq_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Added Skin Types section to faq.html")
    else:
        print("Could not find injection point in faq.html")
else:
    print("Skin Types section already exists in faq.html")
