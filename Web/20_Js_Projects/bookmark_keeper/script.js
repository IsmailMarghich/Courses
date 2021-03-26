const modal = document.getElementById('modal');
const modalShow = document.getElementById('show-modal');
const modalClose = document.getElementById('close-modal');
const bookmarkForm = document.getElementById('bookmark-form');
const websiteNameElement = document.getElementById('website-name');
const websiteUrlElement = document.getElementById('website-url');
const bookmarksContainer = document.getElementById('bookmarks-container');

let bookmarks = []; /*array to store our bookmarks in*/
/*Show modal, focus on input*/
/*Our modal is what allows uses to add bookmarks with their URL and the name they want to use.*/
const showModal = () =>{
    modal.classList.add('show-modal'); /*show the modal*/
    websiteNameElement.focus(); /*focus on the text box so use can enter text easily*/
}


/*Modal event listeners*/
modalClose.addEventListener('click', ()=>{ modal.classList.remove('show-modal')});
modalShow.addEventListener('click', showModal)
window.addEventListener('click',(e) => { console.log(e.target === modal ? modal.classList.remove('show-modal') : false)});
/*Validate user form*/
const validate = (nameValue, urlValue) => {
    const expression = /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_.~#?&/=]*)/g; /*regex to validate url*/
    const regex = new RegExp(expression);

    if (!nameValue || !urlValue){
        alert('Please enter values for both fields')
        return false;
    }

    if (urlValue.match(regex)){
        alert('matches')
    }
    if (!urlValue.match(regex)){
        alert('Please provide valid web address');
        return false;
    }
    /*if everything is okay and valid*/
    return true;
}
/*Function to build bookmarks on the website*/
const buildBookmarks = () => {
    /*build items*/
    bookmarksContainer.textContent = ""; /*clear the bookmark container to prevent duplicate bookmarks being built*/
    bookmarks.forEach((bookmark)=> {
        const {name, url} = bookmark; /*get name and url from bookmark*/
        /*Item*/
        const item = document.createElement('div');
        item.classList.add('item'); /*add classes*/
        /*close icon*/
        const closeIcon = document.createElement('i');
        closeIcon.classList.add('fas','fa-times');
        closeIcon.setAttribute('title', 'Delete Boomark') /*add hover text*/
        closeIcon.setAttribute('onclick', `deleteBookmark('${url}')`) /*run our delete bookmark function*/
        /*Favicon/link container */
        const linkInfo = document.createElement('div');
        linkInfo.classList.add('name');
        /*Favicon*/
        const favicon = document.createElement('img');
        favicon.setAttribute('src', `http://s2.googleusercontent.com/s2/favicons?domain=${url}`) /*favicon url from google using website url*/
        favicon.setAttribute('alt', 'Favicon');
        /*Link*/
        const link = document.createElement('a');
        link.setAttribute('href', `${url}`);
        link.setAttribute('target', '_blank');
        link.textContent = name;
        /*combine all these separate elements together into a bookmark, and append to bookmark container*/
        linkInfo.append(favicon, link);
        item.append(closeIcon, linkInfo);
        bookmarksContainer.appendChild(item);
    });
}

/*Fetch bookmarks from local storage*/
const fetchBookmarks = () =>{
    /*get bookmarks from local storage if available*/
    if (localStorage.getItem('bookmarks')){
        bookmarks = JSON.parse(localStorage.getItem('bookmarks')); /*add localstorage bookmarks to our array*/
    } else {
        /*create bookmarks array in localStorage*/
        bookmarks = [ /*add a default bookmark, to the website of the course instructor*/
            {
                name: 'Jacinto Design',
                url: 'https://jacinto.design'
            },
        ];
        localStorage.setItem('bookmarks', JSON.stringify(bookmarks)) /*set it into local storage for next time*/
    }
    buildBookmarks();
}
/*Delete bookmark*/
const deleteBookmark = (url) => {
    bookmarks.forEach((bookmark, i)=>{ /*iterate over bookmark array to find the url to delete*/
        if (bookmark.url === url){
            bookmarks.splice(i, 1); /*go to index i, and remove 1 element*/
        }
    });
    /*update bookmarks array in local storage*/
    localStorage.setItem('bookmarks', JSON.stringify(bookmarks));
    fetchBookmarks(); /*fetch bookmarks and repopulate page again*/
}
/*Handle data from Form*/
const storeBookmark = (e) => {
    e.preventDefault();
    /*store user input*/
    const nameValue = websiteNameElement.value;
    let urlValue = websiteUrlElement.value; /*we use let because we want to add https ourselves to the link*/
    if (!urlValue.includes('http://') && !urlValue.includes('https://')){ /*if url doesnt have http or https*/
        urlValue = `https://${urlValue}`; /*add it ourselves*/
    }
    if (!validate(nameValue, urlValue)){
        return false;
    }
    const bookmark = { /*store the users data into a bookmark object*/
        name: nameValue,
        url: urlValue,
    };
    bookmarks.push(bookmark) /*add bookmark to array*/
    localStorage.setItem('bookmarks', JSON.stringify(bookmarks)); /*store the bookmarks in browser*/
    buildBookmarks();
    bookmarkForm.reset(); /*reset our form*/
    websiteNameElement.focus(); /*focus on input again*/
}

/*Modal event listener*/
bookmarkForm.addEventListener('submit', storeBookmark);

/*On load, fetch bookmarks*/
fetchBookmarks();