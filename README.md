# Zic0n Engineering Website

Professional civil engineering consultancy website featuring geotechnical, transportation, pavements & materials expertise.

## 🚀 Recent Improvements (December 2024)

### Performance Enhancements
- ✅ Optimized resource loading with preconnect and DNS prefetch
- ✅ Removed unnecessary `defer` attributes for faster initial render
- ✅ Extracted CSS to external stylesheet for better caching
- ✅ Extracted JavaScript to external file for better maintainability
- ✅ Added browser caching via .htaccess
- ✅ Enabled GZIP compression for faster page loads

### User Experience
- ✅ Added smooth scroll-to-top button
- ✅ Implemented intersection observer for fade-in animations
- ✅ Enhanced hover effects on buttons and cards
- ✅ Improved mobile menu with better transitions
- ✅ Added form validation with user feedback
- ✅ Responsive design improvements

### Accessibility
- ✅ Enhanced ARIA labels and roles
- ✅ Improved keyboard navigation
- ✅ Added skip-to-content link
- ✅ Better focus indicators
- ✅ Reduced motion support for users with motion sensitivity
- ✅ Semantic HTML improvements

### SEO Optimization
- ✅ Created comprehensive sitemap.xml
- ✅ Added robots.txt for search engine crawlers
- ✅ Improved meta tags and Open Graph data
- ✅ Added structured data (JSON-LD)
- ✅ Optimized page titles and descriptions
- ✅ Created custom 404 error page

### Security
- ✅ Added security headers (X-Frame-Options, CSP, etc.)
- ✅ Implemented HTTPS redirect
- ✅ Protected sensitive files
- ✅ Disabled directory browsing
- ✅ XSS and clickjacking protection

## 📁 File Structure

```
website/
├── index.html              # Homepage
├── about.html              # About page
├── services.html           # Services overview
├── markets.html            # Target markets
├── capabilities.html       # Technical capabilities
├── projects.html           # Project portfolio
├── approach.html           # Engineering approach
├── leadership.html         # Team profiles
├── newsletter.html         # Newsletter/blog
├── faqs.html              # Frequently asked questions
├── contact.html           # Contact form
├── 404.html               # Custom error page
├── styles.css             # Global styles
├── app.js                 # JavaScript functionality
├── sitemap.xml            # SEO sitemap
├── robots.txt             # Search engine directives
├── .htaccess              # Apache configuration
├── CNAME                  # Custom domain
└── images/                # Image assets
```

## 🛠️ Technologies Used

- **HTML5** - Semantic markup
- **CSS3** - Custom styles with CSS variables
- **JavaScript (ES6+)** - Modern vanilla JS
- **Tailwind CSS** - Utility-first CSS framework
- **Feather Icons** - Beautiful icon set
- **Inter Font** - Professional typography

## 🌐 Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## 📱 Responsive Design

The website is fully responsive and optimized for:
- Desktop (1920px+)
- Laptop (1024px - 1919px)
- Tablet (768px - 1023px)
- Mobile (320px - 767px)

## ⚡ Performance Metrics

Target metrics:
- First Contentful Paint: < 1.5s
- Largest Contentful Paint: < 2.5s
- Time to Interactive: < 3.5s
- Cumulative Layout Shift: < 0.1

## 🔧 Development

### Local Development
Simply open any HTML file in a modern web browser. For best results, use a local server:

```bash
# Using Python
python -m http.server 8000

# Using Node.js
npx serve

# Using PHP
php -S localhost:8000
```

### Making Updates
1. Edit HTML files directly for content changes
2. Modify `styles.css` for styling updates
3. Update `app.js` for functionality changes
4. Run `update-all-pages.py` to apply changes across all pages

## 📊 SEO Checklist

- [x] Unique title tags for each page
- [x] Meta descriptions (150-160 characters)
- [x] Open Graph tags for social sharing
- [x] Structured data (JSON-LD)
- [x] Sitemap.xml
- [x] Robots.txt
- [x] Canonical URLs
- [x] Alt text for images
- [x] Mobile-friendly design
- [x] Fast page load times
- [x] HTTPS enabled

## 🔒 Security Features

- Content Security Policy (CSP)
- X-Frame-Options (clickjacking protection)
- X-XSS-Protection
- X-Content-Type-Options
- Referrer-Policy
- HTTPS enforcement
- File access protection

## 📞 Contact

**Zic0n Engineering**
- Email: info@zic0n.com
- Website: https://zic0n.com
- LinkedIn: https://www.linkedin.com/company/zic0n

## 📄 License

© 2024 Zic0n Engineering. All rights reserved.

---

**Last Updated:** December 4, 2024
