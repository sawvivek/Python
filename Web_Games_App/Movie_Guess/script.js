const movies = [
  {
    title: "Inception",
    year: 2010,
    genre: "Sci-Fi",
    hints: [
      "A skilled thief enters peoples dreams.",
      "The movie features layers within layers of reality.",
      "A spinning top is a key symbol.",
      "Directed by Christopher Nolan.",
    ],
  },
  {
    title: "Titanic",
    year: 1997,
    genre: "Romance/Drama",
    hints: [
      "A love story unfolds during a historic ocean voyage.",
      "The ship is called unsinkable.",
      "One famous line: Im the king of the world.",
      "Directed by James Cameron.",
    ],
  },
  {
    title: "The Dark Knight",
    year: 2008,
    genre: "Action",
    hints: [
      "A caped hero faces a chaotic criminal mastermind.",
      "Gotham City is in danger.",
      "Why so serious? is a famous quote.",
      "The villain is the Joker.",
    ],
  },
  {
    title: "3 Idiots",
    year: 2009,
    genre: "Comedy/Drama",
    hints: [
      "A story set around engineering college life.",
      "The phrase All is well became iconic.",
      "The movie questions traditional education pressure.",
      "Stars Aamir Khan.",
    ],
  },
  {
    title: "Interstellar",
    year: 2014,
    genre: "Sci-Fi",
    hints: [
      "A team travels through a wormhole to save humanity.",
      "Time behaves differently near massive planets.",
      "The film blends space science and emotion.",
      "Features a character named Cooper.",
    ],
  },
  {
    title: "Dangal",
    year: 2016,
    genre: "Sports/Drama",
    hints: [
      "A father trains his daughters in wrestling.",
      "Based on a true story from India.",
      "The film showcases national and international competitions.",
      "Stars Aamir Khan.",
    ],
  },
  {
    title: "Avengers Endgame",
    year: 2019,
    genre: "Superhero",
    hints: [
      "Heroes try to reverse a universe-level disaster.",
      "Time travel plays a major role.",
      "One line says: I am Iron Man.",
      "It concludes a major MCU saga.",
    ],
  },
  {
    title: "Bahubali",
    year: 2015,
    genre: "Epic Action",
    hints: [
      "A powerful kingdom and throne rivalry are central themes.",
      "The question Why did Katappa kill Bahubali? became viral.",
      "Known for grand visuals and scale.",
      "Directed by S. S. Rajamouli.",
    ],
  },
];

const scoreEl = document.getElementById("score");
const roundEl = document.getElementById("round");
const livesEl = document.getElementById("lives");
const bestEl = document.getElementById("best");
const hintTextEl = document.getElementById("hintText");
const hintProgressEl = document.getElementById("hintProgress");
const genreTagEl = document.getElementById("genreTag");
const yearTagEl = document.getElementById("yearTag");
const guessInputEl = document.getElementById("guessInput");
const messageEl = document.getElementById("message");

const submitBtn = document.getElementById("submitBtn");
const hintBtn = document.getElementById("hintBtn");
const skipBtn = document.getElementById("skipBtn");
const quitBtn = document.getElementById("quitBtn");
const startBtn = document.getElementById("startBtn");

let score = 0;
let round = 1;
let lives = 3;
let currentMovie = null;
let hintIndex = 0;
let playedTitles = new Set();
let gameStarted = false;

const bestScore = Number(localStorage.getItem("movie_guess_best")) || 0;
bestEl.textContent = String(bestScore);

function normalize(value) {
  return value
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]/g, "");
}

function setMessage(text, mode = "") {
  messageEl.textContent = text;
  messageEl.className = mode;
}

function enableControls(enabled) {
  guessInputEl.disabled = !enabled;
  submitBtn.disabled = !enabled;
  hintBtn.disabled = !enabled;
  skipBtn.disabled = !enabled;
  quitBtn.disabled = !enabled;
}

function updateScoreboard() {
  scoreEl.textContent = String(score);
  roundEl.textContent = String(round);
  livesEl.textContent = String(lives);
}

function getNextMovie() {
  if (playedTitles.size === movies.length) {
    playedTitles = new Set();
  }

  const available = movies.filter((movie) => !playedTitles.has(movie.title));
  const picked = available[Math.floor(Math.random() * available.length)];
  playedTitles.add(picked.title);
  return picked;
}

function showCurrentHint() {
  hintTextEl.textContent = currentMovie.hints[hintIndex];
  hintProgressEl.textContent = `Hint ${hintIndex + 1}/${currentMovie.hints.length}`;
  genreTagEl.textContent = `Genre: ${currentMovie.genre}`;
  yearTagEl.textContent = `Year: ${currentMovie.year}`;
}

