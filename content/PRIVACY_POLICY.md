# Privacy Policy

**Effective Date**: [To be determined upon public launch]

**Last Updated**: October 2025

---

## 1. Introduction

This Privacy Policy explains how Scrappy Kin ("we", "us", "our", "the Service") collects, uses, stores, and protects your personal information.

**Core Principle**: We collect only what's necessary to send deletion requests on your behalf. We encrypt your data, host it in the EU, and never share it except as required to provide the Service.

---

## 2. Information We Collect

### 2.1 Information You Provide

When you create an account, we collect:

- **Full name** (for deletion requests)
- **Email address** (for deletion requests and service communications)
- **Mailing address** (street, city, country, postal code - for deletion requests)
- **Account password** (hashed and encrypted)

### 2.2 Information We Generate

We automatically create:

- **Run history records** (timestamps, email counts, success/failure rates)
- **Broker health statistics** (aggregate data about broker responsiveness, no link to your identity)
- **Account metadata** (creation date, last login, account status)

### 2.3 Information We Do NOT Collect

We do NOT collect:

- ❌ Browsing history or tracking cookies
- ❌ IP addresses (except temporarily for security/authentication)
- ❌ Device information or fingerprints
- ❌ Social media profiles or third-party data
- ❌ Payment information (during free beta)
- ❌ Any information beyond what's necessary for deletion requests

---

## 3. How We Use Your Information

### 3.1 Primary Purpose

Your information is used to:

1. **Generate deletion request emails** citing GDPR Article 17 or CCPA rights
2. **Send those emails to data broker companies** on your behalf
3. **Track which requests have been sent** (to avoid duplicates and maintain 6-month cycles)
4. **Send you email reports** with status updates and results

### 3.2 Secondary Purposes

We also use your information to:

- Authenticate you when you log in
- Send service updates and important notifications
- Improve the Service (aggregate, anonymized analysis only)
- Comply with legal obligations

### 3.3 What We Do NOT Do

We do NOT:

- ❌ Sell your information to third parties
- ❌ Use your information for advertising or marketing
- ❌ Share your information with anyone except as described in Section 4
- ❌ Use your information for purposes other than providing the Service

---

## 4. How We Share Your Information

### 4.1 Data Broker Companies (Primary Recipients)

**Purpose**: This is the entire point of the Service.

We send your personal information to data broker companies (privacy@, legal@ email addresses) as part of legally-compliant deletion requests under GDPR/CCPA.

**What they receive**:
- Your full name
- Your email address
- Your mailing address
- The deletion request message

**Why this is necessary**: Data brokers need your information to locate and delete your records from their systems.

### 4.2 Email Service Providers (ESPs)

**Purpose**: To deliver deletion request emails.

We use third-party ESPs to send emails. ESPs process:
- Email sender (your email address)
- Email recipient (broker email address)
- Email content (the deletion request message containing your information)
- Email metadata (timestamps, delivery status)

**Current ESPs**:
- Mailgun (EU region) - https://www.mailgun.com/legal/privacy-policy/

**Why this is necessary**: ESPs are required to deliver emails. This is equivalent to using any email service (Gmail, Outlook, etc.). We select ESPs based on EU data residency and privacy-focused policies.

### 4.3 Hosting Provider

**Purpose**: To store your encrypted data securely.

We host the Service on Hetzner servers in Germany:
- Hetzner: https://www.hetzner.com/legal/privacy-policy/

Hetzner provides infrastructure only and does not have access to your decrypted information.

### 4.4 Who We Do NOT Share With

We do NOT share your information with:

- ❌ Advertisers or marketing companies
- ❌ Analytics services (we use minimal, privacy-respecting analytics only)
- ❌ Social media platforms
- ❌ Data brokers (except to send deletion requests)
- ❌ Government agencies (except if legally required by valid court order)

---

## 5. Data Security

### 5.1 Encryption

- **At rest**: All personal information is encrypted using AES-256 encryption
- **In transit**: All communications use TLS/SSL encryption
- **Database**: Encrypted at the application layer and file system layer

### 5.2 Server Security

- Servers located in Germany (Hetzner datacenter)
- Firewall protection (UFW, only essential ports open)
- SSH key-only access (no password authentication)
- Automatic security updates enabled
- Regular security audits and monitoring

### 5.3 Access Controls

- Access to production systems is strictly limited
- All access is logged and monitored
- No unnecessary services or software installed
- Principle of least privilege enforced

### 5.4 What We Cannot Protect Against

Despite our security measures, no system is 100% secure. We cannot protect against:

- Your account credentials being compromised due to your negligence (weak passwords, phishing, etc.)
- Vulnerabilities in third-party services (ESPs, hosting providers)
- Government surveillance or court-ordered disclosures
- Advanced persistent threats or state-level attacks

**Best practices**:
- Use a strong, unique password
- Enable two-factor authentication (when available)
- Keep your email account secure
- Report suspicious activity immediately

---

## 6. Data Retention

### 6.1 How Long We Keep Your Data

| Data Type | Retention Period |
|-----------|------------------|
| **Minimum Identity information** | Until you delete your account |
| **Account credentials** | Until you delete your account |
| **Run history** | 7 days (automatically purged) |
| **Logs** | 3 days (automatically rotated) |
| **Email reports** | Not stored (sent to you only) |
| **Broker health statistics** | Indefinitely (no personal information) |

### 6.2 Account Deletion

When you delete your account:

1. All personal information is immediately marked for deletion
2. Data is securely erased within 7 days
3. Encrypted backups are purged within 30 days
4. No recovery is possible after deletion

