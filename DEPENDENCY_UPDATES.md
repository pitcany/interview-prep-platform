# Dependency Updates

## Latest Update: 2025-11-13

### ✅ Updated Dependencies

#### Production Dependencies
| Package | Old Version | New Version | Type | Notes |
|---------|-------------|-------------|------|-------|
| @anthropic-ai/sdk | 0.27.0 | 0.68.0 | Major | 41 versions behind - critical security update |
| @monaco-editor/react | 4.6.0 | 4.7.0 | Minor | Safe update |
| @xyflow/react | 12.0.0 | 12.9.3 | Minor | Safe update |
| axios | 1.6.0 | 1.13.2 | Minor | Security fixes |
| clsx | 2.0.0 | 2.1.1 | Minor | Safe update |
| html-to-image | 1.11.11 | 1.11.13 | Patch | Safe update |
| lucide-react | 0.294.0 | 0.553.0 | Minor | Safe update (0.x) |
| openai | 6.8.0 | 6.9.0 | Minor | Safe update |
| react | 18.2.0 | 18.3.1 | Minor | Latest React 18 |
| react-dom | 18.2.0 | 18.3.1 | Minor | Latest React 18 |
| react-router-dom | 6.20.0 | 6.30.2 | Minor | Latest v6 |
| recharts | 2.10.0 | 2.15.4 | Minor | Latest v2 |
| zustand | 4.4.7 | 4.5.7 | Minor | Latest v4 |

#### Development Dependencies
| Package | Old Version | New Version | Type | Notes |
|---------|-------------|-------------|------|-------|
| @types/better-sqlite3 | 7.6.8 | 7.6.11 | Patch | Type updates |
| @types/node | 20.10.0 | 22.12.0 | Major | Node 22 LTS types |
| @types/react | 18.2.42 | 18.3.18 | Minor | Match React 18.3.1 |
| @types/react-dom | 18.2.17 | 18.3.5 | Minor | Match React 18.3.1 |
| @typescript-eslint/eslint-plugin | 6.13.0 | 8.24.1 | Major | Latest stable |
| @typescript-eslint/parser | 6.13.0 | 8.24.1 | Major | Latest stable |
| @vitejs/plugin-react | 4.2.1 | 4.3.4 | Minor | Safe update |
| autoprefixer | 10.4.16 | 10.4.20 | Patch | Safe update |
| concurrently | 8.2.2 | 9.2.0 | Major | Safe major |
| electron | 28.0.0 | 33.4.0 | Major | Latest stable |
| electron-builder | 24.9.1 | 25.2.0 | Major | Match Electron 33 |
| eslint | 8.54.0 | 9.20.0 | Major | Latest stable |
| eslint-plugin-react-hooks | 4.6.0 | 5.2.0 | Major | Match React 18 |
| postcss | 8.4.32 | 8.4.51 | Patch | Safe update |
| tailwindcss | 3.3.6 | 3.4.21 | Minor | Safe update |
| typescript | 5.3.2 | 5.7.3 | Minor | Latest stable |
| vite | 5.0.5 | 6.0.13 | Major | Latest stable |
| vite-plugin-electron | 0.28.0 | 0.28.10 | Patch | Safe update |
| vitest | 1.0.4 | 2.1.9 | Major | Latest stable |
| wait-on | 7.2.0 | 8.0.3 | Major | Safe major |

### 🚧 Deferred Updates (Breaking Changes)

These updates require code changes and extensive testing:

#### date-fns: 2.30.0 → 4.1.0
**Breaking Changes:**
- API changes in formatting functions
- Tree-shaking improvements require code changes
- Some functions removed or renamed

**Migration Effort:** Low (only used in a few places)
**Risk:** Low
**Recommendation:** Update in next maintenance cycle

#### node-fetch: 2.7.0 → 3.3.2
**Breaking Changes:**
- Version 3 is ESM-only (no CommonJS)
- Electron's Node.js integration may have issues with pure ESM
- Requires changing all imports to ESM syntax

**Migration Effort:** Medium (Electron build system changes)
**Risk:** Medium (could break Electron build)
**Recommendation:** Keep on v2 for now, or switch to native `fetch` API (available in Electron 28+)

#### React Ecosystem Major Updates
##### react + react-dom: 18.3.1 → 19.2.0
**Breaking Changes:**
- New React Compiler
- Changes to hooks behavior
- Deprecated APIs removed
- New features: Actions, useOptimistic, useFormStatus

**Migration Effort:** High (need to review all components)
**Risk:** Medium-High
**Recommendation:** Defer until React 19 stabilizes further

##### react-router-dom: 6.30.2 → 7.9.6
**Breaking Changes:**
- Data APIs changed
- Loader/action functions restructured
- Route configuration changes
- Some hooks renamed or removed

**Migration Effort:** High (affects routing throughout app)
**Risk:** High
**Recommendation:** Defer - wait for stable migration guide

##### recharts: 2.15.4 → 3.4.1
**Breaking Changes:**
- TypeScript types restructured
- Some props renamed
- Chart API changes

**Migration Effort:** Medium (only used in Progress page)
**Risk:** Medium
**Recommendation:** Update when refactoring Progress page

##### zustand: 4.5.7 → 5.0.8
**Breaking Changes:**
- Middleware API changes
- TypeScript types improved but different
- Some deprecated APIs removed

**Migration Effort:** Low (simple store, no middleware)
**Risk:** Low
**Recommendation:** Can update after testing

## Security Improvements

### Critical Security Updates Applied
1. **@anthropic-ai/sdk**: 41 versions behind - potential security vulnerabilities fixed
2. **axios**: Multiple security fixes in 1.7.x+ releases
3. **Electron**: Updated from 28 to 33 (multiple security patches)

### Recommended Next Steps
1. Consider migrating from `node-fetch` to native `fetch` API (available in Electron 28+)
2. Plan React 19 migration for Q2 2025
3. Monitor zustand v5 adoption before upgrading
4. Test recharts v3 in development branch

## Testing Checklist

After updating dependencies:
- [x] npm install completes successfully
- [ ] npm run typecheck passes
- [ ] npm run build completes
- [ ] npm run dev starts successfully
- [ ] All critical features work:
  - [ ] Code execution
  - [ ] Monaco Editor
  - [ ] Diagram Editor (React Flow)
  - [ ] Progress charts
  - [ ] LLM API calls

## Rollback Plan

If issues occur:
1. Revert package.json changes
2. Delete node_modules and package-lock.json
3. Run `npm install`
4. Run `npm run build`

## Future Updates

**Watch for:**
- React 19 stable release and migration guides
- React Router v7 stable release
- Node.js 22 LTS adoption patterns in Electron
- Zustand v5 community feedback
