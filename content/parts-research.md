---
title: Parts Research Brief
nav: Parts Research
order: 5
summary: What each part does, the current pick, and what to look for when hunting for something cheaper or better.
updated: 2026-11-24
pdf: assets/files/ultravena-parts-research.pdf
---

## The task

For every part below, answer two questions: does the current pick actually work for its job, and is there something cheaper or better. Each section explains what the part does and why the machine needs it, names the current pick with its price, and lists what to check when comparing options.

Every part in the build is listed, including the small ones nobody expects to change (belts, brackets, cables, printed pieces), so the tables double as a checklist that nothing has been forgotten.

Prices marked **confirmed** were read from the supplier's page on 23 or 24 Nov 2026. Prices marked **estimate** have no chosen listing yet, so finding one is part of the job. The live order list with links and IDs is in [UltraVena Hardware Parts List](parts-list.html).

For each part you research, bring back:

- The exact product name, supplier, part number and link.

- Price, shipping time and whether it is in stock.

- The numbers listed under "What to look for" for that part.

- A link to the supplier's 3D model (STEP file) if one exists, so it can go into the CAD.

- One line on what would have to change in the design if we switched to it.

A part that is cheaper but forces a redesign elsewhere is not automatically a win, so always note what it touches.

## How the machine works

UltraVena is a tabletop box the user slides a forearm into. A motorised ultrasound probe scans the arm, finds the fistula, and stamps an ink dot on the skin where the needle should go. Nothing pierces the skin.

The probe hangs from a three-axis gantry (X across the arm, Y along it, Z up and down) and can also turn three ways (yaw, pitch, roll), so it has six axes of motion in total. One scan runs like this:

1.  **Arm in, lights on.** The user rests an arm on the padded rest. LED strips light the inside so the cameras can see.

2.  **Find the arm.** Two depth cameras build a 3D surface of the forearm and track printed markers stuck on the skin.

3.  **Pick a start.** The user taps a spot on the touchscreen, which shows the camera view of the arm.

4.  **Travel and touch down.** The gantry carries the probe above that spot. The servos tilt it square to the skin, and Z lowers it until the load cell feels light contact.

5.  **Scan.** The probe steps along the arm. At each step the computer receives the live ultrasound image (streamed by the Butterfly SDK in the Butterfly build) and a trained model outlines the vessel.

6.  **Watch for movement.** Throughout, a wrist band motion sensor, pressure pads under the arm and the cameras check the arm has not moved. If it has, the machine stops.

7.  **Choose the point.** Software picks the cannulation point from the vessel's depth, width and position.

8.  **Mark it.** The probe lifts slightly, the gantry shifts by a known offset so the marker sits over that point, and a small actuator presses an ink tip onto the skin.

Two controllers share the work. A **Jetson** computer runs the image model, the cameras, the planning and the touchscreen. A **motion controller** turns its commands into motor steps, and a small **microcontroller** reads the fast safety sensors. The three tilt servos sit on one shared cable and report their true angles back, which is how the software keeps all six axes in step.

There are two builds, one around the **Butterfly iQ3** probe and one around the **GE Vscan Extend**. Butterfly has confirmed that its SDK streams imaging in real time to other devices, so in that build the Jetson takes the image straight from the stream and the phone on the front panel is simply the operator's view. The Vscan shows its image only on its own display unit, so that build still points a small camera at the display. Everything else is shared.

## Motion system

