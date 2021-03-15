/*fetching images from unsplash API*/
const imageContainer = document.getElementById('image-container')
const loader = document.getElementById('loader')

let ready = false;
let imagesLoaded = 0;
let totalImages = 0;
let photosArray = [];

const count = 30;
const apiKey = 'KwSM8UNT_ikQNS0s2redyLfBFXa_HN08-Ct5n5cHXsg';
const apiUrl = `https://api.unsplash.com/photos/random/?client_id=${apiKey}&count=${count}`

/*Helper function to check if all images were loaded*/
const imageLoaded = () => {
    imagesLoaded++;
    if (imagesLoaded === totalImages) {
        ready = true; /*if all the images are loaded, we are ready to load more*/
        loader.hidden = true; /*hide our loader spinner after images are loaded*/
    }
}
/*Helper function to add attributes to dom elements*/
const setAttributes = (element, attributes) => {
    for (const key in attributes) {
        element.setAttribute(key, attributes[key])
    }
}
/*Create elements for links and photos*/
const displayPhotos = () => {
    imagesLoaded = 0; /*everytime we reset how many images we loaded, for the helper loader function above*/
    totalImages = photosArray.length;
    photosArray.forEach((photo) => {
        /*Create <a> to link to unsplash*/
        const item = document.createElement('a');
        setAttributes(item, {
            href: photo.links.html,
            target: '_blank',
        })
        /*create img for photo*/
        const img = document.createElement('img')
        setAttributes(img, {
            src: photo.urls.regular,
            alt: photo.alt_description,
            title: photo.alt_description,
        })
        /*Event listener, check when each are finihsed loading*/
        img.addEventListener('load', imageLoaded);
        /*put img inside anchor tag, then put both inside image container*/
        item.append(img);
        imageContainer.appendChild(item);
    });
}

/*get photos from API*/
async function getPhotos() {
    try {
        const response = await fetch(apiUrl);
        photosArray = await response.json();
        displayPhotos();
    } catch (e) {
        console.log(e)
    }
}

/*See if we scroll all the way to the end, and then display new photos*/
window.addEventListener('scroll', () => {
    if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 1000 && ready) {/*if were 1000 pixels away from end of page and images are loaded*/
        ready = false; /*make sure the function is only ready when the previous images have been loaded*/
        getPhotos();
    }
})
getPhotos();
