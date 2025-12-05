// Contact Form Handler
// Supports multiple backends: FormSpree, Netlify Forms, or custom API

(function() {
  'use strict';

  // Configuration - Update with your FormSpree endpoint or API
  const CONFIG = {
    // Option 1: FormSpree (https://formspree.io/)
    formspreeEndpoint: 'https://formspree.io/f/YOUR_FORM_ID',
    
    // Option 2: Netlify Forms (automatically detected)
    useNetlify: false,
    
    // Option 3: Custom API endpoint
    customEndpoint: null,
    
    // Success/Error messages
    messages: {
      success: 'Thank you! Your message has been sent successfully. We\'ll get back to you soon.',
      error: 'Oops! Something went wrong. Please try again or email us directly at info@zic0n.com',
      validation: 'Please fill in all required fields correctly.'
    }
  };

  function initContactForm() {
    const form = document.getElementById('contactForm');
    if (!form) return;

    form.addEventListener('submit', handleSubmit);
  }

  async function handleSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const submitBtn = form.querySelector('button[type="submit"]');
    const formData = new FormData(form);
    
    // Validate form
    if (!validateForm(form)) {
      showMessage(CONFIG.messages.validation, 'error');
      return;
    }

    // Disable submit button and show loading state
    submitBtn.disabled = true;
    submitBtn.classList.add('loading');
    const originalText = submitBtn.textContent;
    submitBtn.textContent = 'Sending...';

    try {
      let response;
      
      if (CONFIG.useNetlify) {
        // Netlify Forms
        response = await fetch('/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: new URLSearchParams(formData).toString()
        });
      } else if (CONFIG.customEndpoint) {
        // Custom API
        response = await fetch(CONFIG.customEndpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(Object.fromEntries(formData))
        });
      } else {
        // FormSpree
        response = await fetch(CONFIG.formspreeEndpoint, {
          method: 'POST',
          body: formData,
          headers: {
            'Accept': 'application/json'
          }
        });
      }

      if (response.ok) {
        showMessage(CONFIG.messages.success, 'success');
        form.reset();
        
        // Track conversion (if analytics is set up)
        if (typeof gtag !== 'undefined') {
          gtag('event', 'form_submission', {
            'event_category': 'Contact',
            'event_label': 'Contact Form'
          });
        }
      } else {
        throw new Error('Form submission failed');
      }
    } catch (error) {
      console.error('Form submission error:', error);
      showMessage(CONFIG.messages.error, 'error');
    } finally {
      // Re-enable submit button
      submitBtn.disabled = false;
      submitBtn.classList.remove('loading');
      submitBtn.textContent = originalText;
    }
  }

  function validateForm(form) {
    let isValid = true;
    const inputs = form.querySelectorAll('input[required], textarea[required]');

    inputs.forEach(input => {
      // Remove previous error states
      input.classList.remove('border-red-500');
      
      // Check if empty
      if (!input.value.trim()) {
        isValid = false;
        input.classList.add('border-red-500');
        return;
      }

      // Validate email
      if (input.type === 'email') {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(input.value)) {
          isValid = false;
          input.classList.add('border-red-500');
        }
      }
    });

    return isValid;
  }

  function showMessage(message, type) {
    // Remove existing messages
    const existingMsg = document.querySelector('.form-message');
    if (existingMsg) {
      existingMsg.remove();
    }

    // Create message element
    const msgDiv = document.createElement('div');
    msgDiv.className = `form-message ${type === 'success' ? 'bg-green-500/10 border-green-500 text-green-400' : 'bg-red-500/10 border-red-500 text-red-400'} border rounded-lg p-4 mt-4`;
    msgDiv.setAttribute('role', 'alert');
    msgDiv.textContent = message;

    // Insert after form
    const form = document.getElementById('contactForm');
    form.parentNode.insertBefore(msgDiv, form.nextSibling);

    // Auto-remove after 10 seconds
    setTimeout(() => msgDiv.remove(), 10000);

    // Scroll to message
    msgDiv.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initContactForm);
  } else {
    initContactForm();
  }
})();