The gantry moves the probe in X, Y and Z. It is built from a cheap 3D printer taken apart for its motors, belts, rails, controller and power supply, then rebuilt as a bridge over the arm. Y uses two motors (one per side rail), X one, Z one.

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| Donor printer | Source of three stepper motors, belts, pulleys, rails, lead screw, controller and the 24 V supply | Creality Ender-3 V3 SE (MatterHackers, M-5EY-NWU0) | 179.00 confirmed | Same printer at Best Buy, 199.00 confirmed. A used Ender 3 of any generation. Buying the motors, rails and controller separately. |
| Fourth stepper motor | Second Y motor. The donor's fourth motor is a short extruder motor with a gear on its shaft and cannot drive a belt. | Pololu 2267, NEMA 17, 42 × 38 mm, 1.7 A | 35.12 confirmed | Generic NEMA 17 motors, likely much cheaper. |
| X and Y side rails | The tracks the bridge and the carriage roll along | 20 mm slotted extrusion from the donor, plus the frame extrusion listed under Structure | Included | Longer lengths if the donor's are under 400 mm. |
| Roller wheels and carriage plates | Carry the bridge along Y and the carriage along X | Donor's wheels and plates, with printed adapters where the hole patterns differ | Included | A wheel and plate kit made for 20 mm extrusion. |
| Timing belts | Pull the bridge (two belts, one per side) and the carriage (one belt) | Donor's 6 mm GT2 belt, with extra length bought by the metre | In the wiring and fasteners lot | Any 6 mm GT2 belt, fibreglass reinforced. |
| Belt pulleys and idlers | Pulley on each motor shaft, free-spinning idler at the far end of each belt | 20-tooth GT2 pulleys and idlers, three of each (donor supplies two) | In the wiring and fasteners lot | Any 20-tooth GT2 set with a 5 mm bore. |
| Z lead screw, nut and shaft coupler | Turns the Z motor's rotation into up and down travel | Donor's 8 mm lead screw, cut to about 150 mm | Included | A ready-cut 150 mm screw with a matching nut. |
| Z linear rail | Guides the Z slide. The probe head hangs 116 mm out from it, so it must resist twisting. | MGN12 rail, 250 mm, with two MGN12H carriages (no supplier chosen) | 30.00 estimate | Any supplier of MGN12 rail; a wheeled plate on the existing extrusion. |
| Z slide plate and motor mounts | Join the rail carriages, the lead nut and the head, and hold the four motors | Printed, or cut from 3 mm aluminium | Filament | A local laser or waterjet cutting service. |
| Limit switches | Give each axis a known home position at startup. A fourth senses the floating head lifting. | Roller-lever micro switch × 4 (no supplier chosen) | 8.00 estimate | Reuse the donor's switches if they fit. |
| Motion controller | Turns move commands from the Jetson into timed motor steps | The donor printer's own board | Included | A generic four-driver printer board. |
| Cable chain | Carries the moving wires to the bridge and the head without snagging | 10 × 15 mm drag chain, about 1 m (no supplier chosen) | In the wiring and fasteners lot | Any small drag chain; a printed cable tray. |

**What to look for**

- **Donor printer:** how many full-size motors it really contains; whether its controller can be reflashed with open firmware and can drive two Y motors; a 24 V supply of at least 300 W (ours peaks near 245 W); rail and belt lengths of at least 400 mm; whether its limit switches are separate parts.

- **Stepper motor:** 42 mm frame (NEMA 17), body at least 38 mm long, plain 5 mm shaft with a flat, 1.8° step, rated 1.5 A or more. It should match the donor's Y motor closely, because the two run as a pair.

- **Linear rail:** carriages must be the long "H" type, two of them, on a rail at least 240 mm long. Check for play by hand if buying in person; cheap rails vary a lot.

- **Controller:** at least four motor drivers, 24 V input, USB connection, and firmware we can configure ourselves.

- **Belts, pulleys and idlers:** all must share the same tooth pattern (GT2, 2 mm pitch) and belt width (6 mm). Total belt needed is about 3 m.

- **Lead screw:** check the nut has no free play along the screw, since any play shows up as an error in how deep the probe sits.

- **Cable chain:** the inside must fit a USB cable, the servo cable and about ten thin wires, and it must bend to a radius of 30 mm or less.

## Tilt servos

Three servos turn the probe: yaw spins it about its own axis, pitch and roll tilt it so its face sits square on the curve of the arm. This was the part of the design most in question, and the design has now moved from hobby servos to servos that report their position.

**The problem is slack, not strength.** Tilting the probe while it presses on the arm takes about 0.2 N·m (roughly 2 kg·cm). Every option below has at least seven times that. What limits accuracy is that ordinary hobby servos have loose gears, about a degree of play, and never report where they really are. One degree of tilt moves the probe face about 1 mm and shifts the ink mark by a similar amount.

The CAD model (version 6) uses the Waveshare ST3215. The hobby servo stays as the fallback, and the Dynamixel is the upgrade if testing shows the ST3215 is not good enough.

