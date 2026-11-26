---
title: Parts Research Brief
nav: Parts Research
order: 5
summary: What each part does, the current pick, and what to look for when hunting for something cheaper or better.
updated: 2026-11-26
pdf: assets/files/ultravena-parts-research.pdf
---

## The task

For every part below, answer two questions: does the current pick actually work for its job, and is there something cheaper or better. Each section explains what the part does and why the machine needs it, names the current pick with its price, and lists what to check when comparing options.

Every part in the build is listed, including the small ones nobody expects to change (belts, brackets, cables, printed pieces), so the tables double as a checklist that nothing has been forgotten.

Prices marked **confirmed** were read from the supplier's page on 23, 24 or 26 Nov 2026. Prices marked **estimate** have no chosen listing yet, so finding one is part of the job. The live order list with links and IDs is in [UltraVena Hardware Parts List](parts-list.html).

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

1. **Arm in, lights on.** The user rests an arm on the padded rest and holds the grip at the far end. LED strips light the inside so the cameras can see.
2. **Find the arm.** Two webcams, one overhead and one at the side, find printed markers stuck on the skin and a matching marker on the probe head, which tells the computer where the arm and the probe are.
3. **Pick a start.** The user taps a spot on the iPad, which shows the camera view of the arm.
4. **Travel and touch down.** The gantry carries the probe above that spot. Four small distance sensors around the probe face measure how far the skin is on each side, the servos tilt the probe square to it, and Z lowers it until the load cell feels light contact.
5. **Scan.** The probe steps along the arm. At each step the computer receives the live ultrasound image (in the Butterfly build the iPad app gets it from the Butterfly SDK and passes it on) and a trained model outlines the vessel.
6. **Watch for movement.** Throughout, pressure pads under the arm and the webcams check the arm has not moved. A slow drift is followed, and a quick move stops the scan.
7. **Choose the point.** Software picks the cannulation point from the vessel's depth, width and position.
8. **Mark it.** The probe lifts slightly, the gantry shifts by a known offset so the marker sits over that point, and a micro servo dips an ink pen onto the skin.

Several processors share the work. A **Jetson** computer runs the image model, the cameras and the planning. An **iPad** in a slot on the front panel is the screen, running an app the team writes. A **motion controller** turns the Jetson's commands into motor steps, a small **microcontroller** reads the fast safety sensors, and a second, smaller board on the probe head gathers the head's sensors for it. The three tilt servos sit on one shared cable and report their true angles back, which is how the software keeps all six axes in step.

There are two builds, one around the **Butterfly iQ3** probe and one around the **GE Vscan Extend**. In the Butterfly build the probe plugs into the iPad, the team's app reads the image through Butterfly's SDK (which the team is getting access to), and the app passes each frame to the Jetson over Wi-Fi. The Vscan shows its image only on its own display unit, so that build still points a small camera at the display and the iPad is only the screen. Everything else is shared.

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

- **Donor printer:** how many full-size motors it really contains; whether its controller can be reflashed with open firmware and can drive two Y motors; a 24 V supply of at least 300 W (ours peaks near 230 W); rail and belt lengths of at least 400 mm; whether its limit switches are separate parts.
- **Stepper motor:** 42 mm frame (NEMA 17), body at least 38 mm long, plain 5 mm shaft with a flat, 1.8° step, rated 1.5 A or more. It should match the donor's Y motor closely, because the two run as a pair.
- **Linear rail:** carriages must be the long "H" type, two of them, on a rail at least 240 mm long. Check for play by hand if buying in person; cheap rails vary a lot.
- **Controller:** at least four motor drivers, 24 V input, USB connection, and firmware we can configure ourselves.
- **Belts, pulleys and idlers:** all must share the same tooth pattern (GT2, 2 mm pitch) and belt width (6 mm). Total belt needed is about 3 m.
- **Lead screw:** check the nut has no free play along the screw, since any play shows up as an error in how deep the probe sits.
- **Cable chain:** the inside must fit a USB cable, the servo cable and about ten thin wires, and it must bend to a radius of 30 mm or less.

## Tilt servos

Three servos turn the probe: yaw spins it about its own axis, pitch and roll tilt it so its face sits square on the curve of the arm. This was the part of the design most in question, and the design has now moved from hobby servos to servos that report their position.

