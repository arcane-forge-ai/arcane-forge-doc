# What is Arcane Forge?

Arcane Forge is an AI-powered game development platform for builders who want to create real, commercial-grade games — games you can ship, sell, or confidently put into a professional portfolio.

It is designed for developers, designers, and small teams who want to use AI as a production accelerator, not as a black box that replaces decision-making.

---

## Who Arcane Forge Is For

Arcane Forge is built for people who want to finish games, not just generate demos.

Typical users include:
- Indie game developers shipping commercial titles
- Small studios building prototypes or vertical slices
- Designers who want to go beyond GDDs and actually build playable content
- Engineers who want AI tools without stitching together dozens of disconnected services

You do not need to be an AI expert.
You do not need to be an engineer to get value.
But you do need to care about building something real.

---

## The Problem Arcane Forge Solves

Today, game developers who use AI face the same issues repeatedly:

- AI tools are fragmented across many products
- Context is lost between tools (design → code → assets)
- Outputs are hard to control or reproduce
- Users constantly copy/paste prompts, specs, and results
- “One-prompt” systems feel magical but are unreliable in production

Arcane Forge solves this by bringing multiple AI tools into a single shared environment with a consistent context and workflow.

Instead of treating AI as isolated generators, Arcane Forge treats AI as collaborators inside a production pipeline.

---

## What Arcane Forge Is (and How It Thinks)

Arcane Forge provides:
- A unified workspace for game development
- AI tools that share the same project context
- Structured workflows aligned with game and software best practices
- Human-controlled decision points at every stage

The core philosophy is:

Human first. AI second.

AI exists to:
- accelerate your work
- reduce repetitive effort
- surface options and tradeoffs
- help you iterate faster

AI does not replace:
- your creative intent
- your design judgment
- your ownership of the final result

Arcane Forge helps you build the game you want to build, not the game an AI happens to output.

---

## What Arcane Forge Is Not

Arcane Forge is not:
- A “one prompt → full game” generator
- A black-box system where logic and decisions are hidden
- A replacement for thinking, designing, or reviewing work

While future versions may automate more steps as reliability improves, the current system intentionally avoids magic-only workflows.

Every major step is:
- visible
- reviewable
- editable by the user

---

## Workflow Is Power

Arcane Forge strongly believes that workflow matters more than raw model power.

The platform provides:
- opinionated but flexible workflows
- best practices for game and software development
- guidance without forcing automation

You can follow the workflow, adapt it, or override it — but you always know what is happening and why.

---

## Builder-Biased by Design

Arcane Forge is intentionally biased toward people who will:
- live with the code they generate
- maintain the assets they create
- ship and support the games they build

That means:
- reliability over novelty
- consistency over surprise
- iteration over one-off generation

If you already have:
- artists, you can use them
- engineers, you can integrate their work
- external tools, you don’t have to replace them

Arcane Forge exists to boost your speed, not force you into an all-AI workflow.

---

## Not Just for Engineers

Arcane Forge is built for cross-disciplinary teams.

Examples:
- Designers can generate visuals, explore mechanics, and scaffold code
- Non-programmers can follow guided code generation flows
- Engineers can stay in control of architecture and logic
- Artists can collaborate without being replaced

If you want to use AI lightly, you can.
If you want to go deep, you can.
Nothing is mandatory.

---

## What to Read Next

- Core Concepts → What is a Project? How context works
- Get Started → Creating your first project
- Ideation → Turning intent into structured design
- Production → Code, images, assets, and music
- Iteration → Refining and evaluating your game

---

# What Is a Project in Arcane Forge?

A **Project** is the core unit of work in Arcane Forge.

Everything you do in Arcane Forge — using AI tools, generating assets, writing code, iterating on ideas — happens **inside a project**. A project is not just a folder; it is a shared context that connects all tools, outputs, and collaborators together.

If Arcane Forge is your workshop, a project is the bench where a specific game lives.

---

## Why Projects Exist

AI tools become unreliable when they lose context.

In many tools today, design ideas, prompts, generated assets, and code live in separate places. Context is constantly copied, rewritten, or lost, which makes results inconsistent and hard to build on.

