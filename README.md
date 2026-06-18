# 🔤 Word Scramble Game 🎮

✨ A fun desktop word-guessing game built with Python's **Tkinter** library! Letters of a random word get shuffled on screen 🔀, and you race to type the correct word before moving on. Need help? Hints reveal one letter at a time 💡, and a running score ◈ tracks your wins!

---

## 🖼️ Interface Preview

```
╔══════════════════════════════════════════════╗
║   🌌  Window: "Word Scramble Game"  700x650   ║
╠══════════════════════════════════════════════╣
║                                                ║
║   Find The Word            ◈Score 003         ║
║                                                ║
║          T  G  E  R  I   🔀 (scrambled)       ║
║                                                ║
║        ┌──────────────────────────┐           ║
║        │   [ TYPE HERE...    ]    │  📝        ║
║        └──────────────────────────┘           ║
║                                                ║
║   [ Submit ↲ ]  [ Reset ↻ ]  [ Next Word ⫸ ]   ║
║              [   Hint 💡   ]                  ║
║                                                ║
║         __  __  __  __  __   (hint row)        ║
║                                                ║
║      ✅/❌  Nice try! Thats not correct!        ║
╚══════════════════════════════════════════════╝
```

🎨 **Color theme:** deep purple background (`#3F045C`) with neon green 🟢, electric blue 🔵, yellow 🟡, and red 🔴 accents on buttons and text for a vibrant, game-like feel.

---

## 🌟 Features

- 📚 Pool of **150+ words** — everyday objects, animals, places, tech terms, and more
- 🔀 Letters shuffled randomly each round
- ◈ Score counter — goes **up** ⬆️ on a correct guess, **down** ⬇️ if you decline to continue after a win
- 💡 Hint button — reveals one letter at a time
- ⌨️ Press **Enter ↲** to submit your answer instantly
- 🔄 Reset button to clear the input box
- 🏆 Victory popup once every word has been guessed!

---

## ⚙️ Requirements

| Requirement | Details |
|---|---|
| 🐍 Python | 3.x |
| 🖼️ Tkinter | Included with most Python installs. On Linux: `sudo apt-get install python3-tk` |

---

## ▶️ How to Run

```bash
python word_scramble.py
```

💬 *(Rename the file to whatever you like before running, e.g. `word_scramble.py`.)*

---

## 🎯 How to Play

1. 👀 The scrambled letters of a word appear at the top of the window.
2. ⌨️ Type your guess into the text box and press **Enter ↲** or click **Submit**.
3. ✅ If correct — your score goes up ◈ and you'll be asked to move to the next word.
4. ❌ If incorrect — a red banner 🔴 lets you know, try again!
5. 🤔 Stuck? Click **Hint 💡** to reveal the next letter.
6. ⏭️ Click **Next Word ⫸** to skip to a new word anytime.
7. 🔄 Click **Reset ↻** to clear your current input.

---

## ⚠️ Known Limitations

- 🔁 Skipping with **Next Word** doesn't remove the word from the pool — it can reappear later.
- 💡 The hint counter doesn't reset when skipping outside the normal `check()` flow, causing minor hint-tracking quirks.
- 💾 No persistent high-score saving between sessions.

---

## 🚀 Possible Improvements

- 💾 Save high scores to a file between sessions
- ⏱️ Add a timer ⏳ or difficulty levels (word length tiers)
- 🚫 Prevent repeated words within the same session more robustly
- 🔊 Add sound effects for correct ✅ / incorrect ❌ guesses
- 📱 Responsive resizing for different screen sizes

---

🎉 **Have fun unscrambling!** 🔤✨
