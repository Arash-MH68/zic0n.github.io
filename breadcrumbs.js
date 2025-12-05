// Breadcrumb Navigation Generator
// Automatically generates breadcrumbs based on page URL

(function() {
  'use strict';

  // Page title mappings
  const PAGE_TITLES = {
    'index.html': 'Home',
    'about.html': 'About',
    'services.html': 'Services',
    'markets.html': 'Markets',
    'capabilities.html': 'Capabilities',
    'projects.html': 'Projects',
    'approach.html': 'Approach',
    'leadership.html': 'Leadership',
    'newsletter.html': 'Newsletter',
    'faqs.html': 'FAQs',
    'contact.html': 'Contact'
  };

  function generateBreadcrumbs() {
    const path = window.location.pathname;
    const filename = path.split('/').pop() || 'index.html';
    
    // Don't show breadcrumbs on homepage
    if (filename === 'index.html' || filename === '') {
      return null;
    }

    const breadcrumbs = [
      { name: 'Home', url: 'index.html' },
      { name: PAGE_TITLES[filename] || filename.replace('.html', ''), url: filename }
    ];

    return breadcrumbs;
  }

  function createBreadcrumbHTML(breadcrumbs) {
    if (!breadcrumbs) return '';

    const items = breadcrumbs.map((crumb, index) => {
      const isLast = index === breadcrumbs.length - 1;
      
      if (isLast) {
        return `
          <li aria-current="page" class="text-cyan-400">${crumb.name}</li>
        `;
      }
      
      return `
        <li><a href="${crumb.url}" class="hover:text-white transition">${crumb.name}</a></li>
        <li aria-hidden="true"><i data-feather="chevron-right" class="w-4 h-4"></i></li>
      `;
    }).join('');

    return `
      <nav aria-label="Breadcrumb" class="max-w-7xl mx-auto px-6 py-4">
        <ol class="flex items-center gap-2 text-sm text-slate-400">
          ${items}
        </ol>
      </nav>
    `;
  }

  function createBreadcrumbSchema(breadcrumbs) {
    if (!breadcrumbs) return null;

    return {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": breadcrumbs.map((crumb, index) => ({
        "@type": "ListItem",
        "position": index + 1,
        "name": crumb.name,
        "item": `https://zic0n.com/${crumb.url}`
      }))
    };
  }

  function insertBreadcrumbs() {
    const breadcrumbs = generateBreadcrumbs();
    if (!breadcrumbs) return;

    // Insert HTML breadcrumbs after header
    const header = document.querySelector('header');
    if (header) {
      const breadcrumbHTML = createBreadcrumbHTML(breadcrumbs);
      header.insertAdjacentHTML('afterend', breadcrumbHTML);
      
      // Replace feather icons
      if (typeof feather !== 'undefined') {
        feather.replace();
      }
    }

    // Insert JSON-LD schema
    const schema = createBreadcrumbSchema(breadcrumbs);
    if (schema) {
      const script = document.createElement('script');
      script.type = 'application/ld+json';
      script.textContent = JSON.stringify(schema);
      document.head.appendChild(script);
    }
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', insertBreadcrumbs);
  } else {
    insertBreadcrumbs();
  }
})();