**The problem is slack, not strength.** Tilting the probe while it presses on the arm takes about 0.2 N·m (roughly 2 kg·cm). Every option below has at least seven times that. What limits accuracy is that ordinary hobby servos have loose gears, about a degree of play, and never report where they really are. One degree of tilt moves the probe face about 1 mm and shifts the ink mark by a similar amount.

The CAD model (version 7) uses the Waveshare ST3215. The hobby servo stays as the fallback, and the Dynamixel is the upgrade if testing shows the ST3215 is not good enough.

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
- The marker actuator, which used to share the servos' 6 V, briefly had a 6 V converter of its own. Both are gone in version 7, where a micro servo on 5 V lifts the pen.
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

**Springs are now in the design.** After the team's design review, CAD version 7 adds a light spring to each tilt joint that keeps it pressed to one side of its slack. If slack is still too high after testing, the remaining fix worth researching is replacing the tilt servos with small geared stepper motors.

## Probe head

The head is everything that hangs from the Z slide, which means a floating mount, the load cell, a small sensor board, the three servos with their springs, the printed gimbal that holds the probe, the tilt sensor, four distance sensors, a tracking marker and the marking pen.

The head **floats**. It hangs on two guide rods and lifts freely by 15 mm if the probe is pushed up, so the most it can ever press on the arm is its own weight (about 7 N by estimate with the heavier servos, to be confirmed by weighing the finished head). This is the mechanical safety limit and must not be designed out.

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| Ultrasound probe | Makes the image. The whole head is shaped around it. | Butterfly iQ3, or GE Vscan Extend with its display unit | Not in this budget | None; the two builds exist to compare these two. |
| Floating mount hardware | Lets the head lift under force | Two 6 mm rods, two bushings, two stop collars (no supplier chosen) | 12.00 estimate | Linear ball bushings; a short second linear rail. |
| Carrier plate | Rides on the two rods and carries the load cell and everything below it | Printed in-house | Filament | Cut from 3 mm aluminium if the print flexes. |
| Lift switch | Trips the moment the head starts to float, which tells the motors to stop | One of the four limit switches in the motion table | Counted there | Same choices as the limit switches. |
| Load cell | Measures how hard the probe presses, so Z can stop at light contact | SparkFun SEN-14729, 5 kg bar (TAL220B) | 15.50 confirmed | A 1 or 2 kg bar of the same size, for finer readings. |
| Load cell amplifier | Turns the load cell's tiny signal into a number the head sensor board reads. Mounted on the head, so the weak signal travels only a few centimetres. | SparkFun SEN-13879 (HX711) | 4.95 confirmed | Amplifier boards with a standard two-wire data bus. |
| Head sensor board | Reads the load cell, tilt sensor and distance sensors, drives the marker servo, and sends everything to the microcontroller down one serial lead | Adafruit QT Py class board (Adafruit 4900) | 9.95 estimate | Any small 3.3 V board with more than eleven pins, which would leave a spare. |
| Printed gimbal (yaw mount, yoke, pitch ring, probe holder) | The nested frames that let the three servos turn the probe about a point 55 mm above its face | Printed in-house, one set per probe | Filament | A print service, or a stiffer material, if the parts flex. |
| Preload springs (× 3) | Hold each tilt joint against one side of its gear slack so the probe does not wobble | Light springs, one per joint (no supplier chosen) | 8.00 estimate for the set | A spring assortment, so the right stiffness can be found by trial. |
| Probe clamp screws and padding | Hold the probe in its holder without marking it | M3 screws with a strip of thin foam | In the wiring and fasteners lot | None needed. |
| Tilt sensor | Reads the probe's true pitch and roll from gravity, as a check on the servos | Adafruit 4754 (BNO085) | 29.50 confirmed | Cheaper motion sensors. |
| Distance sensors (× 4) | Measure how far the skin is on each side of the probe face, which gives the height and the tilt needed to sit square | Adafruit 5396 (VL53L4CD) | 14.95 each confirmed | Smaller boards carrying the same chip; other short-range time-of-flight sensors. |
| Head tracking marker | A printed pattern on the front of the probe holder that the webcams use to see where the probe is | Printed in-house on sticker paper | 0 | None needed. |
| Marker servo | Lifts and dips the ink pen | Adafruit 1143 (MG90D micro servo) | 9.95 confirmed | Any 9 gram metal-gear micro servo. |
| Pen guide and servo shelf | Hold the pen upright beside the probe holder, 48.5 mm from the probe centre (44 mm on the Vscan), with the servo above it | Printed in-house, part of the probe holder | Filament | None needed. |
| Marker pen | Leaves the dot | A skin-safe marker | 0 | Surgical skin markers. |

