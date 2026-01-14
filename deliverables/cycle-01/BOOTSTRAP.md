# BOOTSTRAP

## Prompt interpretation
Create a pair of press plates (top and bottom) sized to standard origami paper (square). When a sheet of origami paper is placed between and pressed, the plates should emboss or score the classic crane prefold pattern. Provide child-friendly illustrated instructions that show the sequence to fold a paper crane using the pre-creased sheet.

## Objectives
- Design two complementary plates that register reliably and transfer the crane crease pattern.
- Output clean, manifold STL files suitable for 3D printing.
- Produce clear, kid-friendly illustrated instructions with minimal text and visual step numbering.
- Document dimensions, tolerances, and print recommendations.

## Proposed team composition
- Bootstrap: interpret prompt and propose plan adjustments.
- Storyteller: shape the kid-friendly narrative tone and instruction voice.
- Orchestrator: formalize the plan and tracking assets.
- Core worker: model the plates and produce STL + fabrication notes + instruction copy.
- Image producer: generate simple vector or raster illustrations for each step.
- PDF assembler: compose instructions into a print-ready PDF and export image assets.
- Reviewer: check STL validity, assembly fit, and instruction clarity.
- Delivery packager: assemble final assets and update releases.
- Retrospective: recommend workflow improvements for next cycle.

## Recommended plan adjustments
- Add a dedicated image production step before PDF assembly to ensure illustrations are ready.
- Split core worker output into two deliverables: CAD/STL assets and instruction copy/layout spec.
- Add a lightweight STL validation check (manifold, scale) in the reviewer step.

## Risks and assumptions
- Assume standard origami paper is 150 mm square; document how to scale for other sizes.
- Plate alignment may require registration pins or a simple frame; include if needed.
- Emboss depth must avoid tearing paper; target shallow relief and rounded edges.

## Primary deliverables for this cycle
- `deliverables/cycle-01/PLATES_TOP.stl`
- `deliverables/cycle-01/PLATES_BOTTOM.stl`
- `deliverables/cycle-01/INSTRUCTIONS.pdf`
- `deliverables/cycle-01/INSTRUCTIONS.md`
- `deliverables/cycle-01/ASSET_NOTES.md`

## Retrospective recommendations (pre-flight)
- Track print parameters (nozzle size, layer height) in a standard template for future cycles.
- Add a small test strip STL for emboss depth validation before full plate printing.

## Next-cycle prompts (human must choose one after this cycle completes)
1) Design a compact storage case for the plates with snap-fit features and add a simple label.
2) Create a variant plate set for a different origami model (frog or tulip) with matching instructions.
3) Produce a classroom kit guide: print settings, paper sourcing, and a 1-page teacher handout.


## Retrospective (post-cycle)
- Add a parametric CAD script (e.g., OpenSCAD) so crease maps and sizes can be regenerated easily.
- Introduce a complementary groove plate for more consistent embossing depth.
- Expand the instruction PDF to two pages for larger, kid-friendly panels.

If you want, I can implement these retrospective improvements and reset the plan for the next cycle once you choose a prompt.
