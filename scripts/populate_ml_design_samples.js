const Database = require('better-sqlite3');
const fs = require('fs');
const path = require('path');
const os = require('os');

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

/**
 * Populates ml_design_questions.sample_solution where empty using structured outlines.
 * If sample exists in SQL seed, leaves it intact.
 */
function main() {
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
  db.transaction(() => {
    rows.forEach((row) => {
      if (row.sample_solution && row.sample_solution.trim().length > 0) return;
      const components = safeArray(row.key_components);
      const requirements = safeArray(row.requirements);
      const outline = buildOutline(row.title || 'ML System', components, requirements);
      update.run(outline, row.question_id);
      filled += 1;
    });
  })();

  console.log(`[ML-SAMPLES] Filled ${filled} missing sample_solution entries.`);
}

function safeArray(value) {
  if (Array.isArray(value)) return value;
  if (typeof value === 'string') {
    try { const p = JSON.parse(value); return Array.isArray(p) ? p : []; } catch { return []; }
  }
  return [];
}

function buildOutline(title, components, requirements) {
  const compList = components.length ? components.map((c, i) => `${i+1}. ${c}`).join('\n') : '- (not specified)';
  const reqList = requirements.length ? requirements.map((r, i) => `${i+1}. ${r}`).join('\n') : '- (not specified)';
  return `# ${title} — Reference Architecture Outline

## Requirements
${reqList}

## Key Components
${compList}

## High-level Architecture
- Data ingestion (batch + streaming via Kafka/Kinesis)
- Offline pipeline (data lake, feature engineering, model training)
- Online serving (feature store online, low-latency model inference)
- Orchestration (Airflow/Argo)
- Storage (object store, OLAP for analytics)
- Monitoring & observability (data, model, system)

## Data Pipeline
- Schema management & validation (Great Expectations)
- Backfills and reprocessing strategy
- Feature computation (batch + streaming parity)
- Feature store (offline/online consistency)

## Modeling
- Baselines and candidate models
- Online vs offline inference considerations
- Personalization/segmentation
- Fairness and responsible AI considerations

## Serving & Scaling
- Latency SLOs, caching, canary rollouts
- AB testing, guardrails, circuit breakers
- Cost controls & efficiency

## Monitoring & Evaluation
- Online metrics and alerting (e.g., drift, CTR, conversion)
- Shadow evaluation, replay tests
- Incident response runbooks
`;
}

main();
