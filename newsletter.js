// Newsletter Signup Handler
// Supports Mailchimp, ConvertKit, or custom API

(function() {
  'use strict';

  // Configuration
  const CONFIG = {
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
    
    // Custom API
    custom: {
      enabled: false,
      endpoint: '/api/newsletter/subscribe'
    },
    
    // Display settings
    popup: {
      enabled: true,
      delay: 15000, // Show after 15 seconds
      showOnExit: true, // Show when user tries to leave
      cookieName: 'newsletter_popup_shown',
      cookieDays: 30 // Don't show again for 30 days
    }
  };

  function initNewsletter() {
    // Initialize inline forms
    const inlineForms = document.querySelectorAll('.newsletter-form');
    inlineForms.forEach(form => {
      form.addEventListener('submit', handleSubmit);
    });

    // Initialize popup if enabled
    if (CONFIG.popup.enabled && !hasSeenPopup()) {
      initPopup();
    }
  }

  async function handleSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const emailInput = form.querySelector('input[type="email"]');
    const submitBtn = form.querySelector('button[type="submit"]');
    const email = emailInput.value.trim();

    // Validate email
    if (!isValidEmail(email)) {
      showMessage(form, 'Please enter a valid email address.', 'error');
      return;
    }

    // Disable button and show loading
    submitBtn.disabled = true;
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Subscribing...';

    try {
      let success = false;

      if (CONFIG.mailchimp.enabled) {
        success = await subscribeMailchimp(email);
      } else if (CONFIG.convertkit.enabled) {
        success = await subscribeConvertKit(email);
      } else if (CONFIG.custom.enabled) {
        success = await subscribeCustom(email);
      } else {
        // Fallback: just show success (no actual subscription)
        success = true;
      }

      if (success) {
        showMessage(form, 'Thank you for subscribing! Check your email for confirmation.', 'success');
        form.reset();
        
        // Track conversion
        if (window.analytics) {
          window.analytics.trackEvent('newsletter_signup', {
            location: form.dataset.location || 'unknown'
          });
        }

        // Close popup if it's in a popup
        const popup = form.closest('.newsletter-popup');
        if (popup) {
          closePopup(popup);
        }
      } else {
        throw new Error('Subscription failed');
      }
    } catch (error) {
      console.error('Newsletter subscription error:', error);
      showMessage(form, 'Something went wrong. Please try again later.', 'error');
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = originalText;
    }
  }

  async function subscribeMailchimp(email) {
    // Note: Direct Mailchimp API calls require CORS proxy or server-side handling
    // This is a simplified example
    const formData = new FormData();
    formData.append('EMAIL', email);

    const response = await fetch(CONFIG.mailchimp.actionUrl, {
      method: 'POST',
      body: formData,
      mode: 'no-cors' // Mailchimp doesn't support CORS
    });

    // With no-cors, we can't read the response, so assume success
    return true;
  }

  async function subscribeConvertKit(email) {
    const response = await fetch(`https://api.convertkit.com/v3/forms/${CONFIG.convertkit.formId}/subscribe`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: email,
        api_key: 'YOUR_API_KEY' // Should be handled server-side
      })
    });

    return response.ok;
  }

  async function subscribeCustom(email) {
    const response = await fetch(CONFIG.custom.endpoint, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ email })
    });

    return response.ok;
  }

  function initPopup() {
    // Create popup HTML
    const popup = document.createElement('div');
    popup.className = 'newsletter-popup fixed inset-0 z-50 hidden items-center justify-center bg-black/50 backdrop-blur-sm';
    popup.innerHTML = `
      <div class="card rounded-2xl p-8 max-w-md mx-4 relative animate-fade-in">
        <button class="popup-close absolute top-4 right-4 text-slate-400 hover:text-white transition" aria-label="Close">
          <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
        
        <div class="text-center mb-6">
          <div class="inline-flex h-16 w-16 rounded-2xl bg-cyan-400/20 items-center justify-center mb-4">
            <svg width="32" height="32" fill="none" stroke="#22d3ee" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
              <polyline points="22,6 12,13 2,6"></polyline>
            </svg>
          </div>
          <h3 class="text-2xl font-bold mb-2">Stay Updated</h3>
          <p class="text-slate-300/90">Get the latest insights on civil engineering, project updates, and industry trends.</p>
        </div>
        
        <form class="newsletter-form" data-location="popup">
          <div class="flex gap-2">
            <input type="email" required placeholder="your.email@example.com" class="flex-1 px-4 py-3 rounded-lg bg-white/5 border border-white/10 focus:outline-none focus:ring-2 focus:ring-cyan-500 text-white transition">
            <button type="submit" class="px-6 py-3 rounded-lg bg-cyan-500 text-black font-semibold hover:bg-cyan-400 transition whitespace-nowrap">
              Subscribe
            </button>
          </div>
        </form>
        
        <p class="text-xs text-slate-400 mt-4 text-center">
          We respect your privacy. Unsubscribe at any time.
        </p>
      </div>
    `;

    document.body.appendChild(popup);

    // Set up event listeners
    const closeBtn = popup.querySelector('.popup-close');
    closeBtn.addEventListener('click', () => closePopup(popup));
    
    popup.addEventListener('click', (e) => {
      if (e.target === popup) {
        closePopup(popup);
      }
    });

    const form = popup.querySelector('.newsletter-form');
    form.addEventListener('submit', handleSubmit);

    // Show popup after delay
    setTimeout(() => showPopup(popup), CONFIG.popup.delay);

    // Show on exit intent
    if (CONFIG.popup.showOnExit) {
      document.addEventListener('mouseout', (e) => {
        if (e.clientY < 0 && !popup.classList.contains('flex')) {
          showPopup(popup);
        }
      });
    }
  }

  function showPopup(popup) {
    popup.classList.remove('hidden');
    popup.classList.add('flex');
    document.body.style.overflow = 'hidden';
  }

  function closePopup(popup) {
    popup.classList.add('hidden');
    popup.classList.remove('flex');
    document.body.style.overflow = '';
    setPopupCookie();
  }

  function hasSeenPopup() {
    return document.cookie.includes(CONFIG.popup.cookieName + '=true');
  }

  function setPopupCookie() {
    const expires = new Date();
    expires.setDate(expires.getDate() + CONFIG.popup.cookieDays);
    document.cookie = `${CONFIG.popup.cookieName}=true; expires=${expires.toUTCString()}; path=/; SameSite=Lax`;
  }

  function isValidEmail(email) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
  }

  function showMessage(form, message, type) {
    // Remove existing message
    const existingMsg = form.querySelector('.newsletter-message');
    if (existingMsg) {
      existingMsg.remove();
    }

    // Create new message
    const msgDiv = document.createElement('div');
    msgDiv.className = `newsletter-message mt-3 p-3 rounded-lg text-sm ${
      type === 'success' 
        ? 'bg-green-500/10 border border-green-500/30 text-green-400' 
        : 'bg-red-500/10 border border-red-500/30 text-red-400'
    }`;
    msgDiv.textContent = message;

    form.appendChild(msgDiv);

    // Auto-remove after 5 seconds
    setTimeout(() => msgDiv.remove(), 5000);
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initNewsletter);
  } else {
    initNewsletter();
  }
})();
