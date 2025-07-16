// Game state
let currentLanguage = '';
let currentWords = [];
let selectedWord = '';

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
    
    // Highlight selected word
    document.querySelectorAll('.word-card').forEach(card => {
        card.classList.remove('selected');
    });
    event.target.closest('.word-card').classList.add('selected');
    
    // Show game step and load sentence
    setTimeout(() => {
        document.getElementById('word-step').style.display = 'none';
        document.getElementById('game-step').style.display = 'block';
        document.getElementById('target-word').textContent = word;
        
        // Load sentence from API
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
        
        sentenceDisplay.innerHTML = `
            <div class="sentence-content">
                <p class="sentence-text">${data.sentence}</p>
                <p class="instruction">What do you think this word means?</p>
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
}

function backToWords() {
    document.getElementById('game-step').style.display = 'none';
    document.getElementById('word-step').style.display = 'block';
    selectedWord = '';
}

function refreshWords() {
    if (currentLanguage) {
        loadWords(currentLanguage);
    }
}

// Step 3: Guessing - Updated to call the scoring API
async function submitGuess() {
    const guess = document.getElementById('guess-input').value;
    if (!guess.trim()) {
        alert('Please enter a guess!');
        return;
    }
    
    // Show loading state
    const feedback = document.getElementById('feedback');
    feedback.innerHTML = '<p><strong>Scoring your guess...</strong></p>';
    feedback.style.display = 'block';
    feedback.className = 'feedback-box';
    
    try {
        // Call the scoring API
        const response = await fetch(`/api/score-guess/${selectedWord}/${currentLanguage}/${guess}`);
        const data = await response.json();
        
        if (data.error) {
            feedback.innerHTML = `<p class="error">Error: ${data.error}</p>`;
            return;
        }
        
        // Display the AI's full response
        feedback.innerHTML = `
            <div class="score-content">
                <p><strong>Your guess:</strong> "${guess}"</p>
                <p><strong>AI Response:</strong></p>
                <div class="ai-response">${data.score}</div>
            </div>
        `;
        
    } catch (error) {
        feedback.innerHTML = `<p class="error">Error scoring guess: ${error}</p>`;
    }
    
    // Clear the input
    document.getElementById('guess-input').value = '';
} 