### 6.3 Legal Retention

We may retain certain data longer if required by law (e.g., tax records, legal holds).

---

## 7. Your Privacy Rights

### 7.1 GDPR Rights (EU Users)

Under GDPR, you have the right to:

- **Access**: Request a copy of your personal data
- **Rectification**: Correct inaccurate information
- **Erasure**: Delete your account and all data
- **Restriction**: Limit how we process your data
- **Portability**: Receive your data in a machine-readable format
- **Object**: Object to processing (though this may prevent us from providing the Service)
- **Withdraw consent**: Stop using the Service and delete your account

**How to exercise**: Email us at [contact email] or log into your account.

### 7.2 CCPA Rights (California Users)

Under CCPA, you have the right to:

- Know what personal information we collect and how it's used
- Request deletion of your personal information
- Opt-out of the "sale" of personal information (we don't sell your data)
- Non-discrimination for exercising your rights

**How to exercise**: Email us at [contact email] or log into your account.

### 7.3 Response Time

We will respond to your request within:
- **30 days** for most requests
- **45 days** for complex requests (with notice)

---

## 8. International Data Transfers

### 8.1 Where Your Data Is Stored

Your data is stored on servers in **Germany** (Hetzner datacenter in Nuremberg or Falkenstein).

### 8.2 Data Transfers

**Within EU**: Data stays in the EU. No transfers outside EU for storage or processing.

**Email delivery**: When we send deletion requests to data brokers:
- US-based brokers receive emails containing your information (this is the service purpose)
- EU/international brokers receive emails (as applicable)

**ESP processing**:
- Mailgun EU: Data processed in EU region

### 8.3 Legal Protections

EU data transfers are protected by:
- GDPR compliance
- Standard Contractual Clauses (SCCs) with service providers
- EU-US Data Privacy Framework (where applicable)

---

## 9. Children's Privacy

This Service is not intended for users under 18 years of age.

We do not knowingly collect information from children. If we discover we have collected information from a child under 18, we will delete it immediately.

If you are a parent/guardian and believe your child has created an account, please contact us at [contact email].

---

## 10. Cookies and Tracking

### 10.1 Essential Cookies

We use minimal, essential cookies only:

- **Session cookies**: To keep you logged in
- **Security cookies**: For authentication and fraud prevention

### 10.2 What We Don't Use

We do NOT use:

- ❌ Advertising cookies or pixels
- ❌ Third-party tracking (Google Analytics, Facebook, etc.)
- ❌ Cross-site tracking
- ❌ Behavioral profiling

### 10.3 Your Control

You can disable cookies in your browser, but this may prevent you from using the Service.

---

## 11. Third-Party Services

### 11.1 Services We Use

| Service | Purpose | Privacy Policy |
|---------|---------|----------------|
| **Mailgun** | Email delivery | https://www.mailgun.com/legal/privacy-policy/ |
| **Hetzner** | Server hosting | https://www.hetzner.com/legal/privacy-policy/ |

### 11.2 Your Responsibility

You should review the privacy policies of these services. While we select privacy-focused providers, we cannot control their practices.

---

## 12. Data Breaches

### 12.1 Our Commitment

If a data breach occurs affecting your personal information:

1. We will investigate immediately
2. We will notify you within 72 hours (as required by GDPR)
3. We will notify relevant authorities
4. We will take steps to mitigate harm
5. We will provide you with guidance on protecting yourself

### 12.2 What You Should Do

If you suspect unauthorized access to your account:

1. Change your password immediately
2. Contact us at support@scrappykin.com
3. Monitor your email for suspicious activity
4. Consider changing passwords on other services if you reused passwords

---

## 13. Changes to This Policy

### 13.1 Updates

We may update this Privacy Policy from time to time. Changes will be:

- Posted on our website with an updated "Last Updated" date
- Sent to your email if the changes are material
- Effective 30 days after posting (or immediately if required by law)

### 13.2 Your Acceptance

Continued use of the Service after changes constitutes acceptance of the updated Privacy Policy.

If you do not agree with changes, you may delete your account before the changes take effect.

---

## 14. Contact & Complaints

### 14.1 Contact Us

For privacy-related questions or to exercise your rights:

- **Email**: support@scrappykin.com
- **Website**: https://www.scrappykin.com

### 14.2 Data Protection Authority

If you believe we have mishandled your personal information, you have the right to lodge a complaint with your local data protection authority:

**EU users**: https://edpb.europa.eu/about-edpb/board/members_en

**California users**: California Attorney General's Office - https://oag.ca.gov/

---

## 15. Legal Basis for Processing (GDPR)

We process your personal information under the following legal bases:

- **Article 6(1)(b)**: Performance of contract
  - Processing necessary to provide the Service you signed up for

- **Article 6(1)(f)**: Legitimate interests
  - Your legitimate interest in exercising data protection rights
  - Our legitimate interest in operating the Service

- **Article 6(1)(a)**: Consent
  - Where you've explicitly consented to processing

---

## 16. Summary (TL;DR)

**What we collect**: Name, email, state/province, country, and partial postal code (for deletion requests)

**How we use it**: Generate and send deletion requests to data brokers every 6 months

**How we protect it**: AES-256 encryption, EU servers (Germany), minimal retention

**Who we share with**:
- Data brokers (the whole point)
- Email service providers (to deliver emails)
- No one else

**Your rights**: Access, correct, delete, export your data anytime

**Our commitment**: Privacy-first, EU-hosted, transparent, secure

---

**By creating an account and using Scrappy Kin, you acknowledge that you have read and understood this Privacy Policy.**
