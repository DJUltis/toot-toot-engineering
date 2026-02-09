# Toot Toot Ontology

This page is intentionally simple for programmatic parsing.

## Schema
Each term is a block with a level-3 heading and key-value lines.

Example:
### Node: Example Term
kind: role | concept | document | file | artifact | system | actor
summary: One-line description.
aliases: Comma-separated aliases or none.
notes: Optional clarifying notes or none.

## Nodes
### Node: Toot Toot Engineering (TTE)
kind: system
summary: The overall workflow and repository for cycle-based production.
aliases: TTE
notes: Workflow version 3.8.

### Node: Toot Toot Network (TTN)
kind: system
summary: A transport-agnostic semantic mesh with explicit AI invocation rules.
aliases: TTN
notes: Defined in `RFCs/TTN-RFC-0001.md`.

### Node: Toot Toot Database (TTDB)
kind: system
summary: A single-file semantic story database with typed edges and stable IDs.
aliases: TTDB, My Mental Palace DB, MMPDB
notes: Defined in `RFCs/TTDB-RFC-0001-File-Format.md`.

### Node: MyMentalPalaceDB.md
kind: document
summary: The active TTDB instance for this repo.
aliases: My Mental Palace DB
notes: Stores records, cursor state, and typed edges.

### Node: TTAI
kind: role
summary: A maker-scale shop assistant and TTDB librarian invoked as "@AI".
aliases: ai_shop_assistant
notes: Defined in `standards/ttai/TTAI_SPEC.md`.

### Node: Default Network
kind: concept
summary: The idle-state narrative circuitry for TTAI.
aliases: default network
notes: Defined in `standards/ttai/DEFAULT_NETWORK.md`.

### Node: Umwelt
kind: concept
summary: The perceived world that bounds what exists for the system.
aliases: none
notes: See `TTE_Umwelt.md` and `standards/umwelt/TTE_Agent_Umwelt_v1.yaml`.

### Node: TTE Umwelt
kind: document
summary: Narrative description of the TTE umwelt and its domains.
aliases: TTE_Umwelt.md
notes: Maker-scale, narrative-aware, semantically explicit.

### Node: TTE Agent Umwelt v1
kind: document
summary: YAML configuration for the agent umwelt.
aliases: TTE_Agent_Umwelt_v1.yaml
notes: Stored under `standards/umwelt/`.

### Node: Bootstrap
kind: role
summary: Interprets the prompt, proposes team composition, objectives, and plan changes, and suggests next-cycle prompts.
aliases: none
notes: Produces `deliverables/cycle-XX/BOOTSTRAP.md`.

### Node: Orchestrator
kind: role
summary: Builds and updates the critical-path plan and logging assets.
aliases: none
notes: Updates `PLAN.md`, `AGENTS.md`, and `LOG.md`.

### Node: Storyteller
kind: role
summary: Refines the narrative thread and creative framing early in the cycle.
aliases: none
notes: Produces `deliverables/cycle-XX/STORYTELLER.md`.

### Node: SVG engineer
kind: role
summary: Specializes in SVG production constraints and strategies.
aliases: none
notes: Produces `deliverables/cycle-XX/SVG_ENGINEER.md` when needed.

### Node: Core worker
kind: role
summary: Produces the primary solution artifacts for the task.
aliases: none
notes: Output varies by cycle and prompt.

### Node: Image producer
kind: role
summary: Generates or composes visual assets programmatically.
aliases: none
notes: Produces `deliverables/cycle-XX/IMAGE_ASSETS.md` and assets.

### Node: PDF assembler
kind: role
summary: Builds print-ready PDFs from assets and layout specifications.
aliases: none
notes: Produces `deliverables/cycle-XX/PRINT_PDF.md` and outputs.

### Node: Reviewer
kind: role
summary: Checks for correctness, gaps, and risks before delivery.
aliases: none
notes: Produces `deliverables/cycle-XX/REVIEW.md`.

### Node: Delivery packager
kind: role
summary: Assembles final assets and export notes.
aliases: none
notes: Produces `deliverables/cycle-XX/DELIVERY.md` and updates `RELEASES.md`.

### Node: Retrospective
kind: role
summary: Recommends changes to prevent issues or improve outcomes.
aliases: none
notes: Updates `deliverables/cycle-XX/BOOTSTRAP.md` with recommendations.

