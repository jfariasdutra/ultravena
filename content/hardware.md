---
title: Hardware Brief
nav: Hardware
order: 2
summary: The design as it stands in CAD version 7, why it is built this way, and how the two probe versions differ.
updated: 2026-11-26
pdf: assets/files/ultravena-hardware-brief.pdf
---

UltraVena is a tabletop enclosure that scans a forearm with a motorised ultrasound probe and stamps an ink dot where a dialysis needle should go. This brief describes the hardware as it stands in CAD model version 7 (the redesign that followed the team's design review), why it is built this way, and how the Butterfly iQ3 and GE Vscan Extend versions differ.

## The machine in one view

![Side view of the rig, Butterfly version, probe raised](assets/img/side-view.png){.diagram}

The user sits at the open front, slides a forearm under the slanted panel onto a padded rest and takes hold of a grip at the far end. Overhead, a bridge rides front to back on two side rails, a carriage runs across it, and a vertical slide hangs from the carriage, which together give the probe its three straight-line motions. At the bottom of that slide a three-servo gimbal tilts and spins the probe. Two ordinary webcams watch the arm, one from above and one from the side, an iPad in a slot on the slanted panel is the screen, and every board and power part hangs on the outside of the back wall so that nothing inside is in the way of the gantry.

## Size and reach

The enclosure is 516 mm wide, 558 mm deep and 590 mm tall, small enough for a clinic table. The six axes and their travel, as checked in a 579-pose sweep of the CAD model with no collisions, are below.

| Axis | What moves | Driven by | Travel |
| --- | --- | --- | --- |
| Y, along the arm | The whole bridge | Two stepper motors, one belt per side | 210 mm |
| X, across the arm | The carriage on the bridge | One stepper motor and a belt | 160 mm (80 mm each side of centre) |
| Z, up and down | The slide on the carriage | One stepper motor and a lead screw | 90 mm |
| Yaw, spin about the probe's own axis | The yoke | Servo 1 | 90° each way |
| Pitch, tilt along the arm | The ring inside the yoke | Servo 2 | 30° each way |
| Roll, tilt across the arm | The probe holder inside the ring | Servo 3 | 20° each way |

The three tilt axes all pass through one point 55 mm above the probe face. Because of that, tilting the probe to sit square on a curved arm barely moves the face sideways, and what little it does move is corrected by X and Y.

## The gantry

The gantry is a 3D printer rebuilt as a bridge. A Creality Ender-3 V3 SE is taken apart for its motors, belts, pulleys, lead screw, controller board and 24 V supply, and those parts are remounted on a frame of 20 mm aluminium extrusion.

- **Y axis.** Two side rails run front to back, 185 mm either side of centre and 400 mm above the base. The bridge spans them and is pulled by a belt on each side, each with its own motor, so the bridge cannot skew. The donor printer only supplies three usable motors (its fourth is a short geared extruder motor), so one matching motor is bought separately.
- **X axis.** A carriage rolls along the bridge on wheels, pulled by a single belt.
- **Z axis.** A linear rail (MGN12 with two long carriages) is bolted upright to the carriage, and a lead screw from the Z motor raises and lowers a slide plate on it. The rail matters because the probe hangs 116 mm in front of the slide, and that overhang would twist a simpler sliding block.
- **Homing.** Each axis has a roller-lever switch that gives it a known zero at power-on.
- **Cabling.** The moving wires travel in a cable chain from the back wall to the bridge, then arch across to the carriage and down the slide.

## The probe head

The head is everything that hangs from the Z slide. From top to bottom it is built in this order, and each layer exists for one reason.

1. **Reach bracket.** Carries the head 116 mm forward of the Z rail, so the yoke can spin a full 90° each way without hitting the rail or the carriage.
2. **Floating mount.** Two 6 mm guide rods with bushings and stop collars. The head hangs on these under its own weight and can lift freely by 15 mm, so the hardest it can ever press on an arm is that weight (about 7 N by estimate). A switch trips as soon as it starts to lift.
3. **Load cell and head sensor board.** A 5 kg bar that carries everything below it and measures the contact force, with its amplifier mounted right beside it on the slide plate so the weak signal travels only a few centimetres. A small microcontroller board next to the amplifier collects every sensor on the head and sends the readings down one serial lead.
4. **Yaw servo and yoke.** The first servo points straight down and spins a printed U-shaped yoke.
5. **Pitch servo and ring.** The second servo sits on one arm of the yoke and tilts a printed ring held between the yoke's arms.
6. **Roll servo and probe holder.** The third servo sits on the back of the ring and tilts the holder that clamps the probe.
7. **On the holder.** A tilt sensor that reads true pitch and roll from gravity, four small distance sensors on tabs around the probe face that measure how far the skin is on each side, a printed tracking marker on the front that the webcams can find, and the marker pen with its lift servo on one side.

All three servos are Waveshare ST3215 units, which report their true angle back over a shared cable. Each joint also carries a light spring that keeps it pressed against one side of its gear slack, so whatever play the servos turn out to have does not show up as wobble at the probe face. The printed parts (yaw mount, yoke, ring, holder, cradles) are specific to the probe, so each version has its own set.

**The marker.** An ink pen slides in a printed guide on the side of the probe holder, and a micro servo (the kind found in small model aircraft) lifts and lowers it through about 15 mm. At rest the tip sits 8 mm above the probe face, so it never touches the skin during a scan. To mark, the probe lifts, the gantry shifts sideways by the fixed distance between the probe centre and the tip, the head comes back down until the tip is just clear of the skin, and the servo dips the pen. Nothing pierces the skin.

## The enclosure

The frame is 20 mm aluminium extrusion on a 12 mm base plate, with 3 mm panels on the back and both sides. The top is left open so the gantry is easy to see and reach during development.

- **Arm opening.** The front is open to a height of 200 mm across the full width, which is where the forearm goes in.
- **Slanted front panel.** Above the opening, a steep panel runs from the front edge up and back to the top rail 110 mm further in. It carries a printed slot that the team's iPad mini drops into from the top, the emergency stop on the right, and on the Butterfly version a hole beside the slot for the probe's cable. The iPad lifts straight out again for charging. The steep slope keeps the panel out of the gantry's way while still facing the user.
- **Arm rest.** A padded rest on the base with six thin pressure pads under the padding, laid out as two columns of three so they can tell a roll from a slide. A shallow cradle steadies the forearm and a grip at the far end gives the hand something to hold, which does more to keep an arm still than any sensor.
- **Lighting.** White LED strips under the top rails, on the back, both sides and the front, so the webcams always see an evenly lit arm and clear markers.
- **Electronics bay.** On the outside of the back wall, from top to bottom, sit the 24 V supply and mains inlet, the fuse block with the power relay and three converters, the USB hub, Teensy and servo adapter, and a shelf with the Jetson and the motion controller. Cables pass through a single grommeted opening in the back wall.
- **Cable holes.** One in the back wall for everything electrical, and one more for the probe cable, whose position depends on the version.

## Sensing

The machine has to answer four questions the whole time it runs, and each has more than one sensor behind it. This is the part of the design that changed most in version 7, where two depth cameras and a wrist band gave way to cheaper parts that each do one narrow job.

| Question | Sensor | Where it sits | What it contributes |
| --- | --- | --- | --- |
| Where is the arm, and where is the probe above it? | Two USB webcams | One overhead at the top left, one low at the front right looking across | Two flat views from different angles, enough to place a marker in three dimensions |
|  | Printed markers on the arm | Stuck on the skin | Fixed reference points the webcams can find exactly, so a tap on the screen maps to a real spot on the arm |
|  | Printed marker on the probe head | Front of the probe holder | Shows where the probe really is in the same camera view as the arm, so the two never have to be related through the gantry's own numbers alone |
| What shape is the skin right under the probe? | Four distance sensors | On tabs around the probe face | The distance to the skin on each side, which gives the height and the tilt needed to sit square, measured exactly where it matters |
|  | Load cell, used as a feeler | In the head | The fallback. Touching down at a few points maps the surface if the distance sensors struggle with gel or skin tone |
| Has the arm moved? | Six pressure pads | Under the arm rest padding, two columns of three | Feel the arm lift, roll or slide within a few milliseconds |
|  | The webcams again |  | See the arm markers drift. A slow drift is followed, a quick move pauses the scan |
| How is the probe sitting on the skin? | Load cell | In the head, above the gimbal | Contact force, so Z stops at a light touch |
|  | Lift switch | On the floating mount | Trips if the head is pushed up at all |
|  | Tilt sensor (BNO085) | On the probe holder | True pitch and roll from gravity, as a check on the servos |
|  | The servos' own angle sensors | Inside each servo | Confirm each tilt move actually finished |

Two cameras are used because the probe head will always block one view of the arm from somewhere, and because one view from above and one from the side are what turn flat pictures into a position in space. The wrist band from earlier versions is gone. Its job was catching a fast twitch, which the pads already do, and it was one more thing to strap onto a patient.

## Design choices

Each row is a decision that could have gone another way, with what it replaced and the reason it went this way.

| Decision | Instead of | Why |
| --- | --- | --- |
| Ink marker stamp | A needle insertion mechanism | Proves the system can find and hit the right point without piercing skin, which keeps the prototype safe to demonstrate. |
| Gantry from a donor 3D printer | Buying motors, rails, controller and supply separately, or a used laser engraver frame | One $179 purchase supplies most of the motion parts and a 350 W supply already matched to them. |
| Two motors on Y | One motor and one belt | A bridge driven from one side skews under load. |
| Linear rail on Z | A printed block sliding on extrusion | The head overhangs by 116 mm, and the rail resists the twist that overhang creates. |
| 116 mm reach bracket | The original 70 mm | The motion sweep showed the yoke hitting the Z rail before yaw reached 90°. |
| Floating head | Relying on the load cell and software to limit force | A purely mechanical limit still works if the software or a sensor fails. |
| Pen lifted by a micro servo | A $103 linear actuator, and before that a solenoid | The pen only has to travel about 15 mm and press with almost no force, which a $10 servo does easily. |
| Feedback bus servos (ST3215) | Hobby servos (SF3218MG) | They report their true angle, need one chained cable, and cost only about $3 more each. |
| A preload spring on each tilt joint | Trusting the servo gears alone | Gear slack is unpublished for these servos, and a spring that holds each joint against one side of the slack removes the wobble for a few dollars. |
| Servos on their own 12 V converter | Sharing the Jetson's 12 V | Three stalled servos can draw 8.1 A, nearly double that converter's rating, and the emergency stop must be able to cut them without cutting the computer. |
| Load cell amplifier on the head | On the back wall with the other boards | The load cell's signal is tiny and would pick up noise over a metre of moving cable. |
| A sensor board on the head | Running every head sensor's wires back to the Teensy | Six sensors and a servo would need far more wires through the cable chain than it can comfortably hold. One board on the head turns them into a single serial lead. |
| Two webcams and printed markers | Two depth cameras | Depth cameras cost several times as much and are known to struggle on smooth bare skin. Markers give the webcams something they can always find. |
| Distance sensors at the probe face | Building the arm's whole surface from the cameras | The only surface that matters is the patch under the probe, and four cheap sensors measure it directly at close range. |
| Hand grip, cradle and pressure pads | A wrist band motion sensor | Holding the arm comfortably prevents most movement, the pads catch the rest, and nothing has to be strapped on. |
| iPad in a slot as the screen | A wired touchscreen plus a phone for the Butterfly app | The Butterfly probe needs an Apple or Android device anyway, so one iPad does both jobs, the app is built with ordinary tools, and the Jetson no longer needs a display output at all. |
| Three walls and a slanted front | An open frame | Keeps hands and stray light out, gives the iPad a place facing the user, and gives the electronics an outside wall to live on. |
| Electronics outside the back wall | Mounted on the gantry or inside | Nothing inside competes with the gantry for space, and the boards stay reachable. |
| Jetson plus a separate Teensy | The Jetson reading every sensor itself | The safety checks keep running a thousand times a second even when the Jetson is busy with images. |
| Emergency stop breaks a relay's coil | The button switching motor power directly | The button was first drawn the wrong way round (normally open). A normally-closed button holding a relay in means a press, a loose connector or a cut wire all stop the machine, and the button never carries the motor current. |
| Emergency stop cuts motion power only | Cutting everything | The screen can still tell the user what happened, and the system does not need to reboot. |
| Tilt pivot 55 mm above the probe face | Pivoting at the servo shafts wherever they fall | Tilting barely shifts the probe face, so less gantry correction is needed. |

## Butterfly and Vscan versions

The two versions share the frame, gantry, floating mount, servos, sensors, computer, power system and software structure. They differ only where the probe itself forces a difference.

|  | Butterfly iQ3 version | GE Vscan Extend version |
| --- | --- | --- |
| Probe body | 152 × 52 × 37 mm, one imaging face | 129 × 39 × 28 mm, dual probe with a transducer at each end |
| Printed gimbal parts | Sized for the wider, longer body | A smaller set, so the two are not interchangeable |
| Where the image appears | The team's own app on the iPad | The Vscan's own display unit |
| Where that display lives | The iPad in its slot on the slanted panel, facing the user | Display unit inside a light-tight box on the outside of the back wall |
| How the Jetson gets the image | The app pulls frames through Butterfly's SDK and sends them to the Jetson over Wi-Fi | A small camera (Arducam IMX219) inside the light box, filming the display |
| Doppler and biplane imaging | Colour Doppler is offered by the SDK. Biplane is not mentioned in it and has to be asked about | Reaches the Jetson only as whatever the filmed screen shows, not as data |
| What the iPad does | The screen and the ultrasound host | The screen only |
| Probe cable route | Forward through a hole in the slanted panel to the iPad | Back through a hole in the back wall to the display unit |
| Extra data cable | None | Camera ribbon cable to the Jetson |
| Marker offset from probe centre | 48.5 mm | 44 mm |
| Extra cost in the parts list | None | About $30 (camera and box) |

The Butterfly version is the stronger of the two on image quality into the software, since frames taken straight from the SDK beat a camera pointed at a screen, and it is the only one where flow data can reach the vessel model. The Vscan version is mechanically lighter and does not depend on Butterfly granting and keeping up SDK access.

## How the design got here

| Revision | What changed |
| --- | --- |
| CAD version 7 | Team design review. Depth cameras replaced by two webcams, a marker on the head and four distance sensors. Touchscreen and phone replaced by an iPad mini in a printed slot. Marker actuator replaced by a pen-lift micro servo. Wrist band dropped for a hand grip and cradle, pads rearranged into two columns. Preload springs on the tilt joints, a sensor board on the head, and a normally-closed stop button holding a relay. |
| CAD version 6 | Hobby servos replaced by ST3215 bus servos. Servo driver board replaced by a bus adapter. Separate 12 V converter for the servos and a small 6 V one for the marker. |
| CAD version 5 | Floating head added as a mechanical force limit. Z slide moved onto a linear rail. |
| CAD version 4 | Second design audit. Dedicated second Y motor added, load cell amplifier moved onto the head, limit switches added. |
| CAD version 3 | First motion sweep. Reach bracket lengthened from 70 to 116 mm so yaw clears the Z rail. Marker solenoid replaced by a linear actuator. |
| CAD version 2 | First fully detailed model with every part, fastener and wire, checked for collisions. |
| Viewer version 7 | Enclosure refactor. Three walls, slanted front panel, electronics moved outside, lighting and wiring mapped. |
| Earlier viewer versions | Open gantry concept. Needle insertion replaced by an ink marker. One corner camera became two. Touchscreen added. |

The early browser viewer has its own numbering and still shows the layout from before the detailed CAD. The 3D page on the project site shows CAD version 7.

## Known limits and open questions

- **Nothing has been built yet.** Every dimension comes from the CAD model and supplier pages, and the probe bodies are modelled from published outer dimensions, not measured from the real probes.
- **Servo slack is unmeasured.** No supplier publishes it. One degree of play moves the probe face about 1 mm. The preload springs are there to hide it, but the first servo to arrive should still be tested before the other two are ordered.
- **Head weight sets the force limit.** The 7 N figure is an estimate and needs confirming by weighing the finished head, which is now a little heavier with the sensors and pen servo on it.
- **Webcam tracking is unproven on a real arm.** Markers can wrinkle, tilt away from a camera or get covered by the probe head, so the two views need testing across the whole travel before the arm tracker is trusted.
- **Distance sensors next to gel and skin.** These sensors time a pulse of infrared light, and wet gel or very dark or very pale skin may throw the reading off. The load cell touch-down is the fallback, and the sensor tabs in the CAD are drawn smaller than the real boards, so they need redrawing.
- **No sensor on the arm itself.** With the wrist band gone, a fast twitch is caught only by the pads, and the pads also feel the probe pressing down, so their thresholds have to be tuned with the probe in contact.
- **The iPad is now a dependency.** The Butterfly version only works with SDK access from Butterfly, an iPad the SDK supports, and a Wi-Fi link to the Jetson that stays up, and the iPad has to be charged outside the rig.
- **Ultrasound gel.** The probe needs gel, and loose gel smears the ink mark. A solid gel pad over the probe face is the likely answer and is not yet in the design.
- **Scanning is stop-and-go.** The probe moves, settles, corrects its tilt and then images. It does not glide continuously, which keeps the six axes in step at the cost of speed.
- **Reach.** 210 mm of travel along the arm covers a typical fistula site but not a whole forearm in one pass, so the arm has to be placed with the site inside that window.
- **The Teensy cannot yet stop the motors by itself.** A transistor in the relay's coil circuit, switched by the Teensy, is recommended and not yet in the CAD.
- **Open top.** Fine for development, but a finished unit would want a lid to keep hands and light out.

Part numbers and prices are in the [parts list](parts-list.html), part-by-part research notes are in the [parts research brief](parts-research.html), and the cable-by-cable map is in the [wiring and software debrief](wiring-software.html).