Arcane Forge projects exist to solve this problem.

A project provides:
- A persistent context shared across AI tools
- A single place where design, code, assets, and iterations stay connected
- A clear boundary between different games or experiments

This allows AI outputs to be more consistent, controllable, and reusable over time.

---

## Creating a Project

When you log into Arcane Forge, the first thing you see is the **Projects Dashboard**.

From here, you can:
- View all existing projects
- Create a new project
- Edit or delete projects you own

Creating a project is intentionally simple. Right now, a project requires only:
- **Project name** — a human-readable identifier for the game or prototype
- **Project description** — a short explanation of what you are building

These fields are lightweight by design. They act as the initial anchor for both humans and AI, without forcing premature structure.

> 📷 Screenshot placeholder: Projects dashboard with multiple projects
> 📷 Screenshot placeholder: New project creation modal

---

## What Lives Inside a Project

Every interaction with Arcane Forge’s AI tools is scoped to a project.

This includes:
- Ideation and game design exploration
- Code generation and refinement
- Image, asset, and music generation
- Evaluation and iteration

Because everything is project-scoped:
- AI tools can reference earlier decisions
- Generated outputs remain connected to their intent
- Iteration builds on previous work instead of starting from scratch

A project is designed to grow with your game — from early concept to a shippable state.

---

## Project Ownership and Permissions

Each project has a **project owner**.

The project owner is the user who created the project. Currently:
- Only the project owner can invite new members
- Only the project owner can manage project membership

This keeps ownership and responsibility explicit, especially in early-stage teams.

---

## Collaborating in a Project

Projects in Arcane Forge are built to support collaboration.

From the project menu, the owner can:
- Open the **Team Members** panel
- Invite collaborators by email

Invited users will see pending invitations in their **Invites** section, where they can:
- Accept the invitation
- Decline the invitation

Once accepted, collaborators gain access to the project and its shared context.

> 📷 Screenshot placeholder: Team members panel
> 📷 Screenshot placeholder: Invite member flow
> 📷 Screenshot placeholder: Pending invitations page

---

## How to Think About Projects

A useful mental model is:

- **One project = one game (or one serious experiment)**
- Projects are long-lived and iterative
- AI works *with* the project, not in isolation

You are encouraged to:
- Keep experiments that matter inside projects
- Let context accumulate over time
- Treat projects as evolving game spaces, not disposable prompt sessions

---

## What’s Next

Once you understand projects, the rest of Arcane Forge becomes easier to reason about.

Next, you may want to explore:
- How Arcane Forge uses AI inside a project
- How ideation turns into structured design
- How assets, code, and music stay connected during iteration

---

# How AI Works Inside a Project

AI in Arcane Forge is **project-scoped, context-aware, and workflow-driven**.

Rather than treating AI as a single chat box or a set of isolated generators, Arcane Forge embeds AI into different stages of a project, each with a clear responsibility and boundary.

The goal is not to replace human judgment, but to make AI a reliable collaborator that understands *what you are building* and *where you are in the process*.

---

## Project Home: The AI Entry Point

Each project has a **Project Home** page. This is the high-level control panel where both humans and AI anchor their understanding of the project.

On Project Home, you can see:
- Project name and **Project ID** (used for support, debugging, and communication)
- Basic project metadata
- Knowledge base status (how much context AI can access)
- A **Game Introduction** section
- Project progress indicators

The Project ID is intentionally visible and stable. When reporting issues or discussing a project with collaborators or support, this ID is the canonical reference.

> 📷 Screenshot placeholder: Project Home overview

---

## Game Introduction: Teaching AI What You’re Building

The **Game Introduction** is one of the most important inputs for AI inside a project.

It does not need to be long or perfect. You can update it at any time.

This section exists to answer a simple question:

> “What is this game, and what are we trying to build?”

AI uses this introduction to:
- Ground design discussions
- Interpret generated assets
- Evaluate design completeness
- Reduce irrelevant or generic suggestions

You can write this yourself, or in the future, have AI help generate or refine it. What matters is that it reflects *your intent*, not a generic template.

