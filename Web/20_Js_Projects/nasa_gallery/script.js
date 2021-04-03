const resultsNav = document.getElementById('resultsNav');
const favoritesNav = document.getElementById('favoritesNav');
const imagesContainer = document.querySelector('.images-container');
const saveConfirmed = document.querySelector('.save-confirmed');
const loader = document.querySelector('.loader');

// NASA API
const count = 10;
const apiKey = 'DEMO_KEY';
const apiUrl = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}&count=${count}`;

let resultsArray = []; //array to store API results in
let favorites = {};

const showContent = (page) => {
    window.scrollTo({top: 0, behavior: "smooth"}) /*scroll back up to the start*/
    if (page === 'results') {
        resultsNav.classList.remove('hidden'); /*show the home navbar*/
        favoritesNav.classList.add('hidden'); /*hide the favorites navbar*/
    } else {
        resultsNav.classList.add('hidden'); /*hide the home navbar*/
        favoritesNav.classList.remove('hidden'); /*add the favorites navbar*/
    }
    loader.classList.add('hidden') /*hide our loader icon*/
}


const createDOMNodes = (page) => { /*this will make the cards that we will display on the website*/
    const currentArray = page === 'results' ? resultsArray : Object.values(favorites) /*check wether we need to render results or favorites page*/
    currentArray.forEach((result) => {
        /*Card container*/
        const card = document.createElement('div');
        card.classList.add('card');
        /*Link*/
        const link = document.createElement('a');
        link.href = result.hdurl;
        link.title = 'View Full Image';
        link.target = '_blank';
        /*Image*/
        const image = document.createElement('img');
        image.src = result.url;
        image.alt = 'NASA Picture of the Day'
        image.loading = 'lazy'
        image.classList.add('card-img-top');
        /*Card Body*/
        const cardBody = document.createElement('div');
        cardBody.classList.add('card-body');
        /*Card Title*/
        const cardTitle = document.createElement('h5');
        cardTitle.classList.add('card-title');
        cardTitle.textContent = result.title;
        /*Save Text*/
        const saveText = document.createElement('p');
        saveText.classList.add('clickable');
        if (page === 'results') {
            saveText.textContent = 'Add favorite';
            saveText.setAttribute('onclick', `saveFavorite('${result.url}')`);
        } else {
            saveText.textContent = 'Remove favorite';
            saveText.setAttribute('onclick', `removeFavorite('${result.url}')`);

        }
        /*Card text*/
        const cardText = document.createElement('p');
        cardText.textContent = result.explanation;
        /*Footer Container*/
        const footer = document.createElement('small');
        footer.classList.add('text-muted');
        /*Date*/
        const date = document.createElement('strong');
        date.textContent = result.date;
        /*Copyright*/
        const copyrightResult = result.copyright === undefined ? '' : result.copyright;
        const copyright = document.createElement('span');
        copyright.textContent = ` ${copyrightResult}`;
        /*Append*/
        footer.append(date, copyright);
        cardBody.append(cardTitle, saveText, cardText, footer)
        link.appendChild(image);
        card.append(link, cardBody);
        imagesContainer.append(card);
    });
}

const updateDOM = (page) => {
    /*get favorites from local storage*/
    if (localStorage.getItem('nasaFavorites')) {
        favorites = JSON.parse(localStorage.getItem('nasaFavorites'))
    }
    imagesContainer.textContent = '';
    createDOMNodes(page);
    showContent(page);
}

/*Get 5 images from NASA API*/
async function getNasaPictures() {
    /*Show loader*/
    loader.classList.remove('hidden')
    try {
        const response = await fetch(apiUrl)
        resultsArray = await response.json()
        updateDOM('results');
    } catch (e) {
        console.log(e);
    }
}

// Add results to favorites
const saveFavorite = (itemURL) => {
    /*Loop through the results array to find the favorite that the user selected*/
    resultsArray.forEach((item) => {
        if (item.url.includes(itemURL) && !favorites[itemURL]) {
            favorites[itemURL] = item; /*set the card object in the favorites array*/
            /*Show save confirmation for 2 seconds*/
            saveConfirmed.hidden = false;
            setTimeout(() => {
                saveConfirmed.hidden = true /*hide the confirmation after 2000ms*/
            }, 2000);
            localStorage.setItem('nasaFavorites', JSON.stringify(favorites))
        }
    })
}
/*Remove item from favorites*/

const removeFavorite = (itemURL) => {
    if (favorites[itemURL]) { /*look through favorites*/
        delete favorites[itemURL] /*if its found, delete it*/
        localStorage.setItem('nasaFavorites', JSON.stringify(favorites)) /*update localstorage*/
        updateDOM('favorites')
    }
}
/*on load*/
getNasaPictures();