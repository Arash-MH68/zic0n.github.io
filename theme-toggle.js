// Theme Toggle - Dark/Light Mode
// Respects user's system preference and saves choice

(function() {
  'use strict';

  const STORAGE_KEY = 'theme-preference';
  const THEMES = {
    DARK: 'dark',
    LIGHT: 'light',
    AUTO: 'auto'
  };

  // Get initial theme
  function getTheme() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored) return stored;
    
    // Check system preference
    if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return THEMES.DARK;
    }
    
    return THEMES.DARK; // Default to dark
  }

  // Set theme
  function setTheme(theme) {
    const root = document.documentElement;
    
    if (theme === THEMES.LIGHT) {
      root.classList.add('light-theme');
      root.classList.remove('dark-theme');
    } else {
      root.classList.add('dark-theme');
      root.classList.remove('light-theme');
    }
    
    localStorage.setItem(STORAGE_KEY, theme);
    updateToggleButton(theme);
  }

  // Toggle theme
  function toggleTheme() {
    const current = getTheme();
    const next = current === THEMES.DARK ? THEMES.LIGHT : THEMES.DARK;
    setTheme(next);
    
    // Track theme change
    if (window.analytics) {
      window.analytics.trackEvent('theme_toggle', { theme: next });
    }
  }

  // Update toggle button
  function updateToggleButton(theme) {
    const button = document.getElementById('themeToggle');
    if (!button) return;

    const icon = button.querySelector('i');
    if (icon) {
      icon.setAttribute('data-feather', theme === THEMES.LIGHT ? 'moon' : 'sun');
      if (typeof feather !== 'undefined') {
        feather.replace();
      }
    }

    button.setAttribute('aria-label', `Switch to ${theme === THEMES.LIGHT ? 'dark' : 'light'} mode`);
  }

  // Create toggle button
  function createToggleButton() {
    const button = document.createElement('button');
    button.id = 'themeToggle';
    button.className = 'fixed bottom-24 right-8 h-12 w-12 rounded-full bg-cyan-400/20 hover:bg-cyan-400/30 grid place-items-center transition z-40 no-print';
    button.setAttribute('aria-label', 'Toggle theme');
    button.innerHTML = '<i data-feather="sun" class="text-cyan-400"></i>';
    
    button.addEventListener('click', toggleTheme);
    
    document.body.appendChild(button);
    
    if (typeof feather !== 'undefined') {
      feather.replace();
    }
  }

  // Listen for system theme changes
  function watchSystemTheme() {
    const mediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
    
    mediaQuery.addEventListener('change', (e) => {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (!stored || stored === THEMES.AUTO) {
        setTheme(e.matches ? THEMES.DARK : THEMES.LIGHT);
      }
    });
  }

  // Initialize
  function init() {
    // Apply theme immediately (before page renders)
    const theme = getTheme();
    setTheme(theme);
    
    // Create toggle button
    createToggleButton();
    
    // Watch for system theme changes
    watchSystemTheme();
  }

  // Run immediately to prevent flash
  init();
})();
