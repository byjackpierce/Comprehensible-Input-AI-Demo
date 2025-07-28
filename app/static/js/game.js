// Game state
let currentLanguage = '';
let currentWords = [];
let selectedWord = '';
let currentSentenceIndex = 0;
let sentences = [];

// Step 1: Language Selection
function selectLanguage(language) {
    currentLanguage = language;
    document.getElementById('selected-language').textContent = language;
    
    // Hide language step, show word step
    document.getElementById('language-step').style.display = 'none';
    document.getElementById('word-step').style.display = 'block';
    
    // Load words for the selected language
    loadWords(language);
}

// Load words from the API
async function loadWords(language) {
    try {
        const response = await fetch(`/api/generate-words/${language}`);
        const data = await response.json();
        
        if (data.error) {
            alert('Error loading words: ' + data.error);
            return;
        }
        
        currentWords = data.words;
        displayWords(data.words);
    } catch (error) {
        alert('Error loading words: ' + error);
    }
}

// Display words in the grid
function displayWords(words) {
    const wordGrid = document.getElementById('word-grid');
    wordGrid.innerHTML = '';
    
    words.forEach(word => {
        const wordCard = document.createElement('div');
        wordCard.className = 'word-card';
        wordCard.innerHTML = `
            <h3>${word}</h3>
            <p>Click to select</p>
        `;
        wordCard.onclick = () => selectWord(word);
        wordGrid.appendChild(wordCard);
    });
}

// Step 2: Word Selection
function selectWord(word) {
    selectedWord = word;
    currentSentenceIndex = 0;
    sentences = [];
    
    // Highlight selected word
    document.querySelectorAll('.word-card').forEach(card => {
        card.classList.remove('selected');
    });
    event.target.closest('.word-card').classList.add('selected');
    
    // Show game step and load first sentence
    setTimeout(() => {
        document.getElementById('word-step').style.display = 'none';
        document.getElementById('game-step').style.display = 'block';
        document.getElementById('target-word').textContent = word;
        
        // Load first sentence
        loadSentence(word, currentLanguage);
    }, 500);
}

// Load sentence from the API
async function loadSentence(word, language) {
    const sentenceDisplay = document.getElementById('sentence-display');
    sentenceDisplay.innerHTML = '<p><strong>Generating sentence...</strong></p>';
    
    try {
        const response = await fetch(`/api/generate-sentence/${language}/${word}`);
        const data = await response.json();
        
        if (data.error) {
            sentenceDisplay.innerHTML = `<p class="error">Error: ${data.error}</p>`;
            return;
        }
        
        // Store sentence and display it
        sentences.push(data.sentence);
        currentSentenceIndex = sentences.length - 1;
        
        sentenceDisplay.innerHTML = `
            <div class="sentence-content">
                <p class="sentence-text">${data.sentence}</p>
                <p class="instruction">What do you think this word means?</p>
                <p class="sentence-counter">Sentence ${currentSentenceIndex + 1} of 5</p>
            </div>
        `;
    } catch (error) {
        sentenceDisplay.innerHTML = `<p class="error">Error loading sentence: ${error}</p>`;
    }
}

// Navigation functions
function backToLanguages() {
    document.getElementById('word-step').style.display = 'none';
    document.getElementById('game-step').style.display = 'none';
    document.getElementById('language-step').style.display = 'block';
    currentLanguage = '';
    selectedWord = '';
    currentSentenceIndex = 0;
    sentences = [];
}

function backToWords() {
    document.getElementById('game-step').style.display = 'none';
    document.getElementById('word-step').style.display = 'block';
    selectedWord = '';
    currentSentenceIndex = 0;
    sentences = [];
}

function refreshWords() {
    if (currentLanguage) {
        loadWords(currentLanguage);
    }
}

// Step 3: Guessing - Updated to use binary feedback
async function submitGuess() {
    const guess = document.getElementById('guess-input').value;
    if (!guess.trim()) {
        alert('Please enter a guess!');
        return;
    }
    
    // Show loading state
    const feedback = document.getElementById('feedback');
    feedback.innerHTML = '<p><strong>Checking your guess...</strong></p>';
    feedback.style.display = 'block';
    feedback.className = 'feedback-box';
    
    try {
        // Call the binary feedback API
        const response = await fetch(`/api/check-guess/${selectedWord}/${currentLanguage}/${guess}`);
        const data = await response.json();
        
        if (data.error) {
            feedback.innerHTML = `<p class="error">Error: ${data.error}</p>`;
            return;
        }
        
        if (data.correct) {
            // Correct guess!
            feedback.innerHTML = `
                <div class="feedback-content correct">
                    <p><strong>Correct! 🎉</strong></p>
                    <p>You got it right! "${selectedWord}" means "${guess}".</p>
                    <button onclick="loadNewWord()" class="next-button">Next Word</button>
                </div>
            `;
        } else {
            // Incorrect guess - show next sentence or try again
            if (currentSentenceIndex < 4) {
                // Load next sentence
                feedback.innerHTML = `
                    <div class="feedback-content incorrect">
                        <p><strong>Not quite right.</strong></p>
                        <p>Let's try with another sentence...</p>
                    </div>
                `;
                
                // Load next sentence after a short delay
                setTimeout(() => {
                    loadSentence(selectedWord, currentLanguage);
                    feedback.style.display = 'none';
                }, 2000);
            } else {
                // No more sentences - show answer
                feedback.innerHTML = `
                    <div class="feedback-content incorrect">
                        <p><strong>Time's up!</strong></p>
                        <p>The word "${selectedWord}" means something else.</p>
                        <button onclick="loadNewWord()" class="next-button">Next Word</button>
                    </div>
                `;
            }
        }
        
    } catch (error) {
        feedback.innerHTML = `<p class="error">Error checking guess: ${error}</p>`;
    }
    
    // Clear the input
    document.getElementById('guess-input').value = '';
}

// Load a new word (reset game state)
function loadNewWord() {
    currentSentenceIndex = 0;
    sentences = [];
    document.getElementById('feedback').style.display = 'none';
    document.getElementById('game-step').style.display = 'none';
    document.getElementById('word-step').style.display = 'block';
    refreshWords();
} 