### Node: Human co-producer
kind: actor
summary: Starts the run and is only needed between steps if blocked.
aliases: human
notes: Provides feedback after the final step.

### Node: Cycle
kind: concept
summary: A bounded production run with role steps and deliverables under `deliverables/cycle-XX/`.
aliases: none
notes: Cycle-01 uses `TTE_PROMPT.md`.

### Node: Step
kind: concept
summary: A single role execution that produces named assets.
aliases: none
notes: One step, one agent, one role.

### Node: Role
kind: concept
summary: A defined responsibility with expected outputs.
aliases: none
notes: Roles are listed in `AGENTS.md`.

### Node: Critical path
kind: concept
summary: The ordered list of steps required to reach delivery.
aliases: plan
notes: Tracked in `PLAN.md`.

### Node: Definition of done
kind: concept
summary: The completion gate for a cycle.
aliases: DoD
notes: Defined in `RFCs/TTE-RFC-0003-Definition-of-Done-and-Release.md`.

### Node: Deliverables
kind: artifact
summary: Named outputs created during a cycle.
aliases: outputs
notes: Stored under `deliverables/cycle-XX/`.

### Node: Placeholder
kind: concept
summary: A temporary marker that must be resolved before step completion.
aliases: none
notes: Placeholders block marking a step complete.

### Node: PLAN.md
kind: document
summary: The authoritative critical-path plan and table of contents.
aliases: Plan
notes: Records deliverable paths and step status.

### Node: AGENTS.md
kind: document
summary: Defines roles, rules, and expected assets.
aliases: Agents
notes: Governs workflow behavior.

### Node: LOG.md
kind: document
summary: The append-only log of decisions, changes, and open questions.
aliases: Log
notes: Updated at the end of each step.

### Node: CHECKLIST.md
kind: document
summary: Step completion and consistency checks.
aliases: Checklist
notes: Consulted during each step.

### Node: RELEASES.md
kind: document
summary: Cycle summaries and deliverable indexes.
aliases: Releases
notes: Updated during delivery packaging.

### Node: README.md
kind: document
summary: Entry point describing workflow and rules.
aliases: Readme
notes: Must be read before work begins.

### Node: WHAT.md
kind: document
summary: Conceptual overview of TTE.
aliases: none
notes: Supplements `README.md`.

### Node: TTE_PROMPT.md
kind: document
summary: The cycle-01 prompt input.
aliases: Prompt
notes: Later cycles use the prompt from the prior cycle's bootstrap.

### Node: TTE_ONTOLOGY.md
kind: document
summary: The ontology of terms and relationships for this repo.
aliases: ontology
notes: Organized into Nodes and Semantic Edges.

### Node: LICENSE
kind: document
summary: The project license.
aliases: MIT License
notes: TTE is MIT-licensed.

### Node: requirements.txt
kind: document
summary: Python dependencies list.
aliases: none
notes: Includes `openai`.

### Node: Activate_bat_run_tte.bat
kind: document
summary: Windows batch helper for running TTE.
aliases: none
notes: Starts the agent workflow on Windows.

### Node: tte_agent.py
kind: file
summary: The main TTE agent loop and tool bridge.
aliases: none
notes: Uses OpenAI Responses API and local tools.

### Node: tte_monitor.py
kind: file
summary: The Tkinter UI that monitors PLAN and LOG.
aliases: TTE Monitor
notes: Renders markdown views for PLAN and LOG.

### Node: ttdb_navigator.py
kind: file
summary: The Tkinter UI that navigates TTDB records.
aliases: TTDB Navigator
notes: Provides list navigation and a globe view for TTDB coordinates.

### Node: RFCs index
kind: document
summary: The index of RFCs in this repo.
aliases: RFCs/INDEX.md
notes: Links to TTN, TTDB, and TTE RFCs.

### Node: TTN RFC manifest
kind: document
summary: Hash manifest for TTN RFC bundle.
aliases: RFCs/TTN-RFC-MANIFEST.md
notes: Records SHA256 for RFCs.

### Node: TTE-RFC-0001
kind: document
summary: Workflow and role definitions for TTE.
aliases: Workflow and Roles RFC
notes: `RFCs/TTE-RFC-0001-Workflow-and-Roles.md`.

### Node: TTE-RFC-0002
kind: document
summary: PLAN, LOG, and checklist requirements.
aliases: Plan and Log RFC
notes: `RFCs/TTE-RFC-0002-Plan-Log-and-Checklist.md`.