**What to look for**

- **Floating mount:** it must slide freely even when the head is tilted or pushed sideways, with at least 15 mm of travel. Sticky bushings defeat the safety limit.
- **Load cell:** bar type, about 80 × 12.7 × 12.7 mm, four wires. It carries the head's weight (about 730 g before the new sensors) all the time, so capacity must exceed that plus the pressing force.
- **Amplifier:** runs from 3.3 V, and offers at least 80 readings per second.
- **Head sensor board:** 3.3 V logic, a serial port, a two-wire sensor bus, at least eleven usable pins, and small and light enough to ride on the Z slide.
- **Tilt sensor:** does its own sensor fusion on the chip, is accurate to about 1°, runs from 3.3 V, and can share a bus with other sensors or fall back to a simple serial mode.
- **Distance sensors:** time-of-flight type that reads from a few millimetres out to at least 100 mm with roughly 1 mm resolution, an enable pin so four can share one bus, and a board small enough to sit beside the probe face. The current pick is about 25.5 × 17.7 mm, which is larger than the tabs drawn in the CAD, so a smaller board would save a redraw. Check how each behaves on skin and near wet gel.
- **Springs:** strong enough to hold the joint against its slack with the probe's weight on it, and light enough that the servo does not run warm fighting them. This will take a trial or two.
- **Marker servo:** the linear actuator it replaced was the most overpriced part in the old list. The job needs about 15 mm of pen travel and almost no force. Look for a 9 gram class servo with metal gears that runs on 5 V and accepts a 3.3 V control pulse.

## Sensing the arm

The machine has to know where the arm is, what the skin under the probe looks like, and whether the arm has moved. In version 7 the two depth cameras and the wrist band are gone. Two webcams and printed markers now find the arm, four distance sensors at the probe face (listed with the head above) read the skin, and a hand grip with six pressure pads keeps the arm still and notices when it is not.

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| Webcams (× 2) | Find the printed markers on the arm and on the probe head. One overhead and one at the side, so the probe head cannot block both and the two views together give a position in space. | Arducam B0468 USB camera | 39.99 each confirmed | Any USB webcam whose focus can be fixed; a wider lens for the overhead view. |
| Camera brackets (× 2) | Hold the overhead camera at the top left and the side camera low at the front right | Printed in-house | Filament | A small ball-head mount, which makes aiming easier. |
| Camera USB cables (× 2) | Carry the pictures to the hub | The cable supplied with each camera, if long enough | Included, to confirm | USB extension leads of about 1 m. |
| Tracking markers on the arm (× 4) | Printed patterns stuck on the skin that the cameras can locate exactly | Printed in-house on sticker paper | 0 | None needed. |
| Pressure pads (× 6) | Feel the arm lift, roll or slide on the rest. Laid out as two columns of three. | Adafruit 1075 square force sensor | 5.95 each confirmed, out of stock | Pololu 1645, same size, 20.49 confirmed. |
| Pad resistors (× 6) | Each pad needs one fixed resistor so the microcontroller can read it | 10 kΩ resistors | In the wiring and fasteners lot | None needed. |
| Hand grip and forearm cradle | Give the hand something to hold and steady the forearm, which prevents most movement before a sensor has to catch it | Printed in-house, on the arm rest | Filament | A soft bicycle-style grip slipped over the printed post. |

**What to look for**

- **Webcams:** these replaced the depth cameras, which were about a third of the old total. What matters now is steadiness more than resolution.
  - A focus that can be fixed. A camera that keeps hunting for focus ruins marker tracking.
  - A lens wide enough to see the whole arm rest from about half a metre, with distortion low enough for the software to calibrate out.
  - Shows up on Linux as a standard USB camera with no special driver, and two can run at once on one hub.
  - A frame rate of 30 a second at the resolution used.
- **Tracking markers:** how large they must be for both cameras to read them across the rig, and a sticker material that stays flat on skin and peels off cleanly.
- **Pressure pads:** sensing area near 38 mm square, responds to forces from about 0.2 N, thin enough to sit under padding, with a tail long enough to reach the edge of the arm rest.

## Computing and screen

