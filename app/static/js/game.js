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
    
    // Show game step after a short delay
    setTimeout(() => {
        document.getElementById('word-step').style.display = 'none';
        document.getElementById('game-step').style.display = 'block';
        document.getElementById('target-word').textContent = word;
        document.getElementById('sentence-display').innerHTML = `
            <p><strong>Loading sentence...</strong></p>
            <p>This feature is coming soon!</p>
        `;
    }, 500);
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

// Step 3: Guessing (placeholder for now)
function submitGuess() {
    const guess = document.getElementById('guess-input').value;
    if (!guess.trim()) {
        alert('Please enter a guess!');
        return;
    }
    
    // For now, just show a placeholder message
    const feedback = document.getElementById('feedback');
    feedback.innerHTML = `
        <p>You guessed: "${guess}"</p>
        <p>This feature is coming soon!</p>
    `;
    feedback.style.display = 'block';
    feedback.className = 'feedback-box';
    
    // Clear the input
    document.getElementById('guess-input').value = '';
} 