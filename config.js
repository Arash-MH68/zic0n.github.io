// Global Configuration for Zic0n Engineering Website
// Centralized settings for all features

window.ZICON_CONFIG = {
  // Site Information
  site: {
    name: 'Zic0n Engineering',
    url: 'https://zic0n.com',
    email: 'info@zic0n.com',
    phone: '+1-XXX-XXX-XXXX', // Update with actual phone
    description: 'Partner-led civil engineering practice providing geotechnical, transportation, pavements & materials expertise.',
    logo: '/images/logo.png',
    social: {
      linkedin: 'https://www.linkedin.com/company/zic0n',
      twitter: '@zic0n' // Update if applicable
    }
  },

  // Locations
  locations: [
    {
      name: 'San Diego Office',
      city: 'San Diego',
      state: 'CA',
      country: 'US',
      type: 'headquarters',
      phone: '+1-XXX-XXX-XXXX',
      geo: {
        lat: 32.7157,
        lng: -117.1611
      }
    },
    {
      name: 'Philadelphia Office',
      city: 'Philadelphia',
      state: 'PA',
      country: 'US',
      type: 'regional',
      phone: '+1-XXX-XXX-XXXX',
      geo: {
        lat: 39.9526,
        lng: -75.1652
      }
    }
  ],

  // Analytics Configuration
  analytics: {
    // Google Analytics 4
    ga4: {
      enabled: false, // Set to true when ready
      measurementId: 'G-XXXXXXXXXX' // Replace with your GA4 ID
    },
    
    // Plausible Analytics (privacy-focused)
    plausible: {
      enabled: false, // Set to true when ready
      domain: 'zic0n.com'
    },
    
    // Event tracking settings
    trackEvents: {
      formSubmissions: true,
      outboundLinks: true,
      fileDownloads: true,
      emailClicks: true,
      phoneClicks: true,
      scrollDepth: true
    }
  },

  // Contact Form Configuration
  contactForm: {
    // FormSpree (https://formspree.io/)
    formspree: {
      enabled: false, // Set to true when configured
      endpoint: 'https://formspree.io/f/YOUR_FORM_ID'
    },
    
    // Netlify Forms
    netlify: {
      enabled: true, // Works automatically on Netlify
    },
    
    // Custom API
    custom: {
      enabled: false,
      endpoint: '/api/contact'
    },
    
    // Messages
    messages: {
      success: 'Thank you! Your message has been sent successfully. We\'ll get back to you soon.',
      error: 'Oops! Something went wrong. Please try again or email us directly at info@zic0n.com',
      validation: 'Please fill in all required fields correctly.'
    }
  },

  // Newsletter Configuration
  newsletter: {
    // Mailchimp
    mailchimp: {
      enabled: false,
      actionUrl: 'https://YOUR_DOMAIN.us1.list-manage.com/subscribe/post?u=YOUR_USER_ID&id=YOUR_LIST_ID'
    },
    
    // ConvertKit
    convertkit: {
      enabled: false,
      formId: 'YOUR_FORM_ID'
    },
    
    // Popup settings
    popup: {
      enabled: false, // Set to true to enable popup
      delay: 15000, // Show after 15 seconds
      showOnExit: true, // Show when user tries to leave
      cookieName: 'newsletter_popup_shown',
      cookieDays: 30 // Don't show again for 30 days
    }
  },

  // Theme Configuration
  theme: {
    default: 'dark', // 'dark' or 'light'
    allowToggle: true,
    respectSystemPreference: true
  },

  // Feature Flags
  features: {
    lazyLoadImages: true,
    breadcrumbs: true,
    backToTop: true,
    themeToggle: true,
    newsletter: false, // Enable when configured
    analytics: false, // Enable when configured
    searchFunctionality: false, // Future feature
    chatWidget: false // Future feature
  },

  // Performance Settings
  performance: {
    lazyLoadOffset: '50px', // Start loading images 50px before viewport
    animationDelay: 100, // Delay between animations (ms)
    debounceDelay: 250 // Debounce delay for scroll/resize events (ms)
  },

  // SEO Settings
  seo: {
    defaultImage: '/images/og-default.jpg',
    twitterHandle: '@zic0n',
    organizationType: 'ProfessionalService',
    foundingDate: '2020', // Update with actual date
    numberOfEmployees: '2-10'
  },

  // Development Settings
  dev: {
    debug: false, // Set to true for console logging
    mockAPI: false // Use mock API responses for testing
  }
};

// Freeze config to prevent accidental modifications
Object.freeze(window.ZICON_CONFIG);

// Log config in development
if (window.ZICON_CONFIG.dev.debug) {
  console.log('Zic0n Config:', window.ZICON_CONFIG);
}