The Jetson is the machine's brain. It runs the vessel-finding model on each ultrasound frame, reads the webcams and plans every move. The screen is no longer wired to it. An iPad mini the team already has sits in a slot on the front panel, runs an app written in Xcode, and talks to the Jetson over a Wi-Fi network that the Jetson hosts. The microcontroller handles the fast safety loop (pressure pads, load cell, lift switch, distance sensors) because that must keep running even if the Jetson is busy. In the Butterfly build the probe plugs into the iPad, and the app forwards each frame from Butterfly's SDK to the Jetson.

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| Main computer | Image model, cameras, planning | NVIDIA Jetson Orin Nano Super Developer Kit (SparkFun DEV-22098) | 249.00 confirmed | Other Jetson kits; a small PC with a graphics chip. |
| Storage | Holds the operating system and software | Not chosen | 30.00 estimate | Any drive the kit accepts. |
| Screen and ultrasound host | Shows the camera view and takes the taps for start, stop and choosing a site. In the Butterfly build it also hosts the probe. | The team's own iPad mini, in a printed slot on the front panel | Not in this budget | Any iPad the Butterfly SDK supports. |
| Ultrasound image link (Butterfly build) | Gets live frames from the probe to the Jetson | Butterfly's imaging SDK for iOS inside the team's app, then Wi-Fi to the Jetson | No hardware cost known | None; confirm the licence terms with Butterfly. |
| Wi-Fi link | Joins the iPad to the Jetson | The wireless module already fitted to the Jetson kit, hosting its own network | Included | A small travel router, if the Jetson cannot host a network reliably. |
| Microcontroller | Fast safety loop and sensor reading | Teensy 4.0 (SparkFun DEV-15583) | 23.80 confirmed | Cheaper microcontroller boards. |
| USB hub | The Jetson has fewer ports than there are devices | Powered USB 3 hub, 7 port (not chosen) | 25.00 estimate | Any powered hub. |
| USB cables | Join the hub, motion controller, microcontroller, servo adapter and webcams to the Jetson | Short cables, some supplied with the parts | In the wiring and fasteners lot | Right-angle plugs where a cable passes through a wall. |

**What to look for**

- **Main computer:** must run our image model at 10 frames a second or better, take two USB webcams at once, host a Wi-Fi network for the iPad, and accept a 9 to 20 V supply. It no longer needs a display output, which is just as well, since this kit has DisplayPort and no HDMI.
- **Storage:** check which drive type and length the kit's slot takes before buying.
- **Microcontroller:** 3.3 V logic, at least six analog inputs for the pressure pads, a spare serial port for the head sensor board, and USB. Note the Teensy is not safe with 5 V signals.
- **iPad:** runs iOS 18 or later (the Butterfly SDK asks for it), has a USB-C port for the probe, and fits the printed slot, which is drawn for the iPad mini at 195.4 × 134.8 × 6.3 mm. It is charged outside the rig, so its battery has to last a session.
- **USB hub:** USB 3, its own power input, at least five ports.
- **Ultrasound image link:** from Butterfly we still need the access token and client key, confirmation that the iPad mini is supported, the delay from probe to frame, and whether biplane imaging is offered (colour Doppler is).

## Power, safety and lighting

One 24 V supply feeds everything. Three converters step it down, giving 12 V for the Jetson and lights, a separate 12 V for the three servos, and 5 V for the USB hub, the head sensor board and the marker servo. The emergency stop is a normally-closed button that holds a relay in, and the relay carries 24 V to the motion controller and the servo converter, so everything that moves loses power when the button is pressed or its wire breaks, while the computer and sensors stay on. Peak draw is about 230 W of the supply's 350 W.

