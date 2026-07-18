<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:FF6B35,100:00B4D8&height=220&section=header&text=Flappy%20Bird%20%F0%9F%90%A6&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35&desc=PyGame%20Remaster%20%7C%20Classic%20Arcade%20%7C%20Python&descAlignY=55&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=2500&pause=500&color=FF6B35&center=true&vCenter=true&width=700&lines=🐤+Flap+Through+Pipes+%26+Collect+Coins!;🔥+Built+with+PyGame+in+Python;🏆+Beat+Your+High+Score!;🎮+Classic+Meets+Modern+Arcade" alt="Typing SVG" />

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyGame](https://img.shields.io/badge/PyGame-2.5-00B4D8?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</div>

---

## 🎯 Overview

A modern reimagining of the classic **Flappy Bird** arcade game — built from scratch in **Python** using **PyGame**. Navigate a bird through procedurally generated pipes, collect shiny coins for bonus points, and compete against your own high score. Smooth physics, sprite animations, background music & sound effects bring the retro experience to life.

---

## 🎬 Game Preview

<div align="center">

| 🏁 Start Menu | 🎮 Gameplay | 💀 Game Over |
|:---:|:---:|:---:|
| <img src="PycharmProjects/Flappy-bird_pygame/screenshots/start_menu.png" width="220"/> | <img src="PycharmProjects/Flappy-bird_pygame/screenshots/gameplay.png" width="220"/> | <img src="PycharmProjects/Flappy-bird_pygame/screenshots/game_over.png" width="220"/> |

| ⏸️ Pause Screen | 🪙 Coin Collect |
|:---:|:---:|
| <img src="PycharmProjects/Flappy-bird_pygame/screenshots/pause_screen.png" width="220"/> | <img src="PycharmProjects/Flappy-bird_pygame/screenshots/coin_collect.png" width="220"/> |

</div>


---

## ✨ Features

<table>
<tr>
<td width="50%" valign="top">

### 🐤 Core Gameplay
- 🕊️ Smooth flap physics with gravity & velocity
- 🏗️ Procedurally generated pipes (random heights)
- 🪙 Collectible coins (+5 bonus points each)
- 📈 Persistent high score tracking
- 🎨 Animated bird sprite (2-frame wing flap)

</td>
<td width="50%" valign="top">

### 🎧 Audio & Experience
- 🎵 Looping background music
- 🔊 Game over sound effect
- ⏸️ Pause / resume anytime (P key)
- 🖥️ Clean dark-themed menus
- 🚀 60 FPS smooth gameplay loop

</td>
</tr>
</table>

---

<div align="center">
<img src="https://capsule-render.vercel.app/api?type=rect&color=0:00B4D8,100:FF6B35&height=3&width=100%"/>
</div>

## 🛠️ Tech Stack

<div align="center">
<img src="https://skillicons.dev/icons?i=python,git,github,vscode" />
</div>

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Game Framework | PyGame 2.5 |
| Audio | `pygame.mixer` (`.wav` / `.mp3`) |
| Graphics | Custom sprites + `pygame.transform` |

---

## 🚀 Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/flappy-bird-pygame.git
cd flappy-bird-pygame
```

**2. Install PyGame**
```bash
pip install pygame
```

**3. Run the game**
```bash
python main.py
```

> **Controls:** `SPACE` to flap / restart · `P` to pause

---

## 🏗️ Project Structure

```
flappy-bird-pygame/
├── assets/               # Game assets
│   ├── background.png    # Scrolling background
│   ├── coin.png          # Collectible coin sprite
│   ├── flap1.png         # Bird frame 1
│   ├── flap2.png         # Bird frame 2
│   ├── game_over.wav     # Game over SFX
│   └── music.mp3         # Background music
├── screenshots/          
│   ├── start_menu.png
│   ├── gameplay.png
│   ├── game_over.png
│   ├── pause_screen.png
│   └── coin_collect.png
├── main.py               # 🎮 Entry point — all game logic
└── README.md             # 📖 You're here
```

---

## 🧠 How It Works

| Concept | Implementation |
|---|---|
| **Bird Physics** | Gravity `0.4` + Jump `-8` velocity — smooth arc motion |
| **Pipe Spawning** | Random height `80–300px` with fixed `190px` gap |
| **Coin System** | Spawns at random Y; +5 score on collision; resets off-screen |
| **Collision** | `pygame.Rect.colliderect()` for bird vs pipes / screen bounds |
| **Game States** | `start_menu()` → `main()` → `game_over()` → loop |

---

## 📈 Roadmap

- [ ] Increasing difficulty (faster pipes over time)
- [ ] Particle effects on coin collect
- [ ] Power-ups (shield, magnet, slow-mo)
- [ ] Mobile touch input support
- [ ] Leaderboard with local scores

---

<div align="center">

### ⭐ Star this repo if you love retro arcade games!

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00B4D8,100:FF6B35&height=120&section=footer"/>

</div>
