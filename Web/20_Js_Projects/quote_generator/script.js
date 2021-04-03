/* We will get quotes from an API to display*/
const quoteContainer = document.getElementById('quote-container')
const quoteText = document.getElementById('quote')
const authorText = document.getElementById('author')
const twitterButton = document.getElementById('twitter')
const newQuoteButton = document.getElementById('new-quote');
const loader = document.getElementById('loader')
/*The elements we will be using ^^*/
let apiQuotes = []; /*global variable to store our quotes*/

/*show loader*/
const loadingSpinner = () => {
    loader.hidden = false;
    quoteContainer.hidden = true;
}
/*hide loader*/
const removeSpinner = () => {
    quoteContainer.hidden = false;
    loader.hidden = true;
}

/*function to show new quote*/
const newQuote = () => {
    loadingSpinner();
    /*pick a random quote*/
    const quote = apiQuotes[Math.floor(Math.random() * apiQuotes.length)]
    if (!authorText) { /*if theres no author, write unknown*/
        authorText.textContent = 'Unknown'
    } else {
        authorText.textContent = quote.author;
    }

    /*check quote length to see if we wanna make it smaller with styling*/
    if (quote.text.length > 120) {
        quoteText.classList.add('long-quote')
    } else {
        quoteText.classList.remove('long-quote')
    }
    /*hide loader*/
    removeSpinner();
    quoteText.textContent = quote.text;

}

async function getQuotes() {
    loadingSpinner(); /*show loading symbol*/
    const apiUrl = 'https://type.fit/api/quotes';
    try {
        const response = await fetch(apiUrl); /* store the quotes from API in variable*/
        apiQuotes = await response.json(); /*turn the response to JSON objects and store in quote array*/
        newQuote();
    } catch (e) {
        /*handle api error*/
        console.log(e, ' API request failed!')
    }
}

const tweetQuote = () => { /*function to tweet the quote*/
    const twitterUrl = `https://twitter.com/intent/tweet?text=${quoteText.textContent} - ${authorText.textContent}`; /*this template string fills a URL to tweet the quote*/
    window.open(twitterUrl, '_blank') /*open a window to tweet the quote*/
}

/*Event listeners*/
newQuoteButton.addEventListener('click', newQuote); /*generate new quote*/
twitterButton.addEventListener('click', tweetQuote); /*tweet the quote*/
/*On load*/
getQuotes(); /*run the function once the page loads*/
newQuote()