| Part | What it does | Current pick | Price (USD) | Other options to price |
| --- | --- | --- | --- | --- |
| 24 V supply | Powers the whole machine | The donor printer's 350 W supply | Included | A standalone 24 V supply if the donor's is unusable. |
| Mains inlet | Wall power in, with switch and fuse | Not chosen | 12.00 estimate | The donor's inlet, if reusable. |
| Mains cord | Wall socket to the inlet | The donor printer's cord | Included | Any cord of the same plug type. |
| Fuse block and fuses | Splits 24 V into separately fused branches, one per always-on converter and one for the motion branch | Six-way blade fuse block, not chosen | 12.00 estimate | Any blade-fuse block. |
| Emergency stop | Drops the relay by hand. Normally closed, so a broken wire also stops the machine. | Not chosen. Candidates are Excel Cell ECS-22RE1RM1Q-010Q, IDEC AVW401-R and Eaton M22-PVT-K01 | 15.00 estimate | Any 22 mm twist-release stop with a normally-closed contact. The earlier pick (DFRobot FIT0156) is normally open and was dropped. |
| Power relay | Carries the 24 V feed to the motors and servos, held closed by the stop button | Not chosen. American Zettler AZ9731-1A-24DC1 is one to price | 6.00 estimate | Any relay with a 24 V coil and a contact rated 10 A or more on DC; an automotive-style relay with a socket. |
| 12 V converter, computer | Jetson and LED strips | Pololu 4095 (D36V50F12), 4.5 A | 44.95 confirmed, backorder | Generic step-down modules. |
| 12 V converter, servos | The three tilt servos, through the bus adapter | Pololu 2885 (D24V150F12), 15 A | 79.95 confirmed, backorder | Pololu's newer D42V110F family; generic 10 A modules. |
| 5 V converter | USB hub, head sensor board and marker servo | Pololu 4091 (D36V50F5), 5.5 A | 44.95 confirmed, backorder | Generic step-down modules. |
| LED strips | Light the inside for the cameras | Adafruit 4612, 1 m, × 2 | 11.95 each confirmed | Any 12 V white strip. |
| LED channels and diffusers | Hold the strips along the top rails and soften the light | Aluminium channel with a frosted cover, about 1.8 m (no supplier chosen) | In the wiring and fasteners lot | Printed clips with a strip of frosted film. |
| Power wire and connectors | Join the supply, fuse block, relay, converters and loads | 18 gauge for 24 V and servo power, 22 gauge elsewhere, with screw terminals or crimp connectors | In the wiring and fasteners lot | Pre-made leads where a part has a specific plug, such as the Jetson's barrel jack. |

**What to look for**

- **Converters:** together these cost about $170, and cheaper modules almost certainly exist. Each must accept at least 28 V in. The continuous ratings to meet are 4.5 A at 12 V for the computer side, 10 A at 12 V for the servos (their combined stall draw is 8.1 A) and 3 A at 5 V. Check for over-current protection and screw terminals.
- **Fuses:** one per branch, sized just above that branch's peak current.
- **Emergency stop:** it must have a normally-closed contact (the circuit breaks when pressed), a twist or pull release, and a 22 mm body to fit the panel hole. It now carries only the relay's coil current, so its contact rating matters far less than it did.
- **Relay:** a 24 V DC coil, a contact rated for at least 10 A at 24 V DC (the motion branch peaks near 6.5 A), and a diode across the coil.
- **LED strips:** 12 V, about 1.8 m in total, neutral white. Even light matters more than brightness, and glare on the printed markers is worth checking.
- **Power wire:** thick enough for its branch, and flexible stranded wire on anything that moves.

## Structure and version-specific parts

The enclosure is a frame of 20 mm aluminium extrusion with panels on the back and both sides, an open top, and a steep slanted panel over the arm opening that carries the iPad slot and the stop button. It is 516 × 562 mm at the base and 590 mm tall. The computer and power parts hang on the outside of the back wall.

