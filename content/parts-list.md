---
title: Parts List
nav: Parts List
order: 4
summary: Every part to order, with supplier, part number, price and what still needs checking.
updated: 2026-11-26
pdf: assets/files/ultravena-parts-list.pdf
---

The full build comes to about $1,390 before shipping and tax, of which $987 is confirmed supplier pricing and the rest is estimated. That is about $765 less than the previous version, after the team's design review.

| Group | Total (USD) | Of which confirmed |
| --- | --- | --- |
| Order list (parts with a listing) | 1,155 | 987 |
| Parts to make or source locally | 235 | 0 |
| Butterfly iQ3 extras | 0 | 0 |
| GE Vscan Extend extras | 30 | 20 |

The largest lines are now the Jetson ($249) and the donor printer ($179). The iPad mini that replaces the touchscreen and phone is supplied by the team and is not counted. This list follows the UltraVena CAD model: whenever the design changes, the affected rows are updated and the change is recorded in the change log at the end. Prices are not rechecked automatically.

## Order list

Every price below marked Confirmed was read from the supplier's page on 23, 24 or 26 Nov 2026. Prices exclude shipping and tax.

### Motion

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Creality Ender-3 V3 SE](https://www.matterhackers.com/store/l/creality-ender-3-v3-se-3d-printer/sk/M5EYNWU0) (donor printer, MatterHackers) | M-5EY-NWU0 | 1 | 179.00 | 179.00 | Confirmed | Supplies three of the four axis motors, the motion controller, the 24 V 350 W supply, belts and rails. Best Buy lists it at $199. |
| [Stepper motor, NEMA 17, 42 × 38 mm, 1.7 A](https://www.pololu.com/product/2267) (Pololu) | 2267 | 1 | 35.12 | 35.12 | Confirmed | Second Y motor. The donor's fourth motor is a short extruder motor sold with a gear on its shaft, so it cannot take a belt pulley. 5 mm D shaft. |
| MGN12 linear rail, 250 mm, with two MGN12H carriages | Not selected | 1 | 30.00 | 30.00 | Estimate | Carries the Z slide. Replaces the plain sliding block. Cut the rail to 240 mm. |
| Limit switch with roller lever | Not selected | 4 | 2.00 | 8.00 | Estimate | One each for X, Y and Z in case the donor's cannot be reused, plus one that senses the floating head lifting. |
| [Waveshare ST3215 30 kg serial bus servo](https://www.waveshare.com/st3215-servo.htm?sku=22414) | SKU 22414 | 3 | 21.99 | 65.97 | Confirmed | Yaw, pitch and roll. Replaces the SunFounder SF3218MG hobby servo ($18.58), which stays the fallback. 6 to 12.6 V, 2.7 A stall, 89 g, built-in position sensor that reports angle, load and temperature back. Gear slack is not published, so test one before buying three. |
| [Waveshare Bus Servo Adapter (A)](https://www.waveshare.com/bus-servo-adapter-a.htm) | SKU 25514 | 1 | 4.99 | 4.99 | Confirmed | Replaces the Adafruit 815 servo driver. Links the three servos, chained on one cable, to the Teensy or to the Jetson over USB, and feeds them 12 V. 9 to 12.6 V input. |
| Small extension springs, assorted | Not selected | 1 set | 8.00 | 8.00 | Estimate | One spring on each tilt joint holds its gears to one side, which removes the free play in the servos. Three are used; an assortment lets the stiffness be tuned. |

### Probe head

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Load cell, 5 kg straight bar, TAL220B](https://sparkfun.com/products/14729) (SparkFun) | SEN-14729 | 1 | 15.50 | 15.50 | Confirmed | Senses how hard the probe presses. |
| [SparkFun load cell amplifier, HX711](https://www.sparkfun.com/products/13879) | SEN-13879 | 1 | 4.95 | 4.95 | Confirmed | Mounted on the Z slide beside the load cell. 3 left when checked. |
| [Adafruit BNO085 9-DOF orientation sensor](https://www.adafruit.com/products/4754) | 4754 | 1 | 29.50 | 29.50 | Confirmed | On the probe holder as the tilt sensor. The second one, for the wrist band, was dropped. |
| [Adafruit micro servo, MG90D metal gear](https://www.adafruit.com/products/1143) | 1143 | 1 | 9.95 | 9.95 | Confirmed | Lifts and lowers the marker pen. Replaces the Actuonix linear servo ($102.94). 4.8 to 6 V, 22.8 x 12.2 x 28.5 mm, 13.4 g. The pen tip is spring-loaded, so the spring sets how hard it presses. In stock. |
| Floating head hardware: two 6 mm guide rods, two bushings, two stop collars | Not selected | 1 | 12.00 | 12.00 | Estimate | Lets the probe head lift 15 mm when pushed, so contact force cannot exceed the head's own weight. |
| Adafruit VL53L4CD time-of-flight distance sensor | 5396 | 4 | 14.95 | 59.80 | Confirmed | Four around the probe, looking down. Together they measure the skin's local tilt and distance before contact, and one reading far means an edge. About 1 to 1300 mm range, 25.5 x 17.7 mm board, which is larger than the 10 x 13 mm drawn in CAD. In stock. |
| Head sensor board, Adafruit QT Py RP2040 or similar | 4900 | 1 | 9.95 | 9.95 | Estimate | Small microcontroller on the Z slide. Reads the four distance sensors, the tilt sensor and the load cell, drives the marker servo, and sends everything to the Teensy down one cable. Price not read from the supplier page. |

### Sensing

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Arducam 1080P low distortion USB camera module](https://www.arducam.com/product/arducam-1080p-low-light-low-distortion-usb-camera-module-with-microphone/) | B0468 | 2 | 39.99 | 79.98 | Confirmed | Replace the two RealSense D405 depth cameras (about $700). One high for the view the user taps on, one low on a side wall that sees under the bridge. They track the printed markers on the arm and on the probe head. 1080p at 30 frames a second, 71 degree horizontal view, manual focus, 38 x 38 mm board, plugs in as a standard USB camera. Stock not shown on the page. |
| [Adafruit square force-sensitive resistor](https://www.adafruit.com/products/1075) | 1075 | 6 | 5.95 | 35.70 | Confirmed | Pressure pads, 38 mm square, now laid out in two columns of three so a rolling arm shifts weight between columns. Out of stock at Adafruit when checked. [Pololu 1645](https://www.pololu.com/product/1645) is the same size at $20.49. |

### Computing

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [NVIDIA Jetson Orin Nano Super Developer Kit](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html) (SparkFun) | DEV-22098 | 1 | 249.00 | 249.00 | Confirmed | In stock. Accepts 9 to 20 V, so it runs from the 12 V converter. |
| Storage for the Jetson (NVMe drive or microSD card) | Not selected | 1 | 30.00 | 30.00 | Estimate | The kit page does not list storage as included. |
| [Teensy 4.0](https://www.sparkfun.com/teensy-4-0.html) (SparkFun) | DEV-15583 | 1 | 23.80 | 23.80 | Confirmed | The microcontroller for the fast safety loop. In stock. |
| iPad mini (supplied by the team) | Not purchased | 1 | 0.00 | 0.00 | Not counted | Replaces the 7 inch touchscreen ($53.99) and the phone. Runs the team's control app, holds the Butterfly probe through its USB-C port, and talks to the Jetson over Wi-Fi. Sits in a printed slot on the front panel and lifts out to charge. 195.4 x 134.8 x 6.3 mm. |
| Powered USB 3 hub, 7 port | Not selected | 1 | 25.00 | 25.00 | Estimate | Any brand; must have its own power input. |

### Power and lighting

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 24 V 350 W power supply | From the donor printer | 1 | 0.00 | 0.00 | Included | MatterHackers lists the printer at 350 W. |
| [Pololu 12 V 4.5 A converter, D36V50F12](https://www.pololu.com/product/4095) | 4095 | 1 | 44.95 | 44.95 | Confirmed | Jetson and lights. Rationed, backorder only. |
| [Pololu 12 V 15 A converter, D24V150F12](https://www.pololu.com/product/2885) | 2885 | 1 | 79.95 | 79.95 | Confirmed | Servo bus only, fed through the emergency stop. Replaces the 6 V 15 A converter (2882) at the same price. Rationed, and Pololu points new designs to its newer D42V110F family. |
| [Pololu 5 V 5.5 A converter, D36V50F5](https://www.pololu.com/product/4091) | 4091 | 1 | 44.95 | 44.95 | Confirmed | USB hub, head sensor board and marker servo. Rationed, backorder only. |
| Emergency stop, 22 mm, normally closed, twist release | Not selected | 1 | 15.00 | 15.00 | Estimate | Replaces the DFRobot FIT0156, which DigiKey lists as normally open, the wrong kind. One candidate is the [Excel Cell ECS-22RE1RM1Q-010Q](https://www.digikey.ca/en/products/detail/excel-cell-electronic-co-ltd/ECS-22RE1RM1Q-010Q/25812945), normally closed, 10 A, twist reset, C$12.61 at DigiKey Canada but out of stock with a 10 week lead. IDEC AVW401-R and Eaton M22-PVT-K01 are others to price. |
| Power relay, 24 V coil, 30 A or more | Not selected | 1 | 6.00 | 6.00 | Estimate | Carries the motor and servo current (up to about 6.5 A). The stop button only breaks the relay's coil circuit, so the button never switches the full load, and a broken wire also drops the relay. American Zettler AZ9731-1A-24DC1 is one to price. |
| [Adafruit ultra flexible white LED strip, 1 m](https://www.adafruit.com/products/4612) | 4612 | 2 | 11.95 | 23.90 | Confirmed | 9 to 12 V, cool white. 33 in stock. |
| Mains inlet with switch and fuse | Not selected | 1 | 12.00 | 12.00 | Estimate | The donor printer may already include one. |
| Fuse block, 6 way | Not selected | 1 | 12.00 | 12.00 | Estimate |  |

## Version-specific parts

Order only the rows for the probe you are building around. The probes themselves are already owned and are not counted.

| Version | Part | ID | Qty | Unit (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| GE Vscan Extend | [Arducam IMX219 camera module for Jetson](https://www.sparkfun.com/arducam-imx219-visible-light-fixed-focus-camera-module-for-nvidiar-jetson-agx-orin-orin-nano-orin-nx.html) (SparkFun) | SEN-28170 | 1 | 19.95 | Confirmed | Reads the Vscan display inside the light box. Has a 15-pin ribbon connector; check which cable the Jetson kit needs. |
| GE Vscan Extend | Light box panels and display cradle | Made locally | 1 | 10.00 | Estimate | Printed cradle plus opaque sheet. |

## Parts to make or source locally

These have no single listing, so every figure here is an estimate and no supplier has been chosen.

| Part | Qty | Estimate (USD) | Notes |
| --- | --- | --- | --- |
| 20 × 20 mm aluminium extrusion for the enclosure frame | About 4.6 m | 50 | Two 578 mm posts, two 188 mm posts, five rails of 424 to 468 mm, two 405 mm sloped rails. [OpenBuilds V-Slot 20x20](https://us.openbuilds.com/v-slot-20x20-linear-rail) (SKU 280-LP) is one source; price by length was not readable. |
| Wall and front panels, 3 mm acrylic | 4 panels | 75 | Back 516 × 578 mm, two sides 558 × 578 mm with the front corner cut, front 508 × 405 mm. |
| Base plate, 516 × 562 mm | 1 | 25 | Plywood or aluminium sheet. |
| Printing filament, 1 kg | 1 | 20 | Gimbal, probe holder with its pen guide and sensor tabs, iPad slot, camera brackets, hand grip posts, shelf brackets. |
| Wire, connectors, cable chain, grommets, fasteners | 1 lot | 50 | Wire gauges are not yet specified. |
| Arm rest padding and hand grip | 1 | 15 | Foam for the cradle and a soft sleeve over the grip bar. The wrist strap was dropped with the wrist band. |
| Tracking markers | 5 | 0 | Printed on paper or sticker sheet. Four go on the arm and one on the probe head, so the cameras see both in the same picture. |
| Skin-safe marker pen with a spring-loaded tip | 1 | 0 | A short spring between the pen and its collar sets the press force. |

## Check before ordering

- [ ] **Butterfly SDK and the iPad mini.** Butterfly publishes an iOS imaging SDK that gives an app live B-mode and Color Doppler frames from a probe plugged into the iPad. Get the access token and client key from Butterfly, confirm the team's iPad mini is on Butterfly's supported device list and runs iOS 18 or newer, and note that biplane is not mentioned on the SDK page. The Vscan route (camera on its display) is in the list.
- [ ] **Gel.** Decide between gel applied by hand before the scan and a solid gel pad clipped over the probe face. Loose gel will smear the marker ink.
- [ ] **Force limit.** Designed in CAD version 5 as a floating head. Weigh the finished head to confirm the limit, and test that the lift switch stops the motors before any use on a person.
- [ ] **Z slide bearing.** Designed in CAD version 5 as a linear rail with two carriages. Choose a supplier for the rail; no listing is confirmed yet.
- [ ] **Webcams and markers.** Before buying both, test one camera tracking a 20 mm printed marker on skin while the arm is nudged by 1 mm, and test that both cameras can see the probe head marker together.
- [ ] **Distance sensors near gel.** Wet gel is shiny and may confuse the sensors. Test one over a gelled forearm at 10 to 40 mm before buying four. The fallback needs no parts: touch down gently at three points and work out the tilt from the load cell.
- [ ] **Donor printer.** Confirm the Ender-3 V3 SE's limit switches and mains inlet can be reused, and that its controller can be reflashed to drive two Y motors. If not, swap in a generic four-driver board.
- [ ] **Pololu converters are backorder only.** Ask for a lead time, or pick in-stock equivalents with the same ratings (12 V at 4.5 A, 12 V at 15 A, 5 V at 5 A).
- [ ] **Servo power path.** Waveshare lists 2.7 A stall per servo at 12 V, so 8.1 A with all three stalled, against 15 A from the servo converter. Confirm the bus adapter's power terminal and the servo chain cable can carry that, and wire 12 V straight to the first servo if not.
- [ ] **Servo slack and springs.** A teammate found a test showing about three times the 0.3 degree target, close to 1 mm at the probe face. Each joint now has a spring that holds its gears to one side. Choose spring stiffness so the spring always wins over the probe's weight at full tilt, and check the servos do not run hot holding against it.
- [ ] **Signal levels.** The Teensy and the head sensor board are 3.3 V boards. Confirm the marker servo accepts a 3.3 V control pulse while powered from 5 V, and that the bus adapter's serial pins work at 3.3 V.
- [ ] **Head sensor board.** The four distance sensors share one address, so each needs its own enable wire from the board. Confirm the chosen board has enough pins for four enables, the sensor bus, the load cell amplifier, the tilt sensor, the marker servo and the serial link to the Teensy (11 in all if one sensor keeps its default address and only three get an enable wire, which is exactly what the QT Py offers and leaves nothing spare), or pick a larger board.
- [ ] **Marker lift.** The pen needs about 15 mm of travel (the tip rides 8 mm above the probe face). Check the micro servo's arm gives that, and pick a spring for the tip that marks clearly without pressing hard.
- [ ] **Emergency stop and relay.** Choose an in-stock normally-closed, twist-release stop button and a relay with a 24 V coil. Confirm the relay's contact rating on DC covers the 6.5 A motor branch.
- [ ] **Camera cable for the Vscan build.** The Arducam module has a 15-pin connector; confirm the Jetson kit's connector and buy an adapter cable if needed.
- [ ] **Out-of-stock items.** The pressure pads were out of stock at Adafruit when checked.
- [ ] **Jetson Wi-Fi.** The iPad talks to the Jetson over Wi-Fi. NVIDIA's page says the kit comes with a wireless module fitted. Confirm it can host its own network, and that antennas are included.

## Change log

| Date | Design revision | What changed in this list |
| --- | --- | --- |
| 26 Nov 2026 | CAD model version 7 (team design review, iPad mini) | Two RealSense D405 cameras replaced by two Arducam USB cameras. Actuonix marker actuator and its 6 V converter replaced by a micro servo. Touchscreen and phone mount replaced by a team-supplied iPad mini in a printed slot. Wrist band sensor dropped. Four distance sensors, a head sensor board, joint springs and a power relay added. Stop button changed to a normally-closed type. Total down from about $2,155 to about $1,390. |
| 24 Nov 2026 | CAD model version 6 (serial bus servos) | Three SunFounder SF3218MG servos replaced by three Waveshare ST3215 bus servos. Adafruit 815 servo driver replaced by the Waveshare Bus Servo Adapter (A). The 6 V 15 A converter (Pololu 2882) replaced by a 12 V 15 A one (2885) for the servos, and a 6 V 2.7 A converter (3783) added for the marker actuator. Ultrasound image path removed from the check list after Butterfly confirmed its SDK streams imaging in real time. Total up about $25. |
| 24 Nov 2026 | CAD model version 5 (floating head, linear rail Z slide) | Linear rail with two carriages and floating head hardware added. Limit switches raised from 3 to 4. |
| 24 Nov 2026 | CAD model version 4 (second design audit) | One NEMA 17 motor (Pololu 2267) and three limit switches added. Load cell amplifier moved onto the probe head, same part. Check list reordered and extended. |
| 23 Nov 2026 | CAD model version 3 (range-of-motion sweep, marker lift actuator) | Solenoid (Adafruit 413) and its switch board (Adafruit 5648) removed. Actuonix L12-30-50-6-R linear servo added. The probe head bracket grew by 46 mm, which changes no purchased part. |
| 23 Nov 2026 | Rig viewer version 7 (enclosure, wiring, lighting, marker stamp, two depth cameras, touchscreen) | First issue of the parts list. |

## Sources

Pages opened on 23 Nov 2026: [MatterHackers](https://www.matterhackers.com/store/l/creality-ender-3-v3-se-3d-printer/sk/M5EYNWU0), [Best Buy](https://www.bestbuy.com/product/creality-ender-3-v3-se-printer/CZT3ZRXZKF), [RobotShop](https://www.robotshop.com/products/sunfounder-sf3218mg-metal-gear-digital-servo-20kg-high-torque), [Adafruit 815](https://www.adafruit.com/product/815), [Adafruit 4754](https://www.adafruit.com/products/4754), [Adafruit 413](https://www.adafruit.com/product/413), [Adafruit 412](https://www.adafruit.com/products/412), [Adafruit 1075](https://www.adafruit.com/products/1075), [Adafruit 4612](https://www.adafruit.com/products/4612), [The Pi Hut](https://thepihut.com/products/adafruit-mosfet-driver-for-motors-solenoids-leds-etc-stemma-jst-ph-2mm), [SparkFun SEN-14729](https://sparkfun.com/products/14729), [SparkFun SEN-13879](https://www.sparkfun.com/products/13879), [SparkFun DEV-22098](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html), [SparkFun DEV-15583](https://www.sparkfun.com/teensy-4-0.html), [SparkFun SEN-28170](https://www.sparkfun.com/arducam-imx219-visible-light-fixed-focus-camera-module-for-nvidiar-jetson-agx-orin-orin-nano-orin-nx.html), [Waveshare](https://www.waveshare.com/product/7inch-hdmi-lcd-h-with-case.htm), [Pololu 4095](https://www.pololu.com/product/4095), [Pololu 4091](https://www.pololu.com/product/4091), [Pololu 2882](https://www.pololu.com/product/2882), [Pololu 1645](https://www.pololu.com/product/1645), [DFRobot](https://www.dfrobot.com/product-521.html), [RealSense](https://realsenseai.com/products/stereo-depth-camera-d405/), [DigiKey China](https://digikey.cn/en/products/detail/intel-realsense/82635DSD405/16056868), [OpenBuilds](https://us.openbuilds.com/v-slot-20x20-linear-rail).

Added since: [RobotShop Canada, Actuonix L12](https://ca.robotshop.com/products/actuonix-l12-actuator-30mm-501-6v-rc-control) and [Pololu 2267](https://www.pololu.com/product/2267), opened 23 and 24 Nov 2026.

Added for CAD version 6, opened 24 Nov 2026: [Waveshare ST3215](https://www.waveshare.com/st3215-servo.htm?sku=22414), [Waveshare Bus Servo Adapter (A)](https://www.waveshare.com/bus-servo-adapter-a.htm), [Pololu 2885](https://www.pololu.com/product/2885) and [Pololu 3783](https://www.pololu.com/product/3783).

Added for CAD version 7, opened 26 Nov 2026: [Arducam B0468](https://www.arducam.com/product/arducam-1080p-low-light-low-distortion-usb-camera-module-with-microphone/), [Adafruit 5396](https://www.adafruit.com/product/5396), [Adafruit 1143](https://www.adafruit.com/products/1143), [DigiKey Canada, Excel Cell emergency stop](https://www.digikey.ca/en/products/detail/excel-cell-electronic-co-ltd/ECS-22RE1RM1Q-010Q/25812945), [DigiKey, DFRobot FIT0156](https://www.digikey.co.nz/en/products/detail/dfrobot/FIT0156/25558530) and the [NVIDIA Jetson Orin Nano hardware layout](https://docs.nvidia.com/jetson/orin-nano-devkit/user-guide/latest/hardware_layout.html).
