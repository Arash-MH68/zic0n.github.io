// ======= Initialize App ======= 
(function() {
  'use strict';

  // Wait for DOM and feather icons to be ready
  function init() {
    if (typeof feather !== 'undefined') {
      feather.replace();
    }
    
    initializeYear();
    initializeNavigation();
    initializeMobileMenu();
    initializeBackToTop();
    initializeAnimations();
    initializeLazyLoading();
    initializeFormValidation();
  }

  // Set current year in footer
  function initializeYear() {
    const yearEl = document.getElementById('year');
    if (yearEl) {
      yearEl.textContent = new Date().getFullYear();
    }
  }

  // Active navigation highlighting
  function initializeNavigation() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('nav a[href]');
    
    navLinks.forEach(link => {
      const linkHref = link.getAttribute('href');
      if (linkHref === currentPage || (currentPage === '' && linkHref === 'index.html')) {
        link.classList.add('text-cyan-400', 'font-medium');
        link.setAttribute('aria-current', 'page');
      }
    });
  }

  // Mobile menu functionality
  function initializeMobileMenu() {
    const menuBtn = document.getElementById('menuBtn');
    const mobileMenu = document.getElementById('mobileMenu');
    
    if (!menuBtn || !mobileMenu) return;

    menuBtn.addEventListener('click', () => {
      const isHidden = mobileMenu.classList.toggle('hidden');
      const icon = menuBtn.querySelector('i');
      
      // Update ARIA attributes
      menuBtn.setAttribute('aria-expanded', !isHidden);
      
      if (icon) {
        icon.setAttribute('data-feather', isHidden ? 'menu' : 'x');
        if (typeof feather !== 'undefined') {
          feather.replace();
        }
      }
    });

    // Close menu when clicking on links
    const mobileLinks = mobileMenu.querySelectorAll('a');
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
        menuBtn.setAttribute('aria-expanded', 'false');
        
        const icon = menuBtn.querySelector('i');
        if (icon) {
          icon.setAttribute('data-feather', 'menu');
          if (typeof feather !== 'undefined') {
            feather.replace();
          }
        }
      });
    });

    // Close menu on escape key
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && !mobileMenu.classList.contains('hidden')) {
        mobileMenu.classList.add('hidden');
        menuBtn.setAttribute('aria-expanded', 'false');
        menuBtn.focus();
      }
    });
  }

  // Back to top button
  function initializeBackToTop() {
    const backToTopBtn = document.getElementById('backToTop');
    if (!backToTopBtn) return;

    // Show/hide button based on scroll position
    window.addEventListener('scroll', () => {
      if (window.pageYOffset > 300) {
        backToTopBtn.classList.add('visible');
      } else {
        backToTopBtn.classList.remove('visible');
      }
    });

    // Scroll to top on click
    backToTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // Intersection Observer for animations
  function initializeAnimations() {
    if (!('IntersectionObserver' in window)) return;

    const observerOptions = {
      threshold: 0.1,
      rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fade-in');
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    // Observe cards and sections
    document.querySelectorAll('.card, .section > div').forEach(el => {
      observer.observe(el);
    });
  }

  // Lazy load images
  function initializeLazyLoading() {
    if (!('IntersectionObserver' in window)) {
      // Fallback for older browsers
      document.querySelectorAll('img[data-src]').forEach(img => {
        img.src = img.dataset.src;
        if (img.dataset.srcset) {
          img.srcset = img.dataset.srcset;
        }
      });
      return;
    }

    const imageObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const img = entry.target;
          
          // Load the image
          if (img.dataset.src) {
            img.src = img.dataset.src;
          }
          if (img.dataset.srcset) {
            img.srcset = img.dataset.srcset;
          }
          
          // Remove loading class and add loaded class
          img.classList.remove('lazy-loading');
          img.classList.add('lazy-loaded');
          
          imageObserver.unobserve(img);
        }
      });
    }, {
      rootMargin: '50px 0px',
      threshold: 0.01
    });

    // Observe all images with data-src
    document.querySelectorAll('img[data-src]').forEach(img => {
      img.classList.add('lazy-loading');
      imageObserver.observe(img);
    });
  }

  // Form validation
  function initializeFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
      form.addEventListener('submit', (e) => {
        const inputs = form.querySelectorAll('input[required], textarea[required]');
        let isValid = true;

        inputs.forEach(input => {
          if (!input.value.trim()) {
            isValid = false;
            input.classList.add('border-red-500');
            
            // Remove error class on input
            input.addEventListener('input', () => {
              input.classList.remove('border-red-500');
            }, { once: true });
          }
        });

        if (!isValid) {
          e.preventDefault();
          
          // Show error message
          const errorMsg = document.createElement('div');
          errorMsg.className = 'text-red-400 text-sm mt-2';
          errorMsg.textContent = 'Please fill in all required fields.';
          errorMsg.setAttribute('role', 'alert');
          
          const existingError = form.querySelector('[role="alert"]');
          if (existingError) {
            existingError.remove();
          }
          
          form.appendChild(errorMsg);
          
          // Remove error message after 5 seconds
          setTimeout(() => errorMsg.remove(), 5000);
        }
      });
    });
  }

  // Initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Re-initialize feather icons if they load late
  window.addEventListener('load', () => {
    if (typeof feather !== 'undefined') {
      feather.replace();
    }
    
    // Handle video background on contact page
    const drillRigVideo = document.getElementById('drillRigVideo');
    if (drillRigVideo) {
      // Try to play video, fallback to image if it fails
      drillRigVideo.play().catch(() => {
        // If video fails to play, hide it and show poster image
        drillRigVideo.style.display = 'none';
      });
    }
  });
})();
