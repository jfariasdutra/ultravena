---
title: 3D Model
nav: 3D Model
order: 7
summary: Turn the CAD model around in the browser, or download it.
updated: 2026-11-24
scripts: viewer
---

This is the actual CAD model (version 6), not an illustration. Drag to turn it, scroll or pinch to zoom, and right-drag or two-finger drag to slide it sideways.

<div class="viewer" id="viewer" data-base="assets/models/">
  <div class="viewer-bar">
    <div class="seg" role="group" aria-label="Probe version">
      <button type="button" data-variant="butterfly" class="on">Butterfly iQ3</button>
      <button type="button" data-variant="vscan">GE Vscan Extend</button>
    </div>
    <label class="check"><input type="checkbox" id="v-wires"> Show wiring</label>
    <label class="check"><input type="checkbox" id="v-walls" checked> Show walls</label>
    <span class="viewer-status" id="v-status">Loading model</span>
  </div>
  <div class="viewer-stage" id="v-stage"></div>
</div>

## Renders

![The whole rig seen from the front left](assets/img/cad-iso.png){.render}

![The probe head, with the three servos, floating mount and marker actuator](assets/img/cad-head.png){.render}

![The electronics on the outside of the back wall](assets/img/cad-electronics.png){.render}

## CAD files

STEP files open in Onshape, Fusion, SolidWorks and FreeCAD. Each version's download holds two files, one with every wire modelled and a lighter one without.

| Download | What is inside | Size |
| --- | --- | --- |
| [Butterfly iQ3 version](assets/files/ultravena-cad-v6-butterfly.zip) | STEP files, with and without wiring | 9 MB |
| [GE Vscan Extend version](assets/files/ultravena-cad-v6-vscan.zip) | STEP files, with and without wiring | 8 MB |
| [Printable parts and source](assets/files/ultravena-cad-v6-parts.zip) | STL files for both versions and the CadQuery scripts that build the model | 0 MB |

## How the model is made

The model is written as a Python script using CadQuery, so every dimension is a named number that can be changed and rebuilt. Two automatic checks run on every version. The first looks for any two parts that overlap. The second moves the machine through 579 poses across the full travel of all six axes and looks for collisions at each one. Version 6 passes both for the Butterfly and Vscan versions.
