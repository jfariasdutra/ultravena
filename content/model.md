---
title: Vessel Model
nav: Vessel Model
order: 6
summary: The image model that outlines the vessel in each ultrasound frame, and where it stands.
updated: 2026-11-24
---

The vessel model is the piece of software that looks at each ultrasound frame and outlines the vessel in it. Everything the machine decides afterwards (how deep the vessel is, how wide, where the best cannulation point lies) is measured from that outline.

## What it is

The model is a U-Net, a kind of neural network built for outlining shapes in medical images. It takes one greyscale ultrasound frame and returns a mask, a same-sized picture in which every pixel is marked as vessel or not vessel. The current version (version 2) has about 1.8 million weights, which is small enough to run many times a second on the Jetson.

## Where it stands

| Item | Status |
| --- | --- |
| Architecture | U-Net, from the team's own notebook |
| Current version | 2 |
| Training images | Computer-generated images that imitate ultrasound |
| Real scans in training | None yet. The team's own scans have not been exported from the ultrasound. |
| Runs in the browser | Yes, inside the labelling dashboard |
| Runs on the Jetson | Not tested yet |

## Results so far

Version 2 was tested on 150 computer-generated images it had never seen, 24 of which contained no vessel at all.

| Measure | Result |
| --- | --- |
| Average overlap between its outline and the true one (IoU) | 0.97 |
| Images where the overlap was 0.80 or better | 99% |
| Vessels it found | 99.5% |
| Outlines it drew that were real vessels | 99% |
| False alarms on the 24 vessel-free images | 0 |

These numbers show that the training and testing pipeline works. They do not show how the model will do on real arms, because it has not seen one. Expect the figures to drop when real scans arrive, and expect that to be the point where the real work on the model starts.

## What comes next

- Export the team's own scans and label them in the dashboard.
- Retrain on real images and report results on real images only.
- Use the Butterfly's Doppler mode (which shows blood flow) to tell artery from vein, and its biplane mode (two views at right angles) to judge vessel direction, once the team confirms those frames come through the SDK stream.
- Measure speed on the Jetson, with a target of 10 frames a second or better.

## The labelling dashboard

The team has a separate dashboard for uploading scans, filtering them by device, drawing vessel outlines by hand and running the model on them. It lives apart from this site for now.