> 📷 Screenshot placeholder: Game Introduction section

---

## Project Progress: Visualizing Where You Are

Arcane Forge tracks high-level project progress across major stages:
- Game design
- Development (coding)
- Image generation
- Sound and music generation
- Release and analytics

This progress view is not meant to enforce a strict pipeline. Instead, it helps you and the AI reason about:
- What has already been explored
- What areas may be incomplete
- What the next logical steps might be

When a game is released, you can attach a game URL and mark the project as shipped. Post-release analytics can then be associated with the same project context.

> 📷 Screenshot placeholder: Project progress indicators

---

## Knowledge Base: Shared Memory for AI

The **Knowledge Base** is the primary mechanism through which AI accesses long-term project context.

Anything placed in the knowledge base is considered **authoritative project knowledge**.

You can add four types of entries:

### Documents
Text-based files such as:
- TXT
- PDF
- Markdown
- Word documents

Typical uses include:
- GDDs and game macros
- Design notes
- Technical specifications

### Links
Any external reference, such as:
- Figma designs
- External documents
- Reference materials

Links allow AI to know *where* important information lives, even if the content itself is external.

### Contacts
Named points of contact, such as:
- Who owns a system
- Who should be consulted for a decision

If AI cannot confidently answer a question, it can surface **who should be asked** instead of hallucinating.

### Other Entries (Key–Value)
Structured metadata stored as key–value pairs. These are useful for facts that should remain stable and explicit.

> 📷 Screenshot placeholder: Knowledge Base entries

---

## Knowledge Base Q&A

Arcane Forge provides a **Knowledge Base Q&A** interface.

This allows you to:
- Ask questions about your project
- Retrieve information from stored documents and entries
- Get concrete answers grounded in project data

Examples:
- “How many levels does the game have?”
- “What platform is this game targeting?”

If the information is missing, the AI will explicitly state that and, when possible, point to the relevant contact instead of guessing.

> 📷 Screenshot placeholder: Knowledge Base Q&A

---

## Ideation: Game Design Assistant

The **Ideation** section hosts the Game Design Assistant.

This is a chat-based AI designed to follow game design best practices. Its primary purpose is to help you:
- Explore mechanics and systems
- Identify missing design decisions
- Produce a clear, structured **Game Design Document (GDD)** and game macro

The assistant is intentionally focused. It is not a general-purpose chatbot.

You are encouraged to:
- Start new conversations for new topics
- Keep discussions scoped to a single design problem

This reduces context drift and keeps outputs precise.

---

## Saving Design Output to the Knowledge Base

When a design discussion reaches a stable point, you can save AI-generated output directly into the Knowledge Base.

From the Ideation interface:
- Toggle the toolbar
- Click **Save File**

Saved documents become part of the project’s long-term memory and are automatically available to:
- Future design discussions
- Design evaluation
- Coding and asset generation stages

This is how short-term conversations turn into durable project knowledge.

> 📷 Screenshot placeholder: Save to Knowledge Base flow

---

## Design Evaluation: AI as a Reviewer

Design Evaluation allows AI to review your current game design from a production-readiness perspective.

When you run an evaluation, AI will:
- Assess whether the design is ready for implementation
- Identify **knowledge gaps** that block engineers or downstream work
- Assign severity levels to gaps

For example, missing target platform or input method is flagged as a critical issue because it directly impacts implementation.

---

## Improving with AI

For each identified gap, you can click **Improve with AI**.

This action:
- Brings you back to the design assistant
- Focuses the discussion on resolving the specific gap
- Helps you make an explicit decision

Once resolved, updated design output can again be saved into the Knowledge Base, closing the loop.

---

## Beyond Gaps: Market and Next Steps

Design Evaluation also includes:
- Market differentiation analysis
- Comparable games
- Clear summaries of risks and recommendations

This helps you reason not only about *whether* a game can be built, but *whether* it should be built in its current form.

---

## The Foundation Layer

Together, Project Home, Knowledge Base, Ideation, and Design Evaluation form the **foundation layer** of Arcane Forge.

