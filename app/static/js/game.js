// Game state
let currentLanguage = '';
let currentWords = [];
let selectedWord = '';
let currentSentenceIndex = 0;
let sentences = [];

// Step 1: Language Selection
function selectLanguage(language) {
    currentLanguage = language;
    
    // Highlight selected language button and disable all language buttons
    document.querySelectorAll('.language-btn').forEach(btn => {
        btn.classList.remove('selected');
        btn.disabled = true; // Disable all language buttons
    });
    event.target.classList.add('selected');
    
    // Show word selection step
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
        wordCard.innerHTML = `<h3>${word}</h3>`;
        wordCard.onclick = () => selectWord(word);
        wordGrid.appendChild(wordCard);
    });
}

// Step 2: Word Selection
function selectWord(word) {
    selectedWord = word;
    currentSentenceIndex = 0;
    sentences = [];
    
    // Highlight selected word and disable all word cards
    document.querySelectorAll('.word-card').forEach(card => {
        card.classList.remove('selected');
        card.style.pointerEvents = 'none'; // Disable clicking
        card.style.opacity = '0.6'; // Visual indication they're disabled
    });
    event.target.closest('.word-card').classList.add('selected');
    event.target.closest('.word-card').style.opacity = '1'; // Keep selected one fully visible
    
    // Disable the refresh button as well
    document.querySelector('.refresh-btn').disabled = true;
    document.querySelector('.refresh-btn').style.opacity = '0.6';
    
    // Show sentence step and load first sentence
    setTimeout(() => {
        document.getElementById('sentence-step').style.display = 'block';
        
        // Load first sentence
        loadSentence(word, currentLanguage);
    }, 500);
}

// Load sentence from the API
async function loadSentence(word, language) {
    try {
        const response = await fetch(`/api/generate-sentence/${language}/${word}`);
        const data = await response.json();
        
        if (data.error) {
            addSentenceToProgression(`<p class="error">Error: ${data.error}</p>`, 'error');
            return;
        }
        
        // Store sentence and add to progression
        sentences.push(data.sentence);
        currentSentenceIndex = sentences.length - 1;
        
        addSentenceToProgression(data.sentence, 'new');
        
        // Show guess section after a short delay
        setTimeout(() => {
            document.getElementById('guess-section').style.display = 'block';
        }, 1000);
        
    } catch (error) {
        addSentenceToProgression(`<p class="error">Error loading sentence: ${error}</p>`, 'error');
    }
}

// Add sentence to the progression display
function addSentenceToProgression(sentence, status = 'new') {
    const progression = document.getElementById('sentence-progression');
    
    const sentenceItem = document.createElement('div');
    sentenceItem.className = `sentence-item ${status}`;
    sentenceItem.innerHTML = `<p class="sentence-text">${sentence}</p>`;
    
    progression.appendChild(sentenceItem);
    
    // Scroll to the new sentence
    sentenceItem.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Mark sentence as incorrect
function markSentenceIncorrect() {
    const sentenceItems = document.querySelectorAll('.sentence-item');
    if (sentenceItems.length > 0) {
        const lastSentence = sentenceItems[sentenceItems.length - 1];
        lastSentence.classList.remove('new');
        lastSentence.classList.add('incorrect');
    }
}

// Mark sentence as correct
function markSentenceCorrect() {
    const sentenceItems = document.querySelectorAll('.sentence-item');
    if (sentenceItems.length > 0) {
        const lastSentence = sentenceItems[sentenceItems.length - 1];
        lastSentence.classList.remove('new');
        lastSentence.classList.add('correct');
    }
}

// Navigation functions
function refreshWords() {
    if (currentLanguage) {
        loadWords(currentLanguage);
    }
}

// Step 3: Guessing - Updated for progressive disclosure
async function submitGuess() {
    const guess = document.getElementById('guess-input').value;
    if (!guess.trim()) {
        alert('Please enter a guess!');
        return;
    }
    
    // Hide guess section temporarily
    document.getElementById('guess-section').style.display = 'none';
    
    try {
        // Call the binary feedback API
        const response = await fetch(`/api/check-guess/${selectedWord}/${currentLanguage}/${guess}`);
        const data = await response.json();
        
        if (data.error) {
            alert('Error: ' + data.error);
            document.getElementById('guess-section').style.display = 'block';
            return;
        }
        
        if (data.correct) {
            // Correct guess!
            markSentenceCorrect();
            
            // Show completion
            setTimeout(() => {
                showCompletion(guess);
            }, 1000);
            
        } else {
            // Incorrect guess - show next sentence or try again
            markSentenceIncorrect();
            
            if (currentSentenceIndex < 4) {
                // Load next sentence after a delay
                setTimeout(() => {
                    loadSentence(selectedWord, currentLanguage);
                }, 2000);
            } else {
                // No more sentences - show completion
                setTimeout(() => {
                    showCompletion(null);
                }, 2000);
            }
        }
        
    } catch (error) {
        alert('Error checking guess: ' + error);
        document.getElementById('guess-section').style.display = 'block';
    }
    
    // Clear the input
    document.getElementById('guess-input').value = '';
}

// Show completion step
function showCompletion(correctGuess) {
    const completionStep = document.getElementById('completion-step');
    const completionContent = document.getElementById('completion-content');
    
    if (correctGuess) {
        completionContent.innerHTML = `
            <div class="success-message">
                <h3>Excellent! You got it right!</h3>
                <p>The word <strong>"${selectedWord}"</strong> means <strong>"${correctGuess}"</strong>.</p>
                <p>You learned this through context clues in ${sentences.length} sentence${sentences.length > 1 ? 's' : ''}!</p>
            </div>
        `;
    } else {
        completionContent.innerHTML = `
            <div class="learning-message">
                <h3>Learning Complete!</h3>
                <p>You saw ${sentences.length} different contexts for the word <strong>"${selectedWord}"</strong>.</p>
                <p>This demonstrates how multiple sentences help build understanding!</p>
            </div>
        `;
    }
    
    completionStep.style.display = 'block';
    completionStep.scrollIntoView({ behavior: 'smooth' });
}

// Start a new demo
function startNewDemo() {
    // Reset all state
    currentLanguage = '';
    currentWords = [];
    selectedWord = '';
    currentSentenceIndex = 0;
    sentences = [];
    
    // Reset UI
    document.getElementById('word-step').style.display = 'none';
    document.getElementById('sentence-step').style.display = 'none';
    document.getElementById('completion-step').style.display = 'none';
    document.getElementById('guess-section').style.display = 'none';
    document.getElementById('sentence-progression').innerHTML = '';
    
    // Reset selections
    document.querySelectorAll('.language-btn').forEach(btn => {
        btn.classList.remove('selected');
    });
    document.querySelectorAll('.word-card').forEach(card => {
        card.classList.remove('selected');
    });
    
    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });
} 