### Node: TTE-RFC-0003
kind: document
summary: Definition of done and release packaging rules.
aliases: Definition of Done RFC
notes: `RFCs/TTE-RFC-0003-Definition-of-Done-and-Release.md`.

### Node: TTDB-RFC-0001
kind: document
summary: TTDB file format and record structure.
aliases: File Format RFC
notes: `RFCs/TTDB-RFC-0001-File-Format.md`.

### Node: TTDB-RFC-0002
kind: document
summary: Cursor semantics for TTDB.
aliases: Cursor Semantics RFC
notes: `RFCs/TTDB-RFC-0002-Cursor-Semantics.md`.

### Node: TTDB-RFC-0003
kind: document
summary: Typed edge semantics for TTDB.
aliases: Typed Edge Semantics RFC
notes: `RFCs/TTDB-RFC-0003-Typed-Edges.md`.

### Node: TTDB-RFC-0004
kind: document
summary: Event ID assignment and collision handling.
aliases: Event ID RFC
notes: `RFCs/TTDB-RFC-0004-Event-ID-and-Collision.md`.

### Node: TTN-RFC-0001
kind: document
summary: TTN core semantic mesh specification.
aliases: Core TTN RFC
notes: `RFCs/TTN-RFC-0001.md`.

### Node: TTN-RFC-0002
kind: document
summary: TTN typed edge taxonomy.
aliases: TTN Typed Edges RFC
notes: `RFCs/TTN-RFC-0002-Typed-Edges.md`.

### Node: TTN-RFC-0003
kind: document
summary: Reference implementation checklist for TTN nodes.
aliases: Reference Implementation RFC
notes: `RFCs/TTN-RFC-0003-Reference-Implementation.md`.

### Node: TTN-RFC-0004
kind: document
summary: Semantic compression and token dictionary for constrained links.
aliases: Semantic Compression RFC
notes: `RFCs/TTN-RFC-0004-Semantic-Compression.md`.

### Node: TTN-RFC-0005
kind: document
summary: Trust, reputation, and moderation modeling.
aliases: Trust and Reputation RFC
notes: `RFCs/TTN-RFC-0005-Trust-and-Reputation.md`.

### Node: TTN-RFC-0006
kind: document
summary: Minimal LoRa packet framing for non-Meshtastic nodes.
aliases: LoRa Framing RFC
notes: `RFCs/TTN-RFC-0006-LoRa-Packet-Framing.md`.

### Node: TTAI_SPEC.md
kind: document
summary: Core identity and behavior requirements for TTAI.
aliases: TTAI Spec
notes: Stored under `standards/ttai/`.

### Node: DEFAULT_NETWORK.md
kind: document
summary: Narrative default network definition for TTAI.
aliases: Default Network Spec
notes: Stored under `standards/ttai/`.

### Node: BEHAVIOR_SPEC.md
kind: document
summary: TTAI idle-time and TTN join/leave behavior.
aliases: Behavior Spec
notes: Stored under `standards/ttai/`.

### Node: Node ID
kind: concept
summary: Stable cryptographic identifier for a TTN node.
aliases: node_id
notes: Required by `RFCs/TTN-RFC-0001.md`.

### Node: Semantic ID
kind: concept
summary: Location-anchored identifier for semantic events.
aliases: semantic_id
notes: Required by `RFCs/TTN-RFC-0001.md`.

### Node: Semantic Event
kind: concept
summary: A structured event in TTN with provenance and typed edges.
aliases: none
notes: Stored in TTDB by default.

### Node: Typed edge
kind: concept
summary: A directional link with a type token between records.
aliases: typed edge
notes: Syntax `type>@TARGET_ID`.

### Node: TTN compliance level
kind: concept
summary: Capability tier for a TTN node.
aliases: TTN-Base, TTN-BBS, TTN-AI, TTN-Gateway
notes: Defined in `RFCs/TTN-RFC-0001.md`.

### Node: Presence event
kind: concept
summary: A semantic event announcing a node on the network.
aliases: presence
notes: Required for minimal viable nodes.

### Node: Mesh grammar
kind: concept
summary: Compact, transport-friendly representation of TTN semantics.
aliases: compact mesh grammar
notes: Referenced in `RFCs/TTN-RFC-0003-Reference-Implementation.md`.

