'use strict';

document.addEventListener('DOMContentLoaded', () => {
  const exclude = document.getElementById('analytics-exclude');
  const include = document.getElementById('analytics-include');
  const status = document.getElementById('analytics-choice-status');
  const analytics = window.scrappyKinAnalytics;
  if (!exclude || !include || !status || !analytics) return;

  const render = () => {
    const automatic = navigator.globalPrivacyControl === true || navigator.doNotTrack === '1';
    if (automatic) {
      status.textContent = 'Your browser sends a privacy signal asking websites not to track you. Scrappy Kin honors that signal and does not count your visits.';
      exclude.hidden = true;
      include.hidden = true;
    } else if (analytics.excluded()) {
      status.textContent = 'Scrappy Kin does not count visits from this browser.';
      exclude.hidden = true;
      include.hidden = false;
    } else {
      status.textContent = 'Scrappy Kin counts visits from this browser.';
      exclude.hidden = false;
      include.hidden = true;
    }
  };
  exclude.addEventListener('click', () => { analytics.exclude(); render(); });
  include.addEventListener('click', () => { analytics.include(); render(); });
  render();
});
