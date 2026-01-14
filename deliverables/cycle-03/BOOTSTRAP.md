# BOOTSTRAP

## Prompt interpretation
Add a snap-fit alignment frame and a compact storage case for the tulip press plates. The frame should help register the top and bottom plates with the paper aligned. The storage case should protect the plates and optionally hold a small stack of paper.

## Objectives
- Design a snap-fit alignment frame compatible with the 150 mm plates.
- Create a storage case that fits both plates and the frame.
- Output printable, manifold STL files with clear assembly notes.
- Keep parts simple for easy printing without supports where possible.

## Proposed team composition
- Bootstrap: interpret prompt and propose plan adjustments.
- Storyteller: define kid-friendly naming and labeling for the case (optional).
- Orchestrator: formalize the plan and tracking assets.
- Core worker: model the frame and case STLs + assembly notes.
- Reviewer: check fit assumptions and printability.
- Delivery packager: assemble final assets and update releases.
- Retrospective: recommend workflow improvements for next cycle.

## Recommended plan adjustments
- Add a fit test strip STL for snap tabs.
- Include a simple label plate for the case lid.

## Risks and assumptions
- Assume plate thickness is 3 mm and plate size is 150 mm.
- Snap-fit tolerances vary by printer; document clearance.
- Case may need extra clearance for elephant foot compensation.

## Primary deliverables for this cycle
- `deliverables/cycle-03/FRAME.stl`
- `deliverables/cycle-03/CASE_BASE.stl`
- `deliverables/cycle-03/CASE_LID.stl`
- `deliverables/cycle-03/ASSEMBLY_NOTES.md`

## Next-cycle prompts (human must choose one after this cycle completes)
1) Create a frog plate set with a jump-themed story and instructions.
2) Build a parametric OpenSCAD generator for plate sizes and crease maps.
3) Add a classroom kit card and quick-start poster for teachers.