### Node: Token dictionary
kind: concept
summary: The on-mesh token set for semantic compression.
aliases: compression tokens
notes: Defined in `RFCs/TTN-RFC-0004-Semantic-Compression.md`.

### Node: LoRa frame
kind: concept
summary: Minimal packet framing for non-Meshtastic TTN nodes.
aliases: LoRa packet framing
notes: Defined in `RFCs/TTN-RFC-0006-LoRa-Packet-Framing.md`.

### Node: TTDB record
kind: concept
summary: A single TTDB node block with ID, metadata, and body.
aliases: record
notes: Header begins with `@LATxLONy`.

### Node: TTDB record ID
kind: concept
summary: A lat/lon coordinate on the knowledge globe.
aliases: @LATxLONy
notes: Deterministic and collision-resolved.

### Node: Knowledge globe
kind: concept
summary: The subjective coordinate map for TTDB IDs.
aliases: globe
notes: Defined in `RFCs/TTDB-RFC-0004-Event-ID-and-Collision.md`.

### Node: Cursor
kind: concept
summary: The active selection window for TTDB records.
aliases: cursor
notes: Defined in `RFCs/TTDB-RFC-0002-Cursor-Semantics.md`.

### Node: Cursor policy
kind: concept
summary: Limits for TTDB preview and node list sizes.
aliases: none
notes: See `MyMentalPalaceDB.md` `cursor_policy`.

### Node: Collision policy
kind: concept
summary: TTDB rule for resolving ID collisions.
aliases: southeast_step
notes: Defined in `RFCs/TTDB-RFC-0004-Event-ID-and-Collision.md`.

### Node: Primitive mode
kind: concept
summary: Reduced umwelt and verb set for constrained devices.
aliases: none
notes: Defined in `standards/ttai/BEHAVIOR_SPEC.md`.

### Node: Monitor UI
kind: artifact
summary: The Tkinter application for viewing plan and log.
aliases: TTE Monitor
notes: Implemented in `tte_monitor.py`.

### Node: TTDB Navigator UI
kind: artifact
summary: The Tkinter application for browsing TTDB records and their coordinates.
aliases: TTDB Navigator
notes: Implemented in `ttdb_navigator.py`.

### Node: OpenAI API key
kind: concept
summary: Environment variable required to run the agent.
aliases: OPENAI_API_KEY
notes: Read by `tte_agent.py`.

### Node: OpenAI Responses API
kind: concept
summary: The model execution interface used by the agent.
aliases: responses.create
notes: Used in `tte_agent.py`.

## Semantic Edges
### Edge: reads
kind: relationship
summary: A role or process consults a document as an input.
aliases: consults
notes: Example: Orchestrator reads `AGENTS.md`.

### Edge: writes
kind: relationship
summary: A role or process creates a new artifact.
aliases: creates
notes: Example: Bootstrap writes `deliverables/cycle-XX/BOOTSTRAP.md`.

### Edge: updates
kind: relationship
summary: A role modifies an existing artifact.
aliases: edits
notes: Example: Orchestrator updates `PLAN.md`.

### Edge: appends to
kind: relationship
summary: A role adds a new entry to a log.
aliases: logs to
notes: Example: Each step appends to `LOG.md`.

### Edge: produces
kind: relationship
summary: A role creates a named deliverable.
aliases: generates
notes: Example: Storyteller produces `deliverables/cycle-XX/STORYTELLER.md`.

### Edge: packages
kind: relationship
summary: A role assembles deliverables for release.
aliases: bundles
notes: Example: Delivery packager packages final assets.

### Edge: validates
kind: relationship
summary: A role verifies correctness or completeness.
aliases: reviews
notes: Example: Reviewer validates primary deliverables.

### Edge: depends on
kind: relationship
summary: A step or output requires another artifact to exist first.
aliases: requires
notes: Example: Delivery depends on Review completion.

### Edge: hands off to
kind: relationship
summary: One role completes a step and signals the next role.
aliases: passes to
notes: Example: Orchestrator hands off to Core worker.

### Edge: records in
kind: relationship
summary: A decision or open question is captured in a log.
aliases: none
notes: Example: Open questions are recorded in `LOG.md`.

### Edge: specifies
kind: relationship
summary: A document defines required behavior or format.
aliases: defines
notes: Example: `AGENTS.md` specifies role outputs.