This layer exists to:
- Make intent explicit
- Reduce ambiguity
- Prepare the project for efficient production

Everything that comes later — coding, asset generation, music, iteration — builds on this shared foundation.

---

# Build Your First Game

This section walks through a **simple, end-to-end workflow** for building your first game with Arcane Forge.

It intentionally avoids deep dives into individual tools. The goal is to help you understand **the flow**, not every feature.

If you are new, start here.

---

## Step 1: Create a Project

Every game in Arcane Forge starts as a **project**.

Create a new project by providing:
- A project name
- A short project description

Think of this as naming the game you are about to build. You can refine everything later.

Once created, all AI tools, assets, and iterations for this game will live inside this project.

---

## Step 2: Start With Game Design (Ideation)

After creating a project, the recommended first step is **Ideation**.

Open the **Game Design Assistant** and describe the game you want to build.

For example:
> “I want to build a modified chess game with unconventional rules. Let’s call it *Crazy Chess*.”

The assistant will:
- Ask clarifying questions
- Help you explore mechanics and systems
- Guide you toward a complete **Game Design Document (GDD)** and game macro

The purpose here is not to be perfect — it is to make your intent explicit and structured.

---

## Step 3: Save Design to the Knowledge Base

Once a design discussion reaches a stable point:
- Save the generated design output to the **Knowledge Base**

This step is critical.

Saving design documents turns transient conversations into **durable project knowledge** that:
- Other AI tools can reference
- Human collaborators can read
- Future iterations can build on

At this point, your project has a shared source of truth.

---

## Step 4: Move Into Production

With design in place, you can move into production in any order that fits your workflow.

Many developers prefer to start with **coding** to validate core gameplay first, then layer in assets.

Typical production paths include:
- Code generation
- Image and asset generation
- Sound and music generation

You are not required to use all AI tools. Arcane Forge supports hybrid workflows where humans and AI collaborate.

---

## Step 5: Coding With AI (External IDEs)

Arcane Forge currently supports a **tool-assisted coding workflow**.

The recommended approach is:
1. Export relevant design documents from the Knowledge Base
2. Load them as context into your AI-enabled IDE (for example, Cursor)
3. Use AI to generate and iterate on code locally

This keeps:
- Your codebase fully under your control
- AI suggestions grounded in your actual design

Arcane Forge provides a quick-start guide under the Coding section that walks through this setup in detail.

---

## Step 6: Generate Assets and Audio

Once gameplay is functional, you can generate:
- Visual assets
- Sound effects (SFX)
- Music

These generations remain scoped to the project and informed by:
- The Game Introduction
- Saved design documents
- Existing project context

Generated assets can be iterated on, replaced, or discarded — nothing is mandatory.

---

## Step 7: Iterate and Release

When your game reaches a playable or released state, you can attach:
- A game URL (store page, build link, or demo)

This allows Arcane Forge to associate post-release activity with the same project.

---

## Step 8: Feedback and Iteration

Iteration in Arcane Forge is driven by **real feedback**.

To enable feedback analysis, provide:
- A game link
- A feedback source (such as an API or comment feed)

Arcane Forge supports two feedback workflows:

### Assisted Review
You select specific comments and ask AI targeted questions about them.

### Automated Analysis
AI runs a broader analysis that produces:
- Categorized feedback
- High-level improvement ideas

This automated output is referred to as a **mutation design**.

---

## Step 9: Improve and Repeat

From feedback analysis, Arcane Forge can generate:
- A **delta GDD** (design changes based on feedback)

You can review, modify, and save this delta design into the Knowledge Base.

At this point, the loop closes:

Design → Build → Release → Learn → Improve

You can now repeat the workflow with clearer intent and stronger context.

---

## The Arcane Forge Loop

A simplified mental model:

1. Design with AI
2. Save intent as knowledge
3. Build with humans and AI
4. Release and observe
5. Learn from feedback
6. Improve design

Arcane Forge is built around this loop, helping you move faster without losing control.

---

# Iteration and Feedback

No game ships perfect on the first attempt.

