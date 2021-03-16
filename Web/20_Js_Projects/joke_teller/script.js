const button = document.getElementById('button');
const audioElement = document.getElementById('audio');

// Disable/Enable Button
function toggleButton() {
    button.disabled = !button.disabled;
}

// VoiceRSS Speech Function, from VoiceRSS.js file
function tellMe(joke) {
    const jokeString = joke.trim().replace(/ /g, '%20'); /*replace parts of the string so we can use it in URL*/
    // VoiceRSS Speech Parameters
    VoiceRSS.speech({
        key: '804246855fa5468d8d47eed325858255',
        src: jokeString,
        hl: 'en-us',
        r: 0,
        c: 'mp3',
        f: '44khz_16bit_stereo',
        ssml: false,
    });
}

// Get jokes from Joke API
async function getJokes() {
    let joke = '';
    const apiUrl = 'https://sv443.net/jokeapi/v2/joke/Programming?blacklistFlags=nsfw,racist,sexist';
    try {
        const response = await fetch(apiUrl); /*wait for API response*/
        const data = await response.json(); /*store response*/
        // Assign One or Two Part Joke
        if (data.setup) {
            joke = `${data.setup} ... ${data.delivery}`;
        } else {
            joke = data.joke;
        }
        // Passing Joke to VoiceRSS API
        tellMe(joke);
        // Disable Button
        toggleButton();
    } catch (error) {
        // Catch Error Here
    }
}

// Event Listeners
button.addEventListener('click', getJokes);
audioElement.addEventListener('ended', toggleButton);
