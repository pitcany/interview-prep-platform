const Database = require('better-sqlite3');
const fs = require('fs');
const path = require('path');
const os = require('os');
require('dotenv').config();
const fetch = require('node-fetch');

function getDatabasePath() {
  const appName = 'interview-prep-platform';
  if (process.platform === 'win32') {
    return path.join(process.env.APPDATA || '', appName, 'interview-prep.db');
  } else if (process.platform === 'darwin') {
    return path.join(os.homedir(), 'Library', 'Application Support', appName, 'interview-prep.db');
  } else {
    return path.join(os.homedir(), '.config', appName, 'interview-prep.db');
  }
}

async function generateWithLocalLLM(title, components, requirements) {
  const baseUrl = process.env.LLM_BASE_URL;
  const model = process.env.LLM_MODEL || 'gpt-oss-20b';
  if (!baseUrl) return null;

  const prompt = `Create a concise, senior-level ML system design sample solution outline for: ${title}\n\nRequirements:\n${requirements.map((r, i) => `${i+1}. ${r}`).join('\n')}\n\nKey Components:\n${components.map((c, i) => `${i+1}. ${c}`).join('\n')}\n\nReturn markdown with headings and bullet points. Include data pipeline, modeling, serving, scalability, and monitoring sections.`;

  try {
    const res = await fetch(`${baseUrl}/v1/chat/completions`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model,
        messages: [
          { role: 'system', content: 'You are a senior ML systems architect.' },
          { role: 'user', content: prompt },
        ],
        temperature: 0.3,
        max_tokens: 1200,
      }),
    });
    if (!res.ok) {
      const t = await res.text();
      console.warn('[ML-SAMPLES] LLM error:', res.status, t);
      return null;
    }
    const data = await res.json();
    const text = data.choices?.[0]?.message?.content || null;
    return text;
  } catch (e) {
    console.warn('[ML-SAMPLES] LLM request failed:', e.message);
    return null;
  }
}

function buildFallbackOutline(title, components, requirements) {
  const compList = components.length ? components.map((c, i) => `${i+1}. ${c}`).join('\n') : '- (not specified)';
  const reqList = requirements.length ? requirements.map((r, i) => `${i+1}. ${r}`).join('\n') : '- (not specified)';
  return `# ${title} — Reference Architecture Outline\n\n## Requirements\n${reqList}\n\n## Key Components\n${compList}\n\n## High-level Architecture\n- Data ingestion (batch + streaming)\n- Offline pipeline (feature engineering, training)\n- Online serving (feature store, low-latency inference)\n- Monitoring & evaluation\n`;
}

function safeArray(value) {
  if (Array.isArray(value)) return value;
  if (typeof value === 'string') {
    try { const p = JSON.parse(value); return Array.isArray(p) ? p : []; } catch { return []; }
  }
  return [];
}

async function main() {
  const dbPath = getDatabasePath();
  console.log('[ML-SAMPLES] DB:', dbPath);
  const db = new Database(dbPath);

  const rows = db.prepare(`
    SELECT q.id as question_id, q.title, ml.sample_solution, ml.key_components, ml.requirements
    FROM ml_design_questions ml
    JOIN questions q ON q.id = ml.question_id
  `).all();

  const update = db.prepare(`
    UPDATE ml_design_questions SET sample_solution = ? WHERE question_id = ?
  `);

  let filled = 0;
  for (const row of rows) {
    if (row.sample_solution && String(row.sample_solution).trim().length > 0) continue;
    const components = safeArray(row.key_components);
    const requirements = safeArray(row.requirements);

    let outline = null;
    outline = await generateWithLocalLLM(row.title || 'ML System', components, requirements);
    if (!outline) outline = buildFallbackOutline(row.title || 'ML System', components, requirements);

    update.run(outline, row.question_id);
    filled += 1;
  }

  console.log(`[ML-SAMPLES] Filled ${filled} missing sample_solution entries.`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