Whether you test internally, with friends, with beta testers, or with the public, real games always generate feedback. The challenge is not collecting feedback — it is **making sense of it** and turning it into actionable improvements.

The Feedback system in Arcane Forge exists to help you:
- Understand player feedback at scale
- Identify meaningful patterns instead of anecdotes
- Turn feedback into concrete design changes
- Feed those changes back into the same project workflow

---

## Philosophy: Feedback Is Part of the Build Loop

Arcane Forge treats feedback as a **first-class input**, not an afterthought.

Feedback is not something you read once and forget. It is material for the next version of your game.

Rather than asking:
> “What did players say?”

Arcane Forge helps you ask:
> “What should we change next, and why?”

---

## Connecting Feedback Sources

To analyze feedback, Arcane Forge needs access to player comments.

Each project supports attaching a **feedback link** as part of its release information. This link points to an API or endpoint where feedback can be retrieved.

Arcane Forge attempts to parse feedback sources intelligently based on the provided API contract.

Currently, feedback analysis has been tested primarily with:
- games.arcane-forge.ai

Other APIs may work as long as they expose structured feedback data. In the future, Arcane Forge plans to support additional integrations, including direct database connections.

---

## The Feedback Page

Once a feedback source is connected, the **Feedback** page becomes available inside the project.

The page has two main areas:

### Player Comments
A continuously loaded list of player feedback.

You can:
- Scroll and read raw comments
- Click individual entries to inspect them
- Select a subset or all comments for analysis

This keeps you close to the actual player voice instead of hiding it behind summaries.

> 📷 Screenshot placeholder: Feedback comments list

---

## Two Ways to Work With Feedback

Arcane Forge supports two complementary feedback workflows.

### 1. Assisted Discussion

You can select specific comments and choose **Discuss**.

This action:
- Sends the selected feedback to the Game Design Assistant
- Allows you to ask targeted questions, such as:
  - “What are the most common complaints?”
  - “Which issues block progression?”
  - “What feedback is likely noise?”

This mode is useful when you want exploratory or hypothesis-driven analysis.

---

### 2. Automated Analysis (Mutation Design)

You can also ask Arcane Forge to run a full automated analysis.

This process produces a **mutation design** — a structured proposal for improving the game based on player feedback.

The analysis typically includes three sections:

#### Feedback Clusters
AI groups feedback into categories such as:
- UI issues
- Difficulty progression
- Controls and input clarity
- UX and menus

Each cluster shows how many comments contributed to it, helping you distinguish systemic problems from edge cases.

#### Opportunities
Actionable improvement ideas derived from the clusters.

These are phrased as concrete changes rather than vague observations.

#### Proposed Mutations
A list of potential design changes, each with:
- A short description
- Estimated impact
- Estimated effort
- Detailed proposed changes

> 📷 Screenshot placeholder: Feedback clusters and opportunities

---

## Selecting and Refining Mutations

You are not required to accept all proposed mutations.

You can:
- Edit mutation descriptions
- Adjust their scope
- Select only the changes you want to pursue

This keeps creative and product control firmly in human hands.

---

## From Feedback to Delta GDD

Once mutations are selected, you can start a **mutation design session**.

This sends you back to the Game Design Assistant, where AI:
- Generates a **delta GDD** (design changes relative to the current design)
- Focuses only on the selected improvements

Because this happens inside the same project:
- All prior design context is preserved
- Changes remain grounded in the existing game

The delta GDD can be reviewed, discussed, and saved to the Knowledge Base just like any other design document.

---

## Closing the Loop

At this point, the loop completes:

Feedback → Analysis → Design Change → Build → Release

Arcane Forge is designed so that each iteration:
- Builds on real player input
- Produces explicit design artifacts
- Improves both the game and the project context

Over time, this compounds into faster iteration and clearer decision-making — without turning the process into a black box.


---

# Assets and Generation (Images, SFX, Music)

Arcane Forge treats **assets** as first-class objects inside a project.

Rather than thinking in terms of one-off generations, Arcane Forge separates the idea of:
- **What the asset is** (intent)
- **How it is generated** (iterations)

