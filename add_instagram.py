import glob

html_files = glob.glob('*.html')

target = """                </form>
            </div>
        </div>
        <div class="max-w-7xl mx-auto mt-16 pt-8 border-t border-brand-beige flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-gray-400 font-light">"""

replacement = """                </form>
                <div class="mt-6">
                    <a href="https://www.instagram.com/the.plaintheory/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-sm text-gray-500 hover:text-brand-green transition-colors font-medium">
                        <i data-lucide="instagram" class="w-5 h-5"></i> @the.plaintheory
                    </a>
                </div>
            </div>
        </div>
        <div class="max-w-7xl mx-auto mt-16 pt-8 border-t border-brand-beige flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-gray-400 font-light">"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content:
        content = content.replace(target, replacement)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added Instagram link to {file}")
    else:
        print(f"Skipped {file}")
