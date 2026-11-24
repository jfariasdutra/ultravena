---
title: Parts List
nav: Parts List
order: 4
summary: Every part to order, with supplier, part number, price and what still needs checking.
updated: 2026-11-24
pdf: assets/files/ultravena-parts-list.pdf
---

The full build comes to about $2,155 before shipping and tax, of which $1,055 is confirmed supplier pricing and the rest is estimated.

| Group | Total (USD) | Of which confirmed |
| --- | --- | --- |
| Order list (parts with a listing) | 1,883 | 1,055 |
| Parts to make or source locally | 235 | 0 |
| Butterfly iQ3 extras | 39 | 0 |
| GE Vscan Extend extras | 30 | 20 |

The two depth cameras are the largest line at an estimated $700, and their US price is not confirmed. This list follows the UltraVena rig viewer: whenever the design changes, the affected rows are updated and the change is recorded in the change log at the end. Prices are not rechecked automatically.

## Order list

Every price below marked Confirmed was read from the supplier's page on 23 or 24 Nov 2026. Prices exclude shipping and tax.

### Motion

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Creality Ender-3 V3 SE](https://www.matterhackers.com/store/l/creality-ender-3-v3-se-3d-printer/sk/M5EYNWU0) (donor printer, MatterHackers) | M-5EY-NWU0 | 1 | 179.00 | 179.00 | Confirmed | Supplies three of the four axis motors, the motion controller, the 24 V 350 W supply, belts and rails. Best Buy lists it at $199. |
| [Stepper motor, NEMA 17, 42 × 38 mm, 1.7 A](https://www.pololu.com/product/2267) (Pololu) | 2267 | 1 | 35.12 | 35.12 | Confirmed | Second Y motor. The donor's fourth motor is a short extruder motor sold with a gear on its shaft, so it cannot take a belt pulley. 5 mm D shaft. |
| MGN12 linear rail, 250 mm, with two MGN12H carriages | Not selected | 1 | 30.00 | 30.00 | Estimate | Carries the Z slide. Replaces the plain sliding block. Cut the rail to 240 mm. |
| Limit switch with roller lever | Not selected | 4 | 2.00 | 8.00 | Estimate | One each for X, Y and Z in case the donor's cannot be reused, plus one that senses the floating head lifting. |
| [Waveshare ST3215 30 kg serial bus servo](https://www.waveshare.com/st3215-servo.htm?sku=22414) | SKU 22414 | 3 | 21.99 | 65.97 | Confirmed | Yaw, pitch and roll. Replaces the SunFounder SF3218MG hobby servo ($18.58), which stays the fallback. 6 to 12.6 V, 2.7 A stall, 89 g, built-in position sensor that reports angle, load and temperature back. Gear slack is not published, so test one before buying three. |
| [Waveshare Bus Servo Adapter (A)](https://www.waveshare.com/bus-servo-adapter-a.htm) | SKU 25514 | 1 | 4.99 | 4.99 | Confirmed | Replaces the Adafruit 815 servo driver. Links the three servos, chained on one cable, to the Teensy or to the Jetson over USB, and feeds them 12 V. 9 to 12.6 V input. |

### Probe head

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [Load cell, 5 kg straight bar, TAL220B](https://sparkfun.com/products/14729) (SparkFun) | SEN-14729 | 1 | 15.50 | 15.50 | Confirmed | Senses how hard the probe presses. |
| [SparkFun load cell amplifier, HX711](https://www.sparkfun.com/products/13879) | SEN-13879 | 1 | 4.95 | 4.95 | Confirmed | Mounted on the Z slide beside the load cell. 3 left when checked. |
| [Adafruit BNO085 9-DOF orientation sensor](https://www.adafruit.com/products/4754) | 4754 | 2 | 29.50 | 59.00 | Confirmed | One on the probe holder as the tilt sensor, one in the wrist band. |
| [Actuonix L12-30-50-6-R micro linear servo](https://ca.robotshop.com/products/actuonix-l12-actuator-30mm-501-6v-rc-control) (RobotShop Canada) | RB-Fir-223, maker no. L12-30-50-6-R | 1 | 102.94 | 102.94 | Confirmed, currency unclear | Lowers and presses the marker. 30 mm stroke, 22 N, 6 V, 460 mA stall, powered by its own 6 V converter, control signal straight from a Teensy pin. 1 left when checked. |
| Floating head hardware: two 6 mm guide rods, two bushings, two stop collars | Not selected | 1 | 12.00 | 12.00 | Estimate | Lets the probe head lift 15 mm when pushed, so contact force cannot exceed the head's own weight. |

### Sensing

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [RealSense D405 depth camera](https://realsenseai.com/products/stereo-depth-camera-d405/) | 82635DSD405 | 2 | 350.00 | 700.00 | Estimate | Works from 7 to 50 cm, which fits this rig. No US price could be read; DigiKey China lists ¥2,973 including tax. |
| [Adafruit square force-sensitive resistor](https://www.adafruit.com/products/1075) | 1075 | 6 | 5.95 | 35.70 | Confirmed | Pressure pads, 38 mm square. Out of stock at Adafruit when checked. [Pololu 1645](https://www.pololu.com/product/1645) is the same size at $20.49. |

### Computing

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| [NVIDIA Jetson Orin Nano Super Developer Kit](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html) (SparkFun) | DEV-22098 | 1 | 249.00 | 249.00 | Confirmed | In stock. Accepts 9 to 20 V, so it runs from the 12 V converter. |
| Storage for the Jetson (NVMe drive or microSD card) | Not selected | 1 | 30.00 | 30.00 | Estimate | The kit page does not list storage as included. |
| [Teensy 4.0](https://www.sparkfun.com/teensy-4-0.html) (SparkFun) | DEV-15583 | 1 | 23.80 | 23.80 | Confirmed | The microcontroller for the fast safety loop. In stock. |
| [Waveshare 7 inch HDMI touchscreen (H) with case](https://www.waveshare.com/product/7inch-hdmi-lcd-h-with-case.htm) | 13857 | 1 | 53.99 | 53.99 | Confirmed | 1024 × 600, capacitive, lists Jetson Orin support. |
| Powered USB 3 hub, 7 port | Not selected | 1 | 25.00 | 25.00 | Estimate | Any brand; must have its own power input. |

### Power and lighting

| Part | ID | Qty | Unit (USD) | Total (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| 24 V 350 W power supply | From the donor printer | 1 | 0.00 | 0.00 | Included | MatterHackers lists the printer at 350 W. |
| [Pololu 12 V 4.5 A converter, D36V50F12](https://www.pololu.com/product/4095) | 4095 | 1 | 44.95 | 44.95 | Confirmed | Jetson and lights. Rationed, backorder only. |
| [Pololu 12 V 15 A converter, D24V150F12](https://www.pololu.com/product/2885) | 2885 | 1 | 79.95 | 79.95 | Confirmed | Servo bus only, fed through the emergency stop. Replaces the 6 V 15 A converter (2882) at the same price. Rationed, and Pololu points new designs to its newer D42V110F family. |
| [Pololu 6 V 2.7 A converter, D36V28F6](https://www.pololu.com/product/3783) | 3783 | 1 | 24.95 | 24.95 | Confirmed | Marker actuator only (460 mA stall), fed through the emergency stop. Rationed. |
| [Pololu 5 V 5.5 A converter, D36V50F5](https://www.pololu.com/product/4091) | 4091 | 1 | 44.95 | 44.95 | Confirmed | Touchscreen and USB hub. Rationed, backorder only. |
| [DFRobot emergency stop switch](https://www.dfrobot.com/product-521.html) | FIT0156 | 1 | 5.90 | 5.90 | Confirmed | 22 mm mounting hole, 10 A. 3 left when checked. |
| [Adafruit ultra flexible white LED strip, 1 m](https://www.adafruit.com/products/4612) | 4612 | 2 | 11.95 | 23.90 | Confirmed | 9 to 12 V, cool white. 33 in stock. |
| Mains inlet with switch and fuse | Not selected | 1 | 12.00 | 12.00 | Estimate | The donor printer may already include one. |
| Fuse block, 6 way | Not selected | 1 | 12.00 | 12.00 | Estimate |  |

## Version-specific parts

Order only the rows for the probe you are building around. The probes themselves are already owned and are not counted.

| Version | Part | ID | Qty | Unit (USD) | Price status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Butterfly iQ3 | MagSafe charger or magnetic mount for the phone | Not selected | 1 | 39.00 | Estimate | Sits on the slanted front panel. A real MagSafe charger needs a USB-C power source, not the plain 5 V rail. |
| GE Vscan Extend | [Arducam IMX219 camera module for Jetson](https://www.sparkfun.com/arducam-imx219-visible-light-fixed-focus-camera-module-for-nvidiar-jetson-agx-orin-orin-nano-orin-nx.html) (SparkFun) | SEN-28170 | 1 | 19.95 | Confirmed | Reads the Vscan display inside the light box. Has a 15-pin ribbon connector; check which cable the Jetson kit needs. |
| GE Vscan Extend | Light box panels and display cradle | Made locally | 1 | 10.00 | Estimate | Printed cradle plus opaque sheet. |

## Parts to make or source locally

These have no single listing, so every figure here is an estimate and no supplier has been chosen.

| Part | Qty | Estimate (USD) | Notes |
| --- | --- | --- | --- |
| 20 × 20 mm aluminium extrusion for the enclosure frame | About 4.6 m | 50 | Two 578 mm posts, two 188 mm posts, five rails of 424 to 468 mm, two 405 mm sloped rails. [OpenBuilds V-Slot 20x20](https://us.openbuilds.com/v-slot-20x20-linear-rail) (SKU 280-LP) is one source; price by length was not readable. |
| Wall and front panels, 3 mm acrylic | 4 panels | 75 | Back 516 × 578 mm, two sides 558 × 578 mm with the front corner cut, front 508 × 405 mm. |
| Base plate, 516 × 562 mm | 1 | 25 | Plywood or aluminium sheet. |
| Printing filament, 1 kg | 1 | 20 | Gimbal, probe holder, stamp bracket, camera brackets, shelf brackets. |
| Wire, connectors, cable chain, grommets, fasteners | 1 lot | 50 | Wire gauges are not yet specified. |
| Arm rest padding and wrist strap | 1 | 15 | Foam and hook-and-loop strap. |
| Tracking markers | 4 | 0 | Printed on paper or sticker sheet. |
| Felt marker tip for the stamp | 1 | 0 | Cut from a skin-safe marker. |

## Check before ordering

- [ ] **Butterfly SDK on the Jetson.** Butterfly confirmed its SDK streams imaging in real time to other devices, so no extra hardware is needed for the image. Still to confirm with them: whether the stream is received on the Jetson directly or relayed from the phone, and whether Doppler and biplane frames come through it. The Vscan route (camera on its display) is in the list.

- [ ] **Gel.** Decide between gel applied by hand before the scan and a solid gel pad clipped over the probe face. Loose gel will smear the marker ink.

- [ ] **Force limit.** Designed in CAD version 5 as a floating head. Weigh the finished head to confirm the limit, and test that the lift switch stops the motors before any use on a person.

- [ ] **Z slide bearing.** Designed in CAD version 5 as a linear rail with two carriages. Choose a supplier for the rail; no listing is confirmed yet.

- [ ] **Depth cameras are over a third of the budget.** Get a real US quote for the D405. One camera, or two plain webcams reading the markers, would be enough to start.

- [ ] **Depth cameras on bare skin.** The D405 relies on visible texture, and smooth skin has little. Test one on a forearm before buying two.

- [ ] **Donor printer.** Confirm the Ender-3 V3 SE's limit switches and mains inlet can be reused, and that its controller can be reflashed to drive two Y motors. If not, swap in a generic four-driver board.

- [ ] **Pololu converters are backorder only.** Ask for a lead time, or pick in-stock equivalents with the same ratings (12 V at 4.5 A, 12 V at 15 A, 6 V at 2.7 A, 5 V at 5 A).

- [ ] **Servo power path.** Waveshare lists 2.7 A stall per servo at 12 V, so 8.1 A with all three stalled, against 15 A from the servo converter. Confirm the bus adapter's power terminal and the servo chain cable can carry that, and wire 12 V straight to the first servo if not.

- [ ] **Servo slack.** No supplier publishes gear slack for the ST3215. Buy one, clamp a 100 mm arm to it and measure the free play at the tip before buying the other two. Under 0.5 mm at the tip (about 0.3 degrees) is the target.

- [ ] **Signal levels.** The Teensy is a 3.3 V board. Confirm the marker actuator accepts a 3.3 V control signal, and that the bus adapter's serial pins work at 3.3 V.

- [ ] **Long sensor cables.** The tilt sensor and wrist band sit over a metre of moving cable from the Teensy. Use the BNO085's serial mode for that run.

- [ ] **Marker actuator price.** The only listing found is on RobotShop's Canadian site, so the $102.94 may be in Canadian dollars, and one unit was left.

- [ ] **Emergency stop contacts.** The DFRobot page does not say whether the contacts are normally closed, which is what the 24 V cut needs.

- [ ] **Camera cable for the Vscan build.** The Arducam module has a 15-pin connector; confirm the Jetson kit's connector and buy an adapter cable if needed.

- [ ] **Out-of-stock items.** The pressure pads were out of stock at Adafruit when checked.

## Change log

| Date | Design revision | What changed in this list |
| --- | --- | --- |
| 24 Nov 2026 | CAD model version 6 (serial bus servos) | Three SunFounder SF3218MG servos replaced by three Waveshare ST3215 bus servos. Adafruit 815 servo driver replaced by the Waveshare Bus Servo Adapter (A). The 6 V 15 A converter (Pololu 2882) replaced by a 12 V 15 A one (2885) for the servos, and a 6 V 2.7 A converter (3783) added for the marker actuator. Ultrasound image path removed from the check list after Butterfly confirmed its SDK streams imaging in real time. Total up about $25. |
| 24 Nov 2026 | CAD model version 5 (floating head, linear rail Z slide) | Linear rail with two carriages and floating head hardware added. Limit switches raised from 3 to 4. |
| 24 Nov 2026 | CAD model version 4 (second design audit) | One NEMA 17 motor (Pololu 2267) and three limit switches added. Load cell amplifier moved onto the probe head, same part. Check list reordered and extended. |
| 23 Nov 2026 | CAD model version 3 (range-of-motion sweep, marker lift actuator) | Solenoid (Adafruit 413) and its switch board (Adafruit 5648) removed. Actuonix L12-30-50-6-R linear servo added. The probe head bracket grew by 46 mm, which changes no purchased part. |
| 23 Nov 2026 | Rig viewer version 7 (enclosure, wiring, lighting, marker stamp, two depth cameras, touchscreen) | First issue of the parts list. |

## Sources

Pages opened on 23 Nov 2026: [MatterHackers](https://www.matterhackers.com/store/l/creality-ender-3-v3-se-3d-printer/sk/M5EYNWU0), [Best Buy](https://www.bestbuy.com/product/creality-ender-3-v3-se-printer/CZT3ZRXZKF), [RobotShop](https://www.robotshop.com/products/sunfounder-sf3218mg-metal-gear-digital-servo-20kg-high-torque), [Adafruit 815](https://www.adafruit.com/product/815), [Adafruit 4754](https://www.adafruit.com/products/4754), [Adafruit 413](https://www.adafruit.com/product/413), [Adafruit 412](https://www.adafruit.com/products/412), [Adafruit 1075](https://www.adafruit.com/products/1075), [Adafruit 4612](https://www.adafruit.com/products/4612), [The Pi Hut](https://thepihut.com/products/adafruit-mosfet-driver-for-motors-solenoids-leds-etc-stemma-jst-ph-2mm), [SparkFun SEN-14729](https://sparkfun.com/products/14729), [SparkFun SEN-13879](https://www.sparkfun.com/products/13879), [SparkFun DEV-22098](https://www.sparkfun.com/nvidia-jetson-orin-nano-developer-kit.html), [SparkFun DEV-15583](https://www.sparkfun.com/teensy-4-0.html), [SparkFun SEN-28170](https://www.sparkfun.com/arducam-imx219-visible-light-fixed-focus-camera-module-for-nvidiar-jetson-agx-orin-orin-nano-orin-nx.html), [Waveshare](https://www.waveshare.com/product/7inch-hdmi-lcd-h-with-case.htm), [Pololu 4095](https://www.pololu.com/product/4095), [Pololu 4091](https://www.pololu.com/product/4091), [Pololu 2882](https://www.pololu.com/product/2882), [Pololu 1645](https://www.pololu.com/product/1645), [DFRobot](https://www.dfrobot.com/product-521.html), [RealSense](https://realsenseai.com/products/stereo-depth-camera-d405/), [DigiKey China](https://digikey.cn/en/products/detail/intel-realsense/82635DSD405/16056868), [OpenBuilds](https://us.openbuilds.com/v-slot-20x20-linear-rail).

Added since: [RobotShop Canada, Actuonix L12](https://ca.robotshop.com/products/actuonix-l12-actuator-30mm-501-6v-rc-control) and [Pololu 2267](https://www.pololu.com/product/2267), opened 23 and 24 Nov 2026.

Added for CAD version 6, opened 24 Nov 2026: [Waveshare ST3215](https://www.waveshare.com/st3215-servo.htm?sku=22414), [Waveshare Bus Servo Adapter (A)](https://www.waveshare.com/bus-servo-adapter-a.htm), [Pololu 2885](https://www.pololu.com/product/2885) and [Pololu 3783](https://www.pololu.com/product/3783).