This structure is shared across **Image Generation**, **SFX Generation**, and **Music Generation**.

---

## Assets: The Core Abstraction

An **asset** represents a single game element, such as:
- A character sprite
- An environment background
- A sound effect
- A music track

Each asset can have **multiple generations**.

This creates a clear one-to-many relationship:

- One asset
- Many generated variants

You can review, compare, favorite, download, or discard individual generations without losing the asset’s original intent.

---

## Asset Overview Pages

Each generation category (Images, SFX, Music) has an **overview page** where you can:
- View all assets of that type
- Create new assets
- Navigate into existing assets

From here, you can either:
- Create assets manually
- Or generate assets directly from design documents

> 📷 Screenshot placeholder: Asset overview page

---

## Creating Assets From Documents

Arcane Forge can help you create assets directly from your design documents.

If your Knowledge Base already contains high-level descriptions of required art or audio, you can:
- Select a document
- Ask Arcane Forge to extract asset candidates

The system will:
- Propose a list of assets
- Generate names, descriptions, and tags

The quality of this step depends on how clear the source document is. Clear design documents produce better asset suggestions.

This feature is designed to save time when a project contains many assets.

---

## Working Inside an Asset

Clicking into an asset opens its **generation view**.

Here you can:
- Generate new variants
- Review previous generations
- Inspect metadata for each generation
- Mark favorite outputs
- Download or delete individual results

Assets act as containers that preserve history and intent across iterations.

---

## SFX and Music Generation Workflow

Sound effects and music generation share the same workflow.

To generate audio:
1. Select an asset
2. Provide a prompt (or generate one from the asset description)
3. Configure generation parameters

Common parameters include:
- Positive and negative prompts
- Duration
- Prompt influence (strict vs loose)
- Number of generations

AI-generated prompts based on asset metadata are often sufficient for SFX and music, especially for early iterations.

Generated audio appears in the **Recent Generations** panel, where you can:
- Preview
- Favorite
- Download
- Inspect metadata

> 📷 Screenshot placeholder: SFX / Music generation panel

---

## Image Generation Workflow

Image generation follows the same asset-based structure, with additional complexity.

The high-level process is:
1. Select an asset
2. Choose or determine a generation workflow
3. Configure prompts and parameters
4. Generate images

---

## Choosing a Workflow

Image generation always uses a **workflow**.

There are two ways to select one:

### Browse Workflow Library
You manually choose a predefined workflow from the workflow library.

### Describe With Chat
You describe what you want, and Arcane Forge recommends a suitable workflow based on your description.

If no suitable workflow exists, you can contact the team. Workflow coverage is actively expanding.

---

## Image Generation Parameters

After selecting a workflow, the generation page becomes similar to SFX and music generation.

Typical parameters include:
- Positive and negative prompts
- Aspect ratio
- Number of outputs
- Background removal (if supported by the workflow)

Some workflows support generating multiple variants from a single prompt, such as:
- Original image
- Background-removed version

Additional variants may be added over time.

AI-assisted prompt generation is available if you prefer not to write prompts manually.

---

## Reviewing Image Generations

Generated images appear in the **Recent Generations** panel.

From there, you can:
- Open images in detail view
- Mark favorites
- Download assets
- Inspect generation metadata

Generation speed and quality depend on the underlying models and workflows.

---

## Current State and Expectations

Image, SFX, and music generation are currently in **early-stage / beta**.

In particular:
- Workflow coverage is limited
- Image generation quality varies by use case
- Results may require iteration and tuning

This is expected.

Asset generation, especially for visuals, requires experience and refinement. Arcane Forge is actively improving this experience through:
- Additional workflows
- Better defaults
- Improved guidance

If generation results are not satisfactory, the team encourages users to reach out for help rather than abandoning the workflow.

---

## How Assets Fit Into the Larger Workflow

Assets are not isolated outputs.

They are meant to:
- Reflect design intent
- Evolve alongside code and gameplay
- Integrate naturally into iteration and feedback cycles

By anchoring generation around assets, Arcane Forge keeps creative control with the builder while still leveraging AI for speed.

