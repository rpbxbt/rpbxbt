# Hi, I'm Reuben (@rpbxbt) 👋

I'm building at the intersection of AI, deep tech, health, and wellness. My mission is **hw/acc** (health & wellness accelerationism) — driving rapid progress toward human flourishing through technology.

## What I'm Building

I'm developing what I call **"Belonging as Knowledge Infrastructure"** — systems that help communities build meaningful connections while leveraging collective intelligence for health and wellness outcomes.

This repository contains a small prototype demonstrating that idea. It loads a list of community members and connections and computes a simple *belonging score*.

Currently working with:
- Claude Code for AI-assisted development
- GitHub Copilot and OpenAI Codex for rapid prototyping
- Prompt engineering and systems architecture for health applications

## Core Principles

**MTSMU** - Maximally Truth-Seeking, Maximally Useful
**HUMMBL** - Highly Useful Mental Model Base Language

These frameworks guide how I approach building technology that genuinely serves human wellbeing.

## Setup

1. Ensure you have Python 3.8+.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the automated tests:
   ```bash
   ./run-tests.sh
   ```

## Example Usage

Use the CLI to compute a belonging score:

```bash
python -m belonging.cli data/sample_data.json
```

Example output:
```
$ python -m belonging.cli data/sample_data.json
Members: Alice, Bob, Charlie, Dana
Belonging score: 0.67
```

## Release Process

Versioned releases are created from Git tags (`vX.Y.Z`). Running `./release.sh` packages the code into `dist/` which is uploaded by the GitHub Actions workflow.
See [CHANGELOG.md](CHANGELOG.md) for details.

## Achievements

- ✅ Automated tests with GitHub Actions
- ✅ Release workflow publishing artifacts
- Prototype demonstrates how community data can be processed to yield useful metrics.

## Let's Collaborate

I'm looking for partners on health & wellness initiatives that create social experiences promoting healthy lifestyles for all. If you're working on:
- Community-driven wellness platforms
- AI applications for preventive health
- Tools that combine human connection with health outcomes

Let's connect. You can check out more of my work at [github.com/rpbxbt](https://github.com/rpbxbt).

## Get in Touch

- Open an [issue](https://github.com/rpbxbt/rpbxbt/issues) or start a discussion.
- Email: **reubenxbt@proton.me**

📍 **Atlanta, GA area?** Let's meet in person! I'm a Performer at Life Time North Druid Hills and offer coaching services.

🏢 **NEXUS AI LLC** - AI Consulting & Development

---

*Building technology that helps humans flourish.*
