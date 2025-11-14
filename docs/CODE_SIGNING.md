# Code Signing Guide

Comprehensive guide to code signing for macOS, Windows, and Linux distributions.

## Table of Contents

- [Why Code Sign?](#why-code-sign)
- [macOS Code Signing](#macos-code-signing)
- [Windows Code Signing](#windows-code-signing)
- [Linux Signing](#linux-signing)
- [Troubleshooting](#troubleshooting)
- [Best Practices](#best-practices)

## Why Code Sign?

### Benefits

1. **Security & Trust**
   - Verifies application hasn't been tampered with
   - Ensures code comes from verified publisher
   - Protects against malware distribution

2. **User Experience**
   - Avoids "Unknown Publisher" warnings
   - Bypasses macOS Gatekeeper restrictions
   - Reduces Windows SmartScreen warnings
   - Increases user confidence

3. **Distribution Requirements**
   - macOS: Required for notarization (mandatory for macOS 10.15+)
   - Windows: Required for SmartScreen reputation
   - Linux: Optional but recommended for enterprise

### Costs

- **macOS:** $99/year (Apple Developer Program)
- **Windows:** $50-$500/year (varies by CA and certificate type)
- **Linux:** Free (self-signed or Let's Encrypt)

## macOS Code Signing

### Prerequisites

1. **Apple Developer Account**
   - Enroll at [developer.apple.com](https://developer.apple.com)
   - Cost: $99/year
   - Approval takes 1-2 business days

2. **macOS Development Machine**
   - macOS 10.15 (Catalina) or later
   - Xcode Command Line Tools
   - Keychain Access app

### Step 1: Create Certificates

#### Generate Certificate Signing Request (CSR)

1. Open **Keychain Access** app
2. **Keychain Access → Certificate Assistant → Request a Certificate from a Certificate Authority**
3. Fill in:
   - **User Email:** Your Apple ID email
   - **Common Name:** Your name or company name
   - **CA Email:** Leave blank
   - **Request:** Saved to disk
   - **Key Pair:** Let Keychain Access create keys
4. Save CSR file (e.g., `CertificateSigningRequest.certSigningRequest`)

#### Create Developer ID Certificate

1. Go to [developer.apple.com/account/resources/certificates](https://developer.apple.com/account/resources/certificates)
2. Click **+** (Add Certificate)
3. Select **Developer ID Application** (for distribution outside App Store)
4. Upload your CSR file
5. Download the certificate (e.g., `developerID_application.cer`)
6. Double-click to install in Keychain Access

#### Verify Installation

```bash
# List available code signing identities
security find-identity -v -p codesigning

# Output should include:
#   1) XXXXXXXXXX "Developer ID Application: Your Name (TEAM_ID)"
```

### Step 2: Configure Electron Builder

Create or update `electron-builder.json5`:

```json5
{
  "appId": "com.yourcompany.interview-prep",
  "productName": "Interview Prep Platform",
  "mac": {
    "category": "public.app-category.education",
    "target": ["dmg", "zip"],
    "icon": "build/icon.icns",

    // Code signing configuration
    "identity": "Developer ID Application: Your Name (TEAM_ID)",
    "hardenedRuntime": true,
    "gatekeeperAssess": false,
    "entitlements": "build/entitlements.mac.plist",
    "entitlementsInherit": "build/entitlements.mac.plist",

    // Notarization (required for macOS 10.15+)
    "notarize": {
      "teamId": "TEAM_ID"
    }
  }
}
```

### Step 3: Create Entitlements File

Create `build/entitlements.mac.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <!-- Allow JIT compilation for V8 JavaScript engine -->
  <key>com.apple.security.cs.allow-jit</key>
  <true/>

  <!-- Allow unsigned executable memory (required for Electron) -->
  <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
  <true/>

  <!-- Disable library validation (required for native modules) -->
  <key>com.apple.security.cs.disable-library-validation</key>
  <true/>

  <!-- Network client access -->
  <key>com.apple.security.network.client</key>
  <true/>

  <!-- Network server (if needed for local LLM) -->
  <key>com.apple.security.network.server</key>
  <true/>

  <!-- File access -->
  <key>com.apple.security.files.user-selected.read-write</key>
  <true/>
</dict>
</plist>
```

**Security Note:** Only include entitlements your app actually needs. Remove unnecessary permissions.

### Step 4: Set Environment Variables

```bash
# Set code signing identity
export CSC_NAME="Developer ID Application: Your Name (TEAM_ID)"

# For notarization
export APPLE_ID="your@email.com"
export APPLE_APP_SPECIFIC_PASSWORD="xxxx-xxxx-xxxx-xxxx"
export APPLE_TEAM_ID="TEAM_ID"
```

**Generate App-Specific Password:**
1. Go to [appleid.apple.com](https://appleid.apple.com)
2. Sign in with your Apple ID
3. Security → App-Specific Passwords
4. Generate new password
5. Copy and save it (won't be shown again)

**Store Credentials Securely:**

```bash
# Store in keychain
xcrun notarytool store-credentials "AC_PASSWORD" \
  --apple-id "your@email.com" \
  --team-id "TEAM_ID" \
  --password "xxxx-xxxx-xxxx-xxxx"

# Then use:
export APPLE_ID="your@email.com"
export APPLE_APP_SPECIFIC_PASSWORD="@keychain:AC_PASSWORD"
```

### Step 5: Build and Sign

```bash
# Build with automatic signing
npm run package:mac

# Output:
# - release/mac/Interview Prep Platform.app (signed)
# - release/Interview Prep Platform-1.0.0.dmg (signed)
# - release/Interview Prep Platform-1.0.0-mac.zip (signed)
```

### Step 6: Verify Signing

```bash
# Verify app signature
codesign -vvv --deep --strict "release/mac/Interview Prep Platform.app"

# Output should be:
#   Interview Prep Platform.app: valid on disk
#   Interview Prep Platform.app: satisfies its Designated Requirement

# Check entitlements
codesign -d --entitlements - "release/mac/Interview Prep Platform.app"

# Verify Gatekeeper will accept it
spctl -a -vvv "release/mac/Interview Prep Platform.app"

# Should show: accepted
```

### Step 7: Notarization

Notarization is automatic if configured correctly in electron-builder, but you can manually notarize:

```bash
# Submit for notarization
xcrun notarytool submit \
  "release/Interview Prep Platform-1.0.0.dmg" \
  --apple-id "your@email.com" \
  --password "xxxx-xxxx-xxxx-xxxx" \
  --team-id "TEAM_ID" \
  --wait

# Check status
xcrun notarytool info <submission-id> \
  --apple-id "your@email.com" \
  --password "xxxx-xxxx-xxxx-xxxx" \
  --team-id "TEAM_ID"

# Staple the ticket (embeds notarization in DMG)
xcrun stapler staple "release/Interview Prep Platform-1.0.0.dmg"

# Verify stapling
xcrun stapler validate "release/Interview Prep Platform-1.0.0.dmg"
```

### Common Issues

**Error: "No identity found"**
```bash
# Check if certificate is installed
security find-identity -v -p codesigning

# If not present, download and install from developer.apple.com
```

**Error: "Failed to parse entitlements"**
- Check XML syntax in `entitlements.mac.plist`
- Ensure proper XML declaration and DOCTYPE
- Validate with: `plutil -lint build/entitlements.mac.plist`

**Error: "Notarization failed: Invalid binary"**
- Ensure hardened runtime is enabled
- Check all entitlements are appropriate
- Verify app is signed correctly before notarizing

## Windows Code Signing

### Prerequisites

1. **Code Signing Certificate**
   - Purchase from Certificate Authority (CA):
     - DigiCert (~$200-500/year)
     - Sectigo (~$100-300/year)
     - GlobalSign (~$200-400/year)
   - Choose: "Code Signing Certificate" or "EV Code Signing"

2. **Certificate Types**
   - **Standard Code Signing:** File-based (.pfx)
   - **EV Code Signing:** Hardware token (USB)
     - Provides immediate SmartScreen reputation
     - More expensive but recommended

### Step 1: Obtain Certificate

#### Standard Certificate

1. Purchase from CA
2. Complete identity verification (business documents required)
3. Download certificate as PFX file
4. Protect with strong password

#### EV Certificate

1. Purchase EV certificate
2. Complete extended validation (takes 3-7 days)
3. Receive USB hardware token
4. Install token drivers

### Step 2: Configure Electron Builder

Update `electron-builder.json5`:

```json5
{
  "win": {
    "target": ["nsis", "zip"],
    "icon": "build/icon.ico",

    // Code signing
    "sign": "./build/sign.js",  // Custom signing (optional)
    "certificateSubjectName": "Your Company Name",  // For EV certs
    "signingHashAlgorithms": ["sha256"],
    "rfc3161TimeStampServer": "http://timestamp.digicert.com"
  },
  "nsis": {
    "oneClick": false,
    "perMachine": false,
    "allowToChangeInstallationDirectory": true,
    "deleteAppDataOnUninstall": false
  }
}
```

### Step 3: Set Environment Variables

**For PFX file:**

```bash
# Windows (PowerShell)
$env:CSC_LINK = "C:\path\to\certificate.pfx"
$env:CSC_KEY_PASSWORD = "your-password"

# Linux/macOS (for cross-compilation)
export CSC_LINK="/path/to/certificate.pfx"
export CSC_KEY_PASSWORD="your-password"
```

**For Windows Certificate Store:**

```bash
# Import certificate to store
certutil -user -p "password" -importpfx My "certificate.pfx"

# Set certificate subject name
$env:CSC_NAME = "Your Company Name"
```

**For EV Certificate (USB token):**

```bash
# No environment variables needed
# electron-builder will find the cert in the token
$env:CSC_KEY_CONTAINER = "USB Token Name"
```

### Step 4: Build and Sign

```bash
# Build for Windows
npm run package:win

# Output:
# - release/win-unpacked/ (unpacked, signed)
# - release/Interview Prep Platform Setup 1.0.0.exe (signed installer)
# - release/Interview Prep Platform-1.0.0-win.zip (signed, portable)
```

### Step 5: Verify Signing

```powershell
# Verify signature
Get-AuthenticodeSignature "release\Interview Prep Platform Setup 1.0.0.exe"

# Should show:
#   SignerCertificate: [Certificate details]
#   TimeStamperCertificate: [Certificate details]
#   Status: Valid

# Check signature in Explorer
# Right-click → Properties → Digital Signatures tab
```

### Custom Signing Script

For advanced control, create `build/sign.js`:

```javascript
const { execSync } = require('child_process');

exports.default = async function(configuration) {
  // configuration.path = file to sign

  // Use signtool.exe directly
  execSync(`signtool sign /f "certificate.pfx" /p "password" /tr http://timestamp.digicert.com /td sha256 /fd sha256 "${configuration.path}"`, {
    stdio: 'inherit'
  });
};
```

### Windows SmartScreen Reputation

**Problem:** Even signed apps show SmartScreen warning initially.

**Solution:**
1. Use **EV Certificate** (instant reputation)
2. Or build reputation over time:
   - Users click "More info" → "Run anyway"
   - After ~100+ downloads, warning disappears
   - Can take weeks to months

### Common Issues

**Error: "SignTool Error: No certificates were found"**
```powershell
# Check certificate store
certutil -user -store My

# If not present, import it
certutil -user -p "password" -importpfx My "certificate.pfx"
```

**Error: "SignTool Error: An unexpected internal error"**
- Install Windows SDK: [developer.microsoft.com](https://developer.microsoft.com/windows/downloads/windows-sdk)
- Ensure signtool.exe is in PATH

**SmartScreen still warns after signing**
- Standard certificates don't have immediate reputation
- Consider EV certificate
- Wait for reputation to build (100+ downloads)

## Linux Signing

Linux doesn't require code signing like macOS/Windows, but you can sign packages for verification.

### AppImage Signing

```bash
# Generate GPG key (if you don't have one)
gpg --full-generate-key

# List keys
gpg --list-secret-keys

# Sign AppImage
gpg --armor --detach-sign "Interview Prep Platform-1.0.0.AppImage"

# Creates: Interview Prep Platform-1.0.0.AppImage.asc

# Users verify with:
gpg --verify "Interview Prep Platform-1.0.0.AppImage.asc" "Interview Prep Platform-1.0.0.AppImage"
```

### Debian Package Signing

```bash
# Sign .deb package
dpkg-sig --sign builder "Interview Prep Platform_1.0.0_amd64.deb"

# Verify
dpkg-sig --verify "Interview Prep Platform_1.0.0_amd64.deb"
```

### RPM Package Signing

```bash
# Configure RPM signing in ~/.rpmmacros
echo "%_gpg_name Your Name" >> ~/.rpmmacros

# Sign RPM
rpm --addsign "Interview Prep Platform-1.0.0.x86_64.rpm"

# Verify
rpm --checksig "Interview Prep Platform-1.0.0.x86_64.rpm"
```

## Troubleshooting

### macOS

**"code object is not signed at all"**
- Certificate not installed or expired
- Run: `security find-identity -v -p codesigning`
- Reinstall certificate if needed

**"errSecInternalComponent"**
- Keychain locked
- Open Keychain Access and unlock
- Or: `security unlock-keychain -p <password> ~/Library/Keychains/login.keychain-db`

**"App is damaged and can't be opened"**
- App not notarized
- User can bypass: `xattr -cr "/path/to/app"`
- Properly notarize for distribution

### Windows

**"Failed to sign: SignerSign() failed"**
- Certificate password incorrect
- Certificate expired
- USB token not connected (for EV certs)

**"Timestamp server unavailable"**
- Network issue
- Try different timestamp server:
  - `http://timestamp.comodoca.com`
  - `http://timestamp.globalsign.com`
  - `http://timestamp.sectigo.com`

**"The specified PFX password is not correct"**
- Check `CSC_KEY_PASSWORD` environment variable
- Verify password with: `openssl pkcs12 -info -in certificate.pfx`

### General

**Build works locally but fails in CI**
- Secrets not configured in CI environment
- Use GitHub Actions secrets / GitLab CI variables
- Never commit certificates to repository

**"Module version mismatch" after signing**
- Rebuild native modules: `npx @electron/rebuild`
- Clear build cache: `rm -rf node_modules/.cache`

## Best Practices

### Security

1. **Protect Certificates**
   - Never commit certificates to Git
   - Store in secure location (encrypted)
   - Use hardware tokens when possible (EV certs)

2. **Rotate Certificates**
   - Track expiration dates
   - Renew before expiry
   - Update signed apps before certificate expires

3. **Use Strong Passwords**
   - Use password manager
   - Don't hardcode in scripts
   - Use environment variables or keychain

### Automation

1. **CI/CD Integration**

```yaml
# GitHub Actions example
- name: Build and Sign (macOS)
  env:
    CSC_NAME: ${{ secrets.CSC_NAME }}
    APPLE_ID: ${{ secrets.APPLE_ID }}
    APPLE_APP_SPECIFIC_PASSWORD: ${{ secrets.APPLE_PASSWORD }}
    APPLE_TEAM_ID: ${{ secrets.APPLE_TEAM_ID }}
  run: npm run package:mac

- name: Build and Sign (Windows)
  env:
    CSC_LINK: ${{ secrets.CSC_LINK }}
    CSC_KEY_PASSWORD: ${{ secrets.CSC_KEY_PASSWORD }}
  run: npm run package:win
```

2. **Testing**
   - Test signed builds on clean machines
   - Verify SmartScreen/Gatekeeper status
   - Check notarization status

3. **Documentation**
   - Document certificate details (expiry, provider)
   - Keep renewal instructions updated
   - Document troubleshooting steps

### Distribution

1. **Verify Before Release**
   - Test signed app on clean VM
   - Check all platforms (if multi-platform)
   - Verify no security warnings

2. **Communicate with Users**
   - Provide SHA-256 checksums
   - Document how to verify signatures
   - Explain security warnings (if any)

## Cost Comparison

| Platform | Required? | Cost/Year | Benefits |
|----------|-----------|-----------|----------|
| **macOS - Standard** | Yes (for notarization) | $99 | Required for macOS 10.15+ |
| **Windows - Standard** | No (but recommended) | $100-500 | Reduces SmartScreen warnings |
| **Windows - EV** | No (but recommended) | $300-700 | Instant SmartScreen reputation |
| **Linux** | No | Free | Optional package verification |

## Further Reading

- [Apple Code Signing Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/CodeSigningGuide/Introduction/Introduction.html)
- [Notarizing macOS Software](https://developer.apple.com/documentation/security/notarizing_macos_software_before_distribution)
- [Windows Code Signing Best Practices](https://docs.microsoft.com/en-us/windows-hardware/drivers/install/code-signing-best-practices)
- [electron-builder Code Signing](https://www.electron.build/code-signing)

## Quick Reference

### Environment Variables

```bash
# macOS
export CSC_NAME="Developer ID Application: Name (TEAM_ID)"
export APPLE_ID="your@email.com"
export APPLE_APP_SPECIFIC_PASSWORD="xxxx-xxxx-xxxx-xxxx"
export APPLE_TEAM_ID="TEAM_ID"

# Windows
export CSC_LINK="/path/to/certificate.pfx"
export CSC_KEY_PASSWORD="password"

# Disable signing (for testing)
export CSC_IDENTITY_AUTO_DISCOVERY=false
```

### Verification Commands

```bash
# macOS
codesign -vvv --deep --strict "app.app"
spctl -a -vvv "app.app"
xcrun stapler validate "app.dmg"

# Windows
Get-AuthenticodeSignature "app.exe"

# Linux
gpg --verify "app.AppImage.asc" "app.AppImage"
```
