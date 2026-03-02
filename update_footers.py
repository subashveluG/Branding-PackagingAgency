import os
import re

footer_content = """    <!-- Footer -->
    <footer class="footer pb-0 bg-dark text-white border-top border-primary border-5">
        <div class="container pt-5 pb-4">
            <div class="row gy-4">
                <div class="col-lg-4 col-md-6">
                    <a href="index.html" class="navbar-brand text-white d-flex align-items-center mb-4 fs-4 fw-bold">
                        <i class="bi bi-intersect me-2 text-primary"></i> BrandEdge
                    </a>
                    <p class="small text-white-50 mb-4" style="max-width: 300px;">Crafting iconic brands and sustainable packaging for the future since 2018.</p>
                    <div class="d-flex gap-3 fs-5">
                        <a href="#" class="text-white-50 hover-highlight"><i class="bi bi-facebook"></i></a>
                        <a href="#" class="text-white-50 hover-highlight"><i class="bi bi-twitter-x"></i></a>
                        <a href="#" class="text-white-50 hover-highlight"><i class="bi bi-instagram"></i></a>
                        <a href="#" class="text-white-50 hover-highlight"><i class="bi bi-linkedin"></i></a>
                    </div>
                </div>
                <div class="col-lg-2 col-md-6 col-6">
                    <h6 class="fw-bold mb-4 text-white">Company</h6>
                    <ul class="list-unstyled">
                        <li class="mb-3"><a href="index.html" class="text-white-50 text-decoration-none hover-highlight small">Home</a></li>
                        <li class="mb-3"><a href="about.html" class="text-white-50 text-decoration-none hover-highlight small">About</a></li>
                        <li class="mb-3"><a href="services.html" class="text-white-50 text-decoration-none hover-highlight small">Services</a></li>
                        <li class="mb-3"><a href="contact.html" class="text-white-50 text-decoration-none hover-highlight small">Contact</a></li>
                    </ul>
                </div>
                <div class="col-lg-2 col-md-6 col-6">
                    <h6 class="fw-bold mb-4 text-white">Support</h6>
                    <ul class="list-unstyled">
                        <li class="mb-3"><a href="#" class="text-white-50 text-decoration-none hover-highlight small">Help Center</a></li>
                        <li class="mb-3"><a href="#" class="text-white-50 text-decoration-none hover-highlight small">Terms of Use</a></li>
                        <li class="mb-3"><a href="#" class="text-white-50 text-decoration-none hover-highlight small">Privacy Policy</a></li>
                        <li class="mb-3"><a href="#" class="text-white-50 text-decoration-none hover-highlight small">Cookie Policy</a></li>
                    </ul>
                </div>
                <div class="col-lg-4 col-md-6">
                    <h6 class="fw-bold mb-4 text-white">Newsletter</h6>
                    <p class="small text-white-50 mb-4">Stay updated with latest trends.</p>
                    <form class="d-flex w-100 shadow-sm rounded">
                        <input type="email" class="form-control bg-dark text-white border-secondary rounded-start rounded-0" placeholder="Email address" style="border-right: none;">
                        <button class="btn btn-primary rounded-end rounded-0 px-4 fw-bold" type="button">Join</button>
                    </form>
                </div>
            </div>
        </div>
        <hr class="border-secondary m-0 opacity-25">
        <div class="container py-4">
            <div class="row align-items-center">
                <div class="col-md-6 text-center text-md-start">
                    <p class="mb-0 small text-white-50">&copy; 2026 BrandEdge Agency. All rights reserved.</p>
                </div>
                <div class="col-md-6 text-center text-md-end">
                    <p class="mb-0 small text-white-50">Premium Branding Solutions.</p>
                </div>
            </div>
        </div>
    </footer>"""

files_to_update = ['index.html', 'home1.html', 'home2.html', 'about.html', 'services.html', 'contact.html']

for filename in files_to_update:
    path = os.path.join(r"c:\\Users\\VISU\\OneDrive\\Documents\\Smartfusion\\Branding&PackagingAgency", filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to match the footer block
        new_content = re.sub(r' *<!-- Footer -->.*?</footer>', footer_content, content, flags=re.DOTALL)
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
