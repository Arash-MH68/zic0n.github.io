// Analytics Integration
// Supports Google Analytics 4, Plausible, and custom tracking

(function() {
  'use strict';

  // Configuration
  const CONFIG = {
    // Google Analytics 4
    ga4: {
      enabled: false,
      measurementId: 'G-XXXXXXXXXX' // Replace with your GA4 Measurement ID
    },
    
    // Plausible Analytics (privacy-focused alternative)
    plausible: {
      enabled: false,
      domain: 'zic0n.com'
    },
    
    // Custom events to track
    trackEvents: {
      formSubmissions: true,
      outboundLinks: true,
      fileDownloads: true,
      emailClicks: true,
      phoneClicks: true,
      videoPlays: false
    }
  };

  // Initialize analytics
  function initAnalytics() {
    if (CONFIG.ga4.enabled) {
      loadGoogleAnalytics();
    }
    
    if (CONFIG.plausible.enabled) {
      loadPlausible();
    }
    
    // Set up event tracking
    setupEventTracking();
  }

  // Load Google Analytics 4
  function loadGoogleAnalytics() {
    // Add GA4 script
    const script = document.createElement('script');
    script.async = true;
    script.src = `https://www.googletagmanager.com/gtag/js?id=${CONFIG.ga4.measurementId}`;
    document.head.appendChild(script);

    // Initialize gtag
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    window.gtag = gtag;
    
    gtag('js', new Date());
    gtag('config', CONFIG.ga4.measurementId, {
      'anonymize_ip': true,
      'cookie_flags': 'SameSite=None;Secure'
    });

    console.log('Google Analytics 4 initialized');
  }

  // Load Plausible Analytics
  function loadPlausible() {
    const script = document.createElement('script');
    script.defer = true;
    script.dataset.domain = CONFIG.plausible.domain;
    script.src = 'https://plausible.io/js/script.js';
    document.head.appendChild(script);

    console.log('Plausible Analytics initialized');
  }

  // Set up event tracking
  function setupEventTracking() {
    // Track outbound links
    if (CONFIG.trackEvents.outboundLinks) {
      document.addEventListener('click', (e) => {
        const link = e.target.closest('a');
        if (link && link.href) {
          const url = new URL(link.href, window.location.href);
          if (url.hostname !== window.location.hostname) {
            trackEvent('outbound_link', {
              url: link.href,
              text: link.textContent.trim()
            });
          }
        }
      });
    }

    // Track email clicks
    if (CONFIG.trackEvents.emailClicks) {
      document.addEventListener('click', (e) => {
        const link = e.target.closest('a[href^="mailto:"]');
        if (link) {
          trackEvent('email_click', {
            email: link.href.replace('mailto:', '')
          });
        }
      });
    }

    // Track phone clicks
    if (CONFIG.trackEvents.phoneClicks) {
      document.addEventListener('click', (e) => {
        const link = e.target.closest('a[href^="tel:"]');
        if (link) {
          trackEvent('phone_click', {
            phone: link.href.replace('tel:', '')
          });
        }
      });
    }

    // Track file downloads
    if (CONFIG.trackEvents.fileDownloads) {
      document.addEventListener('click', (e) => {
        const link = e.target.closest('a');
        if (link && link.href) {
          const fileExtensions = /\.(pdf|doc|docx|xls|xlsx|zip|rar|txt|csv)$/i;
          if (fileExtensions.test(link.href)) {
            trackEvent('file_download', {
              file: link.href,
              type: link.href.split('.').pop()
            });
          }
        }
      });
    }

    // Track scroll depth
    trackScrollDepth();
  }

  // Track custom event
  function trackEvent(eventName, eventParams = {}) {
    // Google Analytics 4
    if (CONFIG.ga4.enabled && typeof gtag !== 'undefined') {
      gtag('event', eventName, eventParams);
    }

    // Plausible
    if (CONFIG.plausible.enabled && typeof plausible !== 'undefined') {
      plausible(eventName, { props: eventParams });
    }

    // Console log for debugging
    console.log('Event tracked:', eventName, eventParams);
  }

  // Track scroll depth
  function trackScrollDepth() {
    const milestones = [25, 50, 75, 100];
    const reached = new Set();

    window.addEventListener('scroll', () => {
      const scrollPercent = Math.round(
        (window.scrollY / (document.documentElement.scrollHeight - window.innerHeight)) * 100
      );

      milestones.forEach(milestone => {
        if (scrollPercent >= milestone && !reached.has(milestone)) {
          reached.add(milestone);
          trackEvent('scroll_depth', {
            percent: milestone,
            page: window.location.pathname
          });
        }
      });
    }, { passive: true });
  }

  // Track page view (for SPAs)
  function trackPageView(path) {
    if (CONFIG.ga4.enabled && typeof gtag !== 'undefined') {
      gtag('config', CONFIG.ga4.measurementId, {
        'page_path': path
      });
    }

    if (CONFIG.plausible.enabled && typeof plausible !== 'undefined') {
      plausible('pageview');
    }
  }

  // Export functions for use in other scripts
  window.analytics = {
    trackEvent,
    trackPageView
  };

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initAnalytics);
  } else {
    initAnalytics();
  }
})();
