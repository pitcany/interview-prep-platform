# Deployment Guide

This guide covers building, packaging, and deploying the Interview Prep Platform to production.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Environment Configuration](#environment-configuration)
- [Building for Production](#building-for-production)
- [Platform-Specific Instructions](#platform-specific-instructions)
- [Code Signing](#code-signing)
- [Distribution](#distribution)
- [Post-Deployment](#post-deployment)
- [Troubleshooting](#troubleshooting)

## Prerequisites

### System Requirements

**Development Machine:**
- Node.js 22.12.0 or later (required for native module compilation)
- npm 10+ or yarn
- Python 3.8+ (for code execution service)
- Git

**For macOS builds:**
- macOS 10.15+ (Catalina or later)
- Xcode Command Line Tools
- Apple Developer account (for code signing)

**For Windows builds:**
- Windows 10/11
- Visual Studio Build Tools or Visual Studio 2019/2022
- Windows SDK
- Code signing certificate (optional)

**For Linux builds:**
- Ubuntu 20.04+ / Debian 11+ / Fedora 36+ (or equivalent)
- gcc/g++ 10+
- Build essentials
- libgtk-3-dev, libnotify-dev, libnss3-dev (for Electron)

### Dependencies

```bash
# Install Node.js dependencies
npm install

# Install Python dependencies
cd python-service
pip install -r requirements.txt
cd ..

# Rebuild native modules for Electron
npx @electron/rebuild
```

## Environment Configuration

### Production Environment Variables

Create a `.env.production` file in the project root:

```bash
# LLM Provider Configuration (choose one)

# Option 1: Local LLM (vLLM, llama.cpp, etc.)
LLM_BASE_URL=http://localhost:8000
LLM_MODEL=gpt-oss-20b

# Option 2: Claude API
CLAUDE_API_KEY=sk-ant-api03-your-key-here

# Option 3: OpenAI API
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4o

# Code Execution Configuration
SANDBOX_MODE=local  # 'local' or 'docker' (docker not yet implemented)
MAX_EXECUTION_TIME=10000  # milliseconds
MAX_MEMORY=512  # MB

# Application Settings
NODE_ENV=production
```

**Important:** Never commit `.env.production` to version control. Use `.env.example` as a template.

### Database Setup

The production build will initialize the database on first run. To pre-seed the database:

```bash
# Initialize schema and seed questions
npm run db:setup
```

Database locations by platform:
- **Linux:** `~/.config/interview-prep-platform/interview-prep.db`
- **macOS:** `~/Library/Application Support/interview-prep-platform/interview-prep.db`
- **Windows:** `%APPDATA%\interview-prep-platform\interview-prep.db`

## Building for Production

### Full Production Build

```bash
# 1. Install dependencies
npm install

# 2. Build React frontend
npm run build:react

# 3. Build Electron main process
npm run build:electron

# 4. Package for current platform
npm run package

# Or package for specific platform
npm run package:mac     # macOS
npm run package:win     # Windows
npm run package:linux   # Linux
```

### Build Output

Packaged applications are output to the `release/` directory:

```
release/
├── win-unpacked/              # Windows unpacked (for testing)
├── mac/                       # macOS .app bundle
├── linux-unpacked/            # Linux unpacked
├── interview-prep-platform-1.0.0.dmg          # macOS installer
├── interview-prep-platform-1.0.0.exe          # Windows installer
├── interview-prep-platform-1.0.0.AppImage     # Linux AppImage
└── interview-prep-platform-1.0.0.deb          # Debian package
```

## Platform-Specific Instructions

### macOS Deployment

#### Build Requirements

```bash
# Install Xcode Command Line Tools
xcode-select --install

# Verify installation
xcode-select -p
# Should output: /Library/Developer/CommandLineTools
```

#### Build and Package

```bash
# Build for macOS (on macOS machine)
npm run package:mac

# Output files:
# - release/mac/interview-prep-platform.app (app bundle)
# - release/interview-prep-platform-1.0.0.dmg (installer)
# - release/interview-prep-platform-1.0.0-mac.zip (zip archive)
```

#### Code Signing (Required for Distribution)

See [Code Signing](#code-signing) section below.

#### Notarization (Required for macOS 10.15+)

```bash
# After building, notarize the app
xcrun notarytool submit \
  release/interview-prep-platform-1.0.0.dmg \
  --apple-id "your@email.com" \
  --password "app-specific-password" \
  --team-id "TEAM_ID" \
  --wait

# Staple the notarization ticket
xcrun stapler staple release/interview-prep-platform-1.0.0.dmg
```

#### Universal Builds (Apple Silicon + Intel)

Update `electron-builder.json5`:

```json5
{
  "mac": {
    "target": {
      "target": "dmg",
      "arch": ["x64", "arm64"]
    }
  }
}
```

Then build:

```bash
npm run package:mac
```

### Windows Deployment

#### Build Requirements

```bash
# Install Windows Build Tools (as Administrator)
npm install --global windows-build-tools

# Or install Visual Studio Build Tools manually
# Download from: https://visualstudio.microsoft.com/downloads/
```

#### Build and Package

```bash
# Build for Windows (on Windows machine or cross-compile)
npm run package:win

# Output files:
# - release/win-unpacked/ (unpacked directory)
# - release/interview-prep-platform-1.0.0.exe (NSIS installer)
# - release/interview-prep-platform-1.0.0-win.zip (zip archive)
```

#### Code Signing (Optional but Recommended)

Windows Defender SmartScreen will warn users about unsigned applications.

```bash
# Set environment variables for signing
$env:CSC_LINK = "path\to\certificate.pfx"
$env:CSC_KEY_PASSWORD = "certificate-password"

# Build with signing
npm run package:win
```

See [Code Signing](#code-signing) section for details.

#### Cross-Compiling from Linux/macOS

```bash
# Install wine (for cross-compilation)
# On macOS:
brew install wine

# On Linux:
sudo apt-get install wine64

# Build
npm run package:win
```

### Linux Deployment

#### Build Requirements

```bash
# Ubuntu/Debian
sudo apt-get install -y build-essential \
  libgtk-3-dev libnotify-dev libnss3-dev \
  libxss1 libxtst6 libatspi2.0-0 libsecret-1-0

# Fedora/RHEL
sudo dnf install -y @development-tools \
  gtk3-devel libnotify-devel nss-devel \
  libXScrnSaver libXtst libatspi libsecret
```

#### Build and Package

```bash
# Build for Linux
npm run package:linux

# Output files:
# - release/linux-unpacked/ (unpacked directory)
# - release/interview-prep-platform-1.0.0.AppImage (AppImage)
# - release/interview-prep-platform-1.0.0.deb (Debian package)
# - release/interview-prep-platform-1.0.0.rpm (RPM package)
```

#### Distribution Formats

**AppImage (Universal):**
```bash
# Make executable
chmod +x release/interview-prep-platform-1.0.0.AppImage

# Run
./release/interview-prep-platform-1.0.0.AppImage
```

**Debian Package:**
```bash
# Install
sudo dpkg -i release/interview-prep-platform-1.0.0.deb

# If dependencies missing:
sudo apt-get install -f
```

**RPM Package:**
```bash
# Install
sudo rpm -i release/interview-prep-platform-1.0.0.rpm

# Or using dnf:
sudo dnf install release/interview-prep-platform-1.0.0.rpm
```

## Code Signing

### Why Code Sign?

- **Security:** Verifies the application hasn't been tampered with
- **Trust:** Users can verify the publisher
- **SmartScreen/Gatekeeper:** Avoids security warnings on macOS/Windows

### macOS Code Signing

#### Obtain Certificate

1. Join Apple Developer Program ($99/year)
2. Create a Developer ID Application certificate at [developer.apple.com](https://developer.apple.com)
3. Download and install the certificate in Keychain Access

#### Configure Signing

```bash
# Set environment variables
export CSC_NAME="Developer ID Application: Your Name (TEAM_ID)"
export APPLE_ID="your@email.com"
export APPLE_APP_SPECIFIC_PASSWORD="xxxx-xxxx-xxxx-xxxx"
export APPLE_TEAM_ID="TEAM_ID"

# Build with signing
npm run package:mac
```

Or configure in `electron-builder.json5`:

```json5
{
  "mac": {
    "identity": "Developer ID Application: Your Name (TEAM_ID)",
    "hardenedRuntime": true,
    "gatekeeperAssess": false,
    "entitlements": "build/entitlements.mac.plist",
    "entitlementsInherit": "build/entitlements.mac.plist"
  }
}
```

#### Entitlements

Create `build/entitlements.mac.plist`:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>com.apple.security.cs.allow-unsigned-executable-memory</key>
  <true/>
  <key>com.apple.security.cs.disable-library-validation</key>
  <true/>
  <key>com.apple.security.network.client</key>
  <true/>
</dict>
</plist>
```

### Windows Code Signing

#### Obtain Certificate

Purchase a code signing certificate from:
- DigiCert
- Sectigo
- GlobalSign

Or use a self-signed certificate for testing:

```powershell
# Create self-signed certificate (testing only)
New-SelfSignedCertificate -Type CodeSigningCert `
  -Subject "CN=Your Name" `
  -KeyAlgorithm RSA -KeyLength 2048 `
  -CertStoreLocation "Cert:\CurrentUser\My" `
  -NotAfter (Get-Date).AddYears(3)

# Export certificate
$cert = Get-ChildItem -Path Cert:\CurrentUser\My | Where-Object {$_.Subject -match "Your Name"}
$pwd = ConvertTo-SecureString -String "password" -Force -AsPlainText
Export-PfxCertificate -Cert $cert -FilePath "certificate.pfx" -Password $pwd
```

#### Configure Signing

```bash
# Windows (PowerShell)
$env:CSC_LINK = "C:\path\to\certificate.pfx"
$env:CSC_KEY_PASSWORD = "password"

# Linux/macOS (cross-compile)
export CSC_LINK="/path/to/certificate.pfx"
export CSC_KEY_PASSWORD="password"

# Build
npm run package:win
```

## Distribution

### Direct Download

Host the installers on your website or file hosting service:

```
https://your-site.com/downloads/
├── interview-prep-platform-1.0.0.dmg
├── interview-prep-platform-1.0.0.exe
├── interview-prep-platform-1.0.0.AppImage
└── interview-prep-platform-1.0.0.deb
```

### GitHub Releases

1. Create a new release on GitHub
2. Upload platform-specific installers as assets
3. Users download from releases page

```bash
# Using GitHub CLI
gh release create v1.0.0 \
  release/*.dmg \
  release/*.exe \
  release/*.AppImage \
  release/*.deb \
  --title "v1.0.0 - Initial Release" \
  --notes "See CHANGELOG.md for details"
```

### Auto-Updates (Optional)

To enable auto-updates, configure `electron-updater`:

```javascript
// electron/main.ts
import { autoUpdater } from 'electron-updater';

autoUpdater.checkForUpdatesAndNotify();
```

Configure update server in `electron-builder.json5`:

```json5
{
  "publish": {
    "provider": "github",
    "owner": "your-username",
    "repo": "interview-prep-platform"
  }
}
```

## Post-Deployment

### Verify Installation

**macOS:**
```bash
# Check signing
codesign -vvv --deep --strict /Applications/interview-prep-platform.app
spctl -a -vvv /Applications/interview-prep-platform.app

# Check notarization
spctl -a -t exec -vv /Applications/interview-prep-platform.app
```

**Windows:**
```powershell
# Check signature
Get-AuthenticodeSignature "interview-prep-platform.exe"

# Should show "Valid" status
```

**Linux:**
```bash
# Verify AppImage
./interview-prep-platform.AppImage --appimage-signature

# Check .deb package
dpkg-deb --info interview-prep-platform.deb
```

### First Run Configuration

Users must configure LLM provider on first run:

1. Create `.env` file in app directory or set environment variables
2. Configure one of:
   - Local LLM: `LLM_BASE_URL` and `LLM_MODEL`
   - Claude API: `CLAUDE_API_KEY`
   - OpenAI API: `OPENAI_API_KEY`
3. Restart application

### Database Initialization

Database is automatically created on first run at:
- macOS: `~/Library/Application Support/interview-prep-platform/`
- Windows: `%APPDATA%\interview-prep-platform\`
- Linux: `~/.config/interview-prep-platform/`

To pre-populate with questions, users can run:
```bash
npm run db:setup
```

## Troubleshooting

### Build Errors

**Error: "Module version mismatch"**
```bash
# Rebuild native modules
npx @electron/rebuild
npm run build:electron
```

**Error: "Cannot find module 'better-sqlite3'"**
```bash
# Clean and reinstall
rm -rf node_modules package-lock.json
npm install
npx @electron/rebuild
```

**Error: "Code signing failed"**
```bash
# Verify certificate
# macOS:
security find-identity -v -p codesigning

# Windows:
certutil -user -store My

# If missing, disable signing temporarily:
export CSC_IDENTITY_AUTO_DISCOVERY=false
npm run package
```

### Runtime Issues

**"Application can't be opened" (macOS)**
- App is not notarized or signed
- User needs to: System Preferences → Security & Privacy → Open Anyway
- Or: `sudo xattr -rd com.apple.quarantine /Applications/interview-prep-platform.app`

**"Windows protected your PC" (Windows)**
- App is not signed
- Click "More info" → "Run anyway"
- Or sign the application

**Database errors on first run**
```bash
# Manually initialize database
npm run db:init
python3 scripts/import_all_questions.py
```

### Performance Issues

**Slow startup:**
- Database initialization on first run (expected)
- Check LLM service availability (can delay startup)
- Verify enough disk space for database

**High memory usage:**
- Monaco Editor and React Flow are memory-intensive
- Expected: 200-500MB RAM usage
- If >1GB, check for memory leaks in custom components

### Getting Help

- Check [TROUBLESHOOTING.md](./TROUBLESHOOTING.md)
- Review [GitHub Issues](https://github.com/your-repo/issues)
- Check Electron logs:
  - macOS: `~/Library/Logs/interview-prep-platform/`
  - Windows: `%USERPROFILE%\AppData\Roaming\interview-prep-platform\logs\`
  - Linux: `~/.config/interview-prep-platform/logs/`

## Next Steps

- [Code Signing Guide](./CODE_SIGNING.md) - Detailed signing instructions
- [Troubleshooting Guide](./TROUBLESHOOTING.md) - Common issues and fixes
- [IPC API Documentation](./IPC_API.md) - For extending functionality
- [Contributing Guide](../CONTRIBUTING.md) - For developers

## Security Checklist

Before production deployment:

- [ ] Code signing configured and working
- [ ] LLM API keys secured (not in code)
- [ ] Database path secured (user data directory)
- [ ] Code execution sandboxed properly
- [ ] Auto-updates configured (if applicable)
- [ ] Error reporting configured (if applicable)
- [ ] Security audit performed
- [ ] Penetration testing completed
- [ ] Privacy policy published
- [ ] Terms of service published