### Edge: promotes to
kind: relationship
summary: A cycle artifact is copied into a reusable location.
aliases: promotes
notes: Example: Promoted artifacts are copied into `library/` or `standards/`.

### Edge: cycle uses prompt
kind: process
summary: The cycle selects its prompt input source.
aliases: prompt selection
notes: Cycle-01 uses `TTE_PROMPT.md`.

### Edge: step completes
kind: process
summary: A step is marked complete only when outputs are placeholder-free.
aliases: none
notes: Recorded in `PLAN.md`.

### Edge: list dir
kind: action
summary: List files and folders in the workspace.
aliases: list_dir
notes: Implemented in `tte_agent.py`.

### Edge: read file
kind: action
summary: Read a file within the workspace.
aliases: read_file
notes: Implemented in `tte_agent.py`.

### Edge: write file
kind: action
summary: Write a file within the workspace.
aliases: write_file
notes: Implemented in `tte_agent.py`.

### Edge: run shell
kind: action
summary: Execute a shell command within the workspace.
aliases: run_shell
notes: Implemented in `tte_agent.py`.

### Edge: run agent
kind: action
summary: Execute the TTE agent loop.
aliases: execute agent
notes: Uses `tte_agent.py`.

### Edge: run monitor
kind: action
summary: Execute the monitor UI.
aliases: monitor
notes: Uses `tte_monitor.py`.

### Edge: refresh monitor
kind: action
summary: Reload plan, log, and DB views.
aliases: refresh
notes: Implemented in `tte_monitor.py`.

### Edge: auto refresh
kind: action
summary: Periodically refresh monitor data.
aliases: poll
notes: Controlled by `REFRESH_MS`.

### Edge: render markdown
kind: process
summary: Render markdown into the monitor text widgets.
aliases: render
notes: Implemented in `tte_monitor.py`.

### Edge: parse TTDB
kind: process
summary: Parse TTDB records and typed edges.
aliases: parse records
notes: Implemented in `tte_monitor.py`.

### Edge: select record
kind: action
summary: Choose a TTDB record as the active selection.
aliases: select
notes: Defined in TTDB cursor semantics.

### Edge: insert record
kind: action
summary: Add a new TTDB record.
aliases: insert
notes: TTDB action.

### Edge: update record
kind: action
summary: Modify a TTDB record.
aliases: update
notes: TTDB action.

### Edge: delete record
kind: action
summary: Remove a TTDB record.
aliases: delete
notes: TTDB action.

### Edge: upsert record
kind: action
summary: Insert or update a TTDB record.
aliases: upsert
notes: TTDB action.

### Edge: find record
kind: action
summary: Search TTDB records by token.
aliases: find
notes: TTDB primitive query.

### Edge: list edges
kind: action
summary: Return edges for a TTDB record.
aliases: edges
notes: TTDB primitive query.

### Edge: last records
kind: action
summary: Return last N records in TTDB.
aliases: last
notes: TTDB primitive query.

### Edge: status
kind: action
summary: Return TTDB status summary.
aliases: status
notes: TTDB primitive query.

### Edge: note
kind: action
summary: Record a short note in TTDB context.
aliases: note
notes: TTDB primitive query.

### Edge: broadcasts
kind: process
summary: Send a presence or join message over TTN.
aliases: broadcast
notes: Defined in `standards/ttai/BEHAVIOR_SPEC.md`.

### Edge: welcomes
kind: process
summary: Send a welcome message to a joining node.
aliases: welcome
notes: Defined in `standards/ttai/BEHAVIOR_SPEC.md`.

### Edge: emits presence
kind: process
summary: Emit presence events on TTN.
aliases: presence
notes: Required by TTN reference implementation.

### Edge: stores event
kind: process
summary: Store semantic events locally in TTDB.
aliases: archives to
notes: Required by TTN reference implementation.

### Edge: expands tokens
kind: process
summary: Expand compressed tokens into semantic events.
aliases: expand
notes: TTN semantic compression.

### Edge: acknowledges
kind: relationship
summary: Acknowledge a command or event.
aliases: ack
notes: TTN typed edge and LoRa ACK behavior.

### Edge: retries
kind: process
summary: Retry a transmission after failed ACK.
aliases: retry
notes: Defined in `RFCs/TTN-RFC-0006-LoRa-Packet-Framing.md`.

### Edge: knows
kind: relationship
summary: Identity/topology relation between nodes.
aliases: none
notes: TTN typed edge.

