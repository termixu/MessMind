# 🧠 MessMind

**Decentralized neural network over mesh networks. No cloud. No central server. No single point of failure.**

MessMind is a swarm of devices (phones, Raspberry Pis, laptops) that collaboratively train and run AI models without any internet connection or central coordinator. Nodes communicate only through local mesh (Wi-Fi Direct, Bluetooth, LoRa, or plain Ethernet) and exchange **knowledge** — never raw data.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

---

## 🤔 Why MessMind?

**Today's AI is centralized:**
- Your data leaves your device
- You need internet access
- One company controls the model
- No internet = no AI

**MessMind flips the model:**
- Data never leaves your device
- Works offline, anywhere
- No central authority
- The network IS the server

---

## ⚙️ How It Works

> **Step 1 — Local Training**  
> Each device trains its own copy of the model on its local data (photos, sensor readings, text). Raw data never leaves the device.

> **Step 2 — Compress Knowledge**  
> Changes to the model (gradients/weights) are compressed to tiny patches (kilobytes, not megabytes).

> **Step 3 — Gossip Protocol**  
> Devices send patches to neighbors via mesh. No central server — just peer-to-peer.

> **Step 4 — Aggregate**  
> Each device averages its model with received patches. Knowledge spreads like a rumor.

> **Step 5 — Repeat**  
> After enough rounds, all devices converge to the same smart model — trained collectively, without anyone seeing anyone else's data.

---

## ✨ What Makes It Unique

- **No internet required** — works in forests, basements, submarines
- **No central server** — no single point of failure or control
- **Works on LoRa** (bits per second) — adapts to ultra-low bandwidth
- **Data stays on device** — privacy by design
- **Resilient to node loss** — network heals itself

---

## 🎯 Use Cases

**Offline Smart Home**  
Sensors learn your patterns without sending data to China or AWS.

**Search & Rescue**  
Team in the wilderness with no cell signal — phones collaboratively identify helicopter sounds and share coordinates via mesh.

**Anonymous Collaborative Learning**  
Journalists train a censorship-detection model without revealing their documents.

**Critical Infrastructure**  
Submarine, mine, or arctic station — no internet, but internal mesh keeps AI running.

**Physical Penetration Testing**  
Five Raspberry Pis in a backpack work as a distributed AI assistant — analyzing Wi-Fi, recognizing devices, recommending attacks. No cloud, no logs on client servers.

---

## 📊 Project Status

⚠️ **Proof of Concept** — We have a working 3-node emulation on a single laptop via Docker. Real hardware tests (Raspberry Pi, LoRa) are next.

**Completed:**
- Basic node communication (HTTP)
- Model exchange skeleton
- Docker compose for 3 nodes

**Next:**
- Federated averaging (FedAvg)
- Gradient compression
- Bluetooth / Wi-Fi Direct transport
- LoRa support
- Raspberry Pi deployment guide

---

## 🚀 Quick Start (3-Node Emulation)

**Option 1: Docker (easiest)**
```bash
git clone https://github.com/yourusername/MessMind.git
cd MessMind
docker-compose up --build
