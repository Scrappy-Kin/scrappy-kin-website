'use strict';

document.addEventListener('DOMContentLoaded', () => {
    const analytics = window.scrappyKinAnalytics;
    const footer = document.querySelector('footer .brand-meta');
    if (!analytics || !footer) return;

    const copy = analytics.copy('scrappykin.com');
    const make = (tag, className, value) => {
        const element = document.createElement(tag);
        if (className) element.className = className;
        if (value) element.textContent = value;
        return element;
    };

    const dialog = make('dialog', 'analytics-consent');
    dialog.setAttribute('aria-labelledby', 'analytics-consent-heading');
    const panel = make('div', 'analytics-consent__panel');
    const close = make('button', 'analytics-consent__close', 'Close privacy choices');
    close.type = 'button';
    close.setAttribute('aria-label', 'Close privacy choices');
    panel.append(close);

    const heading = make('h2', 'analytics-consent__heading', copy.heading);
    heading.id = 'analytics-consent-heading';
    heading.tabIndex = -1;
    panel.append(heading, make('p', 'analytics-consent__purpose', copy.purpose));

    for (const [title, items, className] of [
        [copy.countedHeading, copy.counted, 'analytics-consent__counted'],
        [copy.notCountedHeading, copy.notCounted, 'analytics-consent__not-counted']
    ]) {
        const section = make('section', 'analytics-consent__section');
        section.append(make('h3', 'analytics-consent__label', title));
        const list = make('ul', className);
        for (const item of items) list.append(make('li', '', item));
        section.append(list);
        panel.append(section);
    }

    const status = make('p', 'analytics-consent__status');
    status.setAttribute('role', 'status');
    status.setAttribute('aria-live', 'polite');
    const actions = make('div', 'analytics-consent__actions');
    const decline = make('button', 'analytics-consent__action', copy.decline);
    const accept = make('button', 'analytics-consent__action', copy.accept);
    decline.type = 'button';
    accept.type = 'button';
    actions.append(decline, accept);
    const links = make('p', 'analytics-consent__links');
    const policy = make('a', '', copy.privacyPolicy);
    policy.href = '/privacy.html';
    const terms = make('a', '', copy.terms);
    terms.href = '/tos.html';
    links.append(policy, document.createTextNode(' · '), terms);
    panel.append(status, actions, make('p', 'analytics-consent__change', copy.change), links);
    dialog.append(panel);
    document.body.append(dialog);

    const render = () => {
        const current = analytics.choice();
        accept.disabled = analytics.signalsBlocked() || current === 'unavailable';
        decline.disabled = current === 'unavailable';
        status.textContent = analytics.signalsBlocked() ? copy.signalStatus :
            current === 'accepted' ? copy.acceptedStatus :
            current === 'declined' ? copy.declinedStatus :
            current === 'unavailable' ? copy.unavailableStatus : copy.unsetStatus;
    };
    let opener = null;
    const restoreFocus = () => {
        if (opener && opener.isConnected) opener.focus();
        opener = null;
    };
    const open = (event) => {
        opener = event && event.currentTarget ? event.currentTarget : null;
        render();
        if (!dialog.open) {
            if (dialog.showModal) dialog.showModal();
            else dialog.setAttribute('open', '');
        }
        heading.focus();
    };
    const dismiss = () => {
        if (dialog.close) dialog.close();
        else {
            dialog.removeAttribute('open');
            restoreFocus();
        }
    };
    dialog.addEventListener('close', restoreFocus);
    close.addEventListener('click', dismiss);
    decline.addEventListener('click', () => {
        if (analytics.decline()) dismiss();
        else render();
    });
    accept.addEventListener('click', () => {
        if (analytics.accept()) dismiss();
        else render();
    });

    footer.append(document.createTextNode(' • '));
    const footerButton = make('button', 'analytics-consent__footer-button', copy.choices);
    footerButton.type = 'button';
    footerButton.addEventListener('click', open);
    footer.append(footerButton);
    document.querySelectorAll('[data-analytics-choices]').forEach((button) => {
        button.addEventListener('click', open);
    });

    if (!analytics.signalsBlocked() && ['unset', 'unavailable'].includes(analytics.choice()) &&
        !/^\/privacy(?:[./]|$)/.test(location.pathname)) open();
});