function startRound() {
  currentMovie = getNextMovie();
  hintIndex = 0;
  guessInputEl.value = "";
  guessInputEl.focus();
  showCurrentHint();
  setMessage("New round started. Make your guess.");
  updateScoreboard();
}

function endGame(customMessage = "", customMode = "warn") {
  gameStarted = false;
  enableControls(false);
  hintTextEl.textContent = "Game over. Press Start New Game to play again.";
  hintProgressEl.textContent = "Hint 0/0";
  genreTagEl.textContent = "Genre: -";
  yearTagEl.textContent = "Year: -";
  startBtn.textContent = "Start New Game";

  const storedBest = Number(localStorage.getItem("movie_guess_best")) || 0;
  let isNewBest = false;
  if (score > storedBest) {
    localStorage.setItem("movie_guess_best", String(score));
    bestEl.textContent = String(score);
    isNewBest = true;
  }

  if (customMessage) {
    const finalMessage = isNewBest
      ? `${customMessage} New best score: ${score}.`
      : customMessage;
    setMessage(finalMessage, isNewBest ? "good" : customMode);
    return;
  }

  if (isNewBest) {
    setMessage(`New best score: ${score}. Amazing run!`, "good");
  } else {
    setMessage(`Final score: ${score}. Try to beat your best!`, "warn");
  }
}

function handleCorrectGuess() {
  const points = Math.max(10 - hintIndex * 2, 4);
  score += points;
  round += 1;
  setMessage(
    `Correct! +${points} points. The answer was ${currentMovie.title}.`,
    "good",
  );
  startRound();
}

function handleWrongGuess() {
  lives -= 1;
  if (lives <= 0) {
    setMessage(
      `Wrong guess. The correct answer was ${currentMovie.title}.`,
      "bad",
    );
    updateScoreboard();
    endGame();
    return;
  }
  setMessage("Not correct. Use Next Hint or try another guess.", "bad");
  updateScoreboard();
}

function handleSubmitGuess() {
  if (!gameStarted || !currentMovie) {
    setMessage("Press Start New Game first.", "warn");
    return;
  }

  const guess = guessInputEl.value;
  if (!guess.trim()) {
    setMessage("Enter a movie name before submitting.", "warn");
    return;
  }

  const isCorrect = normalize(guess) === normalize(currentMovie.title);
  guessInputEl.value = "";

  if (isCorrect) {
    handleCorrectGuess();
    return;
  }

  handleWrongGuess();
}

function handleNextHint() {
  if (!gameStarted || !currentMovie) {
    setMessage("Start a game to get hints.", "warn");
    return;
  }

  if (hintIndex < currentMovie.hints.length - 1) {
    hintIndex += 1;
    showCurrentHint();
    setMessage("Hint updated. Fewer points if you guess now.", "warn");
    return;
  }

  lives -= 1;
  setMessage(
    `No hints left. The answer was ${currentMovie.title}. You lost 1 life.`,
    "bad",
  );

  if (lives <= 0) {
    updateScoreboard();
    endGame();
    return;
  }

  round += 1;
  updateScoreboard();
  startRound();
}

function handleSkip() {
  if (!gameStarted || !currentMovie) {
    setMessage("Start a game before using skip.", "warn");
    return;
  }

  lives -= 1;
  if (lives <= 0) {
    setMessage(`You skipped. The answer was ${currentMovie.title}.`, "bad");
    updateScoreboard();
    endGame();
    return;
  }

  round += 1;
  setMessage(
    `Skipped! The answer was ${currentMovie.title}. You lost 1 life.`,
    "warn",
  );
  updateScoreboard();
  startRound();
}

function handleQuit() {
  if (!gameStarted) {
    setMessage("No active game to quit. Press Start New Game first.", "warn");
    return;
  }

  endGame(`You quit the game. Final score: ${score}.`, "warn");
}

function startGame() {
  score = 0;
  round = 1;
  lives = 3;
  gameStarted = true;
  startBtn.textContent = "Restart Round";
  enableControls(true);
  updateScoreboard();
  startRound();
}

startBtn.addEventListener("click", () => {
  startGame();
});

submitBtn.addEventListener("click", handleSubmitGuess);
hintBtn.addEventListener("click", handleNextHint);
skipBtn.addEventListener("click", handleSkip);
quitBtn.addEventListener("click", handleQuit);

guessInputEl.addEventListener("keydown", (event) => {
  if (event.key === "Enter" && !guessInputEl.disabled) {
    handleSubmitGuess();
  }
});