### Edge: seen_near
kind: relationship
summary: Nodes observed in proximity.
aliases: none
notes: TTN typed edge.

### Edge: routes_via
kind: relationship
summary: Routing relation between nodes.
aliases: none
notes: TTN typed edge.

### Edge: connected_over
kind: relationship
summary: Link relation over a transport.
aliases: none
notes: TTN typed edge.

### Edge: board_contains
kind: relationship
summary: BBS board membership relation.
aliases: none
notes: TTN typed edge.

### Edge: thread_root
kind: relationship
summary: BBS thread root relation.
aliases: none
notes: TTN typed edge.

### Edge: replies_to
kind: relationship
summary: BBS reply relation.
aliases: none
notes: TTN typed edge.

### Edge: mentions
kind: relationship
summary: BBS mention relation.
aliases: none
notes: TTN typed edge.

### Edge: moderates
kind: relationship
summary: Moderation relation.
aliases: none
notes: TTN typed edge.

### Edge: supersedes
kind: relationship
summary: Supersession relation.
aliases: none
notes: TTN typed edge.

### Edge: asks_ai
kind: relationship
summary: Request an AI action or response.
aliases: none
notes: TTN typed edge.

### Edge: ai_summarizes
kind: relationship
summary: AI summary relation.
aliases: none
notes: TTN typed edge.

### Edge: ai_flags
kind: relationship
summary: AI flags content relation.
aliases: none
notes: TTN typed edge.

### Edge: ai_responds_to
kind: relationship
summary: AI response relation.
aliases: none
notes: TTN typed edge.

### Edge: ai_refuses
kind: relationship
summary: AI refusal relation.
aliases: none
notes: TTN typed edge.

### Edge: ai_confidence_low
kind: relationship
summary: AI low-confidence relation.
aliases: none
notes: TTN typed edge.

### Edge: reports_sensor
kind: relationship
summary: Sensor report relation.
aliases: none
notes: TTN typed edge.

### Edge: alerts
kind: relationship
summary: Alert relation.
aliases: none
notes: TTN typed edge.

### Edge: commands
kind: relationship
summary: Command relation.
aliases: none
notes: TTN typed edge.

### Edge: escalates
kind: relationship
summary: Escalation relation.
aliases: none
notes: TTN typed edge.

### Edge: supports
kind: relationship
summary: Knowledge graph support relation.
aliases: none
notes: TTN typed edge and TTDB examples.

### Edge: contradicts
kind: relationship
summary: Knowledge graph contradiction relation.
aliases: none
notes: TTN typed edge.

### Edge: refines
kind: relationship
summary: Knowledge graph refinement relation.
aliases: none
notes: TTN typed edge and TTDB examples.

### Edge: duplicates
kind: relationship
summary: Knowledge graph duplication relation.
aliases: none
notes: TTN typed edge.

### Edge: derived_from
kind: relationship
summary: Knowledge graph derivation relation.
aliases: none
notes: TTN typed edge.

### Edge: trusted_by
kind: relationship
summary: Trust relation.
aliases: none
notes: TTN typed edge.

### Edge: muted_by
kind: relationship
summary: Mute relation.
aliases: none
notes: TTN typed edge.

### Edge: blocked_by
kind: relationship
summary: Block relation.
aliases: none
notes: TTN typed edge.

### Edge: flagged_as_spam
kind: relationship
summary: Spam flag relation.
aliases: none
notes: TTN typed edge.

### Edge: quarantined
kind: relationship
summary: Quarantine relation.
aliases: none
notes: TTN typed edge.

### Edge: rehabilitated_by
kind: relationship
summary: Rehabilitation relation.
aliases: none
notes: TTN typed edge.

### Edge: relates
kind: relationship
summary: Generic TTDB relation in record headers.
aliases: none
notes: TTDB header field.

### Edge: inspires
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: anchors
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: references
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: tradeoffs
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: leads_to
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: iterates
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: blocks
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: gates
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: builds
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: depends_on
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: organizes
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: reveals
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: archives
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: expands
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: maps_to
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: observes
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: validates
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: frames
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: constrains
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: drives
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: backgrounds
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: assumes
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: defaults_to
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: operates_in
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: archives_to
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: safeguards
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.

### Edge: tests
kind: relationship
summary: TTDB example relation.
aliases: none
notes: Used in `MyMentalPalaceDB.md`.
