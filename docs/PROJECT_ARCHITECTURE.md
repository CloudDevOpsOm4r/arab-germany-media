# Arab Germany Media - MVP Architecture

## Goal
Build an AI-assisted media pipeline for Arabs in Germany.

## MVP Pipeline
1. Collect news from trusted sources.
2. Remove irrelevant news.
3. Analyze important news with AI.
4. Generate Arabic content.
5. Put content in a human review queue.
6. Publish manually first, automate later.

## Rule
Do not automate publishing before human review.

## Current Modules
- ingest: collect news
- ai: analyze and generate content
- media: create voice/video later
- publish: review and publishing tools
- storage: raw and processed data
- docs: project documentation

## Cost Rule
Use AI only where it adds real value.