|  | Hobby servo (fallback) | Feedback servo, budget (current pick) | Feedback servo, premium |
| --- | --- | --- | --- |
| Product | [SunFounder SF3218MG](https://www.robotshop.com/products/sunfounder-sf3218mg-metal-gear-digital-servo-20kg-high-torque) | [Waveshare ST3215](https://www.waveshare.com/st3215-servo.htm?sku=22414) | [ROBOTIS Dynamixel XL430-W250-T](https://www.robotshop.com/products/robotis-dynamixel-xl430-w250-t-smart-servo-actuator) |
| Price each (USD) | 18.58 confirmed | 21.99 confirmed | 49.90 confirmed |
| Price for three | 55.74 | 65.97 | 149.70 |
| Torque | 20 kg·cm | 30 kg·cm at 12 V (a 7.4 V version gives 19.5) | 1.4 N·m at 11.1 V, about 14 kg·cm |
| Reports its position | No | Yes: position, load, speed, voltage | Yes |
| Position sensor | None readable | 12-bit magnetic encoder, 4096 steps per turn | 12-bit encoder, about 0.088° per step |
| Control | One signal wire each from a driver board | Serial bus, servos chained on one cable | Serial bus, servos chained on one cable |
| Supply | 4.8 to 7.2 V | 6 to 12.6 V (or 4 to 7.4 V version) | 6.5 to 12 V |
| Stall current | Not published; 2.5 A assumed | 2.7 A | 1.3 A at 11.1 V |
| Gears | Metal | Metal | Plastic |
| Weight | Not published | 89 g | 57 g |
| Stated gear slack | Not published | Not published | Not published |

**What feedback fixes, and what it does not.** A feedback servo tells the computer its true angle, so the software can correct for error, confirm a move finished, and time the six axes together. It does not remove gear slack by itself. None of the three pages states a slack figure, so the only way to know is to buy one and measure it.

**What the switch changed in the design**

- The servo driver board (Adafruit 815, $14.95) is gone, replaced by a serial bus adapter at $4.99.

- Wiring dropped from three separate leads to one cable chained from servo to servo.

- The servos now run on 12 V from their own 15 A converter, because three of them can draw 8.1 A when stalled and the Jetson's 12 V converter is rated 4.5 A.

- The marker actuator, which used to share the servos' 6 V, got a small 6 V converter of its own.

- The printed yaw mount, yoke and pitch ring were redrawn with cradles for the new body, which is 45.2 × 24.7 × 35 mm.

- The tilt sensor on the probe holder stays for now as an independent check on pitch and roll.

**Parts that go with the servos**

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| Serial bus adapter | Links the servo cable to the microcontroller or to the Jetson over USB, and feeds the servos 12 V | [Waveshare Bus Servo Adapter (A)](https://www.waveshare.com/bus-servo-adapter-a.htm), SKU 25514 | 4.99 confirmed | Feetech's own adapter boards; the Dynamixel U2D2 if we move to Dynamixel. |
| Servo horns (× 3) | The disc on each servo's shaft that the printed parts bolt to | The metal horn supplied with each servo | Included, to confirm | Aluminium 25-tooth horns. |
| Servo cables (× 3) | Carry power and data from the adapter to yaw, then pitch, then roll | The lead supplied with each servo, extended for the run from the back wall to the head | Included, to confirm | Longer three-wire leads of the same connector type, rated for repeated bending. |
| Printed servo cradles | Clamp each servo body to the yaw mount, the yoke arm and the pitch ring | Printed in-house | Filament | None needed. |

**What to look for**

- A stated backlash or gear-play figure in degrees. Smaller is better; under 0.5° would be a real gain.

- Whether the position sensor is on the output shaft (good) or the motor (blind to gear slack).

- A working code library for Python on the Jetson or for the Teensy.

- Body dimensions and a downloadable 3D model, since any change of body means reprinting the cradles.

- Weight. All three ride on the moving head, and the heaviest is the pitch servo out on the yoke arm.

- Stall current and supply voltage, which decide the converter.

- Other brands in the same family worth pricing: Feetech (the maker behind the ST3215), Hiwonder, and the Dynamixel XC and XM lines.

**If slack is still too high after testing,** two cheap mechanical fixes are worth researching: a light spring that keeps each tilt axis pressed to one side of its slack, and replacing the tilt servos with small geared stepper motors.

## Probe head

The head is everything that hangs from the Z slide: a floating mount, the load cell, the three servos, the printed gimbal that holds the probe, the tilt sensor and the marker.

The head **floats**. It hangs on two guide rods and lifts freely by 15 mm if the probe is pushed up, so the most it can ever press on the arm is its own weight (about 7 N by estimate with the heavier servos, to be confirmed by weighing the finished head). This is the mechanical safety limit and must not be designed out.

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| Ultrasound probe | Makes the image. The whole head is shaped around it. | Butterfly iQ3, or GE Vscan Extend with its display unit | Not in this budget | None; the two builds exist to compare these two. |
| Floating mount hardware | Lets the head lift under force | Two 6 mm rods, two bushings, two stop collars (no supplier chosen) | 12.00 estimate | Linear ball bushings; a short second linear rail. |
| Carrier plate | Rides on the two rods and carries the load cell and everything below it | Printed in-house | Filament | Cut from 3 mm aluminium if the print flexes. |
| Lift switch | Trips the moment the head starts to float, which tells the motors to stop | One of the four limit switches in the motion table | Counted there | Same choices as the limit switches. |
| Load cell | Measures how hard the probe presses, so Z can stop at light contact | SparkFun SEN-14729, 5 kg bar (TAL220B) | 15.50 confirmed | A 1 or 2 kg bar of the same size, for finer readings. |
| Load cell amplifier | Turns the load cell's tiny signal into a number the microcontroller reads. Mounted on the head, so the weak signal travels only a few centimetres. | SparkFun SEN-13879 (HX711) | 4.95 confirmed | Amplifier boards with a standard two-wire data bus. |
| Printed gimbal (yaw mount, yoke, pitch ring, probe holder) | The nested frames that let the three servos turn the probe about a point 55 mm above its face | Printed in-house, one set per probe | Filament | A print service, or a stiffer material, if the parts flex. |
| Probe clamp screws and padding | Hold the probe in its holder without marking it | M3 screws with a strip of thin foam | In the wiring and fasteners lot | None needed. |
| Tilt sensor | Reads the probe's true pitch and roll from gravity, as a check on the servos | Adafruit 4754 (BNO085) | 29.50 confirmed | Cheaper motion sensors. A second one goes in the wrist band. |
| Marker actuator | Lowers an ink tip onto the skin and presses it | Actuonix L12-30-50-6-R linear servo (RobotShop Canada, RB-Fir-223) | 102.94, currency unclear | Cheaper micro linear servos; a small servo driving a rack. |
| Marker actuator clamp | Fixes the actuator to the side of the probe holder, 48.5 mm from the probe centre (44 mm on the Vscan) | Printed in-house | Filament | None needed. |
| Marker tip | Leaves the dot | Tip cut from a skin-safe marker | 0 | Surgical skin markers. |

**What to look for**

- **Floating mount:** it must slide freely even when the head is tilted or pushed sideways, with at least 15 mm of travel. Sticky bushings defeat the safety limit.

- **Load cell:** bar type, about 80 × 12.7 × 12.7 mm, four wires. It carries the head's weight (about 730 g) all the time, so capacity must exceed that plus the pressing force.

- **Amplifier:** runs from 3.3 V, and offers at least 80 readings per second.

- **Tilt sensor:** does its own sensor fusion on the chip, is accurate to about 1°, runs from 3.3 V, and has a serial output mode for the long cable run.

- **Marker actuator:** this is the most overpriced part in the list. The job needs only about 14 mm of travel and a few newtons. Look for travel of 15 mm or more, position control from a standard servo signal that a 3.3 V board can drive, a 6 V supply, closed length under about 85 mm, and weight under 40 g.

## Sensing the arm

The machine has to know where the arm is, what shape its surface is, and whether it has moved. Three independent sensors watch for movement so that no single failure goes unnoticed.

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| Depth cameras (× 2) | Measure the 3D surface of the forearm and track the markers. Two, at opposite corners, so the probe head cannot block both. | RealSense D405 (part no. 82635DSD405) | 350.00 each, estimate | Other RealSense models; other depth cameras; two plain webcams. |
| Camera brackets (× 2) | Hold each camera high in a corner, angled down at the arm | Printed in-house | Filament | A small ball-head mount, which makes aiming easier. |
| Camera USB cables (× 2) | Carry depth data to the hub | The cable supplied with each camera, if long enough | Included, to confirm | USB 3 cables of about 1 m with a locking or right-angle plug. |
| Tracking markers (× 4) | Printed patterns stuck on the skin that the cameras can locate exactly | Printed in-house on sticker paper | 0 | None needed. |
| Wrist band sensor | Catches a twitch faster than the cameras can | A second BNO085 | 29.50 confirmed | Same choices as the tilt sensor. |
| Wrist strap | Holds that sensor on the wrist | Elastic hook-and-loop strap | In the padding and strap lot | Any soft strap that wipes clean. |
| Pressure pads (× 6) | Feel the arm lift or roll on the rest | Adafruit 1075 square force sensor | 5.95 each confirmed, out of stock | Pololu 1645, same size, 20.49 confirmed. |
| Pad resistors (× 6) | Each pad needs one fixed resistor so the microcontroller can read it | 10 kΩ resistors | In the wiring and fasteners lot | None needed. |

**What to look for**

- **Depth cameras:** this is the largest cost in the build, about a third of the total, so it is the most valuable thing to research.

    - Closest working distance of 20 cm or less. Everything in the rig is within half a metre.

    - Depth accuracy of 1 to 2 mm at 30 to 40 cm.

    - Whether it works on bare skin. The D405 has no built-in light pattern and relies on visible texture, which smooth skin lacks. A camera that projects its own pattern may do better.

    - USB 3, and software support for a Jetson running Linux.

    - Whether two can run side by side without interfering.

    - Whether one depth camera plus one cheap webcam would be enough.

- **Pressure pads:** sensing area near 38 mm square, responds to forces from about 0.2 N, thin enough to sit under padding, with a tail long enough to reach the edge of the arm rest.

## Computing and touchscreen

The Jetson is the machine's brain. It runs the vessel-finding model on each ultrasound frame, reads the depth cameras, plans every move and draws the touchscreen. The microcontroller handles the fast safety loop (wrist band, pressure pads, load cell, lift switch) because that must keep running even if the Jetson is busy. In the Butterfly build the ultrasound frames reach the Jetson through Butterfly's SDK, which the company confirmed can stream imaging in real time to other devices.

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| Main computer | Image model, cameras, planning, user interface | NVIDIA Jetson Orin Nano Super Developer Kit (SparkFun DEV-22098) | 249.00 confirmed | Other Jetson kits; a small PC with a graphics chip. |
| Storage | Holds the operating system and software | Not chosen | 30.00 estimate | Any drive the kit accepts. |
| Ultrasound image link (Butterfly build) | Gets live frames from the probe to the Jetson | Butterfly SDK real-time stream | No hardware cost known | None; ask Butterfly about licence terms. |
| Phone (Butterfly build) | Runs the Butterfly app and shows the operator the image | The team's own phone on the front panel | Not in this budget | A tablet, if the SDK allows it. |
| Microcontroller | Fast safety loop and sensor reading | Teensy 4.0 (SparkFun DEV-15583) | 23.80 confirmed | Cheaper microcontroller boards. |
| Touchscreen | Shows the camera view; the user taps to start, stop and choose a site | Waveshare 7 inch HDMI LCD (H) with case, SKU 13857 | 53.99 confirmed | Other 7 inch HDMI touch displays. |
| USB hub | The Jetson has fewer ports than there are devices | Powered USB 3 hub, 7 port (not chosen) | 25.00 estimate | Any powered hub. |
| HDMI and USB cables | Join the touchscreen, hub, motion controller, microcontroller and servo adapter to the Jetson | Short cables, some supplied with the parts | In the wiring and fasteners lot | Right-angle plugs where a cable passes through a wall. |

**What to look for**

- **Main computer:** must run our image model at 10 frames a second or better, take two USB 3 depth cameras at once, drive an HDMI screen, and accept a 9 to 20 V supply.

- **Storage:** check which drive type and length the kit's slot takes before buying.

- **Microcontroller:** 3.3 V logic, at least six analog inputs for the pressure pads, two or more serial ports, and USB. Note the Teensy is not safe with 5 V signals.

- **Touchscreen:** HDMI video plus touch over USB, capacitive, works on Linux without a special driver, runs from 5 V at about 1 A, and fits a space about 190 × 122 mm on the slanted front panel.

- **USB hub:** USB 3, its own power input, at least five ports.

- **Ultrasound image link:** from Butterfly we still need to know which device hosts the probe, whether the Jetson (Linux on an Arm processor) can receive the stream directly or only through the phone, the delay from probe to frame, and whether Doppler and biplane frames are included.

## Power, safety and lighting

One 24 V supply feeds everything. Four converters step it down: 12 V for the Jetson and lights, a separate 12 V for the three servos, 6 V for the marker actuator, and 5 V for the touchscreen and USB hub. The emergency stop cuts 24 V to the motion controller and to the servo and actuator converters, so everything that moves loses power while the computer and sensors stay on. Peak draw is about 245 W of the supply's 350 W.

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| 24 V supply | Powers the whole machine | The donor printer's 350 W supply | Included | A standalone 24 V supply if the donor's is unusable. |
| Mains inlet | Wall power in, with switch and fuse | Not chosen | 12.00 estimate | The donor's inlet, if reusable. |
| Mains cord | Wall socket to the inlet | The donor printer's cord | Included | Any cord of the same plug type. |
| Fuse block and fuses | Splits 24 V into separately fused branches, one per converter and one for the motion controller | Six-way blade fuse block, not chosen | 12.00 estimate | Any blade-fuse block. |
| Emergency stop | Cuts power to everything that moves, by hand | DFRobot FIT0156 | 5.90 confirmed | Any 22 mm emergency stop. |
| 12 V converter, computer | Jetson and LED strips | Pololu 4095 (D36V50F12), 4.5 A | 44.95 confirmed, backorder | Generic step-down modules. |
| 12 V converter, servos | The three tilt servos, through the bus adapter | Pololu 2885 (D24V150F12), 15 A | 79.95 confirmed, backorder | Pololu's newer D42V110F family; generic 10 A modules. |
| 6 V converter | Marker actuator | Pololu 3783 (D36V28F6), 2.7 A | 24.95 confirmed, backorder | Any small 6 V module of 1 A or more. |
| 5 V converter | Touchscreen and USB hub | Pololu 4091 (D36V50F5), 5.5 A | 44.95 confirmed, backorder | Generic step-down modules. |
| LED strips | Light the inside for the cameras | Adafruit 4612, 1 m, × 2 | 11.95 each confirmed | Any 12 V white strip. |
| LED channels and diffusers | Hold the strips along the top rails and soften the light | Aluminium channel with a frosted cover, about 1.8 m (no supplier chosen) | In the wiring and fasteners lot | Printed clips with a strip of frosted film. |
| Power wire and connectors | Join the supply, fuse block, converters and loads | 18 gauge for 24 V and servo power, 22 gauge elsewhere, with screw terminals or crimp connectors | In the wiring and fasteners lot | Pre-made leads where a part has a specific plug, such as the Jetson's barrel jack. |

**What to look for**

- **Converters:** together these cost about $195, and cheaper modules almost certainly exist. Each must accept at least 28 V in. The continuous ratings to meet are 4.5 A at 12 V for the computer side, 10 A at 12 V for the servos (their combined stall draw is 8.1 A), 1 A at 6 V for the marker actuator and 5 A at 5 V. Check for over-current protection and screw terminals.

- **Fuses:** one per branch, sized just above that branch's peak current.

- **Emergency stop:** it must have a normally-closed contact (the circuit breaks when pressed), a twist or pull release, and a contact rating for 24 V DC at 10 A or more. The current pick's page does not state its contact type.

- **LED strips:** 12 V, about 1.8 m in total, neutral white. Even light matters more than brightness.

- **Power wire:** thick enough for its branch, and flexible stranded wire on anything that moves.

## Structure and version-specific parts

The enclosure is a frame of 20 mm aluminium extrusion with panels on the back and both sides, an open top, and a steep slanted panel over the arm opening that carries the touchscreen. It is 516 × 562 mm at the base and 590 mm tall. The computer and power parts hang on the outside of the back wall.

| Part | What it does | Current pick | Price (USD) | What to look for |
| --- | --- | --- | --- | --- |
| Aluminium extrusion, about 4.6 m | Enclosure frame | 20 × 20 mm T-slot (no supplier chosen) | 50 estimate | Cut-to-length service; the same slot size as the donor's extrusion. |
| Corner brackets and slot nuts | Join the extrusions at every corner | Cast corner brackets with M5 screws and slot nuts, about 30 sets | In the wiring and fasteners lot | Brackets and nuts made for the same slot size as the extrusion. |
| Wall panels (× 3) | Close the back and both sides, keep hands out and the light even | 3 mm acrylic | 75 estimate with the front panel | Cut-to-size service; a cheaper opaque sheet would also work. |
| Slanted front panel | Carries the touchscreen and the phone above the arm opening | 3 mm acrylic with cut-outs for the screen and the probe cable | Counted with the wall panels | A service that can cut the openings, or a printed panel in two halves. |
| Base plate | Everything bolts to it | 516 × 562 mm sheet | 25 estimate | Flat and stiff; plywood or aluminium. |
| Rubber feet (× 4) | Stop the box sliding and damp vibration | Stick-on or screw-on feet | In the wiring and fasteners lot | Feet tall enough to clear the screw heads under the base. |
| Electronics shelf | Holds the Jetson and motion controller on the outside of the back wall | Printed or cut from sheet | Filament | Air must reach the Jetson's fan. |
| Standoffs and mounting screws | Fix each board and converter to the back wall | M2.5 and M3 nylon standoffs | In the wiring and fasteners lot | Lengths of 6 to 10 mm, so nothing shorts against the panel. |
| Cable grommets | Line the holes where cables pass through the back wall and the front panel | Rubber grommets, about six | In the wiring and fasteners lot | Inner hole wide enough for a USB plug. |
| Cable tray | Carries the fixed cable run along the back wall | Printed in-house | Filament | None needed. |
| Printing filament | Gimbal, probe holder, cradles, brackets, shelf, cable tray | 1 kg | 20 estimate | A material that does not creep under the servos' load. |
| Wire, cable chain, fasteners | 50 wires in the current model, plus every small item marked as in this lot | One lot | 50 estimate | Flexible cable rated for repeated bending on the moving runs. |
| Arm rest padding and strap | Comfort and holding the arm still | Foam and strap | 15 estimate | Wipe-clean surface. |
| Phone mount (Butterfly build) | Holds the phone that shows the image | Magnetic mount or charger | 39 estimate | Whether it needs power, and what kind. |
| Display unit and light box (Vscan build) | The Vscan's own screen, enclosed so the camera reads it without glare | The Vscan display unit in a printed box on the outside wall | Filament | Matte black inside, with a slot for the probe cable. |
| Camera for the display (Vscan build) | Reads the Vscan's screen inside the light box | Arducam IMX219 for Jetson (SparkFun SEN-28170) | 19.95 confirmed | Sharp focus at about 150 mm; a connector that matches the Jetson kit. |

## Problems no part solves yet

These need research as much as any part above. Getting the ultrasound image into the Jetson used to head this list and has been removed, because Butterfly confirmed in a meeting that its SDK streams imaging in real time to other devices.

- **Ultrasound gel.** The probe needs gel to see anything, and loose gel smears the ink mark. Research solid gel pads that clip over a probe face.

- **Putting Doppler and biplane to use.** Telling artery from vein is no longer a missing capability, since the Butterfly has Doppler (which shows blood flow) and biplane imaging (two views at right angles at once). What remains is software and confirmation: whether those modes come through the SDK stream as data the Jetson can read, how fast the frames arrive in each mode, and how the vessel-finding model should use flow and the second view.

- **The Vscan build has no such stream.** It still reads its image by camera from the display, so anything we build on Doppler or biplane data will work on the Butterfly build only unless GE offers an equivalent.

- **Servo slack is unmeasured.** No supplier publishes it, so the first ST3215 that arrives should be tested before the other two are ordered.

## Sources

Servo and power pages opened on 24 Nov 2026: [Waveshare ST3215](https://www.waveshare.com/st3215-servo.htm?sku=22414), [Waveshare Bus Servo Adapter (A)](https://www.waveshare.com/bus-servo-adapter-a.htm), [RobotShop, Dynamixel XL430-W250-T](https://www.robotshop.com/products/robotis-dynamixel-xl430-w250-t-smart-servo-actuator), [ROBOTIS e-Manual, XL430-W250](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/), [RobotShop, SunFounder SF3218MG](https://www.robotshop.com/products/sunfounder-sf3218mg-metal-gear-digital-servo-20kg-high-torque), [Pololu 2885](https://www.pololu.com/product/2885), [Pololu 3783](https://www.pololu.com/product/3783). The Butterfly SDK, Doppler and biplane points come from the team's meeting with Butterfly, not from a web page. Links for every other confirmed price are in the [parts list](parts-list.html).
