import glob

html_files = glob.glob('*.html')

target = """                </form>
                <div class="mt-6">
                    <a href="https://www.instagram.com/the.plaintheory/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 text-sm text-gray-500 hover:text-brand-green transition-colors font-medium">
                        <i data-lucide="instagram" class="w-5 h-5"></i> @the.plaintheory
                    </a>
                </div>
            </div>
        </div>
        <div class="max-w-7xl mx-auto mt-16 pt-8 border-t border-brand-beige flex flex-col md:flex-row justify-between items-center gap-4 text-xs text-gray-400 font-light">
            <p>&copy; 2026 The Plain Theory. All rights reserved.</p>
            <div class="flex gap-4">
                <a href="#" class="hover:text-brand-green transition-colors">Privacy Policy</a>
                <a href="#" class="hover:text-brand-green transition-colors">Terms of Service</a>
            </div>
        </div>
    </footer>"""

replacement = """                </form>
            </div>
        </div>
        <div class="max-w-7xl mx-auto mt-16 pt-8 border-t border-brand-beige flex flex-col md:flex-row justify-between items-center gap-6 text-sm text-gray-400 font-light">
            <p class="md:w-1/3 text-center md:text-left">&copy; 2026 The Plain Theory.</p>
            
            <div class="md:w-1/3 flex justify-center">
                <a href="https://www.instagram.com/the.plaintheory/" target="_blank" rel="noopener noreferrer" class="text-gray-400 hover:text-brand-green transition-transform hover:scale-110" aria-label="Instagram">
                    <i data-lucide="instagram" class="w-6 h-6"></i>
                </a>
            </div>

            <div class="md:w-1/3 flex justify-center md:justify-end gap-6">
                <a href="#" class="hover:text-brand-green transition-colors">Privacy Policy</a>
                <a href="#" class="hover:text-brand-green transition-colors">Terms of Service</a>
            </div>
        </div>
    </footer>"""

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if target in content:
        content = content.replace(target, replacement)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Moved Instagram link in {file}")
    else:
        print(f"Skipped {file} (target not found)")