| Part | What it does | Current pick | Price (USD) | What to look for |
| --- | --- | --- | --- | --- |
| Aluminium extrusion, about 4.6 m | Enclosure frame | 20 × 20 mm T-slot (no supplier chosen) | 50 estimate | Cut-to-length service; the same slot size as the donor's extrusion. |
| Corner brackets and slot nuts | Join the extrusions at every corner | Cast corner brackets with M5 screws and slot nuts, about 30 sets | In the wiring and fasteners lot | Brackets and nuts made for the same slot size as the extrusion. |
| Wall panels (× 3) | Close the back and both sides, keep hands out and the light even | 3 mm acrylic | 75 estimate with the front panel | Cut-to-size service; a cheaper opaque sheet would also work. |
| Slanted front panel | Carries the iPad slot and the stop button above the arm opening | 3 mm acrylic with holes for the slot's screws, the stop button and the probe cable | Counted with the wall panels | A service that can cut the openings, or a printed panel in two halves. |
| iPad slot | Holds the iPad mini on the slanted panel. Open at the top, so the iPad slides in and lifts out to charge. | Printed in-house | Filament | A lip deep enough that the iPad cannot tip out, and a cut-out that leaves the USB-C port reachable for the probe cable. |
| Base plate | Everything bolts to it | 516 × 562 mm sheet | 25 estimate | Flat and stiff; plywood or aluminium. |
| Rubber feet (× 4) | Stop the box sliding and damp vibration | Stick-on or screw-on feet | In the wiring and fasteners lot | Feet tall enough to clear the screw heads under the base. |
| Electronics shelf | Holds the Jetson and motion controller on the outside of the back wall | Printed or cut from sheet | Filament | Air must reach the Jetson's fan. |
| Standoffs and mounting screws | Fix each board and converter to the back wall | M2.5 and M3 nylon standoffs | In the wiring and fasteners lot | Lengths of 6 to 10 mm, so nothing shorts against the panel. |
| Cable grommets | Line the holes where cables pass through the back wall and the front panel | Rubber grommets, about six | In the wiring and fasteners lot | Inner hole wide enough for a USB plug. |
| Cable tray | Carries the fixed cable run along the back wall | Printed in-house | Filament | None needed. |
| Printing filament | Gimbal, probe holder, iPad slot, hand grip, cradles, brackets, shelf, cable tray | 1 kg | 20 estimate | A material that does not creep under the servos' load. |
| Wire, cable chain, fasteners | 50 wires in the current model, plus every small item marked as in this lot | One lot | 50 estimate | Flexible cable rated for repeated bending on the moving runs. |
| Arm rest padding | Comfort, and a base for the cradle and the pads | Foam | 15 estimate | Wipe-clean surface. |
| Display unit and light box (Vscan build) | The Vscan's own screen, enclosed so the camera reads it without glare | The Vscan display unit in a printed box on the outside wall | Filament | Matte black inside, with a slot for the probe cable. |
| Camera for the display (Vscan build) | Reads the Vscan's screen inside the light box | Arducam IMX219 for Jetson (SparkFun SEN-28170) | 19.95 confirmed | Sharp focus at about 150 mm; a connector that matches the Jetson kit. |

## Problems no part solves yet

These need research as much as any part above. Getting the ultrasound image into the Jetson used to head this list and has been removed, because Butterfly's SDK hands the frames straight to the team's iPad app.

- **Ultrasound gel.** The probe needs gel to see anything, loose gel smears the ink mark, and gel near the distance sensors may confuse them. Research solid gel pads that clip over a probe face.
- **Putting Doppler and biplane to use.** Telling artery from vein is no longer a missing capability, since the Butterfly has Doppler (which shows blood flow) and biplane imaging (two views at right angles at once). The SDK offers colour Doppler frames to the app. Biplane is not mentioned in its documentation, so that is a question for Butterfly. What remains after that is software, meaning how fast the frames arrive in each mode and how the vessel-finding model should use flow.
- **The Vscan build has no such stream.** It still reads its image by camera from the display, so anything we build on Doppler data will work on the Butterfly build only unless GE offers an equivalent.
- **Servo slack is unmeasured.** No supplier publishes it, so the first ST3215 that arrives should be tested, with and without its spring, before the other two are ordered.
- **Tracking an arm with plain webcams.** Whether two webcams and printed markers can hold the arm's position to a millimetre or two, how the markers behave when skin stretches or the probe head covers one, and how fast a move has to be before the scan should pause.
- **Distance sensors on skin.** Whether short-range time-of-flight sensors read reliably on different skin tones, on hair and next to gel. The load cell touching down at a few points is the fallback.
- **The wireless link.** The delay and the dropouts between the iPad and the Jetson, measured in the room the rig will be used in.

## Sources

Servo and power pages opened on 24 Nov 2026: [Waveshare ST3215](https://www.waveshare.com/st3215-servo.htm?sku=22414), [Waveshare Bus Servo Adapter (A)](https://www.waveshare.com/bus-servo-adapter-a.htm), [RobotShop, Dynamixel XL430-W250-T](https://www.robotshop.com/products/robotis-dynamixel-xl430-w250-t-smart-servo-actuator), [ROBOTIS e-Manual, XL430-W250](https://emanual.robotis.com/docs/en/dxl/x/xl430-w250/), [RobotShop, SunFounder SF3218MG](https://www.robotshop.com/products/sunfounder-sf3218mg-metal-gear-digital-servo-20kg-high-torque), [Pololu 2885](https://www.pololu.com/product/2885), [Pololu 3783](https://www.pololu.com/product/3783). The Butterfly SDK, Doppler and biplane points come from the team's meeting with Butterfly, not from a web page. Links for every other confirmed price are in the [parts list](parts-list.html).

The version 7 parts (webcams, distance sensors, micro servo, head sensor board, stop buttons and relay) were priced on 26 Nov 2026 and their links are in the parts list too. The design changes themselves came out of the team's design review.
