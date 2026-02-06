---
sidebar_position: 1
---

# Image Generation

Image generation in Arcane Forge is asset-based: one asset can have many generated variants.

## Asset Abstraction

Treat each asset as a persistent object with intent:
- Character sprite
- Environment background
- UI element

Then iterate variants under that asset without losing history.

## Asset Overview and Creation

Use the image overview page to:
- Create assets manually
- Open existing assets
- Generate from design documents when available

`[AF_SCREENSHOT_SPEC id="asset-overview-page" file="./images/asset-overview-page.png" alt="Image asset overview page" capture="Image generation overview page showing asset list and create actions" replace_with="![Image asset overview page](./images/asset-overview-page.png)"]`

## Workflow Selection

Image generation requires a workflow. Choose one of two approaches:
1. Pick a workflow from the workflow library
2. Describe intent in chat and use the recommended workflow

## Prompt and Parameter Tuning

Typical controls include:
- Positive and negative prompts
- Aspect ratio
- Number of outputs
- Background removal when supported

## Review and Selection

Use Recent Generations to inspect results, favorite strong outputs, and download approved assets.

## Current State

Image generation is in early-stage beta. Quality depends on workflow fit and prompt quality. Plan for iteration.

Next: [SFX Generation](/docs/sfx-generation/